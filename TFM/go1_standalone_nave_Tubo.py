# Copyright (c) 2021-2023, NVIDIA CORPORATION. All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto. Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.
#

from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False})

import carb
import numpy as np
import omni.appwindow
from omni.isaac.core import World
from omni.isaac.core.utils.prims import define_prim, get_prim_at_path
from omni.isaac.nucleus import get_assets_root_path
from omni.isaac.quadruped.robots import SpotFlatTerrainPolicy
from omni.isaac.sensor.scripts.effort_sensor import EffortSensor


import numpy as np

import json


import matplotlib.pyplot as plt
from Pox_X import *

import skfuzzy as fuzz
from skfuzzy import control as ctrl
import math

import os
import tempfile
from typing import Literal

import omni.client
import omni.kit.app

import omni.graph.core as og

import time 

# Inicializar el tiempo de simulación
simulation_start_time = time.time()

# Inicializar las extensiones de Omniverse
manager = omni.kit.app.get_app().get_extension_manager()
manager.set_extension_enabled_immediate("omni.isaac.ros_bridge", True)


NUCLEUS_ASSET_ROOT_DIR = carb.settings.get_settings().get("/persistent/isaac/asset_root/cloud")
"""Path to the root directory on the Nucleus Server."""

NVIDIA_NUCLEUS_DIR = f"{NUCLEUS_ASSET_ROOT_DIR}/NVIDIA"
"""Path to the root directory on the NVIDIA Nucleus Server."""

ISAAC_NUCLEUS_DIR = f"{NUCLEUS_ASSET_ROOT_DIR}/Isaac"
"""Path to the ``Isaac`` directory on the NVIDIA Nucleus Server."""

ISAACLAB_NUCLEUS_DIR = f"{ISAAC_NUCLEUS_DIR}/IsaacLab"
"""Path to the ``Isaac/IsaacLab`` directory on the NVIDIA Nucleus Server."""

# Inicializar las variables globales

first_step = True
reset_needed = False

# Se crea lavariable para posteriormente usarla para crear la carpeta "graficos"

output_dir = "graficos"
os.makedirs(output_dir, exist_ok=True)

# Inicializar robot en el primer paso
def on_physics_step(step_size) -> None:
    global first_step
    global reset_needed
    if first_step:
        go1.initialize()
        first_step = False
    elif reset_needed:
        my_world.reset(True)
        reset_needed = False
        first_step = True
    else:
        go1.advance(step_size, base_command)

# Generación funciones auxiliares
# Calcular la distancia entre dos puntos
def calcular_distancia(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
# Pasar quaternios a ángulo de yaw
def quaternion_to_yaw(quat):
    x, y, z, w = quat
    yaw = np.arctan2(2 * (y * z + x * w), 1 - 2 * (y**2 + x**2))
    return np.degrees(yaw)  # Convertir a grados
# Pasar quaternios a ángulo de pitch   
def quaternion_to_pitch(quat):
    x, y, z, w = quat
    pitch = np.arcsin(2 * (x * y + z * w)) 
    return np.degrees(pitch)

def normalizar_angulo(angulo):
    angulo = angulo % 360
    if angulo > 180:
        angulo -= 360
    return angulo
    
# Conversión de archivos a formato float
def convertir_a_float(val):
    if isinstance(val, np.float32):
        return float(val)  # Convertir a float nativo de Python
    elif isinstance(val, list):
        return [convertir_a_float(i) for i in val]  # Recursión para listas
    elif isinstance(val, dict):
        return {key: convertir_a_float(value) for key, value in val.items()}  # Recursión para diccionarios
    else:
        return val  # Si no es un float32, lo dejamos tal como está

# Guardar los datos de sensor_readings en un archivo JSON
def guardar_sensor_readings(sensor_readings, output_dir="graficos", subcarpeta="sensor_data"):
    # Crear la ruta completa para la subcarpeta dentro de "graficos"
    subcarpeta_path = os.path.join(output_dir, subcarpeta)
    
    # Verificar si la subcarpeta existe, si no, crearla
    if not os.path.exists(subcarpeta_path):
        os.makedirs(subcarpeta_path)  # Crear la subcarpeta si no existe

    # Convertir los datos a un formato serializable por JSON
    sensor_readings_serializables = convertir_a_float(sensor_readings)

    # Definir la ruta base del archivo
    base_filename = "sensor_readings"
    file_extension = ".json"
    archivo_json = os.path.join(subcarpeta_path, f"{base_filename}{file_extension}")

    # Generar un nombre único si el archivo ya existe
    contador = 1
    while os.path.exists(archivo_json):
        archivo_json = os.path.join(subcarpeta_path, f"{base_filename}_{contador}{file_extension}")
        contador += 1

    # Escribir los datos en el archivo JSON
    with open(archivo_json, "w") as f:
        json.dump(sensor_readings_serializables, f, indent=4)
    print(f"Los datos del sensor se han guardado en {archivo_json}")



# Generar el mundo
my_world = World(stage_units_in_meters=1.0, physics_dt=1 / 400, rendering_dt=1 / 60)  # 1/500, 1/50
assets_root_path = get_assets_root_path()
if assets_root_path is None:
    carb.log_error("Could not find Isaac Sim assets folder")

# Generar el escenario
prim = define_prim("/World/Ground", "Xform")
asset_path = "/home/robcib/Desktop/Jorge/My_World_Terreno_Nuevo_Tubo.usd" #assets_root_path + "/Isaac/Environments/Grid/default_environment.usd"
prim.GetReferences().AddReference(asset_path)

# Generar el robot
go1 = SpotFlatTerrainPolicy(
    prim_path="/World/Go1",
    name="Go1",
    usd_path=assets_root_path + "/Isaac/Robots/Unitree/Go1/go1.usd",
    position=np.array([4.5, -2.5, 0.8]),
    orientation=np.array([0, 0, 0,-1])  #Nos aseguramos de que vaya recto.
)


my_world.add_physics_callback("physics_step", callback_fn=on_physics_step)
my_world.reset()

# Movimiento inicial del robot a 0
base_command = np.zeros(3)


waypoints = [
    np.array([3.50, -2.50, 0.00]),  # Waypoint 1
    np.array([2.68, -2.82, 10.00]),  # Waypoint 2
    np.array([1.81, -2.82, 20.00]),  # Waypoint 3
    np.array([1.31, -2.62, 20.00]),  # Waypoint 4
    np.array([1.01, -2.39, 40.00]),  # Waypoint 5
    np.array([0.81, -1.69, 60.00]),  # Waypoint 6
    np.array([0.81, -1.69, 85.00]),  # Waypoint 7
    np.array([0.42, -0.94, 90.00]),  # Waypoint 8
    np.array([0.57, 0.09, 90.00]),  # Waypoint 9
    np.array([0.57, 0.39, 90.00]),  # Waypoint 10
    np.array([0.57, 0.51, 90.00]),  # Waypoint 11
    np.array([0.57, 0.51, 50.00]),  # Waypoint 12
    np.array([0.34, 0.81, 20.00]),  # Waypoint 13
    np.array([0.34, 0.81, 0.00]),  # Waypoint 14
    np.array([0.17, 1.00, 0.00]),  # Waypoint 15
]

# Creación Action Graph para IsaacSim

og.Controller.edit(
    {"graph_path": "/Joint_States_Graph", "evaluator_name": "execution"},
    {
        og.Controller.Keys.CREATE_NODES: [
            ("OnPlaybackTick", "omni.graph.action.OnPlaybackTick"),
            ("PublishJointState", "omni.isaac.ros_bridge.ROS1PublishJointState"),
            ("ReadSimTime", "omni.isaac.core_nodes.IsaacReadSimulationTime"),
        ],
        og.Controller.Keys.CONNECT: [
            ("OnPlaybackTick.outputs:tick", "PublishJointState.inputs:execIn"),
            ("ReadSimTime.outputs:simulationTime", "PublishJointState.inputs:timeStamp"),
        ],
        og.Controller.Keys.SET_VALUES: [
            ("PublishJointState.inputs:targetPrim", "/World/Go1"),
        ],
    },
)

# Inicialización de variables

current_waypoint_index = 0  # Track the current waypoint

visited_positions = []
waypoints_achieved = []
waypoints_achieved_theta = []

sensor_readings = []
sensor_readings_2 = []
sensor_readings_3 = []
sensor_readings_4 = []

pitch_values = []

# Creación de sensores dentro del robot

sensor = EffortSensor(
prim_path="/World/Go1/FL_hip/FL_thigh_joint",
sensor_period=10,
use_latest_data=False,
enabled=True)

sensor_2 = EffortSensor(
prim_path="/World/Go1/FR_hip/FR_thigh_joint",
sensor_period=10,
use_latest_data=False,
enabled=True)

sensor_3 = EffortSensor(
prim_path="/World/Go1/RL_hip/RL_thigh_joint",
sensor_period=10,
use_latest_data=False,
enabled=True)

sensor_4 = EffortSensor(
prim_path="/World/Go1/RR_hip/RR_thigh_joint",
sensor_period=10,
use_latest_data=False,
enabled=True)

#Comienzo de la simulación

while simulation_app.is_running():
    my_world.step(render=True)
    # Si el mundo se detiene
    if my_world.is_stopped():
        reset_needed = True
        # Calcular el porcentaje de waypoints visitados
        total_waypoints = len(waypoints)
        waypoints_visitados = len(waypoints_achieved)
        porcentaje_visitado = (waypoints_visitados / total_waypoints) * 100
        print(f"Porcentaje de waypoints visitados: {porcentaje_visitado:.2f}%")
    #Si el mundo se está ejecutando, haz todo lo demás...
    if my_world.is_playing():
        # Guardar posición actual y ángulos
        pos_IB, q_IB = go1.robot.get_world_pose()
        current_pos = np.array([pos_IB[0], pos_IB[1]])
        visited_positions.append(list(current_pos))
        print(f"Posiciones Visitadas: {visited_positions}")

        current_yaw = round(quaternion_to_yaw(q_IB), 3) 
        current_yaw = normalizar_angulo(current_yaw)
        
        current_pitch = round (quaternion_to_pitch(q_IB))
        current_pitch = normalizar_angulo(current_pitch)
        pitch_values.append(current_pitch)

        #Si no se han alcanzado todos los waypoints..
        if current_waypoint_index < len(waypoints):
            waypoint = waypoints[current_waypoint_index]
            #Cálculo diferencia de posiciones/ángulos
            diferencia_x = waypoint[0] - current_pos[0]
            diferencia_y = waypoint[1] - current_pos[1]
            diferencia_theta = waypoint[2] - current_yaw
            diferencia_theta = normalizar_angulo(diferencia_theta)
            print("--")
            print(f"X: {current_pos[0]}")
            print(f"Y: {current_pos[1]}")
            print(f"Ángulo Actual: {current_yaw}")
            
            #Lectura Sensores de Torque
            reading = sensor.get_sensor_reading(use_latest_data = True)
            print(f"time: {reading.time} value:{reading.value} \n")
            sensor_readings.append(reading.value)
            
            reading_2 = sensor_2.get_sensor_reading(use_latest_data = True)
            print(f"time: {reading.time} value:{reading_2.value} \n")
            sensor_readings_2.append(reading_2.value) 
            
            reading_3 = sensor_3.get_sensor_reading(use_latest_data = True)
            print(f"time: {reading.time} value:{reading_3.value} \n")
            sensor_readings_3.append(reading_3.value) 
            
            reading_4 = sensor_4.get_sensor_reading(use_latest_data = True)
            print(f"time: {reading.time} value:{reading_4.value} \n")
            sensor_readings_4.append(reading_4.value)          

            
            print("--")
            print(f"diferencia_x: {diferencia_x}")
            print(f"diferencia_y: {diferencia_y}")
            print(f"diferencia_angulo: {diferencia_theta}")
            # Si ya se ha alcanzado el primer WP
            if current_waypoint_index > 0:
            	previous_waypoint = waypoints[current_waypoint_index - 1]
            	# Movimientos verticales del robot
            	if 75 <= current_yaw <= 95:
            		velocidad_x = round(calcula_velocidad_x(diferencia_y), 3)
            		V_giro = V_giro = round(Angulo_Giro(diferencia_theta), 2)
            		if current_pos[0] > waypoint[0]:
            			velocidad_y = -round(calcula_velocidad_y(diferencia_x), 3)
            		else:
            			velocidad_y = round(calcula_velocidad_y(diferencia_x), 3)
            		
            		        		
            	else:
            	        # Movimiento solo de giro. Se ha de asegurar que los waypoints (tanto x como y) sean los mismos o muy proximos.
            		if np.isclose(previous_waypoint[0], waypoint[0], atol=1e-2) and np.isclose(previous_waypoint[1], waypoint[1], atol=1e-2):
            		# Solo hacer el giro
            			velocidad_x = 0.0
            			velocidad_y = 0.0
            			V_giro = round(Angulo_Giro(diferencia_theta), 2)
            		else:
                            #Consideraciones para movimientos hacia el eje y negativo.
            			if current_pos[1] < waypoint[1] and current_yaw >115:
            				velocidad_y = round(calcula_velocidad_y(diferencia_y), 3)*2
            			elif current_pos[1] < waypoint[1] and current_yaw <130:
            				velocidad_y = -round(calcula_velocidad_y(diferencia_y), 3)
            			elif current_pos[1] > waypoint[1] and current_yaw >130:
            				velocidad_y = -round(calcula_velocidad_y(diferencia_y), 3)
            			else:
            				velocidad_y = round(calcula_velocidad_y(diferencia_y), 3)  				
            			V_giro = round(Angulo_Giro(diferencia_theta), 2)
            			velocidad_x = round(calcula_velocidad_x(diferencia_x), 3)
            else: #Para ir al primer waypoint
            	if current_pos[1] < waypoint[1]:
            		velocidad_y = -round(calcula_velocidad_y(diferencia_y), 3)
            	else:
            		velocidad_y = round(calcula_velocidad_y(diferencia_y), 3)
            	V_giro = round(Angulo_Giro(diferencia_theta), 2)
            	velocidad_x = round(calcula_velocidad_x(diferencia_x), 3)
            
            print("--")
            print(f"Velocidad en x: {velocidad_x}")
            print(f"Velocidad en y: {velocidad_y}")
            print(f"Velocidad en theta: {V_giro}")   
                    
            #Condición de punto alcanzado
            if (current_pos[0] < waypoint[0]+0.1 and current_pos[0] > waypoint[0]-0.1) and (current_pos[1] < waypoint[1]+0.15 and current_pos[1] > waypoint[1]-0.15) and (current_yaw < waypoint[2]+8 and current_yaw > waypoint[2]-8):
                print("Punto Alcanzado")
                waypoints_achieved.append(current_pos.tolist())
                waypoints_achieved_theta.append(current_yaw.tolist())
                current_waypoint_index += 1  # Mover al siguiente waypoint
                # Si todos los WP han sido alcanzados...
                if current_waypoint_index >= len(waypoints):
                    print("Todos los puntos han sido visitados. Deteniendo el robot.")
                    base_command = np.array([0.0, 0.0, 0.0])  # Detener el robot
                    elapsed_time = time.time() - simulation_start_time
                    print(f"Tiempo total para alcanzar todos los waypoints: {elapsed_time:.2f} segundos")
                     
                    # Guardar datos de los sensores        
                    guardar_sensor_readings(sensor_readings)
                    guardar_sensor_readings(sensor_readings_2)
                    guardar_sensor_readings(sensor_readings_3)
                    guardar_sensor_readings(sensor_readings_4)
                    #Gráficas de trayectoria
                    if visited_positions:
                    	plt.figure()
                        #Se añaden WP aparentes, WP alcanzados y trayectoria ejecutada
                    	waypoints_np = np.array(waypoints)
                    	plt.scatter(waypoints_np[:, 0], waypoints_np[:, 1], color='red', label='Waypoints', marker='x')
                    	waypoints_achieved_np = np.array(waypoints_achieved)
                    	plt.scatter(waypoints_achieved_np[:, 0], waypoints_achieved_np[:, 1], color='green', label='Waypoints Alcanzados', marker='D', s=100)
                    	visited_positions_np = np.array(visited_positions)  # Convertir a numpy solo para plotear
                    	plt.plot(visited_positions_np[:, 0], visited_positions_np[:, 1], marker='o', color='b', label='Puntos Visitados', markersize=5)
                    	plt.title('Puntos Visitados por el Robot')
                    	plt.xlabel('X (m)')
                    	plt.ylabel('Y (m)')
                    	plt.legend()
                    	plt.grid()
                    	plt.axis('equal')
                    	plt.savefig(os.path.join(output_dir, "puntos_visitados.png"))
                    	plt.close()  # Cerrar la figura para liberar memoria
                    	
                    	# Gráficos de errores
                    	errores = []
                    	errores_x = []
                    	errores_y = []
                    	errores_theta = []
                    	for i in range(len(waypoints)):
                    		if i < len(waypoints_achieved):
                                    #Cálculo del error.
                    			error = calcular_distancia(waypoints[i][:2], waypoints_achieved[i][:2])
                    			errores.append(error)
                    			print(f"Error en el waypoint {i+1}: {error:.2f} m")
                    			error_x = waypoints[i][0] - waypoints_achieved[i][0]
                    			error_y = waypoints[i][1] - waypoints_achieved[i][1]
                    			error_theta = waypoints[i][2] - waypoints_achieved_theta[i]
                    			
                    			errores_x.append(error_x)
                    			errores_y.append(error_y)
                    			errores_theta.append(error_theta)
                    	if errores:
                            #Error medio de todos los calculados
                    		error_medio = np.mean(errores)
                    		print(f"Error medio de distancia a los waypoints: {error_medio:.2f} metros")
                    	#Ploteo errores x e y
                    	plt.figure()
                    	plt.plot(range(1, len(errores) + 1), errores, marker='o', label='Error (Distancia)')
                    	plt.plot(range(1, len(errores_x) + 1), errores_x, marker='o', label='Error en X')
                    	plt.plot(range(1, len(errores_y) + 1), errores_y, marker='o', label='Error en Y')
                    	plt.legend()
                    	plt.title('Errores de Posición en Waypoints')
                    	plt.xlabel('Waypoint')
                    	plt.ylabel('Error (m)')
                    	plt.grid()
                    	plt.savefig(os.path.join(output_dir, "errores_waypoints.png"))
                    	plt.close()
                    	#Ploteo errores de theta
                    	plt.figure()
                    	plt.plot(range(1, len(errores) + 1), errores, marker='o')
                    	plt.plot(range(1, len(errores_theta) + 1), errores_theta, marker='o', label='Error en Theta')
                    	plt.legend()
                    	plt.title('Errores de Posición en Waypoints')
                    	plt.xlabel('Waypoint')
                    	plt.ylabel('Error (m)')
                    	plt.grid()
                    	plt.savefig(os.path.join(output_dir, "errores_waypoints_theta.png"))
                    	plt.close()
                    	
                    	# Graficos de los valores de los sensores.
                    	plt.figure()
                    	plt.plot(sensor_readings, marker='o', linestyle='-', color='purple', markersize=4)
                    	plt.title('Valores de Torque del Sensor durante la Simulación')
                    	plt.xlabel('Paso de Tiempo')
                    	plt.ylabel('Valor de Torque')
                    	plt.grid()
                    	plt.savefig(os.path.join(output_dir, "sensor_readings.png"))
                    	plt.close()

                    	# Graficos de los ángulos de pitch.
                    	if pitch_values:
                    		plt.figure()
                    		plt.plot(pitch_values, label='Pitch', color='orange')
                    		plt.title('Evolución del Pitch a lo largo del tiempo')
                    		plt.xlabel('Tiempo (segundos)')
                    		plt.ylabel('Pitch (grados)')
                    		plt.grid(True)
                    		plt.legend()
                    		plt.savefig(os.path.join(output_dir, "evolucion_pitch.png"))
                    		plt.close()
                    		print("El ángulo de pitch máximo es:", max(pitch_values))
                    		print("La media en el ángulo de pitch es:", np.mean(pitch_values))
                    		break                     
        else:
        	velocidad_x = 0
        	velocidad_y = 0
        	V_giro = 0
        	base_command = np.array([velocidad_x, velocidad_y, V_giro])  # Detener el robot

        # Asignar comando base
        base_command = np.array([velocidad_x, velocidad_y, V_giro])

# Al finalizar la simulación, plotea los puntos visitados


simulation_app.close()




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
import omni.appwindow  # Contains handle to keyboard
from omni.isaac.core import World
from omni.isaac.core.utils.prims import define_prim, get_prim_at_path
from omni.isaac.nucleus import get_assets_root_path
from omni.isaac.quadruped.robots import SpotFlatTerrainPolicy
import matplotlib.pyplot as plt
from Fuzzy_Controll import *

import skfuzzy as fuzz
from skfuzzy import control as ctrl
import math

import os
import tempfile
from typing import Literal

import omni.client
import omni.kit.app

import omni.graph.core as og

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

first_step = True
reset_needed = False

# Almacenar posiciones visitadas

output_dir = "graficos"
os.makedirs(output_dir, exist_ok=True)

# initialize robot on first step, run robot advance
def on_physics_step(step_size) -> None:
    global first_step
    global reset_needed
    if first_step:
        spot.initialize()
        first_step = False
    elif reset_needed:
        my_world.reset(True)
        reset_needed = False
        first_step = True
    else:
        spot.advance(step_size, base_command)
        
def calcular_distancia(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def quaternion_to_yaw(quat):
    x, y, z, w = quat
    yaw = np.arctan2(2 * (y * z + x * w), 1 - 2 * (y**2 + x**2))
    return np.degrees(yaw)  # Convertir a grados

def normalizar_angulo(angulo):
    angulo = angulo % 360
    if angulo > 180:
        angulo -= 360
    return angulo

# spawn world
my_world = World(stage_units_in_meters=1.0, physics_dt=1 / 400, rendering_dt=1 / 60)  # 1/500, 1/50
assets_root_path = get_assets_root_path()
if assets_root_path is None:
    carb.log_error("Could not find Isaac Sim assets folder")

# spawn warehouse scene
prim = define_prim("/World/Ground", "Xform")
asset_path = "/home/robcib/Desktop/Jorge/My_World_Spot.usd"#Prueba_Desnivel.usd #assets_root_path + "/Isaac/Environments/Grid/default_environment.usd"
prim.GetReferences().AddReference(asset_path)

# spawn robot
spot = SpotFlatTerrainPolicy(
    prim_path="/World/Spot",
    name="Spot",
    usd_path=assets_root_path + "/Isaac/Robots/BostonDynamics/spot/spot.usd",
    position=np.array([4.5, -2.5, 0.8]),
    orientation=np.array([0, 0, 0,-1])  #Nos aseguramos de que vaya recto.
)
my_world.add_physics_callback("physics_step", callback_fn=on_physics_step)
my_world.reset()

# robot command
base_command = np.zeros(3)

#waypoints = [
    #np.array([2.0, 0.0, 0]),  # Waypoint 1
    #np.array([2.5, -0.25, 10]),
    #np.array([3.0, -0.5, 20]),
    #np.array([3.5, -0.75, 30]),
    #np.array([4, -1, 20]),
    #np.array([4.5, -1, 10]),  # Waypoint 2
    #np.array([5, -1, 0]),
    #np.array([5.5, -1, 0]),
    #np.array([6, -1, -5]),
    #np.array([6.5, -1, 0]),
    #np.array([7, -1, 0]),
    #np.array([7.5, -1, 0]),
    #np.array([8, -1, -10]),
    #np.array([8.5, -0.75, -20]),
    #np.array([9, -0.5, -30]),
    #np.array([9.5, -0.25, -45]),
    #np.array([10, -0.0, -45]),
    #np.array([9.5, 0.25, -25])
#]


waypoints = [
    np.array([3.5, -2.5, 0]),  # Waypoint 1
    np.array([2.5, -2.5, 0]),
    np.array([1.0, -2.5, 0]),
    np.array([0.5, -2.25, 10]),
    np.array([0, -2, 15]),
    np.array([-0.5, -1.75, 15]),  # Waypoint 2
    np.array([-1, -1.75, 15]),
    np.array([-1.5, -1.5, 30]),
    np.array([-1.6, -1.25, 40]),
    np.array([-1.7, -1.0, 60]),
    np.array([-1.75, -0.85, 75]),
    np.array([-1.75, -0.7, 80]), #Waypoint
    np.array([-1.85, 0.5, 85]),
    np.array([-1.85, 0.5, 120]),  
    np.array([-1.85, 0.5, 140]), #Referencia -1.5, 0.7. 91
    np.array([-1.85, 0.5, 170]),
    np.array([-1.6, 0.7, 170]),
    np.array([-1.2, 0.8, 175]),
    np.array([-0.5, 1, 180]),
    np.array([0.5, 1, 180]),
    np.array([1.5, 1, 180]),
    np.array([2.5, 1, 180]),
    np.array([2.5, 1, 145]),
    np.array([2.5, 1, 135]),
    np.array([2.5, 1, 105]),
    np.array([2.5, 1, 90]),
    np.array([2.5, 2, 85]),
    np.array([2.5, 2.5, 85]),
    np.array([2.5, 3.0, 85]),
    np.array([2.5, 3.5, 85])
    
    
    
]


og.Controller.edit(
    {"graph_path": "/ActionGraph", "evaluator_name": "execution"},
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
            # Providing path to /panda robot to PublishJointState node
            ("PublishJointState.inputs:targetPrim", "/World/Spot"),
        ],
    },
)

current_waypoint_index = 0  # Track the current waypoint

visited_positions = []
waypoints_achieved = []
waypoints_achieved_theta = []

while simulation_app.is_running():
    my_world.step(render=True)
    if my_world.is_stopped():
        reset_needed = True
    if my_world.is_playing():
        pos_IB, q_IB = spot.robot.get_world_pose()
        current_pos = np.array([pos_IB[0], pos_IB[1]])
        
        # Guardar posición actual
        visited_positions.append(list(current_pos))
        #print(f"Posiciones Visitadas: {visited_positions}")

        current_yaw = round(quaternion_to_yaw(q_IB), 3) 
        current_yaw = normalizar_angulo(current_yaw)
        
        if current_waypoint_index < len(waypoints):
            waypoint = waypoints[current_waypoint_index]
            diferencia_x = waypoint[0] - current_pos[0]
            diferencia_y = waypoint[1] - current_pos[1]
            diferencia_theta = waypoint[2] - current_yaw
            diferencia_theta = normalizar_angulo(diferencia_theta)
            print("--")
            print(f"X: {current_pos[0]}")
            print(f"Y: {current_pos[1]}")
            print(f"Ángulo Actual: {current_yaw}")
            print("--")
            print(f"diferencia_x: {diferencia_x}")
            print(f"diferencia_y: {diferencia_y}")
            print(f"diferencia_angulo: {diferencia_theta}")
            
            if current_waypoint_index > 0:
            	previous_waypoint = waypoints[current_waypoint_index - 1]
            	if 75 <= current_yaw <= 95: 
            		print("AAAAAAA")
            		velocidad_x = round(calcula_velocidad_x(diferencia_y), 3)#0.5
            		V_giro = round(Angulo_Giro(diferencia_theta), 2)#-0.4  
            		if current_pos[0] > waypoint[0]:
            			velocidad_y = round(calcula_velocidad_y(diferencia_x), 3)#0.2
            		else:
            			velocidad_y = -round(calcula_velocidad_y(diferencia_x), 3)#0.2
            		
            		        		
            	else:
            	
            		if np.isclose(previous_waypoint[0], waypoint[0], atol=1e-2) and np.isclose(previous_waypoint[1], waypoint[1], atol=1e-2):
            		# Solo hacer el giro
            			velocidad_x = 0.0
            			velocidad_y = 0.0
            			V_giro = round(Angulo_Giro(diferencia_theta), 2)
            		else:
            			if current_pos[1] < waypoint[1] and current_yaw >115:
            				velocidad_y = round(calcula_velocidad_y(diferencia_y), 3)
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
            
            if (current_pos[0] < waypoint[0]+0.1 and current_pos[0] > waypoint[0]-0.1) and (current_pos[1] < waypoint[1]+0.15 and current_pos[1] > waypoint[1]-0.15) and (current_yaw < waypoint[2]+5 and current_yaw > waypoint[2]-5):
                print("Punto Alcanzado")
                waypoints_achieved.append(current_pos.tolist())
                waypoints_achieved_theta.append(current_yaw.tolist())
                current_waypoint_index += 1  # Mover al siguiente waypoint

                if current_waypoint_index >= len(waypoints):
                    print("Todos los puntos han sido visitados. Deteniendo el robot.")
                    base_command = np.array([0.0, 0.0, 0.0])  # Detener el robot
                    if visited_positions:
                    	plt.figure()

                    	
                    	waypoints_np = np.array(waypoints)
                    	plt.scatter(waypoints_np[:, 0], waypoints_np[:, 1], color='red', label='Waypoints', marker='x')
                    	# Añadir waypoints "aparentes"
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
                    	
                    	
                    	errores = []
                    	errores_x = []
                    	errores_y = []
                    	errores_theta = []
                    	for i in range(len(waypoints)):
                    		if i < len(waypoints_achieved):
                    			error = calcular_distancia(waypoints[i][:2], waypoints_achieved[i][:2])
                    			errores.append(error)
                    			print(f"Error en el waypoint {i+1}: {error:.2f} m")
                    			error_x = waypoints[i][0] - waypoints_achieved[i][0]
                    			error_y = waypoints[i][1] - waypoints_achieved[i][1]
                    			error_theta = waypoints[i][2] - waypoints_achieved_theta[i]
                    			
                    			errores_x.append(error_x)
                    			errores_y.append(error_y)
                    			errores_theta.append(error_theta)
                    			# Guardar errores en un archivo o procesarlos según sea necesario
                    	#with open(os.path.join(output_dir, "errores_waypoints.txt"), "w") as f:
                    	#	for i, error in enumerate(errores):
                    	#		f.write(f"Error en el waypoint {i+1}: {error:.2f} m\n")
                    	# Grafico errores
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
                        
                       
   
                    
        else:
            base_command = np.array([0.0, 0.0, 0.0])  # Detener el robot

        # Asignar comando base
        base_command = np.array([velocidad_x, velocidad_y, V_giro])
        #print(base_command)

# Al finalizar la simulación, plotea los puntos visitados


simulation_app.close()



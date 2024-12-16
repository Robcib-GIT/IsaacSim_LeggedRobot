import os
import numpy as np
from generador_rutas import *
# Definir los waypoints originales
waypoints = [
    np.array([3.5, -2.5, 0]),  
    np.array([3.0, -2.5, 0]),   
    np.array([1.0, -2.5, 0]),
    np.array([0.5, -2.25, 10]),
    np.array([0, -2, 15]),
    np.array([-0.5, -1.75, 15]),  
    np.array([-1, -1.75, 15]),
    np.array([-1.5, -1.5, 30]),
    np.array([-1.6, -1.25, 40]),
    np.array([-1.7, -1.0, 60]),
    np.array([-1.75, -0.85, 75]),
    np.array([-1.75, -0.7, 80]), 
    np.array([-1.6, 0.5, 88]),
    np.array([-1.7, 0.5, 90]),
    np.array([-1.7, 0.5, 120]),  
    np.array([-1.6, 0.55, 140]), 
    np.array([-1.6, 0.55, 160]),
    np.array([-1.4, 0.55, 170]),
    np.array([-1.0, 0.6, 175]),
    np.array([-0.5, 0.8, 175]),
    np.array([0.5, 1, 175]),
    np.array([1.5, 1, 175]),
    np.array([2, 1, 175]),
    np.array([2.2, 1, 175]),
    np.array([2.2, 1, 145]),
    np.array([2.3, 1.3, 100]),
    np.array([2.3, 1.3, 85]),
    np.array([2.4, 2, 85]),
    np.array([2.5, 2.5, 85]),
    np.array([2.5, 3.0, 85])
]

# Llamar a la función para generar las trayectorias
trayectorias_unicas = generar_trayectorias(waypoints, num_trayectorias=100, incremento=0.01)

# Crear la carpeta "Trayectorias" si no existe
if not os.path.exists("Trayectorias"):
    os.makedirs("Trayectorias")

# Guardar las trayectorias únicas en archivos .txt dentro de la carpeta "Trayectorias"
for index, trayectoria in enumerate(trayectorias_unicas):
    nombre_archivo = f"Trayectorias/trayectoria_unica_{index + 1}.txt"
    with open(nombre_archivo, 'w') as file:
        file.write("waypoints = [\n")  # Iniciar la lista de waypoints
        for i, punto in enumerate(trayectoria):
            file.write(f"    np.array([{punto[0]:.2f}, {punto[1]:.2f}, {punto[2]:.2f}]),  # Waypoint {i + 1}\n")
        file.write("]\n")  # Cerrar la lista de waypoints
    print(f"Trayectoria {index + 1} guardada en {nombre_archivo}")



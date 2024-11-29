import os
import numpy as np

def generar_trayectorias_unicas(waypoints, num_trayectorias=100, incremento=0.01):
    # Lista para almacenar las trayectorias
    trayectorias = []

    # Generar nuevas trayectorias con variaciones solo en los puntos intermedios
    for i in range(num_trayectorias):
        nueva_trayectoria = []

        # Alternar entre incremento positivo y negativo
        signo = (-1) ** i  # Alterna entre -1 y 1 en cada iteración

        for j, wp in enumerate(waypoints):
            if j == 0 or j == len(waypoints) - 1:
                # Mantener el waypoint inicial y final igual
                nueva_trayectoria.append(wp)
            else:
                # Variar solo los puntos intermedios con límite de 0.5
                desplazamiento_x = signo * min(incremento * i, 0.5)
                desplazamiento_y = signo * min(incremento * i, 0.5)
                new_wp = np.array([wp[0] + desplazamiento_x, wp[1] + desplazamiento_y, wp[2]])  # Mantener z constante
                nueva_trayectoria.append(new_wp)

        trayectorias.append(nueva_trayectoria)

    # Convertir trayectorias a tuplas para encontrar únicas
    trayectorias_tuplas = [tuple(map(tuple, trayectoria)) for trayectoria in trayectorias]
    trayectorias_unicas = set(trayectorias_tuplas)  # Usar un conjunto para encontrar únicas

    # Convertir las trayectorias únicas de nuevo a listas
    trayectorias_unicas_listas = [list(map(np.array, trayectoria)) for trayectoria in trayectorias_unicas]

    # Crear la carpeta "Trayectorias" si no existe
    if not os.path.exists("Trayectorias"):
        os.makedirs("Trayectorias")

    # Guardar las trayectorias únicas en archivos .txt dentro de la carpeta "Trayectorias"
    for index, trayectoria in enumerate(trayectorias_unicas_listas):
        nombre_archivo = f"Trayectorias/trayectoria_unica_{index + 1}.txt"
        with open(nombre_archivo, 'w') as file:
            file.write("waypoints = [\n")  # Iniciar la lista de waypoints
            for i, punto in enumerate(trayectoria):
                file.write(f"    np.array([{punto[0]:.2f}, {punto[1]:.2f}, {punto[2]:.2f}]),  # Waypoint {i + 1}\n")
            file.write("]\n")  # Cerrar la lista de waypoints
        print(f"Trayectoria {index + 1} guardada en {nombre_archivo}")

    # Mostrar el número de trayectorias únicas y sus nombres
    numero_trayectorias_unicas = len(trayectorias_unicas_listas)
    print(f"\nNúmero de trayectorias únicas: {numero_trayectorias_unicas}")
    print("Trayectorias guardadas en los siguientes archivos:")
    for index in range(numero_trayectorias_unicas):
        print(f"Trayectorias/trayectoria_unica_{index + 1}.txt")

    return trayectorias_unicas_listas  # Retornar las trayectorias únicas

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

# Generar trayectorias únicas y guardarlas en archivos dentro de la carpeta "Trayectorias"
trayectorias_unicas = generar_trayectorias_unicas(waypoints)


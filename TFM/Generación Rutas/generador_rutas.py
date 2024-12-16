import numpy as np
import matplotlib.pyplot as plt


def generar_trayectorias(waypoints, num_trayectorias, incremento):
# Se usa el set para almacenar trayectorias únicas
    trayectorias = set()

    for i in range(num_trayectorias):
        nueva_trayectoria = []
        
        # Alternar entre incremento positivo y negativo
        signo = (-1) ** i
        
        for j, wp in enumerate(waypoints):
            if j == 0 or j == len(waypoints) - 1:
                # Mantener el waypoint inicial y final igual
                nueva_trayectoria.append(wp)
            else:
                # Variar solo los puntos intermedios con límite de 1
                desplazamiento_x = signo * min(incremento * i, 0.5)  # Se limita el cambio a 0.5 para no alejar mucho los puntos
                desplazamiento_y = signo * min(incremento * i, 0.5)  
                new_wp = np.array([wp[0] + desplazamiento_x, wp[1] + desplazamiento_y, wp[2]])  # Mantener z constante
                nueva_trayectoria.append(new_wp)
        
        # Convertir la trayectoria a tupla para agregarla al set (evita duplicados)
        trayectorias.add(tuple(map(tuple, nueva_trayectoria)))

    # Convertir el set en lista
    return list(trayectorias)

# Trayectoria original
waypoints = [
	np.array([3.50, -2.50, 0.00]),  # Waypoint 1
	np.array([2.87, -2.63, 10.00]),  # Waypoint 2
	np.array([2.50, -2.63, 20.00]),  # Waypoint 3
	np.array([2.50, -2.63, 40.00]),  # Waypoint 3
	np.array([2.50, -2.63, 60.00]),  # Waypoint 3
	np.array([2.30, -1.60, 60.00]),  # Waypoint 3
	np.array([2.10, -0.90, 60.00]),  # Waypoint 6
	np.array([2.10, -0.90, 80.00]),  # Waypoint 6
	np.array([2.2, -0.20, 85.00]),  # Waypoint 6
	np.array([2.2, -0.20, 90.00]),  # Waypoint 6
	np.array([2.1, 0.2, 90.00]),  # Waypoint 6
	np.array([2.2, 0.8, 85.00]),  # Waypoint 6
	np.array([2.17, 1.0, 85.00]),  # Waypoint 6
        np.array([2.27, 1.17, 85.00]),  # Waypoint 27
        np.array([2.37, 2.00, 85.00]),  # Waypoint 29
        np.array([2.50, 3.00, 85.00]),  # Waypoint 30
]





# Número de trayectorias a generar
num_trayectorias = 100

# Incremento por iteración en las coordenadas x e y
incremento = 0.01

trayectorias = generar_trayectorias(waypoints,num_trayectorias,incremento)

# Contar el número de trayectorias únicas
numero_trayectorias_unicas = len(trayectorias)

# Mostrar el resultado
print(f"Número de trayectorias únicas: {numero_trayectorias_unicas}")

# Graficar todas las trayectorias en 2D
plt.figure(figsize=(10, 8))

# Ploteo de la trayectoria original en rojo
trayectoria_original = np.array(waypoints)
plt.plot(trayectoria_original[:, 0], trayectoria_original[:, 1], color='red', label='Trayectoria Original', linewidth=2)

# Color para las trayectorias generadas
colors = plt.cm.viridis(np.linspace(0, 1, num_trayectorias))

# Ploteo de cada trayectoria generada
for i, trayectoria in enumerate(trayectorias):
    trayectoria = np.array(trayectoria)
    plt.plot(trayectoria[:, 0], trayectoria[:, 1], color=colors[i], alpha=0.5)

# Configuración del gráfico
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Trayectorias Generadas (Coordenadas X,Y)')
plt.grid()
plt.axis('equal')  # Para mantener la proporción
plt.legend()  # Agregar leyenda para la trayectoria original
plt.show()


# Extraer las trayectorias óptimas
trayectoria_4 = np.array(trayectorias[2])
trayectoria_0 = np.array(trayectorias[0])
trayectoria_51 = np.array(trayectorias[25])

# Graficar dicha trayectoria
plt.figure(figsize=(10, 8))
plt.plot(trayectoria_4[:, 0], trayectoria_4[:, 1], color='blue', label='Trayectoria 1', linewidth=2)
plt.plot(trayectoria_0[:, 0], trayectoria_0[:, 1], color='red', label='Trayectoria 0', linewidth=2)
plt.plot(trayectoria_51[:, 0], trayectoria_51[:, 1], color='green', label='Trayectoria 25', linewidth=2)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Posibles Trayectorias óptimas(Coordenadas X,Y)')
plt.grid()
plt.axis('equal')  # Para mantener la proporción
plt.legend()
plt.show()

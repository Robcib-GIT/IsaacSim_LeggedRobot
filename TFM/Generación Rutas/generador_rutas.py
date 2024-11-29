import numpy as np
import matplotlib.pyplot as plt

# Trayectoria original
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

# Número de trayectorias a generar
num_trayectorias = 100

# Incremento por iteración en las coordenadas x e y
incremento = 0.01

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
            # Variar solo los puntos intermedios con límite de 1
            desplazamiento_x = signo * min(incremento * i, 0.5)  # No exceder 1
            desplazamiento_y = signo * min(incremento * i, 0.5)  # No exceder 1
            new_wp = np.array([wp[0] + desplazamiento_x, wp[1] + desplazamiento_y, wp[2]])  # Mantener z constante
            nueva_trayectoria.append(new_wp)
    
    trayectorias.append(nueva_trayectoria)

# Convertir trayectorias a tuplas para encontrar únicas
trayectorias_tuplas = [tuple(map(tuple, trayectoria)) for trayectoria in trayectorias]
trayectorias_unicas = set(trayectorias_tuplas)  # Usar un conjunto para encontrar únicas

# Contar el número de trayectorias únicas
numero_trayectorias_unicas = len(trayectorias_unicas)

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


# Extraer la trayectoria 22 (índice 21)
trayectoria_4 = np.array(trayectorias[3])
trayectoria_32 = np.array(trayectorias[31])
trayectoria_0 = np.array(trayectorias[0])
trayectoria_51 = np.array(trayectorias[50])

# Graficar la trayectoria 22
plt.figure(figsize=(10, 8))
plt.plot(trayectoria_4[:, 0], trayectoria_4[:, 1], color='blue', label='Trayectoria 4', linewidth=2)
plt.plot(trayectoria_0[:, 0], trayectoria_0[:, 1], color='red', label='Trayectoria 0', linewidth=2)
plt.plot(trayectoria_32[:, 0], trayectoria_32[:, 1], color='green', label='Trayectoria 32', linewidth=2)
plt.plot(trayectoria_51[:, 0], trayectoria_51[:, 1], color='yellow', label='Trayectoria 51', linewidth=2)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Trayectoria 4 Generada (Coordenadas X,Y)')
plt.grid()
plt.axis('equal')  # Para mantener la proporción
plt.legend()
plt.show()

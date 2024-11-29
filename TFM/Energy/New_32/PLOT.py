import json
import matplotlib.pyplot as plt
import math

# Lista de nombres de archivos
archivos = ['sensor_readings.json', 'sensor_readings_1.json', 'sensor_readings_2.json', 'sensor_readings_3.json']

# Lista para almacenar los datos de cada archivo
datos = []

# Cargar los datos de cada archivo
for archivo in archivos:
    with open(archivo, 'r') as f:
        datos.append(json.load(f))

# Etiquetas para los sensores
etiquetas = [
    'FL_thigh_joint',  # Primer sensor
    'FR_thigh_joint',  # Segundo sensor
    'RL_thigh_joint',  # Tercer sensor
    'RR_thigh_joint'   # Cuarto sensor
]

# Calcular el número de filas necesarias para dos columnas
num_archivos = len(archivos)
num_filas = math.ceil(num_archivos / 2)

# Crear subplots con dos columnas
fig, axs = plt.subplots(num_filas, 2, figsize=(12, num_filas * 4), sharex=True)

# Aplanar los subplots para iterar fácilmente
axs = axs.flatten()

# Generar cada subplot
for i, data in enumerate(datos):
    axs[i].plot(data, label=f'{etiquetas[i]}', linewidth=1.5)
    axs[i].set_title(f"Values of effort {etiquetas[i]}")
    axs[i].set_ylabel("Effort (Nm)")
    axs[i].grid(True, linestyle='--', alpha=0.7)
    axs[i].legend()

# Ocultar subplots vacíos (si hay menos archivos que subplots)
for j in range(len(datos), len(axs)):
    axs[j].axis('off')

# Ajustar diseño
plt.xlabel("Samples")
plt.tight_layout()

# Mostrar el gráfico
plt.show()


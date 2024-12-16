import json
import os
import math

def carga_datos(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            # Cargar los datos desde el archivo JSON
            data = json.load(file)
            return data
    else:
        print(f"El archivo {file_path} no existe.")
        return []

def quita_nans(data):
    clean_data = []
    for value in data:
        if isinstance(value, float) and math.isnan(value):  # Si el valor es NaN
            continue  # Saltar este valor
        elif isinstance(value, str) and value.lower() == "nan":  # Si el valor es la cadena "NaN"
            continue  # Saltar este valor
        clean_data.append(value)
    return clean_data

def calcula(list1, list2):
    # Asegurarse de que las listas tengan la misma longitud
    if len(list1) != len(list2):
        print("Las listas no tienen la misma longitud.")
        print(len(list1))
        print(len(list2))
        return None

    # Calcular el producto elemento a elemento y sumarlos
    result = sum(x * y for x, y in zip(list1, list2))
    return result


def calcula_gasto_joint(list1,list2):
	effort = carga_datos(list1)
	velocity = carga_datos(list2)

	# Eliminar los valores 'NaN' de los datos cargados
	effort = quita_nans(effort)
	velocity = quita_nans(velocity)

        # Esto elimina los valores iniciales de la lista para que ambas sean iguales. Para el esfuerzo 1 para la 0. Para el esfuero, 2 para la 4.
	effort = effort[1:] 

	# Calcular el producto elemento a elemento de las dos listas y la suma total
	result = abs(calcula(effort, velocity))

	if result is not None:
	    print(f"El gasto energético de la articulación es {result} Julios")
	    return result


# Cargar los datos actuales desde los archivos
fl_thigh_effort_file_path = "/home/robcib/.local/share/ov/pkg/isaac-sim-4.2.0/TFM/Energy/sensor_readings.json"
fl_thigh_velocity_file_path = "/home/robcib/.local/share/ov/pkg/isaac-sim-4.2.0/TFM/Energy/FL_thigh_velocity.json"

fr_thigh_effort_file_path = "/home/robcib/.local/share/ov/pkg/isaac-sim-4.2.0/TFM/Energy/sensor_readings_1.json"
fr_thigh_velocity_file_path = "/home/robcib/.local/share/ov/pkg/isaac-sim-4.2.0/TFM/Energy/FR_thigh_velocity.json"

rl_thigh_effort_file_path = "/home/robcib/.local/share/ov/pkg/isaac-sim-4.2.0/TFM/Energy/sensor_readings_2.json"
rl_thigh_velocity_file_path = "/home/robcib/.local/share/ov/pkg/isaac-sim-4.2.0/TFM/Energy/RL_thigh_velocity.json"

rr_thigh_effort_file_path = "/home/robcib/.local/share/ov/pkg/isaac-sim-4.2.0/TFM/Energy/sensor_readings_3.json"
rr_thigh_velocity_file_path = "/home/robcib/.local/share/ov/pkg/isaac-sim-4.2.0/TFM/Energy/RR_thigh_velocity.json"

G1 = calcula_gasto_joint(fl_thigh_effort_file_path,fl_thigh_velocity_file_path)
G2 = calcula_gasto_joint(fr_thigh_effort_file_path,fr_thigh_velocity_file_path)
G3 = calcula_gasto_joint(rl_thigh_effort_file_path,rl_thigh_velocity_file_path)
G4 = calcula_gasto_joint(rr_thigh_effort_file_path,rr_thigh_velocity_file_path)

Gasto_Total = G1+G2+G3+G4
print(Gasto_Total)




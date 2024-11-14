#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState
import matplotlib.pyplot as plt
import json
import os

# Diccionario para almacenar las posiciones, velocidades y esfuerzos por articulación
joint_data = {
    'FL_hip': {'position': [], 'velocity': [], 'effort': []},
    'FR_hip': {'position': [], 'velocity': [], 'effort': []},
    'RL_hip': {'position': [], 'velocity': [], 'effort': []},
    'RR_hip': {'position': [], 'velocity': [], 'effort': []},
    'FL_thigh': {'position': [], 'velocity': [], 'effort': []},
    'FR_thigh': {'position': [], 'velocity': [], 'effort': []},
    'RL_thigh': {'position': [], 'velocity': [], 'effort': []},
    'RR_thigh': {'position': [], 'velocity': [], 'effort': []},
    'FL_calf': {'position': [], 'velocity': [], 'effort': []},
    'FR_calf': {'position': [], 'velocity': [], 'effort': []},
    'RL_calf': {'position': [], 'velocity': [], 'effort': []},
    'RR_calf': {'position': [], 'velocity': [], 'effort': []}
}

def pose_callback(msg: JointState):
    if len(msg.position) == 12 and len(msg.velocity) == 12 and len(msg.effort) == 12:
        joint_names = list(joint_data.keys())
        for i in range(12):
            joint_data[joint_names[i]]['position'].append(msg.position[i])
            joint_data[joint_names[i]]['velocity'].append(msg.velocity[i])
            joint_data[joint_names[i]]['effort'].append(msg.effort[i])

        rospy.loginfo("Updated positions, velocities, and efforts for all joints.")
    else:
        rospy.logwarn("Received joint states with unexpected size.")

def plot_joint_positions():
    # Crear la primera figura con 2 filas y 3 columnas (6 subgráficos)
    plt.figure(figsize=(18, 8))
    positions = [
        joint_data['FL_hip']['position'], joint_data['FR_hip']['position'],
        joint_data['RL_hip']['position'], joint_data['RR_hip']['position'],
        joint_data['FL_thigh']['position'], joint_data['FR_thigh']['position']
    ]
    labels = [
        'FL Hip Position', 'FR Hip Position', 'RL Hip Position', 'RR Hip Position',
        'FL Thigh Position', 'FR Thigh Position'
    ]

    for i in range(6):
        plt.subplot(2, 3, i + 1)
        plt.plot(positions[i][50:], label=labels[i])
        plt.title(f'{labels[i]} Over Time')
        plt.xlabel('Samples')
        plt.ylabel('Position')
        plt.legend()
        plt.grid()

    plt.suptitle('Joint Positions Over Time (1)')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show(block=False)

    plt.figure(figsize=(18, 8))
    positions = [
        joint_data['RL_thigh']['position'], joint_data['RR_thigh']['position'],
        joint_data['FL_calf']['position'], joint_data['FR_calf']['position'],
        joint_data['RL_calf']['position'], joint_data['RR_calf']['position']
    ]
    labels = [
        'RL Thigh Position', 'RR Thigh Position', 'FL Calf Position', 'FR Calf Position',
        'RL Calf Position', 'RR Calf Position'
    ]

    for i in range(6):
        plt.subplot(2, 3, i + 1)
        plt.plot(positions[i][50:], label=labels[i])
        plt.title(f'{labels[i]} Over Time')
        plt.xlabel('Samples')
        plt.ylabel('Position')
        plt.legend()
        plt.grid()

    plt.suptitle('Joint Positions Over Time (2)')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

def save_data_as_json():
    output_directory = "data_files"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Iterar sobre las articulaciones y guardar los datos de velocidad por separado
    for joint_name, data in joint_data.items():
        # Crear el nombre del archivo para cada articulación
        file_path = os.path.join(output_directory, f"{joint_name}_velocity.json")
        
        # Guardar solo los valores de velocidad
        with open(file_path, "w") as file:
            json.dump(data['velocity'], file)
        
        rospy.loginfo(f"Velocity data for {joint_name} has been saved to {file_path}")



if __name__ == '__main__':
    rospy.init_node("Plot_Node")

    sub = rospy.Subscriber("/joint_states", JointState, callback=pose_callback)
    rospy.loginfo("Node has been started")

    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
    finally:
        plot_joint_positions()
        save_data_as_json()


#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState

# Diccionarios para almacenar posiciones, velocidades, esfuerzos y energía por articulación
joints = {
    "FL_hip": {"position": [], "velocity": [], "effort": [], "energy": 0},
    "FR_hip": {"position": [], "velocity": [], "effort": [], "energy": 0},
    "RL_hip": {"position": [], "velocity": [], "effort": [], "energy": 0},
    "RR_hip": {"position": [], "velocity": [], "effort": [], "energy": 0},
    "FL_thigh": {"position": [], "velocity": [], "effort": [], "energy": 0},
    "FR_thigh": {"position": [], "velocity": [], "effort": [], "energy": 0},
    "RL_thigh": {"position": [], "velocity": [], "effort": [], "energy": 0},
    "RR_thigh": {"position": [], "velocity": [], "effort": [], "energy": 0},
    "FL_calf": {"position": [], "velocity": [], "effort": [], "energy": 0},
    "FR_calf": {"position": [], "velocity": [], "effort": [], "energy": 0},
    "RL_calf": {"position": [], "velocity": [], "effort": [], "energy": 0},
    "RR_calf": {"position": [], "velocity": [], "effort": [], "energy": 0}
}

# Guardamos el último timestamp para calcular la diferencia de tiempo
last_time = None

def pose_callback(msg: JointState):
    global last_time, joints

    # Obtener el tiempo actual desde el mensaje
    current_time = msg.header.stamp.to_sec()

    # Calcular la diferencia de tiempo (delta t) desde el último mensaje
    delta_time = current_time - last_time if last_time else 0

    # Verificar que las longitudes de las listas sean correctas
    if len(msg.position) == 12 and len(msg.velocity) == 12 and len(msg.effort) == 12:
        if delta_time > 0:  # Evitar cálculo con delta_time = 0
            # Nombres de articulaciones ordenados como en los índices de JointState
            joint_names = list(joints.keys())
            for i, joint_name in enumerate(joint_names):
                joints[joint_name]["position"].append(msg.position[i])
                joints[joint_name]["velocity"].append(msg.velocity[i])
                joints[joint_name]["effort"].append(msg.effort[i])
                
                # Calcular potencia y sumar energía
                power = abs(msg.effort[i] * msg.velocity[i]) * 256  # Factor de potencia
                joints[joint_name]["energy"] += power * delta_time

        # Actualizar el último timestamp
        last_time = current_time

        rospy.loginfo("Updated positions, velocities, and efforts for all joints.")
    else:
        rospy.logwarn("Received joint states with unexpected size.")

def print_total_energy():
    # Calcular la energía total sumando la energía de todas las articulaciones
    total_energy = sum(joints[joint]["energy"] for joint in joints)
    rospy.loginfo("Total Energy Across All Joints: %.2f Joules", total_energy)

if __name__ == '__main__':
    rospy.init_node("Energy_Node")
    sub = rospy.Subscriber("/joint_states", JointState, callback=pose_callback)
    rospy.loginfo("Node has been started")

    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
    finally:
        # Imprimir la energía total al final de la ejecución
        print_total_energy()


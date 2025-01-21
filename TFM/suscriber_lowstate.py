import rclpy
from rclpy.node import Node
from unitree_go.msg import LowState
import os
import csv

# Configuración de las banderas
INFO_IMU = 1  # Guardar estado del IMU
INFO_FOOT_FORCE = 1  # Guardar fuerzas de las patas
INFO_BATTERY = 1  # Guardar estado de la batería
INFO_TEMPERATURE = 1  # Guardar temperaturas
HIGH_FREQ = 0  # Suscribirse a estados bajos a alta frecuencia (500Hz)

class LowStateToFile(Node):
    def __init__(self):
        super().__init__('low_state_to_file')

        # Crear carpeta para guardar los resultados
        self.result_dir = self.create_results_dir()
        
        # Archivos CSV para los diferentes tipos de datos
        self.imu_file = open(os.path.join(self.result_dir, "imu_state.csv"), "w", newline="") if INFO_IMU else None
        self.foot_force_file = open(os.path.join(self.result_dir, "foot_force.csv"), "w", newline="") if INFO_FOOT_FORCE else None
        self.battery_file = open(os.path.join(self.result_dir, "battery_state.csv"), "w", newline="") if INFO_BATTERY else None
        self.temperature_file = open(os.path.join(self.result_dir, "temperature.csv"), "w", newline="") if INFO_TEMPERATURE else None

        # Configuración del escritor CSV para los datos IMU
        if self.imu_file:
            self.imu_writer = csv.writer(self.imu_file)
            # Escribir el encabezado del archivo CSV
            self.imu_writer.writerow([
                "Timestamp", "Roll", "Pitch", "Yaw", 
                "qw", "qx", "qy", "qz", 
                "wx", "wy", "wz", 
                "ax", "ay", "az"
            ])

        # Configuración del escritor CSV para los datos de las patas
        if self.foot_force_file:
            self.foot_force_writer = csv.writer(self.foot_force_file)
            # Escribir el encabezado del archivo CSV
            self.foot_force_writer.writerow([
                "Timestamp", "foot0", "foot1", "foot2", "foot3", "foot0_est", "foot1_est", "foot2_est", "foot3_est"
            ])

        # Configuración del escritor CSV para los datos de la batería
        if self.battery_file:
            self.battery_writer = csv.writer(self.battery_file)
            # Escribir el encabezado del archivo CSV
            self.battery_writer.writerow([
                "Timestamp", "Current", "Voltage"
            ])

        # Configuración del escritor CSV para los datos de temperatura
        if self.temperature_file:
            self.temperature_writer = csv.writer(self.temperature_file)
            # Escribir el encabezado del archivo CSV
            self.temperature_writer.writerow([
                "Timestamp", "Temperature NTC1", "Temperature NTC2"
            ])

        # Determina el tópico a suscribirse
        topic_name = "lf/lowstate" if not HIGH_FREQ else "lowstate"
        
        # Configuración del suscriptor
        self.subscription = self.create_subscription(
            LowState,
            topic_name,
            self.topic_callback,
            10
        )
        self.subscription  # Evitar advertencias sobre variable no usada

    def create_results_dir(self):
        """Crea una carpeta única para guardar los resultados."""
        base_dir = "Prueba"
        i = 1
        while os.path.exists(f"{base_dir} {i}"):
            i += 1
        dir_name = f"{base_dir} {i}"
        os.makedirs(dir_name)
        self.get_logger().info(f"Resultados se guardarán en: {dir_name}")
        return dir_name

    def topic_callback(self, msg):
        timestamp = self.get_clock().now().to_msg().sec  # Usar el tiempo del mensaje como timestamp

        if INFO_IMU:
            imu = msg.imu_state
            imu_data = [
                timestamp, 
                round(float(imu.rpy[0]), 2),
                round(float(imu.rpy[1]), 2),
                round(float(imu.rpy[2]), 2),
                round(float(imu.quaternion[0]), 2),
                round(float(imu.quaternion[1]), 2),
                round(float(imu.quaternion[2]), 2),
                round(float(imu.quaternion[3]), 2),
                round(float(imu.gyroscope[0]), 2),
                round(float(imu.gyroscope[1]), 2),
                round(float(imu.gyroscope[2]), 2),
                round(float(imu.accelerometer[0]), 2),
                round(float(imu.accelerometer[1]), 2),
                round(float(imu.accelerometer[2]), 2)
            ]
            # Escribir los datos de IMU en el archivo CSV
            self.imu_writer.writerow(imu_data)
            self.imu_file.flush()

        if INFO_FOOT_FORCE:
            foot_force = msg.foot_force
            foot_force_est = msg.foot_force_est
            foot_force_data = [
                timestamp,
                foot_force[0], foot_force[1], foot_force[2], foot_force[3],
                foot_force_est[0], foot_force_est[1], foot_force_est[2], foot_force_est[3]
            ]
            # Escribir los datos de las fuerzas de las patas en el archivo CSV
            self.foot_force_writer.writerow(foot_force_data)
            self.foot_force_file.flush()

        if INFO_BATTERY:
            battery_current = msg.power_a
            battery_voltage = msg.power_v
            battery_data = [
                timestamp,
                round(battery_current, 2),
                round(battery_voltage, 2)
            ]
            # Escribir los datos de la batería en el archivo CSV
            self.battery_writer.writerow(battery_data)
            self.battery_file.flush()

        if INFO_TEMPERATURE:
            temperature_ntc1 = msg.temperature_ntc1
            temperature_ntc2 = msg.temperature_ntc2
            temperature_data = [
                timestamp,
                round(temperature_ntc1, 2),
                round(temperature_ntc2, 2)
            ]
            # Escribir los datos de temperatura en el archivo CSV
            self.temperature_writer.writerow(temperature_data)
            self.temperature_file.flush()

    def destroy_node(self):
        # Cierra los archivos al destruir el nodo
        if self.imu_file:
            self.imu_file.close()
        if self.foot_force_file:
            self.foot_force_file.close()
        if self.battery_file:
            self.battery_file.close()
        if self.temperature_file:
            self.temperature_file.close()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = LowStateToFile()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()


# Evaluación de marcha de robot cuadrúpedo en entornos de desastre
Este repositorio contiene los principales archivos que conforman el TFM "*Evaluación de marcha de robot cuadrúpedo en entornos de desastre*" desarrollado en la Universidad Politécnica de Madrid. 
En dichos ficheros, se muestra el controlador de un robot cuadrúpedo "Unitree Go1" que permite la navegación del mismo en un entorno con obstáculos. Su funcionamiento se basa en el seguimiento de una lista de waypoints desde un punto inicial "A" hasta un punto final "B". Además, en el repositorio se encuentran los mapas de pruebas diseñados, el workspace de ROS Noetic utilizado para realizar un breve análisis cinemático, un planificador de trayectorias y varios vídeos mostrando el funcionamiento del robot.



https://github.com/user-attachments/assets/daa4d364-9b8e-428e-b577-c4ccabf2ac88



Requerimientos
=============
Para el correcto funcionamiento de los programas, se requiere tener instalado:

- Ubuntu 20.04
- Isaac Sim 4.2 
- Nvidia Driver 555
- Cuda 11.8. 
- Ros Noetic

Instalación
=============
1. Clona el repositorio de Github en tu equipo:
`$git clone https://github.com/JTlotus/TFM_Jorge.git`

2.  Sitúa la carpeta "TFM" dentro de tu carpeta de instalación de IsaacSim
`$cd .local/share/ov/pkg/isaac-sim-4.2.0`

3. Copia el workspace "ros_ws" en el escritorio y compílalo.

4. Sigue los pasos de [instalación del entorno Python](https://docs.omniverse.nvidia.com/isaacsim/latest/installation/install_python.html "link title") para crear correctamente el entorno de trabajo.

5. Descarga las librerías "Matplotlib" y "Skfuzzy" mediante el siguiente comando:
`$./python.sh -m pip install name_of_package_here`

Procedimiento
=============

Para reproducir correctamente el script de funcionamiento, se han de seguir los siguientes pasos:

1. Inicializa "roscore" en la terminal
2. Activa el nodo de ROS. Dicho nodo se encuentra en ros_ws/src/joint_visualization/scripts
`$python plot_node.py`

3. Inicializa el script de funcionamiento desde la carpeta de instalación de IsaacSim:
`$./python.sh TFM/go1_standalone.py`

4. Disfruta de la simulación!

**Atención**: Puede que, al iniciar la simulación, IsaacSim tarde en arrancar. En algunos casos, suele aparecer una ventana de error para cancelar la simulación. Ignora estas advertencias y sigue con la prueba hasta que comience. Es necesario mover la cámara nada más comenzar, puesto que la posición inicial se encuentra tapada con una pared.

**Sugerencia**: Es posible modificar la ruta de movimiento del robot. Para ello, sitúese en la carpeta TFM/Rutas y seleccione la ruta deseada. Para cambiar la ruta, basta con modificar la lista "waypoints" del script `go1_standalone.py` por los waypoints deseados.

Resultados
=============
Dentro de tu carpeta de instalación de IsaacSim se generará una carpeta“Resultados” con varias gráficas de la trayectoria implementada. Estas gráficas muestran el recorrido llevado a cabo en la simulación, así como el error existente en cada waypoint. Si se detiene el nodo de ROS, se observarán las gráficas de las posiciones de las articulaciones que el robot presenta a lo largo del recorrido.

Elementos multimedia
=============
A continuación, se pone a disposición un enlace con el canal de Youtube del proyecto, donde se pueden observar los vídeos de las diferentes pruebas realizadas: [Enlace al canal de youtube](https://www.youtube.com/channel/UCgoBx4u17_1CNACcc3sLeRA)

En dicho canal, se pueden observar varias listas de reproducción correspondientes a todos los escenarios analizados durante el proyecto. Además, se muestra un vídeo de la política de locomoción entrenada con IsaacLab.


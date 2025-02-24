# Evaluation of quadruped robot gait in disaster environments
This repository contains the main files that make up the TFM "*Evaluation of quadruped robot gait in disaster environments*" developed at the Polytechnic University of Madrid.
These files show the controller of a quadruped robot "Unitree Go1" that allows the robot to navigate in an environment with obstacles. Its operation is based on following a list of waypoints from a start point "A" to a final point "B". In addition, the repository contains the designed test maps, the ROS Noetic workspace used to perform a brief kinematic analysis, a trajectory planner and several videos showing the robot's operation.

https://github.com/user-attachments/assets/daa4d364-9b8e-428e-b577-c4ccabf2ac88



Requirements
=============
For the correct operation of the programs, it is required to have installed:

- Ubuntu 20.04
- Isaac Sim 4.2 
- Nvidia Driver 555
- Cuda 11.8. 
- Ros Noetic

Installation
=============
1. Clone the Github repository to your computer:
`$git clone https://github.com/JTlotus/TFM_Jorge.git`

2. Place the "TFM" folder inside your IsaacSim installation folder
`$cd .local/share/ov/pkg/isaac-sim-4.2.0`

3. Copy the "ros_ws" workspace to your desktop and compile it.

4. Follow the steps in [Installing the Python Environment]](https://docs.omniverse.nvidia.com/isaacsim/latest/installation/install_python.html "link title") para crear correctamente el entorno de trabajo.

5. Download the "Matplotlib" and "Skfuzzy" libraries using the following command:
`$./python.sh -m pip install name_of_package_here`

Procedure
=============

To correctly reproduce the working script, the following steps must be followed:

1. Initialize "roscore" in the terminal
2. Activate the ROS node. This node is located at ros_ws/src/joint_visualization/scripts
`$python plot_node.py`

3. Initialize the running script from the IsaacSim installation folder:
`$./python.sh TFM/go1_standalone.py`

4. Enjoy the simulation!

**Note**: IsaacSim may take a while to start when you start the simulation. In some cases, an error window will appear asking you to cancel the simulation. Ignore these warnings and continue with the test until it starts. It is necessary to move the camera as soon as it starts, since the initial position is covered by a wall.

**Tip**: It is possible to modify the robot's movement path. To do this, go to the TFM/Routes folder and select the desired path. To change the path, simply modify the "waypoints" list of the `go1_standalone.py` script with the desired waypoints.

Results
=============
Inside your IsaacSim installation folder, a “Results” folder will be generated with several graphs of the implemented path. These graphs show the path taken in the simulation, as well as the error at each waypoint.
![puntos_visitados_nave](https://github.com/user-attachments/assets/2da06b9b-fe87-4482-91c6-e8e156a97058)


![errores_waypoints_nave](https://github.com/user-attachments/assets/e337fb8f-e838-4f99-ae35-c2fe62094a92)



If the ROS node is stopped, graphs of the robot's joint positions along the path will be observed.

![Nave_joints_position_1](https://github.com/user-attachments/assets/d9793afa-5d04-4ef2-90ee-47e2ce503b90)


Multimedia elements
=============
Below is a link to the project's YouTube channel, where you can watch videos of the different tests carried out: [Link to the YouTube channel](https://www.youtube.com/channel/UCgoBx4u17_1CNACcc3sLeRA)

On this channel, you can see several playlists corresponding to all the scenarios analyzed during the project. In addition, a video of the locomotion policy trained with IsaacLab is shown.

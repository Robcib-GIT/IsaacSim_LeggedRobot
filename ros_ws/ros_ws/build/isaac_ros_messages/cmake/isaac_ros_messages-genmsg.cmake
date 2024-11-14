# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "isaac_ros_messages: 0 messages, 1 services")

set(MSG_I_FLAGS "-Igeometry_msgs:/opt/ros/noetic/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(isaac_ros_messages_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/robcib/ros_ws/src/isaac_ros_messages/srv/IsaacPose.srv" NAME_WE)
add_custom_target(_isaac_ros_messages_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "isaac_ros_messages" "/home/robcib/ros_ws/src/isaac_ros_messages/srv/IsaacPose.srv" "std_msgs/Header:geometry_msgs/Pose:geometry_msgs/Vector3:geometry_msgs/Point:geometry_msgs/Twist:geometry_msgs/Quaternion"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(isaac_ros_messages
  "/home/robcib/ros_ws/src/isaac_ros_messages/srv/IsaacPose.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/isaac_ros_messages
)

### Generating Module File
_generate_module_cpp(isaac_ros_messages
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/isaac_ros_messages
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(isaac_ros_messages_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(isaac_ros_messages_generate_messages isaac_ros_messages_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robcib/ros_ws/src/isaac_ros_messages/srv/IsaacPose.srv" NAME_WE)
add_dependencies(isaac_ros_messages_generate_messages_cpp _isaac_ros_messages_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(isaac_ros_messages_gencpp)
add_dependencies(isaac_ros_messages_gencpp isaac_ros_messages_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS isaac_ros_messages_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services
_generate_srv_eus(isaac_ros_messages
  "/home/robcib/ros_ws/src/isaac_ros_messages/srv/IsaacPose.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/isaac_ros_messages
)

### Generating Module File
_generate_module_eus(isaac_ros_messages
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/isaac_ros_messages
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(isaac_ros_messages_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(isaac_ros_messages_generate_messages isaac_ros_messages_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robcib/ros_ws/src/isaac_ros_messages/srv/IsaacPose.srv" NAME_WE)
add_dependencies(isaac_ros_messages_generate_messages_eus _isaac_ros_messages_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(isaac_ros_messages_geneus)
add_dependencies(isaac_ros_messages_geneus isaac_ros_messages_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS isaac_ros_messages_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(isaac_ros_messages
  "/home/robcib/ros_ws/src/isaac_ros_messages/srv/IsaacPose.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/isaac_ros_messages
)

### Generating Module File
_generate_module_lisp(isaac_ros_messages
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/isaac_ros_messages
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(isaac_ros_messages_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(isaac_ros_messages_generate_messages isaac_ros_messages_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robcib/ros_ws/src/isaac_ros_messages/srv/IsaacPose.srv" NAME_WE)
add_dependencies(isaac_ros_messages_generate_messages_lisp _isaac_ros_messages_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(isaac_ros_messages_genlisp)
add_dependencies(isaac_ros_messages_genlisp isaac_ros_messages_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS isaac_ros_messages_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services
_generate_srv_nodejs(isaac_ros_messages
  "/home/robcib/ros_ws/src/isaac_ros_messages/srv/IsaacPose.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/isaac_ros_messages
)

### Generating Module File
_generate_module_nodejs(isaac_ros_messages
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/isaac_ros_messages
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(isaac_ros_messages_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(isaac_ros_messages_generate_messages isaac_ros_messages_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robcib/ros_ws/src/isaac_ros_messages/srv/IsaacPose.srv" NAME_WE)
add_dependencies(isaac_ros_messages_generate_messages_nodejs _isaac_ros_messages_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(isaac_ros_messages_gennodejs)
add_dependencies(isaac_ros_messages_gennodejs isaac_ros_messages_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS isaac_ros_messages_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(isaac_ros_messages
  "/home/robcib/ros_ws/src/isaac_ros_messages/srv/IsaacPose.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/isaac_ros_messages
)

### Generating Module File
_generate_module_py(isaac_ros_messages
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/isaac_ros_messages
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(isaac_ros_messages_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(isaac_ros_messages_generate_messages isaac_ros_messages_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robcib/ros_ws/src/isaac_ros_messages/srv/IsaacPose.srv" NAME_WE)
add_dependencies(isaac_ros_messages_generate_messages_py _isaac_ros_messages_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(isaac_ros_messages_genpy)
add_dependencies(isaac_ros_messages_genpy isaac_ros_messages_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS isaac_ros_messages_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/isaac_ros_messages)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/isaac_ros_messages
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(isaac_ros_messages_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(isaac_ros_messages_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/isaac_ros_messages)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/isaac_ros_messages
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(isaac_ros_messages_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(isaac_ros_messages_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/isaac_ros_messages)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/isaac_ros_messages
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(isaac_ros_messages_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(isaac_ros_messages_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/isaac_ros_messages)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/isaac_ros_messages
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(isaac_ros_messages_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(isaac_ros_messages_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/isaac_ros_messages)
  install(CODE "execute_process(COMMAND \"/home/robcib/anaconda3/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/isaac_ros_messages\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/isaac_ros_messages
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(isaac_ros_messages_generate_messages_py geometry_msgs_generate_messages_py)
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(isaac_ros_messages_generate_messages_py std_msgs_generate_messages_py)
endif()

# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "cortex_control: 2 messages, 1 services")

set(MSG_I_FLAGS "-Icortex_control:/home/robcib/ros_ws/src/cortex_control/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(cortex_control_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/robcib/ros_ws/src/cortex_control/msg/JointPosVelAccCommand.msg" NAME_WE)
add_custom_target(_cortex_control_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "cortex_control" "/home/robcib/ros_ws/src/cortex_control/msg/JointPosVelAccCommand.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/robcib/ros_ws/src/cortex_control/msg/CortexCommandAck.msg" NAME_WE)
add_custom_target(_cortex_control_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "cortex_control" "/home/robcib/ros_ws/src/cortex_control/msg/CortexCommandAck.msg" ""
)

get_filename_component(_filename "/home/robcib/ros_ws/src/cortex_control/srv/MsgService.srv" NAME_WE)
add_custom_target(_cortex_control_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "cortex_control" "/home/robcib/ros_ws/src/cortex_control/srv/MsgService.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(cortex_control
  "/home/robcib/ros_ws/src/cortex_control/msg/JointPosVelAccCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cortex_control
)
_generate_msg_cpp(cortex_control
  "/home/robcib/ros_ws/src/cortex_control/msg/CortexCommandAck.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cortex_control
)

### Generating Services
_generate_srv_cpp(cortex_control
  "/home/robcib/ros_ws/src/cortex_control/srv/MsgService.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cortex_control
)

### Generating Module File
_generate_module_cpp(cortex_control
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cortex_control
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(cortex_control_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(cortex_control_generate_messages cortex_control_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robcib/ros_ws/src/cortex_control/msg/JointPosVelAccCommand.msg" NAME_WE)
add_dependencies(cortex_control_generate_messages_cpp _cortex_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robcib/ros_ws/src/cortex_control/msg/CortexCommandAck.msg" NAME_WE)
add_dependencies(cortex_control_generate_messages_cpp _cortex_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robcib/ros_ws/src/cortex_control/srv/MsgService.srv" NAME_WE)
add_dependencies(cortex_control_generate_messages_cpp _cortex_control_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(cortex_control_gencpp)
add_dependencies(cortex_control_gencpp cortex_control_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS cortex_control_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(cortex_control
  "/home/robcib/ros_ws/src/cortex_control/msg/JointPosVelAccCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/cortex_control
)
_generate_msg_eus(cortex_control
  "/home/robcib/ros_ws/src/cortex_control/msg/CortexCommandAck.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/cortex_control
)

### Generating Services
_generate_srv_eus(cortex_control
  "/home/robcib/ros_ws/src/cortex_control/srv/MsgService.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/cortex_control
)

### Generating Module File
_generate_module_eus(cortex_control
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/cortex_control
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(cortex_control_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(cortex_control_generate_messages cortex_control_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robcib/ros_ws/src/cortex_control/msg/JointPosVelAccCommand.msg" NAME_WE)
add_dependencies(cortex_control_generate_messages_eus _cortex_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robcib/ros_ws/src/cortex_control/msg/CortexCommandAck.msg" NAME_WE)
add_dependencies(cortex_control_generate_messages_eus _cortex_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robcib/ros_ws/src/cortex_control/srv/MsgService.srv" NAME_WE)
add_dependencies(cortex_control_generate_messages_eus _cortex_control_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(cortex_control_geneus)
add_dependencies(cortex_control_geneus cortex_control_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS cortex_control_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(cortex_control
  "/home/robcib/ros_ws/src/cortex_control/msg/JointPosVelAccCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cortex_control
)
_generate_msg_lisp(cortex_control
  "/home/robcib/ros_ws/src/cortex_control/msg/CortexCommandAck.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cortex_control
)

### Generating Services
_generate_srv_lisp(cortex_control
  "/home/robcib/ros_ws/src/cortex_control/srv/MsgService.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cortex_control
)

### Generating Module File
_generate_module_lisp(cortex_control
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cortex_control
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(cortex_control_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(cortex_control_generate_messages cortex_control_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robcib/ros_ws/src/cortex_control/msg/JointPosVelAccCommand.msg" NAME_WE)
add_dependencies(cortex_control_generate_messages_lisp _cortex_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robcib/ros_ws/src/cortex_control/msg/CortexCommandAck.msg" NAME_WE)
add_dependencies(cortex_control_generate_messages_lisp _cortex_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robcib/ros_ws/src/cortex_control/srv/MsgService.srv" NAME_WE)
add_dependencies(cortex_control_generate_messages_lisp _cortex_control_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(cortex_control_genlisp)
add_dependencies(cortex_control_genlisp cortex_control_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS cortex_control_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(cortex_control
  "/home/robcib/ros_ws/src/cortex_control/msg/JointPosVelAccCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/cortex_control
)
_generate_msg_nodejs(cortex_control
  "/home/robcib/ros_ws/src/cortex_control/msg/CortexCommandAck.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/cortex_control
)

### Generating Services
_generate_srv_nodejs(cortex_control
  "/home/robcib/ros_ws/src/cortex_control/srv/MsgService.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/cortex_control
)

### Generating Module File
_generate_module_nodejs(cortex_control
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/cortex_control
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(cortex_control_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(cortex_control_generate_messages cortex_control_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robcib/ros_ws/src/cortex_control/msg/JointPosVelAccCommand.msg" NAME_WE)
add_dependencies(cortex_control_generate_messages_nodejs _cortex_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robcib/ros_ws/src/cortex_control/msg/CortexCommandAck.msg" NAME_WE)
add_dependencies(cortex_control_generate_messages_nodejs _cortex_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robcib/ros_ws/src/cortex_control/srv/MsgService.srv" NAME_WE)
add_dependencies(cortex_control_generate_messages_nodejs _cortex_control_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(cortex_control_gennodejs)
add_dependencies(cortex_control_gennodejs cortex_control_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS cortex_control_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(cortex_control
  "/home/robcib/ros_ws/src/cortex_control/msg/JointPosVelAccCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cortex_control
)
_generate_msg_py(cortex_control
  "/home/robcib/ros_ws/src/cortex_control/msg/CortexCommandAck.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cortex_control
)

### Generating Services
_generate_srv_py(cortex_control
  "/home/robcib/ros_ws/src/cortex_control/srv/MsgService.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cortex_control
)

### Generating Module File
_generate_module_py(cortex_control
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cortex_control
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(cortex_control_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(cortex_control_generate_messages cortex_control_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robcib/ros_ws/src/cortex_control/msg/JointPosVelAccCommand.msg" NAME_WE)
add_dependencies(cortex_control_generate_messages_py _cortex_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robcib/ros_ws/src/cortex_control/msg/CortexCommandAck.msg" NAME_WE)
add_dependencies(cortex_control_generate_messages_py _cortex_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/robcib/ros_ws/src/cortex_control/srv/MsgService.srv" NAME_WE)
add_dependencies(cortex_control_generate_messages_py _cortex_control_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(cortex_control_genpy)
add_dependencies(cortex_control_genpy cortex_control_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS cortex_control_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cortex_control)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cortex_control
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(cortex_control_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/cortex_control)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/cortex_control
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(cortex_control_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cortex_control)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cortex_control
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(cortex_control_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/cortex_control)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/cortex_control
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(cortex_control_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cortex_control)
  install(CODE "execute_process(COMMAND \"/home/robcib/anaconda3/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cortex_control\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cortex_control
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(cortex_control_generate_messages_py std_msgs_generate_messages_py)
endif()

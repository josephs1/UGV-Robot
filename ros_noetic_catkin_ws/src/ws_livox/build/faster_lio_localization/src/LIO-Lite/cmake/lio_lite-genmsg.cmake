# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "lio_lite: 1 messages, 0 services")

set(MSG_I_FLAGS "-Ilio_lite:/home/jstefan1/Documents/CodeWorkspace/UGV-Robot/ros_noetic_catkin_ws/src/ws_livox/src/faster_lio_localization/src/LIO-Lite/msg;-Igeometry_msgs:/opt/ros/noetic/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(lio_lite_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/jstefan1/Documents/CodeWorkspace/UGV-Robot/ros_noetic_catkin_ws/src/ws_livox/src/faster_lio_localization/src/LIO-Lite/msg/Pose6D.msg" NAME_WE)
add_custom_target(_lio_lite_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "lio_lite" "/home/jstefan1/Documents/CodeWorkspace/UGV-Robot/ros_noetic_catkin_ws/src/ws_livox/src/faster_lio_localization/src/LIO-Lite/msg/Pose6D.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(lio_lite
  "/home/jstefan1/Documents/CodeWorkspace/UGV-Robot/ros_noetic_catkin_ws/src/ws_livox/src/faster_lio_localization/src/LIO-Lite/msg/Pose6D.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/lio_lite
)

### Generating Services

### Generating Module File
_generate_module_cpp(lio_lite
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/lio_lite
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(lio_lite_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(lio_lite_generate_messages lio_lite_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/jstefan1/Documents/CodeWorkspace/UGV-Robot/ros_noetic_catkin_ws/src/ws_livox/src/faster_lio_localization/src/LIO-Lite/msg/Pose6D.msg" NAME_WE)
add_dependencies(lio_lite_generate_messages_cpp _lio_lite_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(lio_lite_gencpp)
add_dependencies(lio_lite_gencpp lio_lite_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS lio_lite_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(lio_lite
  "/home/jstefan1/Documents/CodeWorkspace/UGV-Robot/ros_noetic_catkin_ws/src/ws_livox/src/faster_lio_localization/src/LIO-Lite/msg/Pose6D.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/lio_lite
)

### Generating Services

### Generating Module File
_generate_module_eus(lio_lite
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/lio_lite
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(lio_lite_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(lio_lite_generate_messages lio_lite_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/jstefan1/Documents/CodeWorkspace/UGV-Robot/ros_noetic_catkin_ws/src/ws_livox/src/faster_lio_localization/src/LIO-Lite/msg/Pose6D.msg" NAME_WE)
add_dependencies(lio_lite_generate_messages_eus _lio_lite_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(lio_lite_geneus)
add_dependencies(lio_lite_geneus lio_lite_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS lio_lite_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(lio_lite
  "/home/jstefan1/Documents/CodeWorkspace/UGV-Robot/ros_noetic_catkin_ws/src/ws_livox/src/faster_lio_localization/src/LIO-Lite/msg/Pose6D.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/lio_lite
)

### Generating Services

### Generating Module File
_generate_module_lisp(lio_lite
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/lio_lite
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(lio_lite_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(lio_lite_generate_messages lio_lite_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/jstefan1/Documents/CodeWorkspace/UGV-Robot/ros_noetic_catkin_ws/src/ws_livox/src/faster_lio_localization/src/LIO-Lite/msg/Pose6D.msg" NAME_WE)
add_dependencies(lio_lite_generate_messages_lisp _lio_lite_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(lio_lite_genlisp)
add_dependencies(lio_lite_genlisp lio_lite_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS lio_lite_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(lio_lite
  "/home/jstefan1/Documents/CodeWorkspace/UGV-Robot/ros_noetic_catkin_ws/src/ws_livox/src/faster_lio_localization/src/LIO-Lite/msg/Pose6D.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/lio_lite
)

### Generating Services

### Generating Module File
_generate_module_nodejs(lio_lite
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/lio_lite
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(lio_lite_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(lio_lite_generate_messages lio_lite_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/jstefan1/Documents/CodeWorkspace/UGV-Robot/ros_noetic_catkin_ws/src/ws_livox/src/faster_lio_localization/src/LIO-Lite/msg/Pose6D.msg" NAME_WE)
add_dependencies(lio_lite_generate_messages_nodejs _lio_lite_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(lio_lite_gennodejs)
add_dependencies(lio_lite_gennodejs lio_lite_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS lio_lite_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(lio_lite
  "/home/jstefan1/Documents/CodeWorkspace/UGV-Robot/ros_noetic_catkin_ws/src/ws_livox/src/faster_lio_localization/src/LIO-Lite/msg/Pose6D.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/lio_lite
)

### Generating Services

### Generating Module File
_generate_module_py(lio_lite
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/lio_lite
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(lio_lite_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(lio_lite_generate_messages lio_lite_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/jstefan1/Documents/CodeWorkspace/UGV-Robot/ros_noetic_catkin_ws/src/ws_livox/src/faster_lio_localization/src/LIO-Lite/msg/Pose6D.msg" NAME_WE)
add_dependencies(lio_lite_generate_messages_py _lio_lite_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(lio_lite_genpy)
add_dependencies(lio_lite_genpy lio_lite_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS lio_lite_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/lio_lite)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/lio_lite
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(lio_lite_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/lio_lite)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/lio_lite
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(lio_lite_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/lio_lite)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/lio_lite
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(lio_lite_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/lio_lite)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/lio_lite
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(lio_lite_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/lio_lite)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/lio_lite\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/lio_lite
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(lio_lite_generate_messages_py geometry_msgs_generate_messages_py)
endif()

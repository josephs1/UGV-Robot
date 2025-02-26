execute_process(COMMAND "/home/jstefan1/Documents/CodeWorkspace/UGV-Robot/catkin_ws2/build/catkin/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/jstefan1/Documents/CodeWorkspace/UGV-Robot/catkin_ws2/build/catkin/catkin_generated/python_distutils_install.sh) returned error code ")
endif()

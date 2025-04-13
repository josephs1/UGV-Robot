#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/jstefan1/Documents/CodeWorkspace/UGV-Robot/catkin_ws2/src/catkin"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/jstefan1/Documents/CodeWorkspace/UGV-Robot/catkin_ws2/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/jstefan1/Documents/CodeWorkspace/UGV-Robot/catkin_ws2/install/lib/python3/dist-packages:/home/jstefan1/Documents/CodeWorkspace/UGV-Robot/catkin_ws2/build/catkin/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/jstefan1/Documents/CodeWorkspace/UGV-Robot/catkin_ws2/build/catkin" \
    "/usr/bin/python3.8" \
    "/home/jstefan1/Documents/CodeWorkspace/UGV-Robot/catkin_ws2/src/catkin/setup.py" \
    egg_info --egg-base /home/jstefan1/Documents/CodeWorkspace/UGV-Robot/catkin_ws2/build/catkin \
    build --build-base "/home/jstefan1/Documents/CodeWorkspace/UGV-Robot/catkin_ws2/build/catkin" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/jstefan1/Documents/CodeWorkspace/UGV-Robot/catkin_ws2/install" --install-scripts="/home/jstefan1/Documents/CodeWorkspace/UGV-Robot/catkin_ws2/install/bin"

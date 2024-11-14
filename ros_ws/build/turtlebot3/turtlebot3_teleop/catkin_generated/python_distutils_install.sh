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

echo_and_run cd "/home/robcib/ros_ws/src/turtlebot3/turtlebot3_teleop"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/robcib/ros_ws/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/robcib/ros_ws/install/lib/python3/dist-packages:/home/robcib/ros_ws/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/robcib/ros_ws/build" \
    "/home/robcib/anaconda3/bin/python3" \
    "/home/robcib/ros_ws/src/turtlebot3/turtlebot3_teleop/setup.py" \
     \
    build --build-base "/home/robcib/ros_ws/build/turtlebot3/turtlebot3_teleop" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/robcib/ros_ws/install" --install-scripts="/home/robcib/ros_ws/install/bin"

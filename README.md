# Description
Assignments for robotics motion planning and control module in the University of Birmingham (forward kinematics & inverse kinematics) 

<div style="display: flex; justify-content: center; align-items: center;">
  <img src="https://github.com/HyPAIR/Robotics_Motion_Planning_and_Control_Assignment1/blob/main/fk.png" alt="task_allocation" width="680" height="400">
  <img src="https://github.com/HyPAIR/Robotics_Motion_Planning_and_Control_Assignment1/blob/main/ik.png" alt="task_allocation" width="680" height="400">
</div>

## Requirements
 - ROS2 FOXY
 - Ubuntu 20.04
If your laptop does not have the Ubuntu operating system installed, you can use a virtual machine to install Ubuntu 20.04:

    For Windows systems, refer to this [video](https://www.youtube.com/watch?v=x5MhydijWmc) for installation.

    For Mac systems, refer to this [video](https://www.youtube.com/watch?v=Hzji7w882OY) for installation.

## Installation
### Check out the [docker](https://github.com/HyPAIR/panda_ros2_gazebo.git) directory if you want to build this project without installing all the dependencies on your system.
### Otherwise, follow the steps below to complete the installation on your machine.
1. Install ROS2 FOXY:

```shell
locale  # check for UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # verify settings
```

```shell
sudo apt install software-properties-common
sudo add-apt-repository universe
```

```shell
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```

```shell
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

```shell
sudo apt update
sudo apt upgrade
sudo apt install ros-foxy-desktop python3-argcomplete
sudo apt install ros-dev-tools
```

```shell
echo "source /opt/ros/foxy/setup.bash" >> ~/.bashrc
echo "export TURTLEBOT3_MODEL=waffle" >> ~/.bashrc
echo "export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/opt/ros/foxy/share/turtlebot3_gazebo/models" >> ~/.bashrc
echo "source /usr/share/gazebo-11/setup.sh" >> ~/.bashrc
source ~/.bashrc
```

2. Install Dependencies:
```shell
sudo apt-get install libeigen3-dev libxml2-dev coinor-libipopt-dev qtbase5-dev qtdeclarative5-dev qtmultimedia5-dev qml-module-qtquick2 qml-module-qtquick-window2 qml-module-qtmultimedia qml-module-qtquick-dialogs qml-module-qtquick-controls qml-module-qt-labs-folderlistmodel qml-module-qt-labs-settings ros-foxy-xacro ros-foxy-test-msgs ros-foxy-ackermann-msgs ros-foxy-joint-state-publisher ros-foxy-ament-cmake-* swig
```

3. Install Turtlebot3
```shell
sudo apt install -y gazebo11 ros-foxy-gazebo-ros-pkgs ros-foxy-cartographer ros-foxy-cartographer-ros ros-foxy-navigation2 ros-foxy-nav2-bringup ros-foxy-turtlebot3* python3-vcstool
```

4. Build Assignment1:
```shell
mkdir -p ~/assignment1/src
cd ~/assignment1/src
git clone https://github.com/HyPAIR/Robotics_Motion_Planning_and_Control_Assignment1.git
cd ..
colcon build --merge-install --cmake-args -DIDYNTREE_USES_PYTHON=True -DIDYNTREE_USES_IPOPT:BOOL=ON -DCMAKE_BUILD_TYPE=Release
```

```shell
source install/setup.bash
ros2 launch panda_ros2_gazebo gazebo.launch.py
```

4. Build Assignment2:
```shell
mkdir -p ~/assignment2/src
cd ~/assignment2/src
git clone https://github.com/HyPAIR/Robotics_Motion_Planning_and_Control_Assignment2.git
cd ..
colcon build
```

```shell
source install/setup.bash
ros2 launch turtlebot3_navigation2 navigation2.launch.py 
```

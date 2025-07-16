# rtabmap with realsense

ros2 launch realsense2_camera rs_launch.py     enable_gyro:=true     enable_accel:=true     unite_imu_method:=2     enable_depth:=true     enable_color:=true     depth_module.profile:=640x480x30     rgb_camera.profile:=640x480x30

## Debug

# Deactivate conda
conda deactivate

# Verify you're out of conda (should not show (base))
echo $CONDA_DEFAULT_ENV

# Clean all ROS-related environment variables
unset ROS_DISTRO
unset ROS_VERSION
unset ROS_PYTHON_VERSION
unset AMENT_PREFIX_PATH
unset COLCON_PREFIX_PATH
unset CMAKE_PREFIX_PATH
unset LD_LIBRARY_PATH
unset PYTHONPATH

# Remove existing ROS 2 installation
sudo apt remove ros-humble-* --purge
sudo apt autoremove

# Update and reinstall
sudo apt update
sudo apt install ros-humble-desktop
sudo apt install ros-humble-rtabmap-ros
sudo apt install ros-humble-realsense2-*

# Source ROS 2 (do this outside of conda)
source /opt/ros/humble/setup.bash

# Navigate to your workspace
cd ~/ros2_ws

# Rebuild workspace
colcon build

# Source workspace
source install/setup.bash

# Add these lines to avoid conda conflicts with ROS
echo '# ROS 2 setup - do this before conda activation' >> ~/.bashrc
echo 'source /opt/ros/humble/setup.bash' >> ~/.bashrc
echo 'source ~/ros2_ws/install/setup.bash' >> ~/.bashrc

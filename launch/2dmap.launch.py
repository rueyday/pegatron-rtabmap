from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
import os

def generate_launch_description():
    # Declare launch arguments with default values
    rtabmap_args_arg = DeclareLaunchArgument(
        'rtabmap_args',
        default_value='--delete_db_on_start',
        description='Additional arguments for RTAB-Map'
    )
    
    rgb_topic_arg = DeclareLaunchArgument(
        'rgb_topic',
        default_value='/camera/camera/color/image_raw',
        description='RGB image topic'
    )
    
    depth_topic_arg = DeclareLaunchArgument(
        'depth_topic',
        default_value='/camera/camera/depth/image_rect_raw',
        description='Depth image topic'
    )
    
    camera_info_topic_arg = DeclareLaunchArgument(
        'camera_info_topic',
        default_value='/camera/camera/color/camera_info',
        description='Camera info topic'
    )
    
    frame_id_arg = DeclareLaunchArgument(
        'frame_id',
        default_value='camera_link',
        description='Frame ID for the camera'
    )
    
    approx_sync_arg = DeclareLaunchArgument(
        'approx_sync',
        default_value='true',
        description='Use approximate time synchronization'
    )
    
    # Find the rtabmap_launch package
    rtabmap_launch_dir = FindPackageShare('rtabmap_launch')
    
    # Include the original rtabmap.launch.py with our parameters
    rtabmap_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            rtabmap_launch_dir,
            '/launch/rtabmap.launch.py'
        ]),
        launch_arguments={
            'rtabmap_args': LaunchConfiguration('rtabmap_args'),
            'rgb_topic': LaunchConfiguration('rgb_topic'),
            'depth_topic': LaunchConfiguration('depth_topic'),
            'camera_info_topic': LaunchConfiguration('camera_info_topic'),
            'frame_id': LaunchConfiguration('frame_id'),
            'approx_sync': LaunchConfiguration('approx_sync'),
        }.items()
    )
    
    return LaunchDescription([
        rtabmap_args_arg,
        rgb_topic_arg,
        depth_topic_arg,
        camera_info_topic_arg,
        frame_id_arg,
        approx_sync_arg,
        rtabmap_launch
    ])
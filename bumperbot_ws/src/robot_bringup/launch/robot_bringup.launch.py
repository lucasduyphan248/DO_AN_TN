from launch import LaunchDescription
from launch_ros.actions import Node
import launch_ros.actions
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution, LaunchConfiguration
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
      
    return LaunchDescription([

        Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            name="tf_base_link",
            namespace="tf",
            # output="screen" ,
            arguments=["0", "0", "0.05", "0", "0", "0", "base_footprint", "base_link"]
        ),

        Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            name="tf_laser",
            namespace="tf",
            # output="screen" ,
            arguments=["0.15", "0", "0.35", "-3.14", "0", "0", "base_link", "lidar_link"]
        ),


        Node(
            package="robot_bringup",
            executable="cal_odom.py",
            name="cal_odom_node",
            output="screen" ,
        ),

        Node(
            package="robot_bringup",
            executable="control_vel_mortor.py",
            name="control_vel_mortor_node",
            output="screen" ,
        ),

        Node(
            package="bumperbot_firmware",
            executable="simple_serial_receiver.py",
            name="simple_serial_receiver_node",
            output="screen" ,
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('rplidar_ros'),
                    'launch',
                    'rplidar_a1_launch.py'
                ])
            ])
        ),



            ])
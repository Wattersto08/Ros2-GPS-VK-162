from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='vk_162_gps',
            executable='gps',
            name='vk_162_gps_handler',
            output='screen',
            emulate_tty=True,
            parameters=[
                {'deviceName': '/dev/ttyACM0'}
            ]
        )
    ])
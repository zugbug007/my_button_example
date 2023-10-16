from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_button_example',
            executable='button_node',
            name='button_node',
            output='screen',
        ),
    ])

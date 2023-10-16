import RPi.GPIO as GPIO
import rclpy
from rclpy.node import Node
from ButtonState.msg import ButtonState

class ButtonNode(Node):
    def __init__(self):
        super().__init__('button_node')
        self.publisher = self.create_publisher(ButtonState, 'button_state', 10)
        self.button_pin = 4  # Replace with your GPIO pin number
        GPIO.setmode(GPIbutton_nodeO.BCM)
        GPIO.setup(self.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def publish_button_state(self):
        msg = ButtonState()
        while rclpy.ok():
            if GPIO.input(self.button_pin) == GPIO.LOW:
                msg.pressed = True
                self.publisher.publish(msg)
            else:
                msg.pressed = False
            rclpy.spin_once(self)

def main(args=None):
    rclpy.init(args=args)
    node = ButtonNode()
    node.publish_button_state()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

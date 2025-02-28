#!/usr/bin/env python3

from rclpy.node import Node
from geometry_msgs.msg import Twist
import serial
import rclpy
class CmdVelToSerial(Node):
    def __init__(self):
        super().__init__("cmd_vel_to_serial")

        self.declare_parameter("port", "/dev/ttyUSB0")
        self.declare_parameter("baudrate", 115200)
        self.declare_parameter("wheel_base", 0.3)  # Khoảng cách giữa 2 bánh xe (m)
        self.declare_parameter("wheel_radius", 0.065)  # Bán kính bánh xe (m)

        self.port_ = self.get_parameter("port").value
        self.baudrate_ = self.get_parameter("baudrate").value
        self.wheel_base = self.get_parameter("wheel_base").value
        self.wheel_radius = self.get_parameter("wheel_radius").value

        self.subscription = self.create_subscription(Twist, "/cmd_vel", self.cmd_vel_callback, 10)
        self.arduino_ = serial.Serial(port=self.port_, baudrate=self.baudrate_, timeout=0.1)

    def cmd_vel_callback(self, msg):
        linear_x = msg.linear.x  # Vận tốc tuyến tính (m/s)
        angular_z = msg.angular.z  # Vận tốc góc (rad/s)

        # Tính toán vận tốc bánh xe (rad/s)
        right_wheel_vel = (linear_x + (self.wheel_base / 2.0) * angular_z) / self.wheel_radius
        left_wheel_vel = (linear_x - (self.wheel_base / 2.0) * angular_z) / self.wheel_radius

        # Định dạng dữ liệu gửi đến Arduino
        right_wheel_cmd = f"r{'p' if right_wheel_vel >= 0 else 'n'}{abs(right_wheel_vel):.2f},"
        left_wheel_cmd = f"l{'p' if left_wheel_vel >= 0 else 'n'}{abs(left_wheel_vel):.2f},"
        command = right_wheel_cmd + left_wheel_cmd

        self.get_logger().info(f"Sending command: {command}")
        self.arduino_.write(command.encode("utf-8"))


def main():
    rclpy.init()
    node = CmdVelToSerial()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

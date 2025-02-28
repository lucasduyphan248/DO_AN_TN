#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Float32
import math
from geometry_msgs.msg import Quaternion, TransformStamped
from nav_msgs.msg import Odometry
import tf_transformations
import tf2_ros

class ComputeOdometry(Node):

    def __init__(self):
        super().__init__("wheel_velocity_processor")

        self.subscriber_ = self.create_subscription(
            String, "serial_receiver", self.serial_callback, 10
        )

        self.left_wheel_pub_ = self.create_publisher(Float32, "left_wheel_velocity", 10)
        self.right_wheel_pub_ = self.create_publisher(Float32, "right_wheel_velocity", 10)
        self.odom_pub_ = self.create_publisher(Odometry, "odom", 10)

        self.yaw_pub = self.create_publisher(Float32, "yaw_data", 10)
        
        timer_period = 0.05
        self.timer = self.create_timer(timer_period, self.compute_odometry)
        self.tf_broadcaster_ = tf2_ros.TransformBroadcaster(self)

        self.get_logger().info("Wheel Velocity Processor Node has started.")

        self.pi_ = 3.14159
        self.diameter_wheel = 0.13
        self.base_width = 0.3
        self.ticks_per_round = 2688
        self.ticks_per_metter = 0.0

        self.wheel_radius_ = self.diameter_wheel / 2
        self.right_wheel_data = 0.0
        self.left_wheel_data = 0.0  # m/s

        self.x_ = 0.0
        self.y_ = 0.0
        self.theta_ = 0.0

        self.linear_velocity = 0.0
        self.angular_velocity = 0.0
        self.last_time_ = self.get_clock().now()

        self.pose_encod_data_str = [0,0]
        self.pose_encod_data = [0,0]
        self.pose_encod_data_prev = [0,0]
        self.delta_encod_data = [0,0]
        self.delta_travel = [0,0]

        self.v_robot = 0.0
        self.v_theta = 0.0

        self.ticks_per_metter  = 1.0 / (self.pi_ * self.diameter_wheel) * self.ticks_per_round



    def serial_callback(self, msg):
        data = msg.data.strip("b'")

        if not data:
            return

        self.get_logger().info(f"Received data: {data}")

        try:
            
            parts = data.split(",")
            if len(parts) < 4 :
                self.get_logger().error("Invalid data format received!")
                return

            right_wheel_data = parts[0].strip()
            left_wheel_data = parts[1].strip()  

            self.pose_encod_data_str[0] = parts[2].strip()
            self.pose_encod_data_str[1] = parts[3].strip().replace("\r", "").replace("\n", "").replace("\\r", "").replace("\\n", "")



            print("====== ", right_wheel_data)
            print("====== ", left_wheel_data)
            print("self.pose_encod_data_str",self.pose_encod_data_str)

            self.pose_encod_data[0] = float (self.pose_encod_data_str[0])
            self.pose_encod_data[1] = float (self.pose_encod_data_str[1])



            if right_wheel_data.startswith("rp"):
                right_sign = 1
                right_velocity = float(right_wheel_data[2:]) 
            elif right_wheel_data.startswith("rn"):
                right_sign = -1
                right_velocity = float(right_wheel_data[2:])  
            else:
                raise ValueError(f"Invalid format for right wheel: {right_wheel_data}")

            # Kiểm tra và phân tích dữ liệu bánh trái
            if left_wheel_data.startswith("lp"):
                left_sign = 1
                left_velocity = float(left_wheel_data[2:])  # Lấy phần số sau 'lp'
            elif left_wheel_data.startswith("ln"):
                left_sign = -1
                left_velocity = float(left_wheel_data[2:])  
            else:
                raise ValueError(f"Invalid format for left wheel: {left_wheel_data}")

            
            right_speed_m_s = right_velocity * right_sign
            left_speed_m_s = left_velocity * left_sign

            right_speed_m_s = right_velocity * self.wheel_radius_
            left_speed_m_s = left_velocity * self.wheel_radius_

            self.linear_velocity = (right_speed_m_s + left_speed_m_s) / 2.0
            self.angular_velocity = (right_speed_m_s - left_speed_m_s) / self.base_width

            current_time = self.get_clock().now()
            dt = (current_time - self.last_time_).nanoseconds / 1e9 

            self.last_time_ = current_time

            self.delta_encod_data[0] = self.pose_encod_data[0] - self.pose_encod_data_prev[0]
            self.delta_encod_data[1] = self.pose_encod_data[1] - self.pose_encod_data_prev[1]
            

            self.pose_encod_data_prev[0] = self.pose_encod_data[0]
            self.pose_encod_data_prev[1] = self.pose_encod_data[1]

            self.delta_travel[0] = self.delta_encod_data[0] / self.ticks_per_metter
            self.delta_travel[1] = self.delta_encod_data[1] / self.ticks_per_metter

            travel_right  =self.delta_travel[0]
            travel_left = self.delta_travel[1]
            
            delta_x = (travel_right + travel_left ) / 2.0 
            delta_theta = (travel_right - travel_left ) / (self.base_width )


            self.theta_ = self.theta_ + delta_theta

            if self.theta_ >= 6.28:
                self.theta_ = self.theta_ - 6.28
            if self.theta_ <= - 6.28:
                self.theta_ = self.theta_ + 6.28


            delta_x = delta_x* math.cos(self.theta_) 
            delta_y = delta_x* math.sin(self.theta_) 

            # delta_x = self.linear_velocity * dt * float(math.cos(self.theta_))
            # delta_y = self.linear_velocity * dt * float(math.sin(self.theta_))
            # delta_theta = self.angular_velocity * dt



            self.x_ += delta_x
            self.y_ += delta_y
            

            right_msg = Float32()
            right_msg.data = right_velocity
            self.right_wheel_pub_.publish(right_msg)

            yaw_msg = Float32()
            yaw_msg.data = self.theta_ * 180 / self.pi_

            self.yaw_pub.publish(yaw_msg)

            left_msg = Float32()
            left_msg.data = left_velocity
            self.left_wheel_pub_.publish(left_msg)

            self.get_logger().info(f"Right Wheel Velocity: {right_velocity}")
            self.get_logger().info(f"Left Wheel Velocity: {left_velocity}")


        except Exception as e:
            self.get_logger().error(f"Error parsing data: {e}")



    def compute_odometry(self):
        self.publish_robot_state()
        self.send_tf_robot()
    def publish_robot_state(self):

        odom_msg = Odometry()
        odom_msg.header.stamp = self.get_clock().now().to_msg()
        odom_msg.header.frame_id = "odom"
        odom_msg.child_frame_id = "base_footprint"


        odom_msg.pose.pose.position.x = self.x_
        odom_msg.pose.pose.position.y = self.y_
        odom_msg.pose.pose.position.z = 0.0

        quat = tf_transformations.quaternion_from_euler(0, 0, self.theta_)
        odom_msg.pose.pose.orientation = Quaternion(
            x=quat[0], y=quat[1], z=quat[2], w=quat[3]
        )

        odom_msg.twist.twist.linear.x = self.linear_velocity
        odom_msg.twist.twist.angular.z = self.angular_velocity

        self.odom_pub_.publish(odom_msg)




    def send_tf_robot(self):


        quat = tf_transformations.quaternion_from_euler(0, 0, self.theta_)


        transform = TransformStamped()
        transform.header.stamp = self.get_clock().now().to_msg()
        transform.header.frame_id = "odom"
        transform.child_frame_id = "base_footprint"
        transform.transform.translation.x = self.x_
        transform.transform.translation.y = self.y_
        transform.transform.translation.z = 0.0
        transform.transform.rotation = Quaternion(
            x=quat[0], y=quat[1], z=quat[2], w=quat[3]
        )

        self.tf_broadcaster_.sendTransform(transform)




def main():
    rclpy.init()
    node = ComputeOdometry()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

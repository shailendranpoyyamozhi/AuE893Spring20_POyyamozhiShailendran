import rospy
from geometry_msgs.msg import Twist

def move_circle():
    rospy.init_node('circle',anonymous='True')
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size = 10)
    vel_msg = Twist()
    speed = 2
    radius = 1
    vel_msg.linear.x = speed
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = speed/radius

    while not rospy.is_shutdown():
		pub.publish(vel_msg)

    vel_msg.linear.x = 0
    vel_msg.linear.z = 0
    pub.publish(vel_msg)
    s = rospy.Service( 'move_circle', MoveCircle)
    rospy.spin()

if __name__ == "__main__":
    try:
        move_circle()
    except rospy.ROSInterruptException: pass

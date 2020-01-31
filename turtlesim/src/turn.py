import rospy
from geometry_msgs.msg import Twist

def rotation():
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    vel_msg = Twist()
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size = 10)
    vel_msg.angular.z=2
    while not rospy.is_shutdown():

        t0	= rospy.Time.now().to_sec()
        angle_travel = 0

        while ( angle_travel < 1.15*(3.14/2) ):
            pub.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            angle_travel = 2*(t1-t0)
        vel_msg.angular.z=0
        pub.publish(vel_msg)


if __name__ == '__main__':
    try:
        #Testing our function
        rotation()
    except rospy.ROSInterruptException: pass

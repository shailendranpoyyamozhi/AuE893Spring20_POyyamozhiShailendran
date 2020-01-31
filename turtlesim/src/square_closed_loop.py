import rospy
from geometry_msgs.msg import Twist

def move():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    #Receiveing the user's input
    print("Let's move your robot")
    speed = 1
    distance = 2

    vel_msg.linear.x = abs(speed)
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():
        t0 = rospy.Time.now().to_sec()
        current_distance = 0
        while(current_distance < distance):

            velocity_publisher.publish(vel_msg)

            t1=rospy.Time.now().to_sec()

            current_distance= speed*(t1-t0)

        vel_msg.linear.x = 0

        velocity_publisher.publish(vel_msg)

def rotation():
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    vel_msg = Twist()
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size = 10)
    vel_msg.angular.z=2
    while not rospy.is_shutdown():

        t0	= rospy.Time.now().to_sec()
        angle_travel = 0

        while ( angle_travel <3.14):
            pub.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            angle_travel = 2*(t1-t0)
        vel_msg.angular.z=0
        pub.publish(vel_msg)



if __name__ == '__main__':
    try:
        #Testing our function
        move()
        rotation()
    except rospy.ROSInterruptException: pass

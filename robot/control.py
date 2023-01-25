from __future__ import print_function
from six.moves import input

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

try:
    from math import pi, tau, dist, fabs, cos
except:  # For Python 2 compatibility
    from math import pi, fabs, cos, sqrt

    tau = 2.0 * pi

    def dist(p, q):
        return sqrt(sum((p_i - q_i) ** 2.0 for p_i, q_i in zip(p, q)))


from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

arm_group_name = "arm"
grip_group_name = "gripper"

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node("move_group_py", anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
arm_move_group = moveit_commander.MoveGroupCommander(arm_group_name)
gripper_move_group = moveit_commander.MoveGroupCommander(grip_group_name)

display_trajectory_publisher = rospy.Publisher(
    "/move_group/display_planned_path",
    moveit_msgs.msg.DisplayTrajectory,
    queue_size=20
)

# We get the joint values from the group and change some of the values:
joint_goal = arm_move_group.get_current_joint_values()
joint_goal[0] = 0.0
joint_goal[1] = 0 
joint_goal[2] = 0.0
joint_goal[3] = 0.0

# The go command can be called with joint values, poses, or without any
# parameters if you have already set the pose or joint target for the group
arm_move_group.go(joint_goal)


joint_goal = gripper_move_group.get_current_joint_values()
print(joint_goal)
joint_goal[0] = -0.003
gripper_move_group.go(joint_goal, wait=True)

gripper_move_group.stop()
arm_move_group.stop()
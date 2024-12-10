#!/usr/bin/env python

class FK():

    def __init__(self):
        # Define geometric parameters for computing the forward kinematics. 
        # The required parameters are provided in the assignment description document.
        self.dh_params = self.init_dh_params()
        self.joint_offsets = self.init_joint_offsets()

    def init_dh_params(self):
        """
        Initialize dh parameters from all intermediate frames in the form [a, alpha, d]
        (refer to assignment description)
        """

        dh_params = []
        return dh_params

    def init_joint_offsets(self):
        """
        Initialize joint position offsets
        relative to intermediate frames defined using
        DH conventions 
        (refer to assignment description)
        """

        joint_offsets = []
        return joint_offsets

    def build_dh_transform(self, a, alpha, d, theta):
        """
        Construct transformation matrix T,
        using DH parameters and conventions
        """
        
        T = []
        # YOUR CODE STARTS HERE
    
        # YOUR CODE ENDS HERE
        return T

    def forward(self, q):
        """
        INPUT:
        q - 1x7 vector of joint angles [q0, q1, q2, q3, q4, q5, q6]

        OUTPUTS:
        jointPositions - 7 x 3 matrix, where each row corresponds to a rotational joint of the robot
                         Each row contains the [x,y,z] coordinates in the world frame of the respective 
                         joint's center in meters. The base of the robot is located at [0,0,0].

        T0e - a homogeneous transformation matrix,
              representing the end effector frame expressed in the world frame
        """

        jointPositions = []
        T0e = []
        # YOUR CODE STARTS HERE
    
        # YOUR CODE ENDS HERE
        return jointPositions, T0e

if __name__ == "__main__":
    pass

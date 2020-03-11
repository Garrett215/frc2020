#!/usr/bin/env python3
'''Move the arm.'''

from wpilib.command import Command
from wpilib import XboxController
from wpilib.interfaces.generichid import GenericHID

class Climbwithtriggers(Command):
    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.requires(self.robot.climbmotors)
        self.xbox0 = XboxController(0)

    def initialize(self):
        pass

    def execute(self):
        self.robot.climbmotors.climb(-self.xbox0.getTriggerAxis(GenericHID.Hand.kLeft) +
            self.xbox0.getTriggerAxis(GenericHID.Hand.kRight))

    def isFinished(self):
        #Make this return true when this Command no longer needs to run execute()
        return self.isTimedOut()

    def end(self):
        #Called once after isFinished returns true
        pass

    def interrupted(self):
        '''Called when another Command which requires one or more of the same
        subsystems is scheduled to run
        '''
        pass
        self.end()
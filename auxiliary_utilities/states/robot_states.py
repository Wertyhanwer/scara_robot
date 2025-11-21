from enum import Enum

class RobotStates(Enum):
    NON_STATE = 0
    MANUAL_CONTROL_STATE = 1
    AUTO_CONTROL_STATE = 2
    TEST_STATE = 3
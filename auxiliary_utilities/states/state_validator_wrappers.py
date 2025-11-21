from functools import wraps
from robot_states import RobotStates

def validate_manual_control_state(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self._state == RobotStates.MANUAL_CONTROL_STATE:
            return func(self, *args, **kwargs)
        print(f"Запрещено: текущий стейт {self._state}, нужен {RobotStates.MANUAL_CONTROL_STATE}")
    return wrapper
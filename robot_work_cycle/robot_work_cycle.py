

class RobotWorkCycle:
    def __init__(self):
        self._safety_monitor =  SafetyMonitor()
        self._state_handler = StateHandler()
        self._task_manager = TaskManager()
        

from controllers.driver_controller.driver_controller import DriverController
from auxiliary_utilities.states.robot_states import RobotStates
from auxiliary_utilities.states.state_validator_wrappers import validate_manual_control_state
from configs.driver_config import HalDriverConfig

class TestOneDriverController:
    def __init__(self, config: HalDriverConfig):
        self._driver_1 = DriverController(0, "TestDriver0") #Todo: вынести сборку драйвера из класса из за проблем с конфигом или придумать другой способ типо фабрики
        self._state = RobotStates.NON_STATE
        self._config = config

    def start_controller(self):
        self._start_drivers()
        self._set_manual_control_state()


    @validate_manual_control_state
    def rotate_left(self):
        self._driver_1.set_target_position(self._config.driver_max_pos_deg_left)

    @validate_manual_control_state
    def rotate_right(self):
        self._driver_1.set_target_position(self._config.driver_max_pos_deg_right)

    @validate_manual_control_state
    def rotate_stop(self):
        actual_position = self._driver_1.get_target_position()
        self._driver_1.set_target_position(actual_position)

    def _set_manual_control_state(self):
        self._state = RobotStates.MANUAL_CONTROL_STATE

    def _start_drivers(self):
        self._driver_1.start()

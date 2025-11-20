from ..basic_check_util import BasicCheckUtil
from safety_monitors_params_to_check import SafetyMonitorsParamsToCheck
from controllers.driver_controller.driver_controller import DriverController

class SafetyMonitorCheckUtil(BasicCheckUtil):
    def __init__(self, driver: DriverController, params_to_check: SafetyMonitorsParamsToCheck):
        self._driver = driver
        self._params_to_check = params_to_check

    def check_state(self):
        self._driver.get_safety_parameters()



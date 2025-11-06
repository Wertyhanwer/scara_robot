from robot_models.scara_model import ScaraModel
from driver_controller.driver_controller import DriverController


class MasterController:
    def __int__(self):
        self._driver_controller_0 = DriverController(0, "driver_controller_0")
        self._driver_controller_1 = DriverController(1, "driver_controller_1")

        self._robot_model = ScaraModel()


    def set_coord_pos(self, x: int, y: int):
        pos_0, pos_1 = self._robot_model.calculate_reverse_kinematics(x, y)
        self._driver_controller_0.set_target_position(pos_0)
        self._driver_controller_0.set_target_position(pos_1)

    def set_height(self,height: int):
        ...

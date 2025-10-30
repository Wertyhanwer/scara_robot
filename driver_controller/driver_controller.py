import time

from hal_controller.hal_driver_struct import HalDriverStruct


class DriverController:
    def __init__(self, drive_number: int, control_component_name: str):
        self._hal_driver_controller = HalDriverStruct(drive_number, control_component_name)

    def startup(self):
        ...

    def start(self):
        self._hal_driver_controller.driver_halt = False
        self._hal_driver_controller.estop_button = True
        time.sleep(2) #TODO: Избавиться от подобного подхода когда не будет гореть
        self._hal_driver_controller.enable_drive_button = True

    def pause(self):
        self._hal_driver_controller.driver_halt = True

    def stop(self):
        self._hal_driver_controller.driver_halt = True
        self._hal_driver_controller.estop_button = False
        time.sleep(2)  # TODO: Избавиться от подобного подхода когда не будет гореть
        self._hal_driver_controller.enable_drive_button = False

    def poweroff(self):
        ...

    def set_max_speed(self, speed: int):
        ...

    def set_target_position(self, position: int):
        self._hal_driver_controller.command_pos_degrees = position

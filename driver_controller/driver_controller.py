from hal_controller.hal_driver_struct import HalDriverStruct


class DriverController:
    def __int__(self, hal_driver_controller: HalDriverStruct):
        self._hal_driver_controller = hal_driver_controller

    def startup(self):
        ...

    def start(self):
        ...

    def pause(self):
        ...

    def stop(self):
        ...

    def poweroff(self):
        ...

    def set_max_speed(self, speed: int):
        ...

    def set_target_position(self, position: int):
        ...

import time

from controllers.hal_controller.hal_driver_struct import HalDriverStruct


class DriverController:
    def __init__(self, drive_number: int, control_component_name: str):
        self._hal_driver_controller = HalDriverStruct(drive_number, control_component_name)

    def startup(self):
        ...

    def start(self):
        self._hal_driver_controller.estop_button = True
        time.sleep(1) #TODO: Избавиться от подобного подхода когда не будет гореть
        self._hal_driver_controller.enable_drive_button = True

    def pause(self):
        self._hal_driver_controller.enable_drive_button = False

    def resume(self):
        self._hal_driver_controller.enable_drive_button = True
        
    def stop(self):
        self._hal_driver_controller.estop_button = False
        time.sleep(1)  # TODO: Избавиться от подобного подхода когда не будет гореть
        self._hal_driver_controller.enable_drive_button = False

    def get_safety_parameters(self):
        ...

    def poweroff(self):
        ...

    def set_max_speed(self, speed: int):
        ...

    def set_target_position(self, position: int):
        self._hal_driver_controller.target_pos = position
   
    def get_target_position(self):
        return self._hal_driver_controller.target_pos

    def get_actual_position(self):
        return self._hal_driver_controller.actual_position

    def control_run(self):
        self._hal_driver_controller.control_run = True

    def control_stop(self):
        self._hal_driver_controller.control_run = False

    def get_target_velocity(self):
        return self._hal_driver_controller.target_velocity

    def set_target_velocity(self, velocity: float):
        self._hal_driver_controller.target_velocity = velocity

    def get_acceleration(self):
        return self._hal_driver_controller.acceleration

    def set_acceleration(self, acceleration: float):
        self._hal_driver_controller.acceleration = acceleration

    def get_deceleration(self):
        return self._hal_driver_controller.deceleration

    def set_deceleration(self, deceleration: float):
        self._hal_driver_controller.deceleration = deceleration

    def get_torque(self):
        return self._hal_driver_controller.torque

    def set_max_torque(self, torque: float):
        self._hal_driver_controller.max_torque = torque

    def get_max_torque(self):
        return self._hal_driver_controller.max_torque

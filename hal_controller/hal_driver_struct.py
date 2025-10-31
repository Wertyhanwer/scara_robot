import hal
from driver_pins_name_template import DriverPinsNameTemplate
from driver_pin import DriverPin

class HalDriverStruct:
    def __init__(self, drive_number: int, control_component_name: str):
        self._hal_control_component = hal.component(control_component_name)
        self._hal_control_component_name = control_component_name
        self._driver_id = str(drive_number)
        self._create_component_pins()

        self._hal_control_component.ready()

        self._connect_local_pins_to_actual()

    def _create_component_pins(self):
        self._create_read_component_pins()
        self._create_write_component_pins()

    def _create_read_component_pins(self):
        self._actual_position = DriverPin(self, DriverPinsNameTemplate.actual_position, hal.HAL_FLOAT, hal.HAL_IN)
        self._status_word = DriverPin(self, DriverPinsNameTemplate.status_word, hal.HAL_FLOAT, hal.HAL_IN)
        self._error_code = DriverPin(self, DriverPinsNameTemplate.error_code, hal.HAL_FLOAT, hal.HAL_IN)

    def _create_write_component_pins(self):
        self._command_pos_degrees = DriverPin(self, DriverPinsNameTemplate.command_pos_degrees, hal.HAL_FLOAT, hal.HAL_OUT)
        self._max_speed_degrees = DriverPin(self, DriverPinsNameTemplate.max_speed_degrees, hal.HAL_FLOAT, hal.HAL_OUT)
        self._estop_button = DriverPin(self, DriverPinsNameTemplate.estop_button, hal.HAL_BIT, hal.HAL_OUT)
        self._driver_halt = DriverPin(self, DriverPinsNameTemplate.driver_halt, hal.HAL_BIT, hal.HAL_OUT)
        self._driver_fault_reset = DriverPin(self, DriverPinsNameTemplate.driver_fault_reset, hal.HAL_BIT, hal.HAL_OUT)
        self._enable_drive_button = DriverPin(self, DriverPinsNameTemplate.enable_drive_button, hal.HAL_BIT, hal.HAL_OUT)

    def _connect_local_pins_to_actual(self):
        hal.connect(self._actual_position.fullname, f"{self._driver_id}-{self._actual_position.name}")
        hal.connect(self._status_word.fullname, f"{self._driver_id}-{self._status_word.name}")
        hal.connect(self._error_code.fullname, f"{self._driver_id}-{self._error_code.name}")

        hal.connect(self._command_pos_degrees.fullname, f"{self._driver_id}-{self._command_pos_degrees.name}")
        hal.connect(self._max_speed_degrees.fullname, f"{self._driver_id}-{self._max_speed_degrees.name}")
        hal.connect(self._estop_button.fullname, f"{self._driver_id}-{self._estop_button.name}")
        hal.connect(self._driver_halt.fullname, f"{self._driver_id}-{self._driver_halt.name}")
        hal.connect(self._driver_fault_reset.fullname, f"{self._driver_id}-{self._driver_fault_reset.name}")
        hal.connect(self._enable_drive_button.fullname, f"{self._driver_id}-{self._enable_drive_button.name}")
        


    @property
    def hal_control_component_name(self):
        return self._hal_control_component_name

    @property
    def hal_control_component(self):
        return self._hal_control_component

    @property
    def actual_position(self):
        return self._hal_control_component[self._actual_position.name]

    @property
    def status_word(self):
        return self._hal_control_component[self._status_word.name]

    @property
    def error_code(self):
        return self._hal_control_component[self._error_code.name]

    @property
    def command_pos_degrees(self):
        return self._hal_control_component[self._command_pos_degrees.name]

    @command_pos_degrees.setter
    def command_pos_degrees(self, position):
        self._hal_control_component[self._command_pos_degrees.name] = position

    @property
    def max_speed_degrees(self):
        return self._hal_control_component[self._max_speed_degrees.name]

    @max_speed_degrees.setter
    def max_speed_degrees(self, speed):
        self._hal_control_component[self._max_speed_degrees.name] = speed

    @property
    def estop_button(self):
        return self._hal_control_component[self._estop_button.name]

    @estop_button.setter
    def estop_button(self, state):
        self._hal_control_component[self._estop_button.name] = state

    @property
    def driver_halt(self):
        return self._hal_control_component[self._driver_halt.name]

    @driver_halt.setter
    def driver_halt(self, state):
        self._hal_control_component[self._driver_halt.name] = state

    @property
    def driver_fault_reset(self):
        return self._hal_control_component[self._driver_fault_reset.name]

    @driver_fault_reset.setter
    def driver_fault_reset(self, state):
        self._hal_control_component[self._driver_fault_reset.name] = state

    @property
    def enable_drive_button(self):
        return self._hal_control_component[self._enable_drive_button.name]

    @enable_drive_button.setter
    def enable_drive_button(self, state):
        self._hal_control_component[self._enable_drive_button.name] = state











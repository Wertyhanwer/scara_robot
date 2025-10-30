

class HalDriverStruct:
    def __init__(self, drive_number: int, control_component_name: str):
        self._hal_control_component = hal.component(control_component_name)
        self._hal_control_component_name = self._hal_control_component.name
        self._driver_id = str(drive_number)
        self._create_component_pins()

        self._hal_control_component.ready()

        self._connect_local_pins_to_actual()

    def _create_component_pins(self):
        self._create_read_component_pins()
        self._create_write_component_pins()

    def _create_read_component_pins(self):
        self._actual_pos = self._hal_control_component.newpin(f"actual-pos", hal.HAL_INT32, hal.HAL_IN)
        self._status_word = self._hal_control_component.newpin(f"statusword", hal.HAL_UINT16, hal.HAL_IN)
        self._error_code = self._hal_control_component.newpin(f"errorcode", hal.HAL_UINT16, hal.HAL_IN)

    def _create_write_component_pins(self):
        self._command_pos_degrees = self._hal_control_component.newpin(f"cmd-pos-deg", hal.HAL_INT32, hal.HAL_OUT)
        self._max_speed_degrees = self._hal_control_component.newpin(f"max-speed", hal.HAL_UDINT, hal.HAL_OUT)
        self._estop_button = self._hal_control_component.newpin(f"estop-button", hal.HAL_BIT, hal.HAL_OUT)
        self._driver_halt = self._hal_control_component.newpin(f"drv-halt", hal.HAL_BIT, hal.HAL_OUT)
        self._driver_fault_reset = self._hal_control_component.newpin(f"drv-fault-reset", hal.HAL_BIT, hal.HAL_OUT)

    def _connect_local_pins_to_actual(self):
        hal.connect(self._actual_pos.fullname, f"{self._driver_id}-{self._actual_pos.name}")
        hal.connect(self._status_word.fullname, f"{self._driver_id}-{self._status_word.name}")
        hal.connect(self._error_code.fullname, f"{self._driver_id}-{self._error_code.name}")

        hal.connect(self._command_pos_degrees.fullname, f"{self._driver_id}-{self._command_pos_degrees.name}")
        hal.connect(self._max_speed_degrees.fullname, f"{self._driver_id}-{self._max_speed_degrees.name}")
        hal.connect(self._estop_button.fullname, f"{self._driver_id}-{self._estop_button.name}")
        hal.connect(self._driver_halt.fullname, f"{self._driver_id}-{self._driver_halt.name}")
        hal.connect(self._driver_fault_reset.fullname, f"{self._driver_id}-{self._driver_fault_reset.name}")

    @property
    def actual_pos(self):
        return self._actual_pos.value

    @property
    def status_word(self):
        return self._status_word.value

    @property
    def error_code(self):
        return self._error_code.value

    @property
    def command_pos_degrees(self):
        return self._command_pos_degrees.value

    @command_pos_degrees.setter
    def command_pos_degrees(self, position):
        self._command_pos_degrees.value = position

    @property
    def max_speed_degrees(self):
        return self._max_speed_degrees.value

    @max_speed_degrees.setter
    def max_speed_degrees(self, speed):
        self._max_speed_degrees.value = speed

    @property
    def estop_button(self):
        return self._estop_button.value

    @estop_button.setter
    def estop_button(self, state):
        self._estop_button.value = state

    @property
    def driver_halt(self):
        return self._driver_halt.value

    @driver_halt.setter
    def driver_halt(self, state):
        self._driver_halt.value = state

    @property
    def driver_fault_reset(self):
        return self._driver_fault_reset.value

    @driver_fault_reset.setter
    def driver_fault_reset(self, state):
        self._driver_fault_reset.value = state











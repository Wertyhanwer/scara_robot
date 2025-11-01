from enum import Enum


class DriverPinsNameTemplate(Enum):
    actual_position = "actual-pos"
    status_word = "statusword"
    error_code = "errorcode"

    command_pos_degrees = "cmd-pos-deg"
    max_speed_degrees = "max-speed-deg"
    estop_button = "estop-button"
    driver_halt = "drv-halt"
    driver_fault_reset = "drv-fault-reset"
    enable_drive_button = "enable-drive-button"










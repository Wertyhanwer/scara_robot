from enum import Enum


class DriverPinsNameTemplate(Enum):
    actual_position = "actual-pos"
    status_word = "statusword"
    error_code = "errorcode"

    target_pos = "target-pos"
    max_speed_degrees = "max-speed-deg"
    estop_button = "estop-button"
    driver_halt = "drv-halt"
    driver_fault_reset = "drv-fault-reset"
    enable_drive_button = "enable-drive-button"
    control_run = "control-run"
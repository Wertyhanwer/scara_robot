from dataclasses import dataclass


@dataclass
class HalDriverConfig:
    # Позиционные параметры
    target_pos: float = 0.0
    max_speed_degrees: float = 100.0
    target_velocity: float = 50.0
    acceleration: float = 200.0
    deceleration: float = 200.0
    max_torque: float = 100.0

    estop_button: bool = False
    driver_halt: bool = False
    driver_fault_reset: bool = False
    enable_drive_button: bool = False
    control_run: bool = False

    actual_position: float = 0.0
    status_word: float = 0.0
    error_code: float = 0.0
    torque: float = 0.0
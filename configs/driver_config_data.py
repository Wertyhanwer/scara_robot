from pydantic import BaseModel, ConfigDict, Field, PrivateAttr
from pathlib import Path
from typing import Optional, Callable
import json


class HalDriverConfigData(BaseModel):

    model_config = ConfigDict(
        validate_assignment=True,
        arbitrary_types_allowed=True
    )

    target_pos: float = Field(default=0.0, description="Целевая позиция")
    max_speed_degrees: float = Field(default=100.0, gt=0, le=360.0, description="Макс. скорость в градусах")
    target_velocity: float = Field(default=50.0, ge=0, le=100.0, description="Целевая скорость")
    max_velocity: float = Field(default=100, ge=0, le=100.0, description="Максимальная скорость")
    acceleration: float = Field(default=200.0, gt=0, description="Ускорение")
    deceleration: float = Field(default=200.0, gt=0, description="Замедление")
    max_torque: float = Field(default=100.0, ge=0, le=100.0, description="Макс. момент")
    estop_button: bool = Field(default=False, description="Аварийный стоп")
    driver_halt: bool = Field(default=False, description="Остановка драйвера")
    driver_fault_reset: bool = Field(default=False, description="Сброс ошибок")
    enable_drive_button: bool = Field(default=False, description="Включение привода")
    control_run: bool = Field(default=False, description="Запуск управления")


    actual_position: float = Field(default=0.0, description="Текущая позиция")
    status_word: int = Field(default=0, description="Слово состояния")
    error_code: int = Field(default=0, description="Код ошибки")
    torque: float = Field(default=0.0, description="Текущий момент")

    driver_max_pos_deg_left: float = Field(default=-135, description="Ограничения по повороту влево")
    driver_max_pos_deg_right: float = Field(default=135, description="Ограничения по повороту вправо")
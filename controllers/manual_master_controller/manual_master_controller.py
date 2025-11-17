from robot_models.scara_model.default_config import DefaultConfig
from robot_models.scara_model.model import ScaraModel


class ManualController:
    def __init__(self, model: ScaraModel):
        self._model = model

    def move_forward(self):
        ...

    def move_backward(self):
        ...

    def move_left(self):
        ...

    def move_right(self):
        ...

    def move_right_upper_arm(self):
        ...

    def move_left_upper_arm(self):
        ...

    def move_right_forearm(self):
        ...

    def move_left_forearm(self):
        ...


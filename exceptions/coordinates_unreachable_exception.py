

class CoordinatesUnreachableException(Exception):
    def __init__(self, target_coordinates: list, current_coordinates:list=None, message:str=None):
        self.target_coordinates = target_coordinates
        self.current_coordinates = current_coordinates
        self.message = message or f"Цель {target_coordinates} недостижима"
        super().__init__(self.message)

    def __str__(self):
        base_msg = self.message
        if self.target_coordinates:
            return f"{base_msg}. Текущие координаты: {self.target_coordinates}"
        return base_msg
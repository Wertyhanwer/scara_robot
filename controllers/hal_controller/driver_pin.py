


class DriverPin:
    def __init__(self, hal_driver_struct, name_enum, pin_data_type, pin_type):
        self._name = name_enum.value
        self._hal_pin_obj = hal_driver_struct.hal_control_component.newpin(self._name, pin_data_type, pin_type)
        self._component_name = hal_driver_struct.hal_control_component_name
        self._fullname = f"{self._component_name}.{self._name}"

    @property
    def name(self):
        return self._name

    @property
    def fullname(self):
        return self._fullname

    @property
    def component_name(self):
        return self._component_name

    @property
    def hal_pin_obj(self):
        return self._hal_pin_obj
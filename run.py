import time
from controllers.driver_controller.driver_controller import DriverController

driver_controller = DriverController(0, "driver_controller")
driver_controller.start()
driver_controller.set_target_position(5)
time.sleep(2)
driver_controller.set_target_position(15)
time.sleep(2)
driver_controller.set_target_position(30)
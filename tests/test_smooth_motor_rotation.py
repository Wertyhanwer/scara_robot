import time
from driver_controller.driver_controller import DriverController


def main():
    MIN_ANGLE = -5.0
    MAX_ANGLE = 5.0


    driver_1 = DriverController(0, "test_driver_controller_0")
    driver_2 = DriverController(1, "test_driver_controller_1")

    print(f"Запуск драйверов...")
    driver_1.start()
    driver_2.start()

    time.sleep(3)
    angle_1 = angle_2 = MAX_ANGLE

    try:
        while True:
            if driver_1.get_actual_position() >= MAX_ANGLE:
                angle_1 = MIN_ANGLE
            if driver_1.get_actual_position() <= MIN_ANGLE:
                angle_1 = MAX_ANGLE
            if driver_2.get_actual_position() >= MAX_ANGLE:
                angle_2 = MIN_ANGLE
            if driver_2.get_actual_position() <= MIN_ANGLE:
                angle_2 = MAX_ANGLE


            driver_1.set_target_position(angle_1)
            driver_2.set_target_position(angle_2)
  
            #driver_1.lcec_run()
            #driver_2.lcec_run()
            
            time.sleep(0.01)




    except KeyboardInterrupt:
        print(f"\n\nОстановка драйверов...")
        driver_1.stop()
        driver_2.stop()
        print(f"Тест завершён.")


if __name__ == "__main__":
    main()

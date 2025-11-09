import time
from driver_controller.driver_controller import DriverController


def main():
    MIN_ANGLE = -10.0
    MAX_ANGLE = 10.0


    driver_1 = DriverController(0, "test_driver_controller_0")
    driver_2 = DriverController(1, "test_driver_controller_1")

    print(f"Запуск драйверов...")
    driver_1.start()
    driver_2.start()

    driver_1.set_target_velocity(25)
    driver_2.set_target_velocity(25)

    driver_1.set_acceleration(50)
    driver_2.set_acceleration(50)

    driver_1.set_deceleration(50)
    driver_2.set_deceleration(50)

    driver_1.set_max_torque(40)
    driver_2.set_max_torque(40)



    time.sleep(3)
    angle_1 = angle_2 = MAX_ANGLE

    pause_check = False
    pause_start_time = 0

    try:
        while True:
            if driver_1.get_actual_position() >= MAX_ANGLE - 0.2:
                angle_1 = MIN_ANGLE
                driver_1.control_stop()
            if driver_1.get_actual_position() <= MIN_ANGLE + 0.2:
                angle_1 = MAX_ANGLE
                driver_1.control_stop()
            if driver_2.get_actual_position() >= MAX_ANGLE - 0.2:
                angle_2 = MIN_ANGLE
                driver_2.control_stop()
            if driver_2.get_actual_position() <= MIN_ANGLE + 0.2:
                angle_2 = MAX_ANGLE
                driver_2.control_stop()

            if abs(driver_1.get_torque()) >=  driver_1.get_max_torque() * 0.9:
                driver_1.pause()
                driver_2.pause()
                if pause_start_time == 0:
                    pause_start_time = time.time()
            elif abs(driver_2.get_torque()) >=  driver_2.get_max_torque() * 0.9:
                driver_1.pause()
                driver_2.pause()
                if pause_start_time == 0:
                    pause_start_time = time.time()
            else:
                pause_start_time = 0

            if time.time() - pause_start_time >= 10:
                driver_1.stop()
                driver_2.stop()

            driver_1.set_target_position(angle_1)
            driver_2.set_target_position(angle_2)

            driver_1.control_run()
            driver_2.control_run()

            #time.sleep(0.01)




    except KeyboardInterrupt:
        print(f"\n\nОстановка драйверов...")
        driver_1.stop()
        driver_2.stop()
        print(f"Тест завершён.")


if __name__ == "__main__":
    main()
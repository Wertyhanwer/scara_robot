import time
import subprocess
from driver_controller.driver_controller import DriverController


def main():
    subprocess.run(["halrun", "-U"])
    # Запуск скрипта и ожидание завершения
    subprocess.run(["./setup_ethercat.sh"])
    # Вывод результата выполнения скрипта
    MIN_ANGLE = -15.0
    MAX_ANGLE = 15.0


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

    driver_1.set_max_torque(350)
    driver_2.set_max_torque(140)



    time.sleep(3)
    angle_1 = angle_2 = MAX_ANGLE

    pause_check = False
    pause_start_time = 0
    try_to_stop_count = 0

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
               
            print(abs(driver_1.get_torque()), driver_1.get_max_torque() * 0.9, "#####", abs(driver_2.get_torque()), driver_2.get_max_torque() * 0.9)
            if abs(driver_1.get_torque()) >=  driver_1.get_max_torque() * 0.9 or abs(driver_2.get_torque()) >=  driver_2.get_max_torque() * 0.9:
                try_to_stop_count += 1
                pause_check = True

                driver_1.pause()
                driver_2.pause()
                time.sleep(1)

                print(try_to_stop_count)
                if try_to_stop_count == 1:
                    pause_start_time = time.time()
                if try_to_stop_count >= 3:
                    time.sleep(10)
            else:
                if pause_check:
                    driver_1.resume()
                    driver_1.control_stop()
                    driver_2.resume()
                    driver_2.control_stop()
                    time.sleep(0.05)
                    driver_1.control_run()
                    driver_2.control_run()
                    pause_check = False
					
                if (time.time() - pause_start_time) >= 10:
                    pause_start_time = 0
                    try_to_stop_count = 0




           

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

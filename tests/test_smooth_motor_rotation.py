import time
import math
from driver_controller.driver_controller import DriverController


def smooth_oscillation(min_angle, max_angle, period_seconds, elapsed_time):
    """Вычисляет текущий угол для плавного колебания используя синусоиду"""
    amplitude = (max_angle - min_angle) / 2
    center = (max_angle + min_angle) / 2
    omega = 2 * math.pi / period_seconds
    return center + amplitude * math.sin(omega * elapsed_time)


def main():
    MIN_ANGLE = -50.0
    MAX_ANGLE = 50.0
    SPEED_DEGREES_PER_SEC = 1.0
    
    full_range = MAX_ANGLE - MIN_ANGLE
    period = full_range / SPEED_DEGREES_PER_SEC * 2
    
    print(f"Инициализация драйверов...")
    driver_1 = DriverController(0, "test_driver_controller_0")
    driver_2 = DriverController(1, "test_driver_controller_1")
    
    print(f"Запуск драйверов...")
    driver_1.start()
    driver_2.start()
    
    time.sleep(3)
    
    print(f"Начало плавного вращения...")
    print(f"Диапазон: {MIN_ANGLE}° до {MAX_ANGLE}°")
    print(f"Скорость: ~{SPEED_DEGREES_PER_SEC}°/сек")
    print(f"Период полного цикла: {period:.1f} сек")
    print(f"Для остановки нажмите Ctrl+C\n")
    
    start_time = time.time()
    update_interval = 0.1
    
    try:
        while True:
            elapsed = time.time() - start_time
            
            angle_1 = smooth_oscillation(MIN_ANGLE, MAX_ANGLE, period, elapsed)
            angle_2 = smooth_oscillation(MIN_ANGLE, MAX_ANGLE, period, elapsed + period/4)
            
            driver_1.set_target_position(angle_1)
            driver_2.set_target_position(angle_2)

            driver_1.lcec_run()
            driver_2.lcec_run()
            
            if int(elapsed * 10) % 10 == 0:
                print(f"[{elapsed:6.1f}s] Драйвер 1: {angle_1:6.2f}° | Драйвер 2: {angle_2:6.2f}°")
            
            time.sleep(update_interval)
            
    except KeyboardInterrupt:
        print(f"\n\nОстановка драйверов...")
        driver_1.stop()
        driver_2.stop()
        print(f"Тест завершён.")


if __name__ == "__main__":
    main()


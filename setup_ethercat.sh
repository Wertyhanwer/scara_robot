#!/bin/bash
# Остановка всех процессов хал на всякий случай
halrun -U &

# Краткая пауза для инициализации (можно увеличить при необходимости)
sleep 1
# Определение пути к файлу ethercatDelta.xml в той же директории
SCRIPT_DIR="$(dirname "$(realpath "$0")")"
XML_FILE="$SCRIPT_DIR/ethercatDouble.xml"

# Проверяем, существует ли файл ethercatDelta.xml
if [ ! -f "$XML_FILE" ]; then
    echo "Ошибка: Файл $XML_FILE не найден!"
    exit 1
fi




# Загрузка конфигурации EtherCAT
echo "Загружается конфигурация из $XML_FILE"
halcmd loadusr -W lcec_conf "$XML_FILE"
halcmd loadrt lcec
halcmd loadrt threads name1=servo-thread period1=1000000 



# Добавляем функции в servo-thread
halcmd addf lcec.read-all servo-thread
halcmd addf lcec.write-all servo-thread

# Подключаем кнопки и параметры
halcmd net estop-button lcec.0.0.Control.QuickStop lcec.0.0.Control.EnableVoltage  lcec.0.1.Control.QuickStop lcec.0.1.Control.EnableVoltage 
halcmd net enable-drive-button lcec.0.0.Control.SwitchOn lcec.0.0.Control.EnableOperation  lcec.0.1.Control.SwitchOn lcec.0.1.Control.EnableOperation  
halcmd net target-speed lcec.0.0.TargetSpeed lcec.0.1.TargetSpeed 
 
halcmd net reset lcec.0.0.Control.FaultReset lcec.0.1.Control.FaultReset 



# Переменные для первого двигателя (slave idx="0")
halcmd net control-halt lcec.0.0.Control.Halt lcec.0.1.Control.Halt
halcmd net statusword lcec.0.0.StatusWord
halcmd net errorword lcec.0.0.ErrorCode

halcmd net statusword-right lcec.0.1.StatusWord
halcmd net errorword-right lcec.0.1.ErrorCode

halcmd net position-actual-velocity-value lcec.0.0.ActualVelocityValue
halcmd net position-actual lcec.0.0.ActualPosition

halcmd net position-actual-velocity-value-right  lcec.0.1.ActualVelocityValue
halcmd net position-actual-right  lcec.0.1.ActualPosition

halcmd net torque  lcec.0.0.Torque
halcmd net torque-right  lcec.0.1.Torque

halcmd loadrt filter_kalman count=2
halcmd addf filter-kalman.0 servo-thread
halcmd addf filter-kalman.1 servo-thread

halcmd setp filter-kalman.0.Qk 1
halcmd setp filter-kalman.0.Rk 100000

halcmd setp filter-kalman.1.Qk 1
halcmd setp filter-kalman.1.Rk 100000



#net velosityI filter-kalman.0.zk  lcec.0.0.ActualVelocityValue


halcmd net limit lcec.0.0.TorqueLimitPositive lcec.0.0.TorqueLimitNegative  lcec.0.1.TorqueLimitPositive lcec.0.1.TorqueLimitNegative 

halcmd net acceleration-deceleration lcec.0.0.Acceleration lcec.0.0.Deceleration lcec.0.1.Acceleration lcec.0.1.Deceleration 

halcmd sets acceleration-deceleration 500.0
halcmd sets limit 150.0
# Запуск HAL
halcmd start

echo "Конфигурация EtherCAT успешно загружена."
echo "READY"

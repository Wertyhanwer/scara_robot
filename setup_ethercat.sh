#!/bin/bash
set -e

# путь к XML
SCRIPT_DIR="$(dirname "$(realpath "$0")")"
XML_FILE="$SCRIPT_DIR/ethercatDouble.xml"

if [ ! -f "$XML_FILE" ]; then
  echo "Ошибка: Файл $XML_FILE не найден!"
  exit 1
fi

echo "Загружается конфигурация из $XML_FILE"

# чистый halrun (опционально)
# halrun -U 2>/dev/null || true

# загрузка EtherCAT + поток
halcmd loadusr -W lcec_conf "$XML_FILE"
halcmd loadrt lcec
halcmd loadrt threads name1=servo-thread period1=1000000
halcmd addf lcec.read-all  servo-thread

######### УПРАВЛЕНИЕ ПРИВОДАМИ (оба канала)
# один сигнал на оба привода для удобства

halcmd net 0-drv-fault-reset  lcec.0.0.Control.FaultReset     
halcmd net 0-drv-halt         lcec.0.0.Control.Halt             

halcmd net 1-drv-fault-reset  lcec.0.1.Control.FaultReset
halcmd net 1-drv-halt         lcec.0.1.Control.Halt
# CSP / PPM specific: bit4..bit6 (в CSP они неактивны, пусть остаются закомментированными)
# halcmd net ppm-run          lcec.0.0.Control.Run               lcec.0.1.Control.Run
# halcmd net ppm-immediate    lcec.0.0.Control.ChangeSetImmediately  lcec.0.1.Control.ChangeSetImmediately
# halcmd net ppm-absolute     lcec.0.0.Control.AbsoluteTargetPosition lcec.0.1.Control.AbsoluteTargetPosition

halcmd net 0-estop-button        lcec.0.0.Control.QuickStop lcec.0.0.Control.EnableVoltage  
halcmd net 0-enable-drive-button lcec.0.0.Control.SwitchOn  lcec.0.0.Control.EnableOperation 
halcmd net 0-control-run        lcec.0.0.Control.Run

halcmd net 1-estop-button          lcec.0.1.Control.QuickStop lcec.0.1.Control.EnableVoltage
halcmd net 1-enable-drive-button   lcec.0.1.Control.SwitchOn  lcec.0.1.Control.EnableOperation
halcmd net 1-control-run        lcec.0.1.Control.Run

######### CSP LIMITERS — Ограничение позиции, скорости и ускорения
echo "Настраиваются лимиты позиции, скорости и ускорения..."


halcmd net 0-target-pos  lcec.0.0.TargetPosition

# --- Ось Y (slave 1) ---

halcmd net 1-target-pos  lcec.0.1.TargetPosition

# ВАЖНО: выше мы уже связали 0-target-pos/1-target-pos с TargetPosition через лимитеры,
# поэтому далее НЕ создаём ещё один net на те же TargetPosition, чтобы не ловить конфликты.

######### X — цели/факты
# Позиция (градусы, твой scale из XML) — сигнал уже существует и ведёт в TargetPosition
# halcmd net 0-target-pos      lcec.0.0.TargetPosition    # <-- НЕ ДУБЛИРУЕМ
halcmd net 0-actual-pos      lcec.0.0.ActualPosition
# Скорость (град/с в твоём scale)
halcmd net 0-target-vel      lcec.0.0.ProfileVelocity
halcmd net 0-actual-vel      lcec.0.0.ActualVelocity
# Услужебное
halcmd net 0-statusword      lcec.0.0.StatusWord
halcmd net 0-errorcode       lcec.0.0.ErrorCode
halcmd net 0-torque          lcec.0.0.Torque

######### Y — цели/факты
# halcmd net 1-target-pos      lcec.0.1.TargetPosition    # <-- НЕ ДУБЛИРУЕМ
halcmd net 1-actual-pos      lcec.0.1.ActualPosition
halcmd net 1-target-vel      lcec.0.1.ProfileVelocity
halcmd net 1-actual-vel      lcec.0.1.ActualVelocity
halcmd net 1-statusword      lcec.0.1.StatusWord
halcmd net 1-errorcode       lcec.0.1.ErrorCode
halcmd net 1-torque          lcec.0.1.Torque

######### ГРУППОВЫЕ сигналы (если нужно крутить обе оси одной ручкой)
halcmd net both-accel  lcec.0.0.Acceleration  lcec.0.1.Acceleration
halcmd net both-decel  lcec.0.0.Deceleration  lcec.0.1.Deceleration

# добавляем запись после формирования команд
halcmd addf lcec.write-all servo-thread

# старт HAL
halcmd start

echo "Готово."

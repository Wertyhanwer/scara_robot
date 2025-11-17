#!/usr/bin/env -S bash --login -i
set -e

cd /home/jetson/Desktop/scara_robot/tests
python startSh.py

sleep 5

cd /home/jetson/Desktop/scara_robot
export PYTHONPATH="/home/jetson/Desktop/scara_robot:${PYTHONPATH:-}"
python -m tests.simple_rotation_test


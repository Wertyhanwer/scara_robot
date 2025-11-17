#!/bin/bash --login
# ВАЖНО: --login → подхватит твою ~/.bashrc → будет (base) и всё остальное «как вручную»
set -e
# activate conda base
. "$HOME/miniconda3/etc/profile.d/conda.sh"
conda activate base

cd /home/jetson/Desktop/scara_robot/tests
python startSh.py
sleep 5
cd /home/jetson/Desktop/scara_robot
# Добавим корень проекта в PYTHONPATH, чтобы -m tests.simple_rotation_test точно нашёлся

python -m tests.simple_rotation_test


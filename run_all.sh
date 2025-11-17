#!/bin/bash -l
# login shell (-l) → загрузит ~/.bashrc → получим ровно то же окружение, как в твоём терминале "base)"
set -eo pipefail

# 1) на всякий случай активируем conda base (если .bashrc уже активирует — не помешает)
if [ -f "$HOME/miniconda3/etc/profile.d/conda.sh" ]; then
  . "$HOME/miniconda3/etc/profile.d/conda.sh"
  conda activate base
fi

REPO_ROOT="/home/jetson/Desktop/scara_robot"
PY="/home/jetson/miniconda3/bin/python"

# 2) добавим корень проекта в PYTHONPATH, чтобы работал `-m tests.simple_rotation_test`
export PYTHONPATH="$REPO_ROOT:${PYTHONPATH:-}"

# 3) (опционально) лог и диагностика
mkdir -p "$REPO_ROOT/logs"
LOG="$REPO_ROOT/logs/run_$(date +%F_%H-%M-%S).log"
exec > >(tee -a "$LOG") 2>&1

echo "=== RUN START $(date) ==="
echo "[whoami] $(whoami)"
echo "[conda] CONDA_DEFAULT_ENV=${CONDA_DEFAULT_ENV:-<none>}"
echo "[python] $(which python)"
echo "[env] PYTHONPATH=$PYTHONPATH"
echo "[env] PATH=$PATH"

# 4) первый скрипт — из tests (как ты делаешь вручную)
cd "$REPO_ROOT/tests"
"$PY" startSh.py

# пауза 5 сек
sleep 5

# 5) второй — из корня модулем (как ты делаешь вручную)
cd "$REPO_ROOT"
"$PY" -m tests.simple_rotation_test

echo "=== RUN DONE $(date) ==="


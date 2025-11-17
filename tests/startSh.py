import time
import subprocess


def main():
    subprocess.run(["/home/jetson/linuxcnc-dev/scripts/halrun", "-U"])

    time.sleep(1)
    # Запуск скрипта и ожидание завершения
    subprocess.run(["./setup_ethercat.sh"])
    time.sleep(1)

if __name__ == "__main__":
    main()

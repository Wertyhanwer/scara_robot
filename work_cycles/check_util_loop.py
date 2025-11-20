import multiprocessing as mp
import logging
import time


class CheckUtilLoop:
    def __init__(self, name, period_nc, utility: BasicCheckUtil, logger=None):
        self.name = name
        self._period_nc = period_nc
        self._utility = utility
        self._running = False
        self._process = None

        self._logger = logger
        self._setup_interprocess_logging()

    def _setup_interprocess_logging(self):
        if self._logger is None:
            logging.basicConfig(level=logging.INFO)
            self._logger = logging.getLogger(f"{self.name}_loop")

    def start(self):
        if self._running:
            self._logger.warning(f"Loop {self.name} is already running")
            return

        self._running = True
        self._process = mp.Process(
            target=self._run_wrapper,
            name=self.name,
            daemon=True
        )
        self._process.start()
        self._logger.info(f"Loop {self.name} started (PID: {self._process.pid})")

    def stop(self):
        if not self._running:
            return

        self._running = False
        if self._process is not None:
            self._process.terminate()
            self._process.join(timeout=2.0)
            self._process = None

        self._logger.info(f"Loop {self.name} stopped")

    def _run_wrapper(self):
        try:
            self._logger.info(f"Process {self.name} started")
            self._run_loop()
        except Exception as e:
            self._logger.error(f"Error in loop {self.name}: {e}")
        finally:
            self._logger.info(f"Process {self.name} finished")

    def _run_loop(self):
        while self._running:
            start_time = time.time()
            try:
                self._utility.check_state()
            except Exception as e:
                self._logger.error(f"Error in {self._utility.name}: {e}")
                break

            elapsed = time.time() - start_time
            sleep_time = max(0.001, self._period_nc - elapsed)
            if sleep_time > 0:
                time.sleep(sleep_time)

    def is_running(self):
        return self._running and self._process is not None and self._process.is_alive()

    def get_period(self):
        return self._period_nc


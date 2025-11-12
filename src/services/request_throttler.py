import logging
import threading
import time

LOGGER = logging.getLogger(__name__)

class RequestThrottler:
    """
    Simple time-based throttler to enforce a maximum rate per minute.
    """

    def __init__(self, rate_per_minute: int = 60) -> None:
        self.rate_per_minute = max(1, rate_per_minute)
        self._lock = threading.Lock()
        self._min_interval = 60.0 / float(self.rate_per_minute)
        self._last_request_ts = 0.0

    def acquire(self) -> None:
        with self._lock:
            now = time.monotonic()
            elapsed = now - self._last_request_ts
            if elapsed < self._min_interval:
                sleep_for = self._min_interval - elapsed
                LOGGER.debug("Throttling for %.3f seconds.", sleep_for)
                time.sleep(sleep_for)
            self._last_request_ts = time.monotonic()
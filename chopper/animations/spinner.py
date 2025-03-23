import threading
import itertools
import sys
import time

class Spinner:
    def __init__(self, message="Loading..."):
        self.message = message
        self.stop_event = threading.Event()
        self.spinner_thread = threading.Thread(target=self._spin)

    def _spin(self):
        spinner_cycle = itertools.cycle(['|', '/', '-', '\\'])
        while not self.stop_event.is_set():
            sys.stdout.write(f'\r{self.message} {next(spinner_cycle)}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\r' + ' ' * (len(self.message) + 4) + '\r')  # Clean line

    def start(self):
        self.spinner_thread.start()

    def stop(self):
        self.stop_event.set()
        self.spinner_thread.join()

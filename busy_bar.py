#!/bin/env python3
"""
Provies a context manager and decorator that prints a work bar
during function execution.
This is done using multiprocessing.Process and writing to sys.stdout.

Examples:
@progress()
def long_work():
    sleep(3)

with Progress("Busy..."):
    sleep(3)
"""
from sys import stdout
from time import sleep
from itertools import cycle
from multiprocessing import Process

DEFAULT_WORK = "Working..."
DEFAULT_DONE = "Done!"
DEFAULT_RATE = 0.15


class Progress(Process):
    """Contextmanager progress bar."""
    def __init__(self, work=DEFAULT_WORK, done=DEFAULT_DONE, rate=DEFAULT_RATE):
        super().__init__()
        self.cycle = cycle("|/-\\")
        self.work = work
        self.done = done
        self.rate = rate

    def run(self, *args, **kw):
        while True:
            char = next(self.cycle)
            stdout.write(f"\r{self.work} {char}\r")
            sleep(self.rate)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args, **kw):
        print(f"\r{self.work} {self.done}")
        self.terminate()


def progress(work=DEFAULT_WORK, done=DEFAULT_DONE, rate=DEFAULT_RATE):
    """Decorator progress bar."""
    def dec(func):
        def decored(*args, **kw):
            with Progress(work, done, rate):
                return func(*args, **kw)
        return decored
    return dec


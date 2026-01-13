import time
import psutil
import os

def measure_time(func, *args, **kwargs):
    """
    Measures execution time of a function.
    """
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time

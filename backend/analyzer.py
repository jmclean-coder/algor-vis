import timeit
import psutil
import os

# def measure_time(func, *args, **kwargs):
#     """
#     Measures execution time of a function.
#     """
#     start_time = time.time()
#     func(*args, **kwargs)
#     end_time = time.time()
#     return end_time - start_time

import timeit

def measure_execution_time(func, *args, **kwargs):
    exec_time = timeit.timeit(lambda: func(*args, **kwargs), number=1)
    return exec_time

def measure_memory(func, *args, **kwargs):
    """
    Measures the peak memory usage of a function.
    """
    process = psutil.Process(os.gitpid())
    before_memory = process.memory_info().rss
    func(*args, **kwargs)
    after_memory = process.memory_info().rss
    return (after_memory - before_memory) / 1024 / 1024  # Memory in MB
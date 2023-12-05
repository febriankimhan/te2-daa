import tracemalloc
import time

from partition import DP, BNB
from generator import generate_array

def run_dp(arr):
    tracemalloc.start()
    start_time = time.time()

    DP.partition(arr)

    end_time = time.time()
    used_memory = tracemalloc.get_traced_memory()[1]/1024
    tracemalloc.stop()

    time_taken = (end_time - start_time) * 1000

    return (used_memory, time_taken)

def run_bnb(arr):
    tracemalloc.start()
    start_time = time.time()

    BNB.partition(arr)

    end_time = time.time()
    used_memory = tracemalloc.get_traced_memory()[1]/1024
    tracemalloc.stop()

    time_taken = (end_time - start_time) * 1000

    return (used_memory, time_taken)


if __name__ == "__main__":
    for n in [10, 40, 80]:
        arr = generate_array(n, 0, 500, 0, False)
        print(f'Array size {n}')
        mem_dp, time_dp = run_dp(arr)
        mem_bnb, time_bnb = run_bnb(arr)
        print(f'Time (dp)   : {time_dp} ms')
        print(f'Time (bnb)  : {time_bnb} ms')
        print(f'Memory (dp)     : {mem_dp} KB')
        print(f'Memory (bnb)    : {mem_bnb} KB')
        print()
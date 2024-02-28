import random
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

array_sizes = [10, 100, 1000, 10000]

for size in array_sizes:
    best_case_data = [i for i in range(size)]
    worst_case_data = [size - i for i in range(size)]
    average_case_data = [random.randint(0, size * 10) for _ in range(size)]

    # Best case benchmark
    start_time = time.time_ns()
    quicksort(best_case_data.copy())
    end_time = time.time_ns()
    print(f"Best Case - Array Size: {size}, Time: {end_time - start_time} ns")

    # Worst case benchmark
    start_time = time.time_ns()
    quicksort(worst_case_data.copy())
    end_time = time.time_ns()
    print(f"Worst Case - Array Size: {size}, Time: {end_time - start_time} ns")

    # Average case benchmark
    start_time = time.time_ns()
    quicksort(average_case_data.copy())
    end_time = time.time_ns()
    print(f"Average Case - Array Size: {size}, Time: {end_time - start_time} ns\n")

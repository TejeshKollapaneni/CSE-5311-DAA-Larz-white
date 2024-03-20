

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def ith_order_statistic(arr, i):
    quicksort(arr, 0, len(arr) - 1)
    return arr[i - 1]

# Example usage:
arr = [5, 8, 2, 11, 6, 9]
i = 2
print(f"The {i}nd order statistic is: {ith_order_statistic(arr, i)}")

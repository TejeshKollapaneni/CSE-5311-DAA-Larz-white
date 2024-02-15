import heapq

def merge_sorted_arrays(array1, array2, array3):
    return list(heapq.merge(array1, array2, array3))

if __name__ == "__main__":
    array01 = [1, 3, 5, 7]
    array02 = [2, 4, 6, 8]
    array03 = [0, 9, 10, 11]
    merged_array = merge_sorted_arrays(array01, array02, array03)
    print(merged_array)
    
    array11 = [1, 3, 7]
    array12 = [2, 4, 8]
    array13 = [9, 10, 11]
    merged_array = merge_sorted_arrays(array11, array12, array13)
    print(merged_array)


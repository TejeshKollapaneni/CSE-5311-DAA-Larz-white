def remove_duplicates(arr):
    max_val = arr[-1]
    frequency_array = [0] * (max_val + 1)
    count = 0
    for i in arr:
        if frequency_array[i] == 0:
            count += 1
            frequency_array[i] += 1
    sorted_array = [0] * count
    count1 = 0
    for i, freq in enumerate(frequency_array):
        if freq == 1:
            sorted_array[count1] = i
            count1 += 1
    return sorted_array

arr1 = [2, 2, 2, 2, 2]
print("Array 1 Before Removing Duplicates: ")
print(arr1)
print("Array After Removing Duplicates: ")
print(remove_duplicates(arr1))

arr2 = [1, 2, 2, 3, 4, 4, 4, 5, 5]
print("Array 2 Before Removing Duplicates: ")
print(arr2)
print("Array After Removing Duplicates: ")
print(remove_duplicates(arr2))

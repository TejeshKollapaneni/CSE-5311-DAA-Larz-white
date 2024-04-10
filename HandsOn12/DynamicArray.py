import ctypes

class DynamicArray:
    def __init__(self):
        self._size = 0
        self._array = self.createArray(1)

    def __len__(self):
        return self._size

    def __repr__(self):
        return f"DynamicArray({[self.get(i) for i in range(self._size)]})"

    def add(self, value):
        if self._size == len(self._array):
            self.resizeArray(2 * len(self._array))
        self._array[self._size] = value
        self._size += 1

    def get(self, index):
        if not 0 <= index < self._size:
            raise IndexError('Index out of range')
        return self._array[index]

    def remove(self, value):
        index = 0
        while index < self._size:
            if self._array[index] == value:
                for i in range(index, self._size - 1):
                    self._array[i] = self._array[i + 1]
                self._size -= 1
                return
            index += 1
        raise ValueError('Value not found')

    def createArray(self, capacity):
        return (ctypes.c_int * capacity)()

    def resizeArray(self, new_capacity):
        new_array = self.createArray(new_capacity)
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array

# Example
Array = DynamicArray()
Array.add(15)
Array.add(25)
Array.add(35)
Array.add(45)
Array.add(55)

print("Array size:", len(Array))
print("Values in the Array:", Array)

Array.add(65)
print("Values after adding:", Array)
print("Array size after adding:", len(Array))
print("Value at index 2:", Array.get(2))

Array.remove(25)
print("Values after removing 25:", Array)
print("Array size after removing:", len(Array))

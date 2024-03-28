class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class HashTable:
    def __init__(self, initial_size=8):
        self.size = initial_size
        self.count = 0
        self.array = [None] * initial_size

    def insert(self, key, value):
        if self.is_full():
            self.resize(self.size * 2)

        index = self.hash_function(key)
        new_node = Node(key, value)

        if self.array[index] is None:
            self.array[index] = new_node
        else:
            current = self.array[index]
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

        self.count += 1

    def remove(self, key):
        index = self.hash_function(key)
        current = self.array[index]

        while current:
            if current.key == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.array[index] = current.next
                if current.next:
                    current.next.prev = current.prev
                self.count -= 1

                if self.is_empty() and self.size > 1:
                    self.resize(self.size // 2)
                return
            current = current.next

    def search(self, key):
        index = self.hash_function(key)
        current = self.array[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None  # Key not found

    def hash_function(self, key):
        A = 0.6180339887  # Multiplicative constant (Golden ratio)
        f = key * A
        index = int(self.size * (f - int(f)))
        return index

    def is_full(self):
        return self.count >= self.size

    def is_empty(self):
        return self.count == 0

    def resize(self, new_size):
        new_array = [None] * new_size

        for i in range(self.size):
            current = self.array[i]
            while current:
                index = self.hash_function(current.key)
                if new_array[index] is None:
                    new_array[index] = Node(current.key, current.value)
                else:
                    new_current = new_array[index]
                    while new_current.next:
                        new_current = new_current.next
                    new_current.next = Node(current.key, current.value)
                    new_current.next.prev = new_current
                current = current.next

        self.size = new_size
        self.array = new_array

# Example usage
ht = HashTable()
ht.insert(11, 110)
ht.insert(22, 220)
ht.insert(33, 330)
ht.insert(44, 440)
ht.insert(55, 550)
ht.insert(66, 660)
ht.insert(77, 770)

print("Value for key 33:", ht.search(33))

ht.remove(33)

print("Value for key 33 after removal:", ht.search(33))

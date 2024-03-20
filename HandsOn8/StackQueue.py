class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = [0] * max_size
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1

    def push(self, value):
        if self.is_full():
            print("Stack Overflow")
            return
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        value = self.stack[self.top]
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack[self.top]

    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        for i in range(self.top, -1, -1):
            print(self.stack[i])


class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [0] * max_size
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def enqueue(self, value):
        if self.is_full():
            print("Queue Overflow")
            return
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = value
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        value = self.queue[self.front]
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return value

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        i = self.front
        while i != self.rear:
            print(self.queue[i])
            i = (i + 1) % self.max_size
        print(self.queue[self.rear])


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return None
        if self.head.next is None:
            data = self.head.data
            self.head = None
            return data
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        data = second_last.next.data
        second_last.next = None
        return data

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


# Example usage:
stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)  # Stack Overflow
stack.display()
print("Popped:", stack.pop())
print("Top element:", stack.peek())

queue = Queue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)  # Queue Overflow
queue.display()
print("Dequeued:", queue.dequeue())
print("Front element:", queue.peek())

linked_list = LinkedList()
linked_list.insert_at_end(1)
linked_list.insert_at_end(2)
linked_list.insert_at_end(3)
linked_list.insert_at_end(4)
linked_list.insert_at_end(5)
linked_list.display()
print("Deleted from beginning:", linked_list.delete_at_beginning())
print("Deleted from end:", linked_list.delete_at_end())
linked_list.display()

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
        return "ok"

    def pop(self):
        if self.top is None:
            raise IndexError("pop from empty stack")
        value = self.top.value
        self.top = self.top.next
        self._size -= 1
        return value

    def top(self):
        if self.top is None:
            raise IndexError("top from empty stack")
        return self.top.value

    def size(self):
        return self._size

    def clear(self):
        self.top = None
        self._size = 0
        return "ok"
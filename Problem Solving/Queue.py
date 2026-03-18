import sys
from collections import deque


# https://informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=58#1
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
        return "ok"

    def pop(self):
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return value

    def front(self):
        return self.head.value

    def size(self):
        return self._size

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        return "ok"

def process_queue_commands():
    queue = Queue()

    for line in sys.stdin:
        command = line.strip().split()

        if command[0] == "push":
            print(queue.push(int(command[1])))
        elif command[0] == "pop":
            if queue.size():
                print(queue.pop())
            else:
                print("error")
        elif command[0] == "front":
            if queue.size():
                print(queue.front())
            else:
                print("error")
        elif command[0] == "size":
            print(queue.size())
        elif command[0] == "clear":
            print(queue.clear())
        elif command[0] == "exit":
            print("bye")
            break


# https://informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=112502#1
def simulate_queue_operations():
    queue = deque()
    error = False

    with open('input.txt', 'r') as fin, open('output.txt', 'w') as fout:
        for line in map(lambda x: x.strip(), fin.readlines()):
            if line[0] == '+':
                number = int(line[1:])
                queue.append(number)
            else:
                if queue:
                    queue.popleft()
                else:
                    fout.write('ERROR')
                    exit()
    
    if queue:
        fout.write(' '.join(map(str, queue)))
    else:
        fout.write('EMPTY')
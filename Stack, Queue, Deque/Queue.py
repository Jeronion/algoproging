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

def solution_58():
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
def solution_112502():
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


# https://informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=112504#1
def solution_112504():
    with open("input.txt", "r") as fin:
        finput = lambda: fin.readline().rstrip()
        N, M = map(int, finput().split())
        x, y = map(int, finput().split())
        color = int(finput())
        matrix = [list(map(int, finput().split())) for _ in range(N)]
    
    counter = 0
    old_color = matrix[y][x]
    matrix[y][x] = color
    queue = deque()
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
    if color != old_color:
        queue.append((x, y))
        counter = 1
    
    while queue:
        nx, ny = queue.popleft()
        
        for d in directions:
            dx, dy = nx + d[0], ny + d[1]
            if dx < 0 or dx >= M or dy < 0 or dy >= N:
                continue
            if matrix[dy][dx] == old_color:
                matrix[dy][dx] = color
                queue.append((dx, dy))
                counter += 1
    
    with open("output.txt", "w") as fout:
        fout.write(str(counter) + "\n")
        for row in matrix:
            fout.write(" ".join(map(str, row)) + "\n")




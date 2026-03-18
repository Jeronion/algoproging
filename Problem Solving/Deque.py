from collections import deque
import sys


class ListNode:
    __slots__ = ["key", "prev", "next"]

    def __init__(self, key: int) -> None:
        self.key = key
        self.prev = None
        self.next = None


class MyDeque:
    __slots__ = ["begin", "end", "length"]

    def __init__(self):
        self.begin = None
        self.end = None
        self.length = 0

    def begin_deque(self, key: int) -> None:
        node = ListNode(key)
        self.begin = node
        self.end = node
        self.length = 1

    def push_front(self, key: int) -> str:
        if self.begin is None:
            self.begin_deque(key)
            return "ok"

        node = ListNode(key)
        self.begin.prev = node
        node.next = self.begin
        self.begin = node
        self.length += 1
        return "ok"

    def push_back(self, key: int) -> str:
        if self.end is None:
            self.begin_deque(key)
            return "ok"

        node = ListNode(key)
        self.end.next = node
        node.prev = self.end
        self.end = node
        self.length += 1
        return "ok"

    def pop_front(self):
        if self.begin is None:
            return "error"

        res = self.begin.key

        if self.begin == self.end:
            self.begin = None
            self.end = None
        else:
            self.begin = self.begin.next
            self.begin.prev = None

        self.length -= 1
        return res

    def pop_back(self):
        if self.end is None:
            return "error"

        res = self.end.key

        if self.begin == self.end:
            self.begin = None
            self.end = None
        else:
            self.end = self.end.prev
            self.end.next = None

        self.length -= 1
        return res

    def front(self):
        if self.begin is None:
            return "error"
        return self.begin.key

    def back(self):
        if self.end is None:
            return "error"
        return self.end.key

    def size(self):
        return self.length

    def clear(self):
        self.begin = None
        self.end = None
        self.length = 0
        return "ok"


# https://informatics.msk.ru/mod/statements/view.php?id=207&chapterid=62#1
def process_deque_commands():
    dq = MyDeque()

    for line in sys.stdin:
        cmd = line.strip().split()

        if cmd[0] == "push_front":
            print(dq.push_front(int(cmd[1])))

        elif cmd[0] == "push_back":
            print(dq.push_back(int(cmd[1])))

        elif cmd[0] == "pop_front":
            print(dq.pop_front())

        elif cmd[0] == "pop_back":
            print(dq.pop_back())

        elif cmd[0] == "front":
            print(dq.front())

        elif cmd[0] == "back":
            print(dq.back())

        elif cmd[0] == "size":
            print(dq.size())

        elif cmd[0] == "clear":
            print(dq.clear())

        elif cmd[0] == "exit":
            print("bye")
            break


# https://informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=112984#1
def process_goblin_queue():
    N = int(input())
    data = [input().split() for _ in range(N)]
    left, right = deque(), deque()
    for line in data:
        if line[0] == "-":
            print(left.popleft())
        elif line[0] == "+":
            right.append(line[1])
        else:
            if len(left) > len(right):
                right.appendleft(line[1])
            else:
                left.append(line[1])
        if len(left) < len(right):
            left.append(right.popleft())
        elif len(left) > len(right) + 1:
            right.appendleft(left.pop())


# https://informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=112507#1
def distribute_tasks_by_type():
    with open("input.txt", "r") as fin, open("output.txt", "w") as fout:
        N = int(fin.readline().strip())
        deques = [deque() for _ in range(N)]

        for line in fin:
            t, num = line.strip().split()
            deques[int(t) - 1].append(num)

        for i in range(N):
            while deques[i]:
                fout.write(f"{i + 1} {deques[i].popleft()}\n")


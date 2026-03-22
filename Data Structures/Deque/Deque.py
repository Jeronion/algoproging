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
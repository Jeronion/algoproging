from collections import deque
import sys

# https://informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=112984#1
def solution_112984():
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
def solution_112507():
    with open("input.txt", "r") as fin, open("output.txt", "w") as fout:
        N = int(fin.readline().strip())
        deques = [deque() for _ in range(N)]

        for line in fin:
            t, num = line.strip().split()
            deques[int(t) - 1].append(num)

        for i in range(N):
            while deques[i]:
                fout.write(f"{i + 1} {deques[i].popleft()}\n")

solution_112507()
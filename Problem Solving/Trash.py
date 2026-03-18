from collections import deque
import math
import sys


# https://informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=112491#1
def solution_112491():
    stack = []
    error = False

    with open("input.txt", "r") as fin:
        for line in fin:
            line = line.strip()
            if line == "":
                break

            if line[0] == '+':
                try:
                    number = int(line[1:])
                    stack.append(number)
                except:
                    error = True
                    break
            elif line == '-':
                if stack:
                    stack.pop()
                else:
                    error = True
                    break
            else:
                error = True
                break

    with open("output.txt", "w") as fout:
        if error:
            fout.write("ERROR")
        else:
            if not stack:
                fout.write("EMPTY")
            else:
                fout.write(" ".join(map(str, stack)))



# https://informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=112493#1
def solution_112493():
    def swap():
        b = dq.pop()
        a = dq.pop()
        dq.append(b)
        dq.append(a)


    def dup():
        a = dq.pop()
        dq.append(a)
        dq.append(a)


    def over():
        b = dq.pop()
        a = dq.pop()
        dq.append(a)
        dq.append(b)
        dq.append(a)


    def plus():
        b = dq.pop()
        a = dq.pop()
        dq.append(a + b)


    def minus():
        b = dq.pop()
        a = dq.pop()
        dq.append(a - b)


    def mul():
        b = dq.pop()
        a = dq.pop()
        dq.append(a * b)


    def div():
        b = dq.pop()
        a = dq.pop()
        dq.append(a // b)


    dq = deque()
    functions = {"DROP": dq.pop, "SWAP": swap, "DUP": dup, "OVER": over, "+": plus, "-": minus, "*": mul, "/": div}


    with open("input.txt", "r") as f, open("output.txt", "w") as f2:
        try:
            while (S := f.readline().strip()):
                try:
                    dq.append(int(S))
                except:
                    functions[S]()

            if not dq:
                f2.write("EMPTY")
            else:
                f2.write(' '.join(map(str, dq)))
        except:
            f2.write("ERROR")



# https://informatics.msk.ru/mod/statements/view.php?id=206&chapterid=51#1
def solution_51():
    seq = input()
    br_d = {")": "(", "]": "[", "}": "{"}
    stack = []
    for i in seq:
        if i in "({[":
            stack.append(i)
        else:
            if stack:
                if stack[-1] == br_d[i]:
                    stack.pop()
                else:
                    return "no"
            else:
                return "no"
    return "no" if stack else "yes"


# https://informatics.msk.ru/mod/statements/view.php?id=206&chapterid=51#1
def solution_51():
    seq = input()
    br_d = {")": "(", "]": "[", "}": "{"}
    stack = []
    for i in seq:
        if i in "({[":
            stack.append(i)
        else:
            if stack:
                if stack[-1] == br_d[i]:
                    stack.pop()
                else:
                    return "no"
            else:
                return "no"
    return "no" if stack else "yes"


# https://informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=114261#1
def solution_114261():
    s = input()
    nums = []
    ops = []
    priority = {"+": 1, "-": 1, "*": 2, "/": 2}
    
    def apply_op(a, b, op):
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        return a // b
    
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            nums.append(num)
        else:
            while ops and priority[ops[-1]] >= priority[s[i]]:
                b = nums.pop()
                a = nums.pop()
                op = ops.pop()
                nums.append(apply_op(a, b, op))
            ops.append(s[i])
            i += 1
    
    while ops:
        b = nums.pop()
        a = nums.pop()
        op = ops.pop()
        nums.append(apply_op(a, b, op))
    
    print(nums[0])


# https://informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=114262#1
def solution_114262():
    seq = input()
    priority = {"+": 1, "-": 1, "*": 2, "/": 2}
    ops = deque()
    stack = deque()
    i = 0
    
    def apply_op(a, b, op):
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        return a // b
    
    while i < len(seq):
        if seq[i].isdigit():
            num = 0
            while i < len(seq) and seq[i].isdigit():
                num = num * 10 + int(seq[i])
                i += 1
            stack.append(num)
            continue
        
        if seq[i] in priority:
            while (ops and ops[-1] in priority and
                   priority[ops[-1]] >= priority[seq[i]]):
                B, A = stack.pop(), stack.pop()
                op = ops.pop()
                stack.append(apply_op(A, B, op))
            ops.append(seq[i])
        
        elif seq[i] == "(":
            ops.append(seq[i])
        
        elif seq[i] == ")":
            while ops and ops[-1] != "(":
                B, A = stack.pop(), stack.pop()
                op = ops.pop()
                stack.append(apply_op(A, B, op))
            ops.pop()
        
        i += 1

    while ops:
        b = stack.pop()
        a = stack.pop()
        op = ops.pop()
        stack.append(apply_op(a, b, op))
    
    print(stack[0])


# informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=112500#1
def solution_112500():
    seq = input()
    priority = {"+": 1, "-": 1, "*": 2, "/": 2}
    stack = deque()
    ops = deque()
    i = 0
    
    def apply_op(a, b, op):
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "*":
            return a * b
        if op == "/":
            return a / b
    
    func_dict = {"sin(": math.sin, "cos(": math.cos, "abs(": abs, "sqrt(": math.sqrt, "(": lambda x: x}
    
    while i < len(seq):
        if seq[i].isdigit():
            num = 0
            while i < len(seq) and seq[i].isdigit():
                num = num * 10 + int(seq[i])
                i += 1
            stack.append(num)
            continue
        
        if seq[i] in priority:
            while ops and ops[-1] in priority and priority[seq[i]] <= priority[ops[-1]]:
                B, A = stack.pop(), stack.pop()
                op = ops.pop()
                stack.append(apply_op(A, B, op))
            ops.append(seq[i])
        
        elif seq[i] == "(":
            ops.append(seq[i])
        
        elif seq[i].isalpha():
            func = ''
            while i < len(seq) and seq[i].isalpha():
                func += seq[i]
                i += 1
            func += seq[i]
            ops.append(func)
        
        elif seq[i] == ")":
            while ops and ops[-1] in priority:
                B, A = stack.pop(), stack.pop()
                op = ops.pop()
                stack.append(apply_op(A, B, op))
            stack.append(func_dict[ops.pop()](stack.pop()))
        
        i += 1
    
    while ops:
        B, A = stack.pop(), stack.pop()
        op = ops.pop()
        stack.append(apply_op(A, B, op))
    
    print(f"{round(stack.pop(), 3):.3f}")


# https://informatics.msk.ru/mod/statements/view.php?id=206&chapterid=49#1
def solution_49():
    # не ебу почему не работает
    d9, d10, d11 = deque(), deque(), deque()
    for row in sys.stdin:
        if not row:
            continue
        row = row.strip()
        if row[:2] == "9 ":
            d9.append(row)
        elif row[:2] == "10":
            d10.append(row)
        else:
            d11.append(row)
    while d9:
        print(d9.popleft())
    while d10:
        print(d10.popleft())
    while d11:
        print(d11.popleft())


# https://informatics.msk.ru/mod/statements/view.php?id=654&chapterid=207#1
def solution_207():
    N = int(input())
    dp = [1] * (N + 2)
    for i in range(2, N + 2):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[N + 1]


# https://informatics.msk.ru/mod/statements/view.php?id=654&chapterid=913#1
def solution_913():
    N = int(input())
    dp = [1] * (N + 2)
    for i in range(2, N + 2):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[N + 1]


# https://informatics.msk.ru/mod/statements/view.php?id=654&chapterid=912#1
def solution_912():
    N = int(input())
    dp = [1] * (N + 2)
    dp[2] = 2
    for i in range(3, N + 2):
        dp[i] = sum(dp[i - 3: i])
    return dp[N + 1]

print(*range(13, 26))

т е
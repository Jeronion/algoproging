from collections import deque
import math
import sys

# https://informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=54#
def solution_54():
    stack = []
    while True:
        s = input().split()
        if s[0] == "push":
            stack.append(int(s[1]))
            print("ok")
        elif s[0] == "pop":
            print(stack.pop())
        elif s[0] == "back":
            print(stack[-1])
        elif s[0] == "size":
            print(len(stack))
        elif s[0] == "clear":
            stack.clear()
            print("ok")
        else:
            print("bye")
            exit()

# https://informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=56#
def solution_56():
    stack = []
    while True:
        s = input().split()
        if s[0] == "push":
            stack.append(int(s[1]))
            print("ok")
        elif s[0] == "pop":
            if stack:
                print(stack.pop())
            else:
                print("error")
        elif s[0] == "back":
            if stack:
                print(stack[-1])
            else:
                print("error")
        elif s[0] == "size":
            print(len(stack))
        elif s[0] == "clear":
            stack.clear()
            print("ok")
        elif s[0] == "exit":
            print("bye")
            break


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



# https://informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=112492#1
def solution_112492():
    seq = input()
    stack = deque()
    brackets_dict = {">": "<", ")": "(", "}": "{", "]": "["}
    for i in seq:
        if i not in "(){}[]<>":
            continue
        if i in "{[<(":
            stack.append(i)
        elif stack:
            if brackets_dict[i] != stack.pop():
                return False
        else:
            return False
    else:
        if stack:
            return False
        else:
            return True


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


# https://informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=112484#1
def solution_112484():
    with open("input.txt", "r") as fin, open("output.txt", "w") as fout:
        N = fin.readline()
        arr = map(int, fin.readline().strip().split())
        stack = deque()
        for i in arr:
            stack.append(i)
        while stack:
            fout.write(str(stack.pop()) + " ")


# https://informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=112494#1
def solution_112494():
    data = input().split()
    stack = deque()
    try:
        for s in data:
            if s.isdigit():
                stack.append(int(s))
            else:
                if s == "*":
                    B, A = stack.pop(), stack.pop()
                    stack.append(A * B)
                elif s == "+":
                    B, A = stack.pop(), stack.pop()
                    stack.append(A + B)
                elif s == "-":
                    B, A = stack.pop(), stack.pop()
                    stack.append(A - B)
                elif s == "/":
                    B, A = stack.pop(), stack.pop()
                    stack.append(A // B)
    except:
        print("ERROR")
    else:
        if stack:
            A = stack.pop()
            if stack:
                print("ERROR")
            else:
                print(A)


# https://informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=112495#1
def solution_112495():
    def plus():
        B, A = stack.pop(), stack.pop()
        stack.append(A + B)
    
    def minus():
        B, A = stack.pop(), stack.pop()
        stack.append(A - B)
    
    def mul():
        B, A = stack.pop(), stack.pop()
        stack.append(A * B)
    
    def div():
        B, A = stack.pop(), stack.pop()
        stack.append(A / B)
    
    def sqrt():
        A = stack.pop()
        stack.append(math.sqrt(A))
    
    def cos():
        A = stack.pop()
        stack.append(math.cos(A))

    def sin():
        A = stack.pop()
        stack.append(math.sin(A))
    
    def abs_():
        A = stack.pop()
        stack.append(abs(A))
    
    func_dict = {"+": plus, "-": minus, "*": mul, "/": div, "sqrt": sqrt, "cos": cos, "sin": sin, "abs": abs_}
    data = input().split()
    stack = deque()
    try:
        for s in data:
            if func_dict.get(s, None) is not None:
                func_dict[s]()
            else:
                stack.append(int(s))  
    except:
        print("ERROR")
    else:
        if stack:
            A = stack.pop()
            if stack:
                print("ERROR")
            else:
                print(f"{A:.3f}")


# https://informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=112496#1
def solution_112496():
    def plus():
        B, A = stack.pop(), stack.pop()
        stack.append(A + B)
    
    def minus():
        B, A = stack.pop(), stack.pop()
        stack.append(A - B)
    
    def mul():
        B, A = stack.pop(), stack.pop()
        stack.append(A * B)
    
    def div():
        B, A = stack.pop(), stack.pop()
        stack.append(A / B)
    
    def sqrt():
        A = stack.pop()
        stack.append(math.sqrt(A))
    
    def cos():
        A = stack.pop()
        stack.append(math.cos(A))

    def sin():
        A = stack.pop()
        stack.append(math.sin(A))
    
    def abs_():
        A = stack.pop()
        stack.append(abs(A))
    
    func_dict = {"+": plus, "-": minus, "*": mul, "/": div, "sqrt": sqrt, "cos": cos, "sin": sin, "abs": abs_}
    seq, *vars = list(map(lambda x: x.strip(), sys.stdin.readlines()))
    stack = deque()
    seq = seq.split()
    vars = {var.split("=")[0]: int(var.split("=")[1]) for var in vars}
    try:
        for s in seq:
            if func_dict.get(s) is not None:
                func_dict[s]()
            elif vars.get(s) is not None:
                stack.append(vars[s])
            else:
                stack.append(int(s))  
    except:
        print("ERROR")
    else:
        if stack:
            A = stack.pop()
            if stack:
                print("ERROR")
            else:
                print(f"{A:.3f}")


# https://informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=112497#1
def solution_112497():
    expr = input()
    priority = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    output = []
    i = 0

    while i < len(expr):
        if expr[i].isdigit():
            num = []
            while i < len(expr) and expr[i].isdigit():
                num.append(expr[i])
                i += 1
            output.append(''.join(num))
            continue

        op = expr[i]
        while stack and priority[stack[-1]] >= priority[op]:
            output.append(stack.pop())
        stack.append(op)
        i += 1

    while stack:
        output.append(stack.pop())

    print(' '.join(output))


# https://informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=112498#1
def solution_112498():
    expr = input()
    priority = {'+': 1, '-': 1, '*': 2, '/': 2, "sin": 3, "cos": 3, "abs": 3, "sqrt": 3}
    stack = []
    output = []
    i = 0

    while i < len(expr):
        if expr[i].isdigit():
            num = []
            while i < len(expr) and expr[i].isdigit():
                num.append(expr[i])
                i += 1
            output.append(''.join(num))
            continue
        
        if expr[i].isalpha():
            word = []
            while i < len(expr) and expr[i].isalpha():
                word.append(expr[i])
                i += 1
            stack.append("".join(word))
            continue
        
        if expr[i] == "(":
            stack.append(expr[i])
            
        elif expr[i] == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()
            
            if stack and stack[-1] in priority and stack[-1].isalpha():
                output.append(stack.pop())
        
        elif expr[i] in priority:
            while (stack and stack[-1] in priority and priority[stack[-1]] >= priority[expr[i]]):
                output.append(stack.pop())
            stack.append(expr[i])
        
        i += 1

    while stack:
        output.append(stack.pop())

    print(' '.join(output))


# https://informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=114261#1
def apply_op(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    return a // b


# https://informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=114261#1
def solution_114261():
    s = input()
    nums = []
    ops = []
    priority = {"+": 1, "-": 1, "*": 2, "/": 2}
    
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


solution_114261()
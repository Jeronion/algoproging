from collections import deque
import math
import sys


# https://informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=112492#1
def brackets_check():
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


# https://informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=112484#1
def reverse_array():
    with open("input.txt", "r") as fin, open("output.txt", "w") as fout:
        N = fin.readline()
        arr = map(int, fin.readline().strip().split())
        stack = deque()
        for i in arr:
            stack.append(i)
        while stack:
            fout.write(str(stack.pop()) + " ")


# https://informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=112496#1
def evaluate_postfix_expression():
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


# https://informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=112498#1
def infix_to_postfix():
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


# https://informatics.msk.ru/mod/statements/view.php?id=11575&chapterid=112501#1
def evaluate_infix_expression():
    seq = input()
    vars = {i: int(j) for i, j in map(lambda x: x.rstrip().split("="), sys.stdin.readlines())}
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
        
        if seq[i].isalpha():
            word = ''
            while i < len(seq) and seq[i].isalpha():
                word += seq[i]
                i += 1
            if i != len(seq) and word + seq[i] in func_dict:
                word += seq[i]
                ops.append(word)
                i += 1
            else:
                stack.append(vars[word])
            continue
        
        if seq[i] in priority:
            while ops and ops[-1] in priority and priority[seq[i]] <= priority[ops[-1]]:
                B, A = stack.pop(), stack.pop()
                op = ops.pop()
                stack.append(apply_op(A, B, op))
            ops.append(seq[i])
        
        elif seq[i] == "(":
            ops.append(seq[i])
        
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
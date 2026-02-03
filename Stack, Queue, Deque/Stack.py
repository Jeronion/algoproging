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

solution_56()
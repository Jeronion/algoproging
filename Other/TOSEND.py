import sys
sys.setrecursionlimit(10**6)

class Node:
    __slots__  = ["key", "left", "right"]
    
    def __init__(self, key: int) -> None:
        self.key = key
        self.left = None
        self.right = None


def delete(root: Node | None, key: int) -> tuple[Node | None, bool]:
    if root is None:
        return None, False

    if key < root.key:
        root.left, deleted = delete(root.left, key)
        return root, deleted

    elif key > root.key:
        root.right, deleted = delete(root.right, key)
        return root, deleted

    else:
        if root.left is None and root.right is None:
            return None, True

        if root.left is None:
            return root.right, True
        if root.right is None:
            return root.left, True

        max_left = root.left
        while max_left.right:
            max_left = max_left.right

        root.key = max_left.key
        root.left, _ = delete(root.left, max_left.key)

        return root, True



def insert(root: Node | None, key: int) -> Node:
    dummy = root
    node = Node(key)
    if root is None:
        print("DONE")
        return node
    while True:
        if key < dummy.key:
            if dummy.left is None:
                dummy.left = node
                break
            dummy = dummy.left
        elif key > dummy.key:
            if dummy.right is None:
                dummy.right = node
                break
            dummy = dummy.right
        else:
            print("ALREADY")
            return root
    print("DONE")
    return root


def search(root: Node | None, key: int) -> bool:
    dummy = root
    while dummy:
        if key < dummy.key:
            dummy = dummy.left
        elif key > dummy.key:
            dummy = dummy.right
        else:
            return True
    return False


def print_tree(root: Node, level: int=0) -> None:
    if root is None:
        return
    
    print_tree(root.left, level + 1)
    print("." * level + str(root.key))
    print_tree(root.right, level + 1)


def main() -> None:
    root = None

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        if line.startswith("ADD"):
            _, x = line.split()
            root = insert(root, int(x))

        elif line.startswith("DELETE"):
            _, x = line.split()
            root, deleted = delete(root, int(x))
            print("DONE" if deleted else "CANNOT")

        elif line.startswith("SEARCH"):
            _, x = line.split()
            print("YES" if search(root, int(x)) else "NO")

        elif line.startswith("PRINTTREE"):
            print_tree(root)


main()
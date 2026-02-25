class Node:
    def __init__(self, key: int) -> None:
        self.key = key
        self.left = None
        self.right = None
        self.dubs = 1


def insert(root: Node, key: int) -> Node:
    if root is None:
        return Node(key)
    dummy = root
    while True:
        if key < dummy.key:
            if dummy.left is None:
                dummy.left = Node(key)
                break
            dummy = dummy.left
        elif key > dummy.key:
            if dummy.right is None:
                dummy.right = Node(key)
                break
            dummy = dummy.right
        else:
            dummy.dubs += 1
            break
    return root


def inorder(root: Node) -> None:
    if root.left is not None:
        inorder(root.left)
    print(root.key, root.dubs)
    if root.right is not None:
        inorder(root.right)

def main() -> None:
    array = map(int, input().split())
    root = None
    for key in array:
        if key:
            root = insert(root, key)
    inorder(root)

if __name__ == "__main__":
    main()
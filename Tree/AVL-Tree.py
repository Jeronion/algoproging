class Node:
    __slots__ = ["key", "left", "right", "height"]
    
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def height(node: Node | None) -> int:
    if not node:
        return 0
    return node.height


def right_rotate(y: Node) -> Node:
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x


def left_rotate(x: Node) -> Node:
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y


def get_balance(node: Node | None) -> int:
    if not node:
        return 0
    return height(node.left) - height(node.right)


def insert(node: Node | None, key: int) -> Node:
    if not node:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    else:
        return node

    node.height = 1 + max(height(node.left), height(node.right))
    balance = get_balance(node)

    # Left Left Case
    if balance > 1 and node.left.key > key:
        return right_rotate(node)

    # Right Right Case
    if balance < -1 and node.right.key < key:
        return left_rotate(node)

    # Left Right Case
    if balance > 1 and node.left.key < key:
        node.left = left_rotate(node.left)
        return right_rotate(node)

    # Right Left Case
    if balance < -1 and node.right.key > key:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node


def minValueNode(node):
    current = node
    
    while current.left is not None:
        current = current.left
        
    return current


def delete(node: Node | None, key: int) -> Node | None:
    if not node:
        return None

    if key < node.key:
        node.left = delete(node.left, key)

    elif key > node.key:
        node.right = delete(node.right, key)

    else:
        if node.left is None:
            return node.right

        if node.right is None:
            return node.left

        temp = minValueNode(node.right)
        node.key = temp.key
        node.right = delete(node.right, temp.key)

    if node is None:
        return None

    node.height = 1 + max(height(node.left), height(node.right))
    balance = get_balance(node)

    # Left Left
    if balance > 1 and get_balance(node.left) >= 0:
        return right_rotate(node)

    # Left Right
    if balance > 1 and get_balance(node.left) < 0:
        node.left = left_rotate(node.left)
        return right_rotate(node)

    # Right Right
    if balance < -1 and get_balance(node.right) <= 0:
        return left_rotate(node)

    # Right Left
    if balance < -1 and get_balance(node.right) > 0:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node
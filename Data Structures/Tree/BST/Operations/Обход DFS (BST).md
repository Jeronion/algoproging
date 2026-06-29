
## Определение

**DFS (Depth-First Search)** — обход дерева вглубь.

---

## Типы обхода DFS

### Inorder (центрированный)
Посещаем левое поддерево, затем узел, затем правое. Для BST даёт отсортированный порядок.

```python
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)
```

### Preorder (прямой)
Узел, затем левое, затем правое.

```python
def preorder(root):
    if root:
        print(root.key, end=' ')
        preorder(root.left)
        preorder(root.right)
```

### Postorder (концевой)
Левое, правое, затем узел.

```python
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=' ')
```


---

## Типы обхода DFS (итеративные)

### Inorder (центрированный)
Посещаем левое поддерево, затем узел, затем правое. Для BST даёт отсортированный порядок.

```python
def inorder(root):
    st = []
    cur = root
    while st or cur:
        while cur:
            st.append(cur)
            cur = cur.left
        cur = st.pop()
        print(cur.data, end=" ")
        cur = cur.right
```

### Preorder (прямой)
Узел, затем левое, затем правое.

```python
def preOrder(self, root):
    st = []
    cur = root
    while st or cur:
        while cur:
            print(cur.data, end=" ")
            if cur.right:
                st.append(cur.right)
            cur = cur.left
        
        if st:
            cur = st.pop()
```

### Postorder (концевой)
Левое, правое, затем узел.

```python
def postOrder(root):
    res = []
    st = []
    while True:
        while root:
            st.append(root)
            st.append(root)
            root = root.left
        if not st:
            return res
        root = st.pop()
        if st and st[-1] == root:
            root = root.right
        else:
            res.append(root.data)
            root = None
```

### Morris Inorder (центрированный)

```python
def inorder(root):
    res = []
    curr = root

    while curr is not None:
        if curr.left is None:

            # If no left child, visit this node 
            # and go right
            res.append(curr.data)
            curr = curr.right
        else:

            # Find the inorder predecessor of curr
            prev = curr.left
            while prev.right is not None \
            and prev.right != curr:
                prev = prev.right

            # Make curr the right child of its 
            # inorder predecessor
            if prev.right is None:
                prev.right = curr
                curr = curr.left
            else:

                # Revert the changes made in the 
                # tree structure
                prev.right = None
                res.append(curr.data)
                curr = curr.right

    return res
```

### Morris Preorder (прямой)

```python
def preorder(node):
    result = []
    while node:
        if node.left is None:
            result.append(node.data)
            node = node.right
        else:
            current = node.left
            while current.right and current.right != node:
                current = current.right

            if current.right == node:
                current.right = None
                node = node.right
            else:
                result.append(node.data)
                current.right = node
                node = node.left
    return result
```
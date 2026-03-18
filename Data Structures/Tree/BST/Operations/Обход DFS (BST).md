
tags: #tree #bst #ds #binary_tree

---

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

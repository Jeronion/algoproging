
tags: #tree #bst #ds #binary_tree

---

Минимум в BST — самый левый узел.

```python
def find_min(root):
    if root is None:
        return None
    while root.left:
        root = root.left
    return root.key
```

---

### Сложность
- **Время:** O(h).
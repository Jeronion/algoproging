
Максимум в BST — самый правый.

```python
def find_max(root):
    if root is None:
        return None
    while root.right:
        root = root.right
    return root.key
```

---

### Сложность
- **Время:** O(h).
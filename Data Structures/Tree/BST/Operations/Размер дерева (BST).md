
Размер дерева - количество узлов в дереве.

```python
def getSize(self, root):
    def size(root):
        if root is None:
            return 0
        return size(root.left) + size(root.right) + 1
    return size(root)
```

---

### Сложность
- **Время:** O(n).
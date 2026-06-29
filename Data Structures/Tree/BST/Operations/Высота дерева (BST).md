
Высота дерева - количество рёбер в дереве от корня до самого глубокого узла.

```python
def height(self, root):
    def depth(root):
        if root is None:
            return -1
        return max(depth(root.left), depth(root.right)) + 1
    return depth(root)
```

---

### Сложность
- **Время:** O(n).
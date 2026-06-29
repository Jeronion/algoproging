
Ширина дерева - максимальное количество узлов на любом уровне.

```python
def maxWidth(self, root):
    widths = []
    def dfs(root, dist):
        if root is None:
            return
        
        if len(widths) == dist:
            widths.append(1)
        else:
            widths[dist] += 1
        
        dfs(root.left, dist + 1)
        dfs(root.right, dist + 1)
    
    dfs(root, 0)
    return max(widths)
```

---

### Сложность
- **Время:** O(n).
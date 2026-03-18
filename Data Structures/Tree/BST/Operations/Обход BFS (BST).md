
tags: #tree #bst #ds #binary_tree

---

## Определение

**BFS (Breadth-First Search)** — обход дерева по уровням (level-order traversal): узлы посещаются уровень за уровнем, слева направо. Для реализации используется **очередь**.

---

## Алгоритм

1. Если корень пуст — завершить.
2. Поместить корень в очередь.
3. Пока очередь не пуста:
    
    - Извлечь узел из начала очереди.
    - Обработать его данные (вывести, сохранить и т.д.).
    - Добавить левого ребенка в конец очереди (если существует).
    - Добавить правого ребенка в конец очереди (если существует).

---

```python
from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def bfs(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.key, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```
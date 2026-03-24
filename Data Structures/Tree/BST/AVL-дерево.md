
## Определение

**AVL-дерево** — это самобалансирующееся бинарное дерево поиска (BST), в котором для каждого узла выполняется условие: модуль разности высот левого и правого поддеревьев (фактор баланса) не превышает 1. Названо по фамилиям создателей — **Г. М. Адельсон-Вельский** и **Е. М. Ландис** (1962).

Балансировка гарантирует, что высота дерева всегда остаётся **O(log n)**, что обеспечивает логарифмическую сложность основных операций.

---

## Фактор баланса

**Фактор баланса** узла вычисляется как:

```
balance_factor = height(left_subtree) - height(right_subtree)
```

Для AVL-дерева допустимые значения: **-1, 0, 1**. Если после вставки или удаления фактор выходит за эти пределы, выполняются **повороты** для восстановления баланса.

Высота пустого поддерева обычно считается -1 или 0 (в разных реализациях). В классическом определении высота листа равна 0, тогда фактор баланса листа — 0.

---

## Основные операции

От обычного BST отличаются только:

### 1. Вставка (Insert)

1. Выполняется стандартная вставка BST (новый узел добавляется как лист).
2. После вставки обновляются высоты узлов на пути к корню.
3. Проверяется фактор баланса каждого узла. Если он стал ±2, выполняется соответствующий поворот (один из четырёх типов).
4. Повороты могут выполняться несколько раз, но в целом вставка требует не более двух поворотов.

### 2. Удаление (Delete)

1. Выполняется стандартное удаление из BST (три случая).
2. После удаления обновляются высоты на пути к корню и проверяется баланс.
3. При нарушении баланса выполняются повороты. Удаление может потребовать нескольких поворотов (вплоть до O(log n)), но амортизированная сложность остаётся O(log n).

---

## Типы поворотов

Для восстановления баланса используются четыре типа поворотов:

### LL (Left-Left) — правый поворот

Возникает, когда узел вставлен в **левое поддерево левого ребёнка**. Фактор баланса корня становится +2.

```
    z
   /
  y
 /
x
```

**Решение:** правый поворот вокруг z.

```
    y
   / \
  x   z
```

### RR (Right-Right) — левый поворот

Возникает при вставке в **правое поддерево правого ребёнка**. Фактор баланса корня становится -2.

```
z
 \
  y
   \
    x
```

**Решение:** левый поворот вокруг z.

```
    y
   / \
  z   x
```

### LR (Left-Right) — левый поворот вокруг левого ребёнка, затем правый поворот

Возникает при вставке в **правое поддерево левого ребёнка**.

```
    z
   /
  y
   \
    x
```

**Решение:** сначала левый поворот вокруг y, затем правый поворот вокруг z.

```
    x
   / \
  y   z
```

### RL (Right-Left) — правый поворот вокруг правого ребёнка, затем левый поворот

Возникает при вставке в **левое поддерево правого ребёнка**.

```
  z
   \
    y
   /
  x
```

**Решение:** сначала правый поворот вокруг y, затем левый поворот вокруг z.

```
    x
   / \
  z   y
```

Каждый поворот выполняется за **O(1)** и сохраняет свойство BST.

---

## Сложность операций

| Операция | Средний случай | Худший случай |
|----------|----------------|---------------|
| Поиск    | O(log n)       | O(log n)      |
| Вставка  | O(log n)       | O(log n)      |
| Удаление | O(log n)       | O(log n)      |

Высота AVL-дерева строго ограничена ≈ 1.44 log₂(n), что гарантирует логарифмическую сложность даже в худшем случае.

---

## Пример реализации

```python
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # высота поддерева с этим узлом

def height(node):
    return node.height if node else 0

def update_height(node):
    node.height = 1 + max(height(node.left), height(node.right))

def balance_factor(node):
    return height(node.left) - height(node.right) if node else 0

def rotate_right(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    update_height(y)
    update_height(x)
    return x

def rotate_left(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    update_height(x)
    update_height(y)
    return y

def balance(node):
    bf = balance_factor(node)
    # LL
    if bf > 1 and balance_factor(node.left) >= 0:
        return rotate_right(node)
    # LR
    if bf > 1 and balance_factor(node.left) < 0:
        node.left = rotate_left(node.left)
        return rotate_right(node)
    # RR
    if bf < -1 and balance_factor(node.right) <= 0:
        return rotate_left(node)
    # RL
    if bf < -1 and balance_factor(node.right) > 0:
        node.right = rotate_right(node.right)
        return rotate_left(node)

    return node

def insert(node, key):
    if not node:
        return AVLNode(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    else:
        return node  # дубликаты не допускаются

    update_height(node)
    return balance(node, key)

def delete(node, key):
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
		min_node = node.right
		while min_node.left:
			min_node = min_node.left
			node.key = min_node.key
			node.right = delete(node.right, min_node.key)
	
	update_height(node)
	return balance(node)
```

---
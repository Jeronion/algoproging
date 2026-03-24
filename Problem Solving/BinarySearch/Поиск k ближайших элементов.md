
tags: #binary_search #sliding_window

---

## Определение

Дан отсортированный массив, найти `k` ближайших к `x` элементов. Результат должен быть отсортирован.

---

## Реализация (LeetCode 658)

```python
def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    left, right = 0, len(arr) - k
    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    return arr[left:left + k]
```

---

## Сложность

- Время: O(log n + k)
- Память: O(1) (кроме вывода)

---
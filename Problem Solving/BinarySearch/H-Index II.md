
tags: #binary_search

---

## Определение

Дан массив цитирований, отсортированный по возрастанию. Найти h-индекс — максимальное число `h` такое, что как минимум `h` статей имеют `h` и более цитирований.

---

## Реализация (LeetCode 275)

```python
def hIndex(citations: List[int]) -> int:
    n = len(citations)
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if citations[mid] >= n - mid:
            right = mid - 1
        else:
            left = mid + 1
    return n - left
```

---

## Сложность

- Время: O(log n)
- Память: O(1)

---
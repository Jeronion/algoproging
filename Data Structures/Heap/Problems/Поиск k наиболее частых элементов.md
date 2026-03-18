
tags: #array #hash-table #heap #bucket-sort #leetcode

---

## Условие

Задача известна как [LeetCode 347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/).

Дан целочисленный массив `nums` и целое число `k`. Требуется вернуть массив из **k наиболее часто встречающихся элементов**. Ответ может быть возвращён в любом порядке.

**Пример:**
```
nums = [1,1,1,2,2,3], k = 2
Вывод: [1,2] (элементы 1 и 2 встречаются чаще всего)
```

---

## Идея решения

Очевидный подход: сначала подсчитать частоту каждого элемента, а затем выбрать `k` элементов с наибольшими частотами. Подсчёт частот выполняется за O(n) с помощью хеш-таблицы. Для выбора топ-k есть несколько способов:

1. **Сортировка по убыванию частот** — O(n log n).
2. **Куча (min-heap) размером k** — O(n log k).
3. **Bucket sort** — использует тот факт, что максимальная частота не превышает n, и раскладывает элементы по корзинам (buckets) индексированным частотой. Это даёт O(n) времени и O(n) памяти.
4. **Quickselect** — средний O(n), но в худшем случае O(n²).

---

## Реализация

```python
def topKFrequent(nums: List[int], k: int) -> List[int]:
    if k == len(nums):
        return nums
    freq = Counter(nums)
    return nlargest(k, freq.keys(), key=freq.get)
```

В приведённом коде используется простейший вариант с `nlargest` из модуля `heapq`, который неявно использует кучу размера k (но внутри может работать чуть сложнее, но в целом это O(n log k)).

---

## Альтернативный подход: bucket sort

Bucket sort использует массив списков, где индекс соответствует частоте. Элементы с одинаковой частотой попадают в одну корзину.

```python
def topKFrequent(nums, k):
    freq = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, cnt in freq.items():
        buckets[cnt].append(num)
    result = []
    for i in range(len(buckets)-1, -1, -1):
        result.extend(buckets[i])
        if len(result) >= k:
            return result[:k]
    return result
```

Этот подход работает за O(n) времени и O(n) памяти.

---

## Сложность

- **Время:** 
  - С использованием `nlargest` (или min-heap размера k): O(n log k).
  - С использованием bucket sort: O(n) (линейное).
  - Сортировка: O(n log n).
- **Память:** O(n) для хранения частот и дополнительных структур (корзины или куча).

---
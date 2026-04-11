
tags: #array

---

## Определение

Дан массив целых чисел размера `n` и целое число `k`. Требуется найти все элементы, которые встречаются **более чем `n/k` раз**. Таких элементов может быть не более `k-1` (если бы их было `k`, каждый встречался бы > n/k, что в сумме дало бы > n — противоречие).

Задача обобщает классическую задачу поиска большинства (> n/2) на случай произвольного `k`.

---

## 1. Решение с хешированием (простое и универсальное)

Подсчитываем частоту каждого элемента в словаре, затем отбираем те, у которых частота > n/k.

```python
from collections import Counter

def count_occurence(arr, k):
    n = len(arr)
    threshold = n // k
    freq = Counter(arr)
    return sum(1 for cnt in freq.values() if cnt > threshold)

# Пример
arr = [3, 4, 2, 2, 1, 2, 3, 3]
k = 4
print(count_occurence(arr, k))  # 2 (элементы 2 и 3)
```

- **Время:** O(n)
- **Память:** O(n)

---

## 2. Обобщённый алгоритм Бойера-Мура (для малых k)

Идея: поддерживать `k-1` кандидатов и их счётчики. Проходим по массиву:
- Если текущий элемент совпадает с одним из кандидатов — увеличиваем его счётчик.
- Иначе если есть свободное место (счётчик = 0) — добавляем нового кандидата.
- Иначе уменьшаем счётчики **всех** кандидатов на 1.

После первого прохода получаем не более `k-1` потенциальных кандидатов. Во втором проходе проверяем их реальные частоты.

```python
class EleCount:
    def __init__(self):
        self.elem = None
        self.cnt = 0

def more_than_ndk(arr, k):
    n = len(arr)
    if k < 2:
        return []
    # массив кандидатов размера k-1
    candidates = [EleCount() for _ in range(k-1)]

    # Первый проход: поиск кандидатов
    for x in arr:
        # ищем среди существующих кандидатов
        found = False
        for cand in candidates:
            if cand.elem == x:
                cand.cnt += 1
                found = True
                break
        if found:
            continue
        # ищем свободное место
        for cand in candidates:
            if cand.cnt == 0:
                cand.elem = x
                cand.cnt = 1
                found = True
                break
        if found:
            continue
        # нет места — уменьшаем все счётчики
        for cand in candidates:
            cand.cnt -= 1

    # Второй проход: проверка реальных частот
    result = []
    for cand in candidates:
        if cand.cnt == 0:
            continue
        actual_cnt = sum(1 for v in arr if v == cand.elem)
        if actual_cnt > n // k:
            result.append(cand.elem)
    return result

# Пример
arr = [3, 4, 2, 2, 1, 2, 3, 3]
k = 4
print(more_than_ndk(arr, k))  # [2, 3]
```

- **Время:** O(n·k) — на каждом шаге проверяем до `k-1` кандидатов.
- **Память:** O(k)

Для малых `k` (например, k = 3, 4) этот метод эффективен и не требует хеш-таблицы.

---

## 3. Использование Counter (Pythonic way)

Для Python самое короткое решение — использовать `collections.Counter`:

```python
from collections import Counter

def elements_gt_ndk(arr, k):
    n = len(arr)
    freq = Counter(arr)
    return [elem for elem, cnt in freq.items() if cnt > n // k]
```

- **Время:** O(n)
- **Память:** O(n)

---

## Сравнение подходов

| Подход               | Время      | Память | Примечание                         |
|----------------------|------------|--------|------------------------------------|
| Хеширование          | O(n)       | O(n)   | Проще всего, универсален           |
| Обобщённый Бойер-Мур | O(n·k)     | O(k)   | Хорош для маленьких k, не требует доп. памяти |
| Counter (Python)     | O(n)       | O(n)   | Лаконично, но зависит от реализации |

---

## Применение

- Задача «Majority Element II» (LeetCode 229) — частный случай при k = 3.
- Анализ логов, поиск доминирующих элементов в потоковых данных.
- Обобщение для произвольного порога `n/k`.

---
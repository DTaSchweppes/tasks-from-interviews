'''
Задачи просят выполнять в блокноте, на скорость, без внимания к оптимизации. Никак не связаны с задачами,
которыми занимается отдел.

1.Массив чисел является монотонным, если все его
элементы не убывают, или, наоборот, не возрастают.
Нужно проверить, является ли массив монотонным

Нет уточнений по входным данным как в источнике откуда взята задача, примеров по типу ниже ТОЖЕ НЕТ:

"Массив является монотонным, если он либо монотонно увеличивается, либо монотонен decreasing.
An массив A монотонно увеличивается, если для всех i <= j, A[i] <= A[j]. Массив A монотонно уменьшается, если для всех i <= j, A[i] >= A[j]>.
Возвращает “True”, если данный массив A монотонен, иначе возвращает “False” (без кавычек)."

РЕШЕНИЕ:
'''
def is_monotonic(array):
    increasing = decreasing = True

    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            increasing = False
        if array[i] < array[i + 1]:
            decreasing = False

    return increasing or decreasing

array2 = [5, 4, 3, 2, 1] # проверка
print(is_monotonic(array2)) # принт

'''
2. Дан массив целых чисел, вернуть True, если количество вхождений 
каждого числа в массиве уникально        
'''


def is_unique_counts(nums):
    counts = {}

    # Подсчет количества вхождений каждого числа
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # Проверка на уникальность количества вхождений
    occurrences = set(counts.values())
    return len(occurrences) == len(counts)

array = [1, 2, 2, 3, 3, 3]
print(is_unique_counts(array))

'''
3.Дана строка 's'. Необходимо сказать, можно ли переставить буквы в строке так, чтобы получился палиндром.
'''
def can_permute_palindrome(s):
    char_count = {}
    odd_count = 0

    # Подсчет количества символов в строке
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Проверка на количество символов с нечетным количеством
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
            if odd_count > 1:
                return False

    return True

# Пример использования
string = 'sdds'
print(can_permute_palindrome(string))  # Вывод: True

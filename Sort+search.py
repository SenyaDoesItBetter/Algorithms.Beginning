seq = [int(x) for x in input("Введите числа от 1 до 99 в любом порядке, через пробел: ").split()]


def merge_sort(seq):
    if len(seq) < 2:
        return seq[:]
    else:
        middle = len(seq) // 2
        left = merge_sort(seq[:middle])
        right = merge_sort(seq[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


print(merge_sort(seq))


def binary_search(a: int, array: list) -> int:
    left, right = 0, len(array)
    while left < right:
        middle = (left + right) // 2
        if array[middle] < a:
            left = middle + 1
        else:
            right = middle
    return left


while True:
    try:
        num = int(input("Введите число от 1 до 99 для поиска позиции: "))
        if num < 1 or num > 99:
            raise Exception
        break
    except ValueError:
        print("Нужно ввести число!")
    except Exception:
        print("Неправильный диапазон!")

print('Позиция первого числа, меньше введенного')
print(binary_search(num, merge_sort(seq)) - 1)
print("Позиция введенного числа в списке")
print(binary_search(num, merge_sort(seq)))
print("Позиция первого числа, больше введенного")
print(binary_search(num, merge_sort(seq)) + 1)

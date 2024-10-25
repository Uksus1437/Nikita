def to_ternary(n):
    """Преобразует число n в троичную систему счисления."""
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.append(str(n % 3))
        n //= 3
    return ''.join(digits[::-1])

def replace_digits(ternary):
    """Заменяет цифры в троичной записи по заданному правилу."""
    return ''.join('2' if digit == '1' else '0' if digit == '2' else '1' for digit in ternary)

def remove_leading_zeros(s):
    """Удаляет незнаечащие нули из строки."""
    return s.lstrip('0')

def reverse_string(s):
    """Переворачивает строку."""
    return s[::-1]

def sum_of_digits(ternary):
    """Суммирует цифры в троичной записи."""
    return sum(int(digit) for digit in ternary)

def find_min_r():
    min_r = float('inf')
    for n in range(1, 100):  # Пробуем числа от 1 до 99 (включительно)
        ternary = to_ternary(n)
        replaced = replace_digits(ternary)
        no_leading_zeros = remove_leading_zeros(replaced)
        reversed_ternary = reverse_string(no_leading_zeros)

        digit_sum = sum_of_digits(ternary)
        sum_ternary = to_ternary(digit_sum)

        final_number = reversed_ternary + sum_ternary
        r = int(final_number, 3)  # Преобразуем обратно в десятичную систему

        if r < min_r:
            min_r = r

    return min_r

# Получаем минимальное значение R
min_R = find_min_r()
print(min_R)

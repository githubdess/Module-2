first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')
print(first, second, third)
if first == second == third:
    print('Все числа равны')
elif first == second or second == third or first == third:
    print('Два числа равны')
elif first != second != third:
    print('Одинаковых чисел нет')

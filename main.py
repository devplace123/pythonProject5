a = int(input('Введите первое число - '))
sign = input('Введите арифметический знак ')
b = int(input('Введите второе число - '))

if sign == '+':
    print(a+b)
elif sign == '-':
    print(a-b)
elif sign == '*':
    print(a*b)
elif sign == '/':
    print(a/b)
else:
    print('Неизвестный арифметический знак')


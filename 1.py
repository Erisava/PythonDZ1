'''Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет'''

a = int (input('Введите число дня недели от 1 до 7: '' '))
print(a)
if a < 1 or a > 7:
    print ('Неверные данные')
elif a > 5:
    print ('День является выходным')
else:
    print ('Рабочий день')
    
"""
Написать программу, которая будет конвертировать значение температуры из градусов
Цельсия в Фаренгейты и наоборот
Входные данные: 60C, 45F, ....
Результат: 140F, 7C.....
Расчётные формулы:
с = (F-32) * 5/9
F = C * 9/5 + 32
"""

t='45F'
suffix=t[-1]
val=int(t[:-1])

if suffix in ['C', 'c']:
    conv_val = val*9/5 + 32
    res=str(conv_val) + "F"
elif suffix in ['F', 'f']:
    conv_val = (val-32)*5/9
    res=str(conv_val) + "C"
else:
    res = "wrong value"

print(t, ' is ', res)



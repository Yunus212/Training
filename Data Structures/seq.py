shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
name = 'swaroop'

# Операция индексирования
print('element 0 -', shoplist[0])
print('element 1 -', shoplist[1])
print('element 2 -', shoplist[2])
print('element 3 -', shoplist[3])
print('element -1 -', shoplist[-1])
print('element -2 -', shoplist[-2])
print('Symbol 0 -', name[0])

# Вырезка из списка
print('Элементы с 1 по 3:', shoplist[1:3])
print('Элементы с 2 док конца:', shoplist[2:])
print('Элементы с 1 по -1:', shoplist[1:-1])
print('Элементы от начала до конца:', shoplist[:])

# Вырезка из строки
print('Символы с 1 по 3:', name[1:3])
print('Символы с 2 до конца:', name[2:])
print('Символы с 2 до -1:', name[1:-1])
print('Символы от начала до конца:', name[:])
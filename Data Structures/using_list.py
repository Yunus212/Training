# Это мой список покупок
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']

print('Я должен сделать', len(shoplist), 'покупки.')

print('Покупки:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nТакже нужно купить риса.')
shoplist.append('рис')
print('Теперь мой список покупок таков:', shoplist)

print('Отсортирую-ка я свой список')
shoplist.sort()
print('Отсортированный списокпокупок выглядит так:', shoplist)

print('Первое что мне нужно купить, это', shoplist[0])
olditem = shoplist[0]
del shoplist[1]
print('Я купил, olditem')
print('Теперь мой список покупок:', shoplist)
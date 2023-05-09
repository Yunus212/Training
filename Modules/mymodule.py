def sayhi():
    print('Привет! Это говорит мой модуль.')

__version__ = '0.1'

# Конец модуля mymodule.py

# Ещё один модуль (сохраните как mymodule_demo.py):
import mymodule

mymodule.sayhi()
print ('Версия', mymodule.__version__)

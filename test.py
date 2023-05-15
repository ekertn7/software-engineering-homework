'''This module show how to work with decorators.'''
import time
import signal


def time_break(func):
    def wrapper(*args, **kwargs):
        try:
            print ("Запускаем тестируемую функцию") 
            signal.alarm(5)
            res = func(*args, **kwargs)
            signal.alarm(0)
            print ("Нормальное завершение")
            return res
        except Exception as e:
            print(e)
            return None

    return wrapper


@time_break
def do_work():
    j = 0;
    while True:
        time.sleep(1)
        j = j + 1
        print(j) 

# Тестируем
while True:
    do_work()


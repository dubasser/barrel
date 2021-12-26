import random
import logging


logging.basicConfig(filename="log.log", level=logging.ERROR)
log = logging.getLogger("SEED")
while True:
    try:
        n = int(input('Введите натуральное число N (кол-во боченков): '))
        if n <= 0:
            print('Неверный формат. Попробуйте заново')
            log.exception("Value Error! Число меньше или равно 0")
            continue
        break
    except ValueError:
        print('Неверный формат. Попробуйте заново')
        log.exception("Value Error! Неверный Формат")

array=[]
sequence=[]
for number in range(1,n+1):
    array.append(number)
while True:
    temp=input('Чтобы вытащить боченок нажмите Enter')
    if temp!='' :
        break
    random_index=random.randint(0, n-1)
    sequence.append(array[random_index])
    print('Боченок номер ' + str(array[random_index]))
    print('Текущая последовательность: ')
    print(sequence)
    array.pop(random_index)
    n-=1
    if n==0:
        print('Боченки закончились')
        break
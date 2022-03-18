while True:
    a = input(('Введите предложение: '))
    b = len(a.split(' '))
    if b < 6:
        print('Введите ещё раз, предложение не меньше 6 слов')
        continue
    else:
        print('Верно')
        breaky	

x = int(input('Введите число: '))
for i in range(1, x+1):
    elem = i
    while elem>1:
        if elem % 3 == 0: elem /= 3
        elif elem % 5 == 0: elem /= 5
        elif elem %7 == 0: elem /= 7
        else: break
    if elem == 1:
        print(i)
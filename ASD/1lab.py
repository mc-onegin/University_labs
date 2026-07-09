s = str(input('Введите строку, состоящую из скобок '))
mas = [] #стек
scobs = {')':'(', '}':'{', ']':'['}
open=0
close=0
for i in s:
    if i in '({[':
        mas.append(i)
        open+=1
    elif i in ')}]':
        if len(mas) > 0 and scobs[i] == mas[-1]:
            mas.pop()
            close+=1
        else:
            print('Строка неверна')
            exit()
if open == close:
    print('Строка верная')
else:
    print('Строка неверна')
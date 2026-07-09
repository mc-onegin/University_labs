import operator

def Scobs(s):
    mas_scobs = []
    scobs = {')':'(', '}':'{', ']':'['}
    open=0
    close=0
    for i in s:
        if i in '({[':
            mas_scobs.append(i)
            open+=1
        elif i in ')}]':
            if len(mas_scobs) > 0 and scobs[i] == mas_scobs[-1]:
                mas_scobs.pop()
                close+=1
            else:
                print('Выражение записано не корректно')
                return False
    if open == close:
        return True
    else:
        print('Выражение записано не корректно')
        return False


def Count(s_fin):
    mas_c=[]
    for i in s_fin:
        if i in numbers:
            mas_c.append(i)
        elif i in symbols:
            if len(mas_c)<2:
                 return print('Выражение записано не корректно')
            if i=='/' and mas_c[-1]=='0':
                return print('Выражение записано не корректно')
            mas_c.append(op[i](int(mas_c[-2]), int(mas_c[-1])))
            mas_c.pop(-2)
            mas_c.pop(-2)
    return print(mas_c[0])


s=str(input('Введите выражение '))
mas_main=[]
s_fin=''

symbols='+-/*'
pri={'+':1, '-':1, '*':2, '/':2}
op={'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

numbers='0123456789'

if Scobs(s):
    if s.count('=')>=2:
            print('Выражение записано не корректно')
            exit()
    for i in s:
        if i in numbers:
            s_fin+=i
        elif i=='(':
            mas_main.append(i)
        elif i==')':
            while mas_main and mas_main[-1]!='(':
                s_fin+=mas_main.pop()
        elif i in symbols:
            while mas_main and mas_main[-1]!='(' and pri[i]<=pri[mas_main[-1]]:
                s_fin+=mas_main.pop()
            mas_main.append(i)
        if i=='=' and i!=s[-1]:
            print('Выражение записано не корректно')
            exit()
        elif i=='=' and i==s[-1]:
            while mas_main:
                s_fin+=mas_main.pop()
print(s_fin)
Count(s_fin)
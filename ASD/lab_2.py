def correct_brackets(s):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    flag = True
    for i in s:
        if i in '{([':
            stack.append(i)
        elif i in '})]':
            if not stack or stack[-1] != bracket_pairs[i]:
                flag = False
            stack.pop()
    if not stack and flag:
        return True
    else:
        return print('Строка введена некорректно')
    
def calc(s_post):
    stack_ = []
    for elem_ in s_post:
        if elem_ in digits:
            stack_.append(elem_)
        elif len(stack_) < 2:
            return print('Ошибка: выражение некорректно')
        elif elem_ in operators:
            if elem_ == '/' and int(stack_[-1]) == 0:
                return print('Ошибка: деление на 0')
            stack_.append(operators[elem_](int(stack_[-2]), int(stack_[-1])))
            stack_.pop(-2)
            stack_.pop(-2)       
    return print(stack_[0])


import operator
digits = '0123456789'
operators = {'+': operator.add, '-': operator.sub,
             '*': operator.mul, '/': operator.truediv}
priority = {'+': 1, '-': 1, '*': 2, '/': 2}

s = input('Введите выражение: ')
s_post = ''
stack = []
for elem in s:
    if elem in digits:
        s_post += elem
    elif elem == '(':
        stack.append(elem)
    elif elem == ')':
        while stack[-1] != '(':
            s_post += stack.pop()
        if stack[-1] == '(':
            stack.pop()
    elif elem in operators:
        while (stack and stack[-1] != '(' and priority[elem] <= priority[stack[-1]]):
            s_post += stack.pop()
        stack.append(elem)
while stack:
    s_post += stack.pop()
print(s_post)


if correct_brackets(s):
    calc(s_post)





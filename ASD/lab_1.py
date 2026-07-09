s = input('Введите строку: ')
stack = []
bracket_pairs = {')': '(', '}': '{', ']': '['}
for i in s:
    if i in '{([':
        stack.append(i)
    elif i in '})]':
        if not stack or stack[-1] != bracket_pairs[i]:
            print('Неверная строка')
            exit()
        stack.pop()
if not stack:
    print('Строка введена корректно')
else:
    print("Неверная строка")
    
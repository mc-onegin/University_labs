s=input('Введите бинарное дерево поиска: ')

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
    
def build(s):
    main_end=s.find('(')
    if main_end==-1:
        return TreeNode(int(s))
    main_val = int(s[:main_end])
    main=TreeNode(main_val)
    s_remain=s[main_end:]
    mas=[]
    comma=-1
    for i, j in enumerate(s_remain):
        if j=='(':
            mas.append('(')
        elif j==')':
            mas.pop()
        elif j==',' and len(mas)==1:
            comma=i
            break
    if comma!=-1:
        left_part = s_remain[1:comma]
        right_part=s_remain[comma+1:-1]
        main.left=build(left_part)
        main.right=build(right_part)
    else:
        if s_remain[-1]==")":
            left_part=s_remain[1:-1]
            main.left=build(left_part)
    return main

def search(root, val):
    if root is None:
        return None
    
    if root.val == val:
        return root
    elif val < root.val:
        return search(root.left, val)
    else:
        return search(root.right, val)
    
def insert(root, val):
    if root is None:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root

def find_min(node):
    curr = node
    while curr.left is not None:
        curr = curr.left
    return curr

def delete(root, val):
    if root is None:
        return None
    
    if val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            min_node = find_min(root.right)
            root.val = min_node.val
            root.right = delete(root.right, min_node.val) 
    return root

def to_linear_bracket(root):
    if root is None:
        return ""

    result = str(root.val)
    if root.left is not None or root.right is not None:
        result += "("
        if root.left is not None:
            result += to_linear_bracket(root.left)
        if root.right is not None:
            if root.left is not None:
                result += ","
            result += to_linear_bracket(root.right)
        result += ")"
    
    return result

tree = build(s)
while True:
    print("1. Добавить вершину")
    print("2. Удалить вершину")
    print("3. Найти вершину")
    print("4. Показать дерево")
    print("5. Выход")

    option = input('Введите операцию: ')

    match option:
        case '1':
            val = int(input("Введите значение для добавления: "))
            root = insert(tree, val)
        case '2':
            val = int(input("Введите значение для удаления: "))
            root = delete(tree, val)
        case '3':
            val = int(input("Введите значение для поиска: "))
            if search(tree, val):
                print(f"Вершина {val} найдена")
            else:
                print(f"Вершина {val} не найдена")
        case '4':
            print(to_linear_bracket(tree))
        case '5':
            break



s=input('Введите бинарное дерево: ')

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

def Non_recursive(main):
    if not main:
        return []
    result=[]
    mas=[main]
    while mas:
        node=mas.pop()
        result.append(node.val)
        if node.right:
            mas.append(node.right)
        if node.left:
            mas.append(node.left)
    return result

def build(s):
    main_end=s.find('(')
    if main_end==-1:
        return TreeNode(int(s))
    main_val = int(s[:main_end])
    main=TreeNode(main_val)
    s_remain=s[main_end:]
    mas=[]
    index=-1
    for i, j in enumerate(s_remain):
        if j=='(':
            mas.append('(')
        elif j==')':
            mas.pop()
        elif j==',' and len(mas)==1:
            index=i
            break
    if index!=-1:
        left_part = s_remain[1:index]
        right_part=s_remain[index+1:-1]
        main.left=build(left_part)
        main.right=build(right_part)
    else:
        if s_remain[-1]==")":
            left_part=s_remain[1:-1]
            main.left=build(left_part)
    return main

main=build(s)
print(f"Не рекурсивный прямой обход: {Non_recursive(main)}")
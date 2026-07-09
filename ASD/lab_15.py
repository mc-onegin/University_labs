s=input('Введите бинарное дерево ')

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

result_strainght=[]
def Straight(main):
    if main:
        result_strainght.append(main.val)
        Straight(main.left)
        Straight(main.right)
    return result_strainght

result_central=[]
def Central(main):
    if main:
        Central(main.left)
        result_central.append(main.val)
        Central(main.right)
    return result_central

result_post_order=[]
def Post_Order(main):
    if main:
        Post_Order(main.left)
        Post_Order(main.right)
        result_post_order.append(main.val)
    return result_post_order

def build(s):
    main_end=s.find('(')
    if main_end == -1:
        return TreeNode(int(s))
    main_val=int(s[:main_end])
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

main=build(s)
print(f"Прямой обход: {Straight(main)}")
print(f"Центральный обход: {Central(main)}")
print(f"Концевой обход: {Post_Order(main)}")
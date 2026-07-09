s=str(input('введите последовательность чисел '))
mas_or=[int(i) for i in s]
mas_fin=[]
mas_fin.append(mas_or[0])
for i in range(1, len(mas_or)):
    T=False
    for i_s in range(len(mas_fin)-1, -1, -1):
        if mas_or[i]>=mas_fin[i_s]:
            T=True
            mas_fin.insert(i_s+1, mas_or[i])
            break
    if T==False:
        mas_fin.insert(0, mas_or[i])
print(mas_fin)
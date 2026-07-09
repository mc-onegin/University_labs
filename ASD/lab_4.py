sp = [int(i) for i in input('Введите последовательность: ').split()]
lenght = len(sp)
while lenght > 1:
    lenght=int(round(lenght/1.247, 1))
    for i in range(0, len(sp)-lenght):
        if sp[i] > sp[i+lenght]:
            tpm = sp[i]
            sp[i] = sp[i+lenght]
            sp[i+lenght]=tpm
print(sp)
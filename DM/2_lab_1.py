I = "ЧЕРЕСПОЛОСИЦА"
letters = list(I)

words_set = []
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                word = a + b + c + d
                flag = True
                for ch in word:
                    if word.count(ch) > I.count(ch):
                        flag = False
                        break
                if flag and word not in words_set:
                    words_set.append(word)
                    print(word)


print(len(words_set))
def search_pattern(text, pattern):
    if not pattern:
        return []
    
    m = len(pattern)
    alphabet = set(pattern)
    table = [{} for i in range(m + 1)]
    
    for state in range(m + 1):
        for char in alphabet:
            if state < m and char == pattern[state]:
                table[state][char] = state + 1
            else:
                for new_state in range(state, 0, -1):
                    if pattern[new_state - 1] != char:
                        continue
                    
                    flag = True
                    for i in range(1, new_state):
                        if pattern[new_state - 1 - i] != pattern[state - i]:
                            flag = False
                            break
                    
                    if flag:
                        table[state][char] = new_state
                        break
                else:
                    table[state][char] = 0
    
    positions = []
    state = 0
    
    for i, char in enumerate(text):
        if char in table[state]:
            state = table[state][char]
        else:
            state = 0
        if state == m:
            positions.append(i - m + 1)
    
    return positions


text = "ABABABCBABABCABABABC"
pattern = "ABAB"

result = search_pattern(text, pattern)
print(f"Образец: '{pattern}'")
print(f"Текст: '{text}'")
print(f"Найдено на позициях: {result}")

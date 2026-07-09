def bm_search(text, pattern):
    if not pattern:
        return []
    
    n = len(text)
    m =  len(pattern)
    
    table = {}
    for i, ch in enumerate(pattern):
        table[ch] = i
    
    result = []
    i = 0
    
    while i <= n - m:
        j = m - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        
        if j < 0:
            result.append(i)
            i += 1
        else:
            ch = text[i + j]
            i += max(1, j - table.get(ch, -1))
    
    return result

text = "ABABABCBABABCABABABC"
pattern = "ABAB"

result = bm_search(text, pattern)
print(f"Образец: '{pattern}'")
print(f"Текст: '{text}'")
print(f"Найдено на позициях: {result}")
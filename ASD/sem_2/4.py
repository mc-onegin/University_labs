def count_prefix(p):
    prefix = [0] * len(p)
    
    for i in range(1, len(p)):
        j = prefix[i-1]
        
        while j > 0 and p[i] != p[j]:
            j = prefix[j-1]
        if p[i] == p[j]:
            j += 1
        
        prefix[i] = j
    
    return prefix

def kmp_search(text, pattern):
    if not pattern:
        return []

    prefix = count_prefix(pattern)
    result = []
    j = 0
    
    for i, char in enumerate(text):
        while j > 0 and char != pattern[j]:
            j = prefix[j-1]
        if char == pattern[j]:
            j += 1
        if j == len(pattern):
            result.append(i - j + 1)
            j = prefix[j-1]
    
    return result

text = "ABABABCBABABCABABABC"
pattern = "ABABD"

result = kmp_search(text, pattern)
print(f"Образец: '{pattern}'")
print(f"Текст: '{text}'")
print(f"Найдено на позициях: {result}")
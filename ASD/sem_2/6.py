def rabin_karp_search(text, pattern):
    if not pattern or not text:
        return []
    
    m = len(pattern)
    n = len(text)
    p = 11
    mod = 10**9 + 7

    p_pow = p**(m-1)
    
    pattern_hash = 0
    window_hash = 0
    
    for i in range(m):
        pattern_hash = (pattern_hash * p + ord(pattern[i])) % mod
        window_hash = (window_hash * p + ord(text[i])) % mod
    
    positions = []
    
    for i in range(n - m + 1):
        if window_hash == pattern_hash:
            if text[i: i + m] == pattern:
                positions.append(i)
        
        if i < n - m:
            old_char = ord(text[i])
            new_char = ord(text[i + m])
            
            window_hash = (window_hash - old_char * p_pow) % mod
            window_hash = (window_hash * p + new_char) % mod
            
            if window_hash < 0:
                window_hash += mod
    
    return positions

text = "ABABABCBABABCABABABC"
pattern = "ABABD"

result = rabin_karp_search(text, pattern)
print(f"Образец: '{pattern}'")
print(f"Текст: '{text}'")
print(f"Найдено на позициях: {result}")
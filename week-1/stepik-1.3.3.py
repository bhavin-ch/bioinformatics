with open('Vibrio_cholerae.txt', 'r') as file:
    text = file.read().replace('\n', '')
pattern = 'CTTGATCAT'
pattern_length = len(pattern)

ans = [str(i) for i in range(len(text)) if text[i:i+pattern_length] == pattern]
print(' '.join(ans))

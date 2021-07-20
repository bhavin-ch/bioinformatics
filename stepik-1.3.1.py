text = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'
length = len(text)
skew_diffs = {
    'G': 1,
    'C': -1,
    'A': 0,
    'T': 0
}

ans = [None] * (length + 1)
ans[0] = 0
for i in range(1, length + 1):
    ans[i] = ans[i-1] + skew_diffs[text[i-1]]

print(' '.join(str(x) for x in ans))

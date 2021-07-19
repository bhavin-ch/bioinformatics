with open('E_coli.txt', 'r') as file:
    TEXT = file.read().replace('\n', '')
K=9
L=500
T=3

def get_close_occrs(occrs, k, l, t):
    if len(occrs) < t:
        return 0
    count = 0
    for i in range(len(occrs) - t + 1):
        if occrs[i + t-1] + k - occrs[i] + 1 <= l:
            count = count + 1
    return count

occr_dict = {}
for i in range(len(TEXT)):
    kmer = TEXT[i:i+K]
    if kmer in occr_dict:
        occr_dict[kmer].append(i)
    else:
        occr_dict[kmer] = [i]

print(len(occr_dict))

clumps = {kmer: get_close_occrs(occrs, K, L, T) for kmer, occrs in occr_dict.items()}
clumps = {kmer: count for kmer, count in clumps.items() if count > 0}
print(sum(clumps.values()))
print(len(clumps.keys()))
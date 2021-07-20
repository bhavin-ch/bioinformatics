# # from frequent_words_mismatch_complements.txt
TEXT = 'TTAAAATTAAAAGCTTAGCAAAGTTTGAAAAAAAAAAAATTATTAGTTTGGTTAAATTATGAAATTAGTTAAAGTTTTAAAAAAATGTGAAAAAAGCTTAGCGTTTTAGTTTGTGTTAGTTTTATTATGTTAGCTGAAAGCTGGCGCTTATGGCAAAAAAGCGCTGAAAGTTTGTTAGCAAAGCGCAAAAAAGCGTTAAAGTTTTAGTTGTTAAATGTG'
K = 5
D = 2

# # from dataset_9_10.txt
# TEXT = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
# K = 4
# D = 1

swap_map = {
    'A': 'TCG',
    'T': 'CGA',
    'C': 'GAT',
    'G': 'ATC'
}
comp_map = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

def remove_duplicates(somelist):
    return list(set(somelist))

def single_letter_neighborhood(pattern, i):
    return [pattern[:i] + x + pattern[i+1:] for x in swap_map[pattern[i]]]

def one_neighborhood(pattern):
    neighbors = []
    for i in range(len(pattern)):
        neighbors = [*neighbors, *single_letter_neighborhood(pattern, i)]
    return remove_duplicates(neighbors)

def rev_comp(pattern):
    rev = pattern[::-1]
    comp = [comp_map[x] for x in rev]
    return ''.join(comp)

def get_neighbours_upto_d(pattern, d):
    neighborhood = one_neighborhood(pattern)
    if d > len(pattern):
        return []
    for _ in range(d-1):
        for pattern in neighborhood:
            neighborhood = [*neighborhood, *one_neighborhood(pattern)]
    return remove_duplicates(neighborhood)

# print(get_neighbours_upto_d('AA', 2))

def get_all_apprx_kmer_freqs(text, k, d):
    ans = {}
    for i in range(len(text) - k + 1):
        exact_kmer = text[i:i+k]
        revcomp_kmer = rev_comp(exact_kmer)
        apprx_kmers = get_neighbours_upto_d(exact_kmer, d)
        apprx_kmers_rc = get_neighbours_upto_d(revcomp_kmer, d)
        all_kmers = remove_duplicates([exact_kmer, *apprx_kmers])
        all_kmers_rc = remove_duplicates([revcomp_kmer, *apprx_kmers_rc])
        for kmer in all_kmers:
            if kmer in ans:
                ans[kmer] += 1
            else:
                ans[kmer] = 1
        for kmer in all_kmers_rc:
            if kmer in ans:
                ans[kmer] += 1
            else:
                ans[kmer] = 1
    return ans

def get_most_frequent(freq):
    max_freq = max(list(freq.values()))
    return {key: val for key, val in freq.items() if val == max_freq}

all_apprx_kmers = get_all_apprx_kmer_freqs(TEXT, K, D)
max_apprx_kmers = get_most_frequent(all_apprx_kmers)
print(max_apprx_kmers)
print(' '.join(max_apprx_kmers.keys()))

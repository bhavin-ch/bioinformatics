# # from frequent_words_mismatch.txt
# TEXT = 'CACAGTAGGCGCCGGCACACACAGCCCCGGGCCCCGGGCCGCCCCGGGCCGGCGGCCGCCGGCGCCGGCACACCGGCACAGCCGTACCGGCACAGTAGTACCGGCCGGCCGGCACACCGGCACACCGGGTACACACCGGGGCGCACACACAGGCGGGCGCCGGGCCCCGGGCCGTACCGGGCCGCCGGCGGCCCACAGGCGCCGGCACAGTACCGGCACACACAGTAGCCCACACACAGGCGGGCGGTAGCCGGCGCACACACACACAGTAGGCGCACAGCCGCCCACACACACCGGCCGGCCGGCACAGGCGGGCGGGCGCACACACACCGGCACAGTAGTAGGCGGCCGGCGCACAGCC'
# K = 10
# D = 2

# from dataset_9_9
TEXT = 'GCCTACGCACGCGCGCCTGCCTCACGCGCCGCCACGTTTACGACGCGCACGTTTACGACGCGCCGCTTTCGCTTTGCCTCACGGCCTGCCTCACGCACGGCCTCACGACGACGACGCACGCGCCGCACGCACGCACGGCCTCACGGCCTCGCCGCCACGACGACGCACGTTTCACGACGACGACGGCCTACGACGCGCACGTTTGCCTTTTCGCCACGTTTGCCTTTTTTTCACGGCCTGCCTGCCTCACGTTTCGCTTTACGTTTGCCTCACGGCCTGCCTGCCTCGCGCCTACGCGCCGCCACGGCCTCACGGCCTCACGTTTACGGCCTACGGCCTTTTACGGCCTACGACGACGCACGTTTACGGCCTACGACGCGCCACGCGCCACG'
K = 7
D = 2

swap_map = {
    'A': 'TCG',
    'T': 'CGA',
    'C': 'GAT',
    'G': 'ATC'
}

def single_letter_neighborhood(pattern, i):
    return [pattern[:i] + x + pattern[i+1:] for x in swap_map[pattern[i]]]

def one_neighborhood(pattern):
    neighbors = []
    for i in range(len(pattern)):
        neighbors = [*neighbors, *single_letter_neighborhood(pattern, i)]
    return list(set(neighbors))

def get_neighbours_upto_d(pattern, d):
    neighborhood = one_neighborhood(pattern)
    if d > len(pattern):
        return []
    for _ in range(d-1):
        for pattern in neighborhood:
            neighborhood = list(set([*neighborhood, *one_neighborhood(pattern)]))
    return neighborhood

# print(get_neighbours_upto_d('AA', 2))

def get_all_apprx_kmer_freqs(text, k, d):
    ans = {}
    for i in range(len(text) - k + 1):
        exact_kmer = text[i:i+k]
        apprx_kmers = get_neighbours_upto_d(exact_kmer, d)
        all_kmers = list(set([exact_kmer, *apprx_kmers]))
        for kmer in all_kmers:
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

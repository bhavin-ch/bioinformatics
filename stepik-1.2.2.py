K = 9

def make_circular(data, k):
    firstpairs = data[0:k-1]
    return data + firstpairs

def get_freqs(data, L):
    freq = {}
    for i in range(L):
        kmer_i = data[i:i+K]
        if kmer_i in freq:
            freq[kmer_i] = freq[kmer_i] + 1
        else:
            freq[kmer_i] = 1
    return freq

def most_frequent(freq, fuzzy):
    max_freq = max(list(freq.values()))
    if fuzzy:
        return {key: val for key, val in freq.items() if val >= 0.75*max_freq}
    else:
        return {key: val for key, val in freq.items() if val == max_freq}

with open('Vibrio_cholerae.txt', 'r') as file:
    text = file.read().replace('\n', '')
length = len(text)

circular_text = make_circular(text, K)
freqs = get_freqs(circular_text, length)
max_kmers = most_frequent(freqs, False)
print(max_kmers)

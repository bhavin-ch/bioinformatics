# Taken from dataset_4_5.txt
TEXT = 'ATTCGAACTCCTGCAACCCCCTGATTAACAAACCACTAGTAGTAGCCCTTTACGGTTTACCGCGGCTTTACCCGGCTTTACCGGCTTTACCTATACTGGCCTGTGATTTGGTGGGTCGTAATAAGCAGGACCATCGAATCGGAATGATCTCTTATGCCGTGTAACTGCTTAGTGAACTATGGCACCTTGTCTGTGCGCCTAACACGCCTGGAGCATTTCTCATAGGTCCACCGACTATCCTTATGTCCAATGACACCCGCCGTTCGCACTTATTTTTGCTTTTGCTTTTTTTTGCTTTTGGCCAAATTGAACGATTATTGTGCATTAGGATATTTTGATTTTGCATTTTGCCTATTACATAAATAGATACACTGACCGAAGTCACACCTCTCTTAGTACCTAAGGCGAGTAGGGGCTATCTCTCTGTAGAGCCTTTTTAGAGCCTTTTAATTGCAGCAGCGAAAGGCAAGTCGATGCACGAACCATAACCTACGCCCCTCGCAGATCAGTTGACTTTAGAAATCTGGGATACACTGTCGACCAATCGAATCTTGCCCGGTTGGATCGTACCCCTTGAAGTTTTTGTGATTTCAGGGTAACGATTGAGGAACTAGGATACCCTCAGAGTATCGATCGGTATCGTCCCGTATCAATCGATAAGTTATATCCCACGTGGGGACTTCGTCCTTATCGATGGTAGTTCTCTTGTGCCTAATTCTTTTGCTAGGTTCGGTGTAGGTTAGTAGGCGTGAGGGGTCATCGGAGGACACACCTTTGGCCTCGGCCTTCTACAGCCGAGCTATTCATGTAGACATTATTATGTACACCACACACCACCGAAATAAGATAGCAGCACAGCATCGCGGGTGCCAGGCTGATTAGAGGAAATAAATCACATAGTGTTGGAGCTCGGACCTCTATCCTCAAGGCACAGCTGGGTGGTCAAGAAGACAAGTTGTGTGCGCGAAATGCGTCCGGTATATAGCCTCTACTTGCGGGAGACGAAAGGGGAGACGAAGAAGAACCACTAGCTCCGGACCAATTAAGTATTCCTCGTTTACTGAGAACTAGCGTGTGTGGATGTCGGTTTCGGCGGTCGGATCCAAAGAATCATAGTTGTATTCAGTCGATCACTGTACTGCGTTAGGCGCGACAGAACTGGGCGATCTTACTGACACCGGCTGACACCGGCACCGGCCATTCTCCAGGAGGTACCATTGCACATGCACACCTAGAATATGTAGAGGTGCTTCCGAGCATGTGAAGATCTACACTGTGTGTATCTTATAGTAGTGATGTCGACCACTTCATGAAGAGCGATAAGTAGCTCCATGAACGCCCATGAACGCCCAAAAGGACGCTTACTCCCTACTGAGCGCATTGACTATATGTGCAAATTTTCACGTTAGTAAAACAGGTGCGCTTAAGAGTACGAGCATGCGAATTACTGGTGTGGTTCTTGCGTATTACCGGAGGTTGATATAACCACTACAATCGGTCCATTCCTTCAGAAAGTCTCCAAGTCGACCCTTTACAACAGCACACTCCAGCAGGCACCACCATAACGTTGACAAGTCCTTGACAAGTCAGGCGCCGCATGGAGAGGTTTTTATGGTAAAGTACCGTTGTTGGTAAGCTTTTTCGGGCCAATTGGGGTTATAGCCCAAAGTGAATTACTGTACTGGGGCAGTCATAGACGTTCTCGTTTGAGCTTCGTCTCGTAAATACGTCCATGGTCATCATAGATAGAGTATTGAGTATAGAGTATTTAACAATATAACTTGTCGGCACCACCATTGGGTTCTGACATTGCACAATAGCGGTCGATACGACTACTTGTCAATGCTGCCACCTCGTCCCACTGGTTTGGGTTTCAT'
K=10
L=24
T=3

def get_occurance_freqs(text, k):
    freqs_dict = {}
    for i in range(len(text)):
        kmer = text[i:i+k]
        if kmer in freqs_dict:
            freqs_dict[kmer] = freqs_dict[kmer] + 1
        else:
            freqs_dict[kmer] = 1
    return freqs_dict

def filter_occurance_freqs(freqs_dict, t):
    return {key: val for key, val in freqs_dict.items() if val >= t}

def get_occurance_indices(text, pattern):
    pattern_length = len(pattern)
    return [i for i in range(len(text)) if text[i:i+pattern_length] == pattern]

def get_clumps(text, freqs_dict, k, l):
    kmer_index = {}
    for kmer in freqs_dict.keys():
        occurance_index = get_occurance_indices(text, kmer)
        if (occurance_index[-1] + k - occurance_index[0] <= l):
            kmer_index[kmer] = get_occurance_indices(text, kmer)
    return kmer_index

kmer_freqs = get_occurance_freqs(TEXT, K)
kmer_freqs = filter_occurance_freqs(kmer_freqs, T)
kmer_index = get_clumps(TEXT, kmer_freqs, K, L)

print(kmer_index)
# # from ApproximatePatternCount.txt
# TEXT = 'GAATCCGCCAAGTACCAAGATGTAAGTGAGGAGCGCTTAGGTCTGTACTGCGCATAAGCCTTAACGCGAAGTATGGATATGCTCCCCGGATACAGGTTTGGGATTTGGCGGTTACCTAAGCTAACGGTGAGACCGATATGACGAGGTTCCTATCTTAATCATATTCACATACTGAACGAGGCGCCCAGTTTCTTCTCACCAATATGTCAGGAAGCTACAGTGCAGCATTATCCACACCATTCCACTTATCCTTGAACGGAAGTCTTATGCGAAGATTATTCTGAGAAGCCCTTGTGCCCTGCATCACGATTTGCAGACTGACAGGGAATCTTAAGGCCACTCAAA'
# PATTERN = 'TACAG'
# D = 2

# from dataset_9_6 
TEXT = 'CATGCCATTCGCATTGTCCCAGTGA'
PATTERN = 'CCC'
D = 2

def print_num_list_as_str(numlist, glue=' '):
    print(glue.join(str(x) for x in numlist))

def hamming_distance(text1, text2):
    if len(text1) != len(text2):
        return -1
    return sum([0 if text1[i] == text2[i] else 1 for i in range(len(text1))])

def count_approx_kmers(text, pattern, d):
    k = len(pattern)
    return sum([1 for i in range(len(text)-k+1) if hamming_distance(text[i:i+k], pattern) <= d])

ans = count_approx_kmers(TEXT, PATTERN, D)
print(ans)


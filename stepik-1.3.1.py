# from Bio.Seq import Seq

# with open('dataset_3_2.txt', 'r') as file:
#     text = file.read().replace('\n', '')

# my_seq = Seq(text)
# print(my_seq.reverse_complement())

# def swap(char):
#     if char == 'A':
#         return 'T'
#     if char == 'T':
#         return 'A'
#     if char == 'C':
#         return 'G'
#     if char == 'G':
#         return 'C'

comp_map = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

def rev_comp1(seq):
    rev = seq[::-1]
    # comp = []
    # for i, x in enumerate(rev):
    #     comp[i] = swap(x)
    comp = [comp_map[x] for x in rev]
    return ''.join(comp)

def rev_comp2(seq):
    rev = seq[::-1]
    rev = rev.replace('A', 'B')
    rev = rev.replace('T', 'A')
    rev = rev.replace('B', 'T')
    rev = rev.replace('C', 'B')
    rev = rev.replace('G', 'C')
    rev = rev.replace('B', 'G')
    return rev

text = 'AAAACCCGGT'
print(rev_comp2(text))

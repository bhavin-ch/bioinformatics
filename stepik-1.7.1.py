
# from dataset_3014_4.txt
TEXT = 'CCAGTCAATG'
D = 1

swap_map = {
    'A': 'TCG',
    'T': 'CGA',
    'C': 'GAT',
    'G': 'ATC'
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

def get_neighbours_upto_d(pattern, d):
    neighborhood = one_neighborhood(pattern)
    if d > len(pattern):
        return []
    for _ in range(d-1):
        for pattern in neighborhood:
            neighborhood = [*neighborhood, *one_neighborhood(pattern)]
    return remove_duplicates(neighborhood)

print(' '.join(get_neighbours_upto_d(TEXT, D)))

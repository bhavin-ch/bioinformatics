from collections import Counter
K = 9

def make_circular(data, k):
    firstpairs = data[0:k-1]
    return data + firstpairs

def get_sequences(data, no_of_letters, k):
    return [data[i:i+k] for i in range(no_of_letters)]

def most_frequent(dataset):
    c=Counter(dataset)
    freqs = list(c.values())
    max_freq = max(freqs)
    max_kmers = {key: val for key, val in c.items() if val >= 0.9*max_freq}
    return max_kmers


with open('Vibrio_cholerae.txt', 'r') as file:
    data = file.read().replace('\n', '')

data_circle = make_circular(data, K)
no_of_kmers = len(data)
kmers_dataset = get_sequences(data_circle, no_of_kmers, K)
print(most_frequent(kmers_dataset))
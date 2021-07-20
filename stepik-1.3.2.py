from matplotlib import pyplot as plt

with open('dataset_7_10.txt', 'r') as file:
    text = file.read().replace('\n', '')
# text = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'
length = len(text)
skew_diffs = {
    'G': 1,
    'C': -1,
    'A': 0,
    'T': 0
}

def plotter(somelist):
    plt.plot(somelist)
    plt.show()
    pass

def print_num_list_as_str(numlist, glue=' '):
    print(glue.join(str(x) for x in numlist))

# initialize
ans = [None] * (length + 1)
ans[0] = 0
min = ans[0]
min_indices = [0]

# run in loop. Graph skew and min
for i in range(1, length + 1):
    ans[i] = ans[i-1] + skew_diffs[text[i-1]]
    if ans[i] < min:
        min = ans[i]
        min_indices = [i]
    elif ans[i] == min:
        min_indices.append(i)
    else:
        pass

plotter(ans)
print_num_list_as_str(min_indices)

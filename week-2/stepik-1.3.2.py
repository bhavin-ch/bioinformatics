from matplotlib import pyplot as plt

# with open('dataset_7_10.txt', 'r') as file:
#     text = file.read().replace('\n', '')
text = 'CATTCCAGTACTTCATGATGGCGTGAAGA'
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
max = ans[0]
max_indices = [0]

# run in loop. Graph skew and max
for i in range(1, length + 1):
    ans[i] = ans[i-1] + skew_diffs[text[i-1]]
    if ans[i] > max:
        max = ans[i]
        max_indices = [i]
    elif ans[i] == max:
        max_indices.append(i)
    else:
        pass

plotter(ans)
print_num_list_as_str(max_indices)

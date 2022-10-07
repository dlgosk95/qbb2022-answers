#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

# 8 is p value
# 0 is chr
# 2 is BP
# scatter plot
# want nested numpy array [[1,231, .23423], ...]
# first row is header

association = np.genfromtxt("output_CB1908.assoc.linear", dtype = None, encoding = None, names = ["chr", "snp", "bp", "a1", "test", "nmiss", "beta", "stat", "pvalue"])
# print(association[0:4])

dictionary = {}
number = 0 # to index
# print (association[chr, 1])

# make for loop
for i in association[1:]:
    if int(i["chr"]) not in dictionary.keys():
        dictionary[int(i["chr"])] = []
    dictionary[int(i["chr"])].append([number, -np.log10(float(i["pvalue"]))])
    number += 1

print(dictionary[1][:4])
# [[0, 1.1563935280754891], [1, 0.486516043295743], [2, 0.661145253747677], [3, 0.027612000892527164]]
## assuming they are ordered, and they are.

significant = []

fig, ax = plt.subplots(1)
colors = ['darkblue', 'blue']
x_labels = []
x_labels_pos = []
for key, value in dictionary.items():
    # print(value[:4])
    value = np.array(value).T
    # x, y = value # ValueError: too many values to unpack (expected 2)
    ax.scatter(x = value[0], y = value[1], color=colors[key % len(colors)])
    x_labels.append(str(key))
    if value[1] > 5:
        significant.append(value)
    # x_labels_pos.append((group['ind'].iloc[-1] - (group['ind'].iloc[-1] - group['ind'].iloc[0])/2))
    x_labels_pos.append(max(value[0])/2)
ax.set_xticks(x_labels_pos)
ax.set_xticklabels(x_labels)
ax.axhline(y=5)

## graph points less than 10^-5 with red color to overwrite
## if float(i["pvalue"])) < , add to a separate new list in line 22

## have lables at correct spots
## axes labels
plt.savefig("manhattan_plot.png")
plt.show()
plt.close()















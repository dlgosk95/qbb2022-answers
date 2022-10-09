#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

## 8 is p value
## 0 is chr
## scatter plot
## want nested numpy array [[1,231, .23423], ...]
## first row is header

association = np.genfromtxt("output_CB1908.assoc.linear", dtype = None, encoding = None, names = ["chr", "snp", "bp", "a1", "test", "nmiss", "beta", "stat", "pvalue"])
# print(association[0:4])

dictionary = {}
sig_list = []
number = 0 ## to index
# print (association[chr, 1])

## make for loop
for i in association[1:]:
    if int(i["chr"]) not in dictionary.keys():
        dictionary[int(i["chr"])] = []
    dictionary[int(i["chr"])].append([number, -np.log10(float(i["pvalue"]))])
    if -np.log10(float(i["pvalue"])) > 5:
        sig_list.append([number, -np.log10(float(i["pvalue"]))])
    number += 1


# print(dictionary[1][:4])
## [[0, 1.1563935280754891], [1, 0.486516043295743], [2, 0.661145253747677], [3, 0.027612000892527164]]
## assuming they are ordered, and they are.

sig = np.array(sig_list).T

fig, ax = plt.subplots(1, figsize = (13,10))
colors = ['darkblue', 'blue']
x_labels = []
x_labels_pos = []
for key, value in dictionary.items():
    # print(value[:4])
    value = np.array(value).T
    ## Transpose: switch one list per row like a matrix
    ## x, y = value # ValueError: too many values to unpack (expected 2)
    ax.scatter(x = value[0], y = value[1], color=colors[key % len(colors)], s = 2)
    x_labels.append(str(key))
    x_labels_pos.append((max(value[0])-min(value[0]))/2 + min(value[0]))
ax.scatter(sig[0], sig[1], color = "red", s = 2)
ax.set_xticks(x_labels_pos)
ax.set_xticklabels(x_labels, fontsize = 8)
ax.axhline(y=5)
ax.set_xlabel("Chromosomes")
ax.set_ylabel("-log10(P-value)")
plt.savefig("manhattan_plot.png")
plt.show()
plt.close()



#!/usr/bin/env python3
import matplotlib.pyplot as plt
from vcfParser import *
import numpy as np

parsed = parse_vcf('sac_predict.vcf')

# print (parsed)

# print (parsed [1]) # 0 was info
# print (len(parsed)) # 41779
# print (parsed [41778])

# print (parsed [1][9][2])
# print (parsed [1][17][2])
# print (parsed[1][7]["AF"])
# print (parsed[1][7]["ANN"])
# predicted = parsed[1][7]["ANN"].split('|')
# print(predicted)
# print(predicted[1])
# print(parsed[1][7]["ANN"].split('|')[1])

read_depth =[]
genotype_quality = []
allele_frequency = []
predicted_effect = []

for i in range(1, len(parsed)): # 1~41778
    for j in range(9, 18): #9~17
        if parsed[i][j][2] != ".":
            read_depth.append(int(parsed[i][j][2]))
        if parsed[i][j][1] != ".":
            genotype_quality.append(float(parsed[i][j][1]))
        if parsed[i][7]["AF"] != ".":
            allele_frequency.append(float(parsed[i][7]["AF"]))
        if parsed[i][7]["ANN"].split('|')[1] != ".":
            predicted_effect.append(parsed[i][7]["ANN"].split('|')[1])

effects_dict = {}
for pred_effect in predicted_effect:
    if pred_effect == '':
        pred_effect = "no_effect" # if predicted effect is empty string, write no effect
    if pred_effect not in effects_dict:
        effects_dict[pred_effect] = 0
    effects_dict[pred_effect]+=1
# print (effects_dict)
x = list(effects_dict.keys())
height = list(effects_dict.values())
# print(x)
# print(height)

# print (read_depth)
# print (max(read_depth)) # 486
# print (genotype_quality)
# print (allele_frequency)
# print (predicted_effect)

fig, ax = plt.subplots(2,2, figsize = (10,10))
ax[0,0].hist(read_depth, bins = np.arange(0, max(read_depth) + 1, 1))
ax[0,0].set_xlabel("Read Depth")
ax[0,0].set_ylabel("Number of Variants")
ax[0,1].hist(genotype_quality, bins = np.arange(0, max(genotype_quality) + 1, 1))
ax[0,1].set_xlabel("Read Quality")
ax[0,1].set_ylabel("Number of Variants")
ax[1,0].hist(allele_frequency)
ax[1,0].set_xlabel("Allele Frequency")
ax[1,0].set_ylabel("Number of Variants")
ax[1,1].bar(x, height) 
ax[1,1].set_ylabel("Number of Variants")
plt.xticks(rotation=90, ha='right') # rotate the lables
plt.tight_layout()
plt.savefig("graphs.png")
plt.show()
plt.close()

# QBB2022 - Day 3 - Homework Exercises Submission

exercise 1
(base) [~/qbb2022-answers/day3-homework $]plink --vcf ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz --pca 3

excercise 2
#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt

eigenvec = np.genfromtxt("plink.eigenvec", dtype = None, encoding = None, names = ["indiv", "family", "x", "y", "z"])

fig, ax = plt.subplots()
ax.scatter(eigenvec["x"], eigenvec["y"], label = "PCA 1 and 2")
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
plt.savefig("ex2_a.png")

plt.show()

fig, ax = plt.subplots()
ax.scatter(eigenvec["x"], eigenvec["z"], label = "PCA 1 and 3")
ax.set_xlabel("PC1")
ax.set_ylabel("PC3")
plt.savefig("ex2_b.png")

plt.show()

There are three clusters, which may indicate genetic similarity within clusters.

exercise 3

#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt

eigenvec = np.genfromtxt("join.txt", dtype = None, encoding = None, names = ["sample", "pop", "super_pop", "gender", "family", "x", "y", "z"])

fig, ax = plt.subplots()

unique_gender = np.unique(eigenvec["gender"])
for sex in unique_gender:
    row = np.where(eigenvec["gender"] == sex)
    subset_data = eigenvec[row] # index with variable name
    ax.scatter(subset_data["x"], subset_data["y"], label = sex)
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.legend()
ax.title.set_text('PCA analysis of genomic variation colored by sex')
plt.savefig("ex3_a.png")
plt.show()

fig, ax = plt.subplots()

unique_super = np.unique(eigenvec["super_pop"])
for superpop in unique_super:
    row = np.where(eigenvec["super_pop"] == superpop)
    subset_data = eigenvec[row] 
    ax.scatter(subset_data["x"], subset_data["y"], label = superpop)
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.legend()
ax.title.set_text('PCA analysis of genomic variation colored by super population')
plt.savefig("ex3_b.png")
plt.show()

fig, ax = plt.subplots()

unique_pop = np.unique(eigenvec["pop"])
for pop in unique_pop:
    row = np.where(eigenvec["pop"] == pop)
    subset_data = eigenvec[row] 
    ax.scatter(subset_data["x"], subset_data["y"], label = pop)
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.legend(bbox_to_anchor=(1, 1))
ax.title.set_text('PCA analysis of genomic variation colored by population')
plt.tight_layout()
plt.savefig("ex3_c.png")
plt.show()


#!/usr/bin/env python

import numpy as np
import sys
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

gene_names = []
k562_model_predictions = []
k562_observations = []
descriptions = []

for i, line in enumerate(open(sys.argv[1])):
    if line.strip('"').startswith("##"):
        header = np.array(line.strip('"\r\n').split('\t'))
        k562_obs_idx = np.where(header == "E123")[0][0]
    elif not line.strip('"').startswith("#"):
        fields = line.strip('"\r\n').split('\t')
        k562_model_predictions.append(float(fields[4]))
        k562_observations.append(float(fields[k562_obs_idx]))
        gene_names.append(fields[1])
        descriptions.append(fields[2])

genesoi = ["PIM1", "SMYD3", "FADS1", "PRKAR2B", "GATA1", "MYC"]
genesoilocs =[]

for geneoi in genesoi:
    genesoilocs.append(np.where(np.array(gene_names) == geneoi)[0][0])
for i in range(len(descriptions)):
    if "hemoglobin subunit" in descriptions[i]:
        genesoi.append(gene_names[i])
        genesoilocs.append(i)

fig, ax = plt.subplots()
ax.scatter(k562_model_predictions, k562_observations, alpha=1, color="blue", s=0.25)
ax.set_xlabel("Predicted K562 expression level,\n10-fold cross-validated")
ax.set_ylabel("K562 expression level (log10)")
corr = pearsonr(k562_model_predictions, k562_observations)
ax.text(.5, 3.75, "r^2 = " + str(round(corr.statistic**2,2)) + "\nn = " + str(len(k562_observations)))
line_xs = np.linspace(max(min(k562_model_predictions), min(k562_observations)), min(max(k562_model_predictions), max(k562_observations)), 100)
line_ys = 0 + 1 * line_xs
ax.plot(line_xs, line_ys, color = "maroon")
for i, geneoi in enumerate(genesoi):
    ax.text(k562_model_predictions[genesoilocs[i]], k562_observations[genesoilocs[i]], geneoi, color="maroon", fontweight="demi")
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
plt.tight_layout()
plt.savefig("week10_inclass.png")
plt.show()
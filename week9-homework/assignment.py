#!/usr/bin/env python

import sys

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors


input_arr = np.genfromtxt("dros_gene_expression.csv", delimiter=',', names=True, dtype=None, encoding='utf-8')
col_names = list(input_arr.dtype.names)
# print(col_names)
## ['t_name', 'male_10', 'male_11', 'male_12', 'male_13', 'male_14', 'female_10', 'female_11', 'female_12', 'female_13', 'female_14']
# row_names = []
# for i in range(len(input_arr)):
#     row_names.append(input_arr[i][0])
# # print(row_names[0])
row_names = input_arr['t_name']
# print(row_names)
## ['FBtr0114258' 'FBtr0346770' 'FBtr0302440' ... 'FBtr0114216' 'FBtr0114222' 'FBtr0114283']
# print(row_names.shape)
## (34718,)

fpkm_values = input_arr[col_names[1:]]
# print(fpkm_values)

import numpy.lib.recfunctions as rfn
fpkm_values_2d = rfn.structured_to_unstructured(fpkm_values, dtype=float)
# print(fpkm_values_2d)

tx_med = np.median(fpkm_values_2d, axis=1)
# print(len(tx_med))
## 34718
# print(len(row_names))
## 34718

fpkm_subset = fpkm_values_2d[np.where(tx_med > 0)]
# print(fpkm_subset.shape)
## (9117, 10)

transcript_subset = row_names[np.where(tx_med > 0)]
# print(transcript_subset.shape)
## 9117

fpkm_log = np.log2(fpkm_subset + 0.1)
# print(fpkm_log)

fpkm_log_T = fpkm_log.T
# print(fpkm_log_T[0]) ## gives me column samples
# print(fpkm_log_T[:,0]) ## gives me row transcripts

# print(fpkm_log_T.shape)
## (10, 9117)


## Using linkage and leaves_list, cluster the filtered and log2 transformed gene expression data matrix (derived from fpkm_values_2d earlier) for both genes and samples based on their patterns of expression (so both the rows and columns of the matrix). You will find the numpy transpose functionality useful in order to cluster the columns.
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list

col_Z = linkage(fpkm_log_T, method='ward', metric='euclidean', optimal_ordering=False)
# print(col_Z)
leaves_list(col_Z)
## [9 4 8 1 6 3 2 5 0 7] Column

row_Z = linkage(fpkm_log, method='ward', metric='euclidean', optimal_ordering=False)
# print(row_Z)
leaves_list(row_Z)

fig,ax = plt.subplots(2)
ax[0].imshow(fpkm_log[leaves_list(row_Z),:][:,leaves_list(col_Z)], cmap = "magma_r", aspect = 'auto')
## The aspect ratio of the Axes. This parameter is particularly relevant for images since it determines whether data pixels are square.
## indexing

dn = dendrogram(col_Z, ax = ax[1])
## ax: needs to know where to draw
## orientation 
## seabron cluster map

plt.savefig("heatmap_and_dendrogram.png")
# plt.show()



import statsmodels.formula.api as smf

## the stage number and the observed fpkm value for that stage

# print(fpkm_log)
# print(fpkm_log.shape)
## (9117,10)

# print(range(len(col_names)))
## 11

sexes = []
stages = []
slope_list = []
pvalue_list = []
for i in range(1,len(col_names)):
    sexes.append(col_names[i].split('_')[0])
    stages.append(col_names[i].split('_')[1])
# print(sexes)
# print(stages)

for i in range(fpkm_log.shape[0]):
    list_of_tuples = []
    for j in range(len(col_names)-1):
        list_of_tuples.append((row_names[i],fpkm_log[i,j], sexes[j], stages[j]))
    longdf = np.array(list_of_tuples, dtype=[('transcript', 'S11'), ('fpkm', float), ('sex', 'S6'), ('stage', int)])
    fpkm_stage = smf.ols('fpkm ~ stage', data = longdf)
    results_stage = fpkm_stage.fit()
    # print(results_stage.summary())
    parameters = results_stage.params
    slope_list.append(parameters['stage'])
    pvalue_list.append(results_stage.pvalues['stage'])
# print(longdf)
# print(slope_list)
# print(pvalue_list)

## 1+ means use intercept.-1 or 0 means don't use intercept.

# print(parameters)
## parameters are already dictionaries. 
# print(parameters['stage'])


import statsmodels.api as sm

from scipy.stats import uniform
pval = np.array(pvalue_list)
# print(pval.shape)
## 9117
sm.qqplot(pval, line = '45', dist = uniform)
plt.savefig("qqplot.png")
# plt.show()

from statsmodels.stats import multitest

boolean = multitest.multipletests(pval, alpha=0.1, method='fdr_bh')[0]
# print(fdr.shape)
## 9117

# print(transcript_subset[boolean])
## giving me true only
## 3265

np.savetxt('transcript_10false.txt', transcript_subset[boolean], fmt="%s")
## np expects all numbers. but ours is string.

## dist uniform distribution because when null is true, we expect uniform distribution of p values.
## more significant results 
## wrong model (negative bionomial which allows more spectrum of # between 0 and 1 and more dispersion bc there is technical and biological disparities)
## dependent data (time series)
## t test continuous data discrete data numbers







## controlling for sex as a covariate


slope_list_sex = []
pvalue_list_sex = []
for i in range(fpkm_log.shape[0]):
    list_of_tuples = []
    for j in range(len(col_names)-1):
        list_of_tuples.append((row_names[i],fpkm_log[i,j], sexes[j], stages[j]))
    longdf = np.array(list_of_tuples, dtype=[('transcript', 'S11'), ('fpkm', float), ('sex', 'S6'), ('stage', int)])
    fpkm_stage_sex = smf.ols('fpkm ~ stage + sex', data = longdf)
    results_stage_sex = fpkm_stage_sex.fit()
    # print(results_stage.summary())
    slope_list_sex.append(results_stage_sex.params['stage'])
    pvalue_list_sex.append(results_stage_sex.pvalues['stage'])

pval_sex = np.array(pvalue_list_sex)
boolean_sex = multitest.multipletests(pval_sex, alpha=0.1, method='fdr_bh')[0]
np.savetxt('transcript_10false_sex.txt', transcript_subset[boolean_sex], fmt="%s")


## Compare the lists–what is the percentage overlap with and without sex as a covariate? We suggest defining the percentage of overlap as ((# overlapping transcripts) / (# transcripts differentially expressed by stage without sex covariate)) * 100


overlap = [value for value in transcript_subset[boolean] if value in transcript_subset[boolean_sex]]
# print(len(overlap))
## 2971
# print (transcript_subset[boolean].shape)
## (3265,)
percent_overlap = len(overlap)/transcript_subset[boolean].shape[0]
# print(percent_overlap)
## 0.9099540581929556

with open('percent_overlap.txt', 'w', encoding='utf-8') as f:
    f.write(str(percent_overlap))

## volcano plot of the differential expression (with sex as a covariate) results. Use the betas on the x axis and -log10(p-value) on the y-axis. Color the significant points in a different color.

y = -np.log(pvalue_list_sex)
x = slope_list_sex

color = ["Orange" if x == True else "Black" for x in boolean_sex]
## masking list
## or you can do for loop

fig,ax = plt.subplots()
ax.scatter(x,y, c = color, s=0.25, alpha=1)

ax.set_xlabel("Slope")
ax.set_ylabel("-Log10 (p-values)")

plt.savefig("volcano_plot.png")
# plt.show()



















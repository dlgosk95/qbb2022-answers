#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from vcfParser import *


association = np.genfromtxt("output_CB1908.assoc.linear", dtype = None, encoding = None, names = ["chr", "snp", "bp", "a1", "test", "nmiss", "beta", "stat", "pvalue"])

min_var = ''
min_pval = 1
for i in association[1:]:
    var_id = i[1]
    var_pval = float(i[8])
    if var_pval < min_pval :
        min_var = var_id
        min_pval = var_pval

# print (min_var) # rs10876043
# print (min_pval) # 8.199e-12

## make dictionary {genotype 00/01/11/no info, IC50 values}
## retrieve genotypes of most associated SNPs
## match to IC50 of patients 175

parsed = parse_vcf('genotypes.vcf')

# print(parsed[:4])
## 0 is header
## ['1', 558185, 'rs9699599', 'A', 'G', '.', '.', {'PR': None}, 'GT', '0/0', '0/0', '0/0', '0/1', '0/0', '0/1', './.', '0/0', '0/0', '0/0', '0/1', '0/0', '0/0', '0/0', '0/0', '0/1', '0/0', '0/1', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', './.', '0/0', '0/0', '0/0', '0/0', '0/1', '0/0', '0/1', '0/1', '0/0', '0/1', './.', '0/1', '0/1', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/1', '0/0', '0/1', '0/0', '0/0', '0/0', '0/1', '0/0', '0/1', '0/0', '0/0', '0/0', './.', '0/0', '0/0', '0/0', '0/1', '0/0', '0/1', '0/0', '0/1', '0/0', '0/1', '0/0', '0/0', '0/1', '0/0', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.']
## starting from 1, 2 is the snp id, after 9 is genotype of each patient

genotype_dict = {}
patient_ids = parsed[0][9:]
# print(patient_ids)


for line in parsed[1:]:
    snp_id = line[2]
    # print(snp_id)
    if snp_id == min_var:
        patient_genotypes = line[9:]
        break
# print(patient_genotypes)

## I want {patient_ID : genotypes}
for i in range(len(patient_ids)):
    genotype_dict[patient_ids[i]] = patient_genotypes[i]
# print(genotype_dict)
## {'1001_1001': '0/1', ..., '1176_1176': '0/0'}

## I want {pateint_ID : IC 50}
phenotype = np.genfromtxt("CB1908_IC50.txt", dtype = None, encoding = None, names = ["FID", "IID", "IC50"])
phenotype_dict = {}
for line in phenotype[1:]:
    patient_id = line["FID"]+"_"+line["IID"]
    # print(patient_id) # 1001_1001
    try:
        phenotype_dict[patient_id] = float(line["IC50"])
        # ValueError: could not convert string to float: 'NA'
    except:
        phenotype_dict[patient_id] = None
# print (phenotype_dict)
## {'1001_1001': 6.927465594, ..., '1176_1176': 4.742201188}

## I want {genotypes : IC 50 multiple values}
# gen_phen_dict = {}
# for d in (genotype_dict, phenotype_dict):
#      for key, value in d.items():
#          gen_phen_dict[key].append(value)
# print (gen_phen_dict) # KeyError: '1001_1001'

# ds = [genotype_dict, phenotype_dict]
# d = {}
# for k in genotype_dict.keys():
#   d[ds[0][k]] = ds[1][k]
# print(d) ## {'0/1': 6.907481918, './.': 6.964156628, '1/1': 7.062508215, '0/0': 4.742201188}

# ds = [genotype_dict, phenotype_dict]
# d = {}
# for k in genotype_dict.keys():
#   d[k] = tuple(d[k] for d in ds)
# print(d)
## {'1001_1001': ('0/1', 6.927465594), '1002_1002': ('0/1', 11.88728968), ..., '1176_1176': ('0/0', 4.742201188)}

ds = [genotype_dict, phenotype_dict]
d = {'0/0':[], '0/1':[], '1/1':[]}
for key, value in genotype_dict.items():
    if phenotype_dict[key] is not None:
        if genotype_dict[key] == '0/1':
            d['0/1'].append(phenotype_dict[key]) 
        # elif genotype_dict[key] == './.':
        #     if phenotype_dict[key] is not None:
        #         d['./.'].append(phenotype_dict[key])
        elif genotype_dict[key] == '1/1':
            d['1/1'].append(phenotype_dict[key])
        elif genotype_dict[key] == '0/0':
            d['0/0'].append(phenotype_dict[key])
# print(d)
## {'0/0': [9.214520671, ..., 4.742201188], '0/1': [6.927465594, ..., 6.907481918], '1/1': [10.23771873, ..., 7.062508215]}

fig, ax = plt.subplots(1)
labels, data = d.keys(), d.values()
# print(labels) ## dict_keys(['0/1', './.', '1/1', '0/0'])
# print (data) ## dict_values([[6.927465594, ..., 4.742201188]])
plt.xlabel("Genotype")
plt.ylabel("IC50")
plt.boxplot(data)
plt.xticks(range(1, len(labels) + 1), labels)
plt.savefig("boxplot.png")
plt.show()
plt.close()

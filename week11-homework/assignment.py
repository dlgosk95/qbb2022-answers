#!/usr/bin/env python

import scanpy as sc
import matplotlib.pyplot as plt
# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()


## Produce a PCA plot before and after filtering 

# sc.tl.pca(adata)
# sc.pl.pca(adata, save = 'before')

# sc.pp.recipe_zheng17(adata)
# sc.tl.pca(adata)
# sc.pl.pca(adata, save = 'after')


# sc.pp.recipe_zheng17(adata)
# sc.pp.neighbors(adata)
# sc.tl.leiden(adata)
# sc.tl.tsne(adata)
# sc.pl.tsne(adata, color = "leiden", save = 'leiden')

# sc.pp.recipe_zheng17(adata)
# sc.pp.neighbors(adata)
# sc.tl.leiden(adata)
# sc.tl.umap(adata, maxiter = 1000)
# sc.pl.umap(adata, color = "leiden", save = 'leiden')


# sc.pp.recipe_zheng17(adata)
# sc.pp.neighbors(adata)
# sc.tl.leiden(adata)
# sc.tl.rank_genes_groups(adata, groupby = 'leiden', method = 't-test')
# sc.pl.rank_genes_groups(adata, save = 'rank_ttest')

# sc.pp.recipe_zheng17(adata)
# sc.pp.neighbors(adata)
# sc.tl.leiden(adata)
# sc.tl.rank_genes_groups(adata, groupby = 'leiden', method = 'logreg')
# sc.pl.rank_genes_groups(adata, save = 'rank_logreg')

# print(adata)
## AnnData object with n_obs × n_vars = 11843 × 31053 var: 'gene_ids', 'feature_types', 'genome'

sc.pp.recipe_zheng17(adata)
sc.pp.neighbors(adata)
sc.tl.leiden(adata)
sc.tl.tsne(adata)

# sc.pl.tsne(adata, color = "Gad67", color_map = "jet", save = "Gad67")


# markers = {'Microglia':'Cx3cr1', 'Astrocytes':'Aldh1l1', 'Blood cells':'Hbb-bs', 'Schwann cells':'Gap43', 'Oligodendrocytes':'Olig1', 'Gabaergic neurons':'Gad1'}
# fig = sc.pl.tsne(adata, color = list(markers.values()), return_fig=True, ncols=3, color_map="magma")
# plt.savefig('6_markers')
# plt.show()

cluster2annotation = {
     '16': 'Blood cells',
     '5': 'Astrocytes',
     '14': 'Astrocytes',
     '21':'Oligodendrocytes',
     '24': 'Schwann cells',
     '26': 'Microglia', '2': 'GABaergic neruons', '27': 'GABaergic neruons', '19':'GABaergic neruons', '12': 'GABaergic neruons', '15': 'GABaergic neruons'}


adata.obs['cell type'] = adata.obs['leiden'].map(cluster2annotation).astype('category')
sc.pl.tsne(adata, color='cell type', legend_loc='on data', frameon=False, legend_fontsize=10, legend_fontoutline=2, save='6_types')














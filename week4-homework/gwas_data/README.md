plink --vcf genotypes.vcf --pca 10
(base) [~/qbb2022-answers/week4-homework/gwas_data $]plink --vcf genotypes.vcf --freq


--vcf
--pheno
--linear
--allow-no-sex
pca eigenval as covariates
--covar c.txt

controlling for that relatednes
twice

plink --vcf genotypes.vcf --linear --pheno CB1908_IC50.txt --covar plink.eigenvec --allow-no-sex --out output_CB1908
plink --vcf genotypes.vcf --linear --pheno GS451_IC50.txt --covar plink.eigenvec --allow-no-sex --out output_GS451

OR
pip install qmplot

7. For the top loci associated with each of the phenotypes, use the UCSC Genome Browser to investigate the potential causal genes in the region. Note that the reference genome build being used here is hg18. (How could you figure this out if you didn't know?). Summarize your results in your README.md.

dbSNP: rs10876043
Position: chr12:49190411-49190411
Band: 12q13.13
Genomic Size: 1
Summary: A>A/G (chimp allele displayed first, then '>', then human alleles)

DIP2B
DIP2 disco-interacting protein 2 homolog B (Drosophila) is a protein that in humans is encoded by the DIP2B gene.[5] A member of the disco-interacting protein homolog 2 protein family, it contains a binding site for the transcriptional regulator DNA methyltransferase 1 associated protein 1, as well as AMP-binding sites. The presence of these sites suggests that DIP2B may participate in DNA methylation. This gene is located near a folate-sensitive fragile site.[5][6]
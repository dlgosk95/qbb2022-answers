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
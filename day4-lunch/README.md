exercise 1


*** Subsetting .vcf for each feature
--- Subsetting exons.chr21.bed.vcf
    + Covering 1107407 bp
--- Subsetting processed_pseudogene.chr21.bed.vcf
    + Covering 956640 bp
--- Subsetting protein_coding.chr21.bed.vcf
    + Covering 13780687 bp

follow the instruction in readme
it will make 4 plots 
processed_pseudogene.chr21.bed.vcf.png
random_snippet.vcf.png
protein_coding.chr21.bed.vcf.png
exons.chr21.bed.vcf.png	

first open both files and check if they are the same:
(day4-lunch) [~/cmdb-plot-vcfs $]open processed_pseudogene.chr21.bed.vcf.png
(day4-lunch) [~/cmdb-plot-vcfs $]open ./cache/processed_pseudogene.chr21.bed.vcf.png 

#1) cmp: This command is used to compare two files character by character.
#2) comm: This command is used to compare two sorted files.
#3) diff: This command is used to compare two files line by line.

(day4-lunch) [~/cmdb-plot-vcfs $]cmp processed_pseudogene.chr21.bed.vcf.png ./cache/processed_pseudogene.chr21.bed.vcf.png 
processed_pseudogene.chr21.bed.vcf.png ./cache/processed_pseudogene.chr21.bed.vcf.png differ: char 73, line 3

(day4-lunch) [~/cmdb-plot-vcfs $]less -S processed_pseudogene.chr21.bed.vcf.png
"processed_pseudogene.chr21.bed.vcf.png" may be a binary file.  See it anyway? 
(day4-lunch) [~/cmdb-plot-vcfs $]less -S ./cache/processed_pseudogene.chr21.bed.vcf.png 
"./cache/processed_pseudogene.chr21.bed.vcf.png" may be a binary file.  See it anyway? 
The only difference was on line 3 matplotlib version was 3.5.1 for me while in cache the matplotlib version was 3.5.3
So the same plots.

(day4-lunch) [~/cmdb-plot-vcfs $]less -S gencode.v41.annotation.gtf 
Other types of genetypes are: 
transcribed_unprocessed_pseudogene
unprocessed_pseudogene
miRNA
lncRNA
snRNA
protein_coding
There must be more but I need to parse (bc there are too many info in one column seperated by tabs) and sort and unique-c to find all types of genetypes.
I find miRNA lncRNA and snRNA interesting because they are RNA with specialized functions.

exercise 2

In plot_vcf_ac.py, after ax.hist( ac, density=True ), add
plt.yscale('log')
ax.title.set_text('Log scale Frequency of Allele Count')
ax.set_ylabel("Log 10 Number of Occurences")
ax.set_xlabel("Allele Count")

Save and run do_all.sh



In subset_regions.sh, added lncRNA
for TYPE in protein_coding processed_pseudogene lncRNA

Save and run do_all.sh

exercise 3

Synopsis – <50 words
Usage – syntax including input file requirements
Dependencies – software requirements
Description – how it works (bullet points or prose)
Output – example output

 SYNOPSIS
     bxlab/cmdb-plot-vcfs -- 
	 Plots histogram of log10 scaled allele count from vcf file, using the specific gene types extracted from gtf file
	 

 USAGE
     bash do_all.sh <file1.vcf> <file2.gtf>

Dependencies
bedtools                  2.30.0               h0e31d98_3    bioconda
blas                      1.0                         mkl    anaconda
brotli                    1.0.9                hb1e8313_2    anaconda
bzip2                     1.0.8                h1de35cc_0    anaconda
ca-certificates           2022.4.26            hecd8cb5_0    anaconda
certifi                   2022.6.15       py310hecd8cb5_0    anaconda
cycler                    0.11.0             pyhd3eb1b0_0    anaconda
fonttools                 4.25.0             pyhd3eb1b0_0    anaconda
freetype                  2.11.0               hd8bbffd_0    anaconda
giflib                    5.2.1                haf1e3a3_0    anaconda
intel-openmp              2021.4.0          hecd8cb5_3538    anaconda
jpeg                      9e                   hca72f7f_0    anaconda
kiwisolver                1.4.2           py310he9d5cce_0    anaconda
lcms2                     2.12                 hf1fd2bf_0    anaconda
libcxx                    14.0.6               hccf4f1f_0    conda-forge
libffi                    3.3                  hb1e8313_2    anaconda
libpng                    1.6.37               ha441bb4_0    anaconda
libtiff                   4.2.0                hdb42f99_1    anaconda
libwebp                   1.2.2                h56c3ce4_0    anaconda
libwebp-base              1.2.2                hca72f7f_0    anaconda
libzlib                   1.2.12               hfe4f2af_2    conda-forge
lz4-c                     1.9.3                h23ab428_1    anaconda
matplotlib                3.5.1           py310hecd8cb5_1    anaconda
matplotlib-base           3.5.1           py310hfb0c5b7_1    anaconda
mkl                       2021.4.0           hecd8cb5_637    anaconda
mkl-service               2.4.0           py310hca72f7f_0    anaconda
mkl_fft                   1.3.1           py310hf879493_0    anaconda
mkl_random                1.2.2           py310hc081a56_0    anaconda
munkres                   1.1.4                      py_0    anaconda
ncurses                   6.3                  hca72f7f_2    anaconda
numpy                     1.22.3          py310hdcd3fac_0    anaconda
numpy-base                1.22.3          py310hfd2de13_0    anaconda
openssl                   1.1.1o               hca72f7f_0    anaconda
packaging                 21.3               pyhd3eb1b0_0    anaconda
pillow                    9.0.1           py310hde71d04_0    anaconda
pip                       21.2.4          py310hecd8cb5_0    anaconda
pyparsing                 3.0.4              pyhd3eb1b0_0    anaconda
python                    3.10.4               hdfd78df_0    anaconda
python-dateutil           2.8.2              pyhd3eb1b0_0    anaconda
readline                  8.1.2                hca72f7f_1    anaconda
setuptools                61.2.0          py310hecd8cb5_0    anaconda
six                       1.16.0             pyhd3eb1b0_1    anaconda
sqlite                    3.38.5               h707629a_0    anaconda
tk                        8.6.12               h5d9f67b_0    anaconda
tornado                   6.1             py310hca72f7f_0    anaconda
tzdata                    2022a                hda174b7_0    anaconda
wheel                     0.37.1             pyhd3eb1b0_0    anaconda
xz                        5.2.5                hca72f7f_1    anaconda
zlib                      1.2.12               h4dc903c_2    anaconda
zstd                      1.5.2                hcb37349_0    anaconda

Specifically, we have installed:
matplotlib
bedtools
python
bash
sys
awk

 DESCRIPTION
     1. Create .bed files for features of interest
         - Run subset_regions.sh Bash script
         - Use grep to extract Chromosome 21 from gtf file to create subset gtf file
		 - Use grep to extract name, position start, position end of the specific gene_type (protein_coding processed_pseudogene and lncRNA) from the subset gft file to create bed file
	2. Subset .vcf for each feature
	     - Run do_all.sh
		 - Use bedtools to sort and intersect the vcf file and bed file based on gene type, and save as a vcf file
	3. Create histogram plots of Allele count for each .vcf
		- Run plot_vcf_ac.py
		- Grab the info column and split by ";" and remove "AC="
		- Appends all into a list
		- Use the data to create a log 10 scaled histogram with labels and title
		- Saves as png files

Output
*** Creating .bed files for features of interest
--- Creating protein_coding.chr21.bed
--- Creating processed_pseudogene.chr21.bed
--- Creating lncRNA.chr21.bed
--- Creating exons.chr21.bed
*** Subsetting .vcf for each feature
--- Subsetting exons.chr21.bed.vcf
    + Covering 1107407 bp
--- Subsetting lncRNA.chr21.bed.vcf
    + Covering 8663528 bp
--- Subsetting processed_pseudogene.chr21.bed.vcf
    + Covering 956640 bp
--- Subsetting protein_coding.chr21.bed.vcf
    + Covering 13780687 bp
*** Plotting AC for each .vcf
--- Plotting AC for exons.chr21.bed.vcf
--- Plotting AC for lncRNA.chr21.bed.vcf
--- Plotting AC for processed_pseudogene.chr21.bed.vcf
--- Plotting AC for protein_coding.chr21.bed.vcf
--- Plotting AC for random_snippet.vcf


	 
	 take gene_type of protein_coding processed_pseudogene and lncRNA of Chromosome 21 from gtf file and save into bed file
	 using bedtools to intersect 
	 subset into vcf files taking allele counts













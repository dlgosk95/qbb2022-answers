(base) [~/qbb2022-answers/week3-homework $]bwa mem -R "@RG\tID:A01_09\tSM:A01_09" -o A01_09.sam sacCer3.fa A01_09.fastq 

for SAMPLE in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_62
do
	bwa mem \
	-R "@RG\tID:${SAMPLE}\tSM:${SAMPLE}" \
	-t 4 \
	-o ${SAMPLE}.sam \
	sacCer3.fa ${SAMPLE}.fastq
done

for SAMPLE in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_62
do
	samtools sort -@4 -O bam -o ${SAMPLE}.bam ${SAMPLE}.sam
done

for SAMPLE in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_62
do
	samtools index -b ${SAMPLE}.bam
done

(base) [~/qbb2022-answers/week3-homework $]ls A01_*.bam > bam.txt

freebayes --genotype-qualities -f sacCer3.fa \
-L bam.txt -p1 > sacCer3.vcf

vcffilter -f "QUAL > 20" sacCer3.vcf > sac_qual.vcf

vcfallelicprimitives -k -g sac_qual.vcf > sac_decompose.vcf
We suggest using the -k and -g flags to keep annotations for the variant sites and sample genotypes in your VCF.

ls -l .

conda install snpeff=5.0 -y
snpeff download R64-1-1.99

snpeff ann --help | less -S

(base) [~/qbb2022-answers/week3-homework $]snpeff ann R64-1-1.99 sac_decompose.vcf > sac_predict.vcf

The read depth distribution of variant genotypes (histogram)
FORMAT=<ID=DP,Number=1,Type=Integer,Description="Read Depth">





(base) [~/qbb2022-answers/week3-homework $]ls
-L			A01_23.bam		A01_27.bam.bai		A01_35.fastq		A01_62.sam		readme.md		sac_decompose.vcf
A01_09.bam		A01_23.bam.bai		A01_27.fastq		A01_35.sam		A01_63.fastq		sacCer3.fa		sac_predict.vcf
A01_09.bam.bai		A01_23.fastq		A01_27.sam		A01_39.bam		BYxRM.tar.gz		sacCer3.fa.amb		sac_qual.vcf
A01_09.fastq		A01_23.sam		A01_31.bam		A01_39.bam.bai		__pycache__		sacCer3.fa.ann		snpEff_genes.txt
A01_09.sam		A01_24.bam		A01_31.bam.bai		A01_39.fastq		assignment.py		sacCer3.fa.bwt		snpEff_summary.html
A01_11.bam		A01_24.bam.bai		A01_31.fastq		A01_39.sam		bam.txt			sacCer3.fa.fai		vcfParser.py
A01_11.bam.bai		A01_24.fastq		A01_31.sam		A01_62.bam		livecoding		sacCer3.fa.pac
A01_11.fastq		A01_24.sam		A01_35.bam		A01_62.bam.bai		livecoding.tar.gz	sacCer3.fa.sa
A01_11.sam		A01_27.bam		A01_35.bam.bai		A01_62.fastq		parsed.txt		sacCer3.vcf
# qbb 2022 day 1 homework

Exercise 1
```
#!/bin/bash
#USAGE: bash exercise1.sh input_VCF

vcffile=$1

for nuc in A C G T
do
  echo "Considering " $nuc 
  awk -v nuc="$nuc" '/^#/{next} {if ($4 == nuc) {print $5}}' $vcffile | sort | uniq -c
done
```

```
(base) [~/qbb2022-answers/day1-homework $]bash exercise1.sh ~/data/vcf_files/random_snippet.vcf
Considering  A
 354 C
1315 G
 358 T
Considering  C
 484 A
 384 G
2113 T
Considering  G
2041 A
 405 C
 485 T
Considering  T
 358 A
1317 C
 386 G
```
Do the results make sense given what you know about the biology of these bases?
Wikipedia says:
Transition, in genetics and molecular biology, refers to a point mutation that changes a purine nucleotide to another purine (A ↔ G), or a pyrimidine nucleotide to another pyrimidine (C ↔ T). Approximately two out of three single nucleotide polymorphisms (SNPs) are transitions.

So this is an example of transition!

Exercise 2

Using this segmentation, do promoters appear to be clearly and objectively defined?
No promoter parts are not clear. I assume promoters to be including and upstream of TSS. 
 
```
(base) [~/qbb2022-answers/day1-homework $]awk '{if ($4 == 1 || $4 == 2 || $4 == 3) {print}}' ~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed > promoter.bed

(base) [~/qbb2022-answers/day1-homework $]bedtools intersect -a $vcffile -b $promoter -wa > intersect.vcf

(base) [~/qbb2022-answers/day1-homework $]awk '{if ($4 == "C") {print ($5)}}' ~/qbb2022-answers/day1-homework/intersect.vcf | sort | uniq -c > Cytosine.txt

(base) [~/qbb2022-answers/day1-homework $]head Cytosine.txt 
  12 A
  11 G
  41 T
```

Finally, do the observed results lead you to any biological observations, hypotheses, or conclusions?
Pyrimidine (C) is exchanged with pyrimidine (T) the most: this is an example of transition as mentioned above. It is possibly due to their similar size, structure and molecular mechanisms to generate them.
Transition vs Transversion

Exercise 3

```
 #!/bin/bash

 #USAGE: bash exercise3.sh input_VCF

awk '/^#/{next} {print $1,$2-1, $2}' $1 > variants.bed
 #if the beggining starts with #, skip
 #print column 1 (begi, result of column2-1 (size), and column2 (end)
 #export as variants.bed
 
sort -k1,1 -k2,2n ~/data/bed_files/genes.bed >  genes.sorted.bed
 #from ~/data/bed_files/genes.bed
 #sort column 1 (end at column 1)
 #and sort column 2 (end at column 2) numerically not alphabetically
 #export as genes.sorted.bed

bedtools closest -a variants.bed -b genes.sorted.bed
 #use bedtools to find sorted genes that intersect or be closest to the variant
```

Error: unable to open file or unable to determine types for file
The error because variants.bed file format is delimited by space but it must be tab.

```
awk '/^#/{next} {print $1"\t"$2-1"\t"$2}' $1 > variants.bed
```

Error: Sorted input specified, but the file variants.bed has the following out of order record
It ran into the error while running because the previous file (variants.bed) is not sorted (out of order) and for some technical reason (Why??) it needs to be sorted first

```
awk '/^#/{next} {print $1"\t"$2-1"\t"$2}' $1 > variants.bed
sort -k1,1 -k2,2n variants.bed > variants.sorted.bed
sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed
bedtools closest -a variants.sorted.bed -b genes.sorted.bed > closest.bed
```

```
(base) [~/qbb2022-answers/day1-homework $]wc -l closest.bed 
10293 closest.bed
```

which is variants

```
sort -k7 closest.bed | cut -f 7 | uniq -c | wc -l
200
```

which is genes
the average is 10293/200
(base) [~/qbb2022-answers/week14-homework/metagenomics_data/Krona/KronaTools $]python assignment.py ../../step0_givendata/KRAKEN/SRR492197.kraken SRR492197
Repeated to all files
or 
for sample in SRR492183.kraken SRR492188.kraken SRR492190.kraken SRR492194.kraken SRR492186.kraken SRR492189.kraken SRR492193.kraken SRR492197.kraken
do
...
done

(base) [~/qbb2022-answers/week14-homework/metagenomics_data/Krona/KronaTools $]ktImportText -q SRR492183_krona.txt 
Writing text.krona.html...
(base) [~/qbb2022-answers/week14-homework/metagenomics_data/Krona/KronaTools $]ktImportText -q SRR492186_krona.txt
Writing text.krona.html...
(base) [~/qbb2022-answers/week14-homework/metagenomics_data/Krona/KronaTools $]ktImportText -q SRR492188_krona.txt
Writing text.krona.html...
(base) [~/qbb2022-answers/week14-homework/metagenomics_data/Krona/KronaTools $]ktImportText -q SRR492189_krona.txt
Writing text.krona.html...
(base) [~/qbb2022-answers/week14-homework/metagenomics_data/Krona/KronaTools $]ktImportText -q SRR492190_krona.txt
Writing text.krona.html...
(base) [~/qbb2022-answers/week14-homework/metagenomics_data/Krona/KronaTools $]ktImportText -q SRR492193_krona.txt
Writing text.krona.html...
(base) [~/qbb2022-answers/week14-homework/metagenomics_data/Krona/KronaTools $]ktImportText -q SRR492194_krona.txt
Writing text.krona.html...
(base) [~/qbb2022-answers/week14-homework/metagenomics_data/Krona/KronaTools $]ktImportText -q SRR492197_krona.txt
Writing text.krona.html...

or
for sample in SRR492183_krona.txt SRR492186_krona.txt SRR492188_krona.txt SRR492189_krona.txt SRR492190_krona.txt SRR492193_krona.txt SRR492194_krona.txt SRR492197_krona.txt
do
...
done

moved to day 1 ~ day 8 folders

Question 1: In your README, briefly comment on the trends you see in the gut microbiota throughout the first week.

Day 1: noticeable virus content; actinobacteria which disappears the next day
Day 2~4: less virus content; mostly lactobacillales and some bacillales
Day 5: slightly increased bacillales
Day 6: noticeable virus content; actinobacteria appears
Day 7: less virus content; increased bacillales
Day 8: decreased bacillales; largely increased actinobacteria

Question 2: In your README, comment on what metrics in the contigs could we use to group them together?
Overlaps of base or taxonomical knowledge


(base) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]bwa index assembly.fasta 

(base) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]bwa mem -t4 assembly.fasta ./READS/SRR492183_1.fastq ./READS/SRR492183_2.fastq > SRR492183.sam
(base) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]bwa mem -t4 assembly.fasta ./READS/SRR492186_1.fastq ./READS/SRR492186_2.fastq > SRR492186.sam
(base) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]bwa mem -t4 assembly.fasta ./READS/SRR492188_1.fastq ./READS/SRR492188_2.fastq > SRR492188.sam
(base) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]bwa mem -t4 assembly.fasta ./READS/SRR492189_1.fastq ./READS/SRR492189_2.fastq > SRR492189.sam
(base) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]bwa mem -t4 assembly.fasta ./READS/SRR492190_1.fastq ./READS/SRR492190_2.fastq > SRR492190.sam
(base) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]bwa mem -t4 assembly.fasta ./READS/SRR492193_1.fastq ./READS/SRR492193_2.fastq > SRR492193.sam
(base) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]bwa mem -t4 assembly.fasta ./READS/SRR492194_1.fastq ./READS/SRR492194_2.fastq > SRR492194.sam
(base) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]bwa mem -t4 assembly.fasta ./READS/SRR492197_1.fastq ./READS/SRR492197_2.fastq > SRR492197.sam

(base) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]samtools sort SRR492183.sam -o sorted_SRR492183.bam 
(base) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]samtools sort SRR492186.sam -o sorted_SRR492186.bam 
(base) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]samtools sort SRR492188.sam -o sorted_SRR492188.bam 
(base) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]samtools sort SRR492189.sam -o sorted_SRR492189.bam 
(base) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]samtools sort SRR492190.sam -o sorted_SRR492190.bam 
(base) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]samtools sort SRR492193.sam -o sorted_SRR492193.bam 
(base) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]samtools sort SRR492194.sam -o sorted_SRR492194.bam 
(base) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]samtools sort SRR492197.sam -o sorted_SRR492197.bam 

##Wrong; did them separately
<!-- (metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]jgi_summarize_bam_contig_depths --outputDepth depth.txt sorted_SRR492183.bam
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]metabat2 -i assembly.fasta -a depth.txt -o bins_dir/bin
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]jgi_summarize_bam_contig_depths --outputDepth depth.txt sorted_SRR492186.bam
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]metabat2 -i assembly.fasta -a depth.txt -o bins_dir/bin
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]jgi_summarize_bam_contig_depths --outputDepth depth.txt sorted_SRR492188.bam
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]metabat2 -i assembly.fasta -a depth.txt -o bins_dir/bin
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]jgi_summarize_bam_contig_depths --outputDepth depth.txt sorted_SRR492189.bam
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]metabat2 -i assembly.fasta -a depth.txt -o bins_dir/bin
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]jgi_summarize_bam_contig_depths --outputDepth depth.txt sorted_SRR492190.bam
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]metabat2 -i assembly.fasta -a depth.txt -o bins_dir/bin
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]jgi_summarize_bam_contig_depths --outputDepth depth.txt sorted_SRR492193.bam
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]metabat2 -i assembly.fasta -a depth.txt -o bins_dir/bin
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]jgi_summarize_bam_contig_depths --outputDepth depth.txt sorted_SRR492194.bam
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]metabat2 -i assembly.fasta -a depth.txt -o bins_dir/bin
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]jgi_summarize_bam_contig_depths --outputDepth depth.txt sorted_SRR492197.bam
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]metabat2 -i assembly.fasta -a depth.txt -o bins_dir/bin

Question 3A: In your README, answer: How many bins did you get?
4 bins, 2, 3, 3, 2, 5, 3, 6

Question 3B: In your README, comment on roughly what percentage of the assembly do they represent?

(Hint: You can see how many and which contigs are in each bin fasta file by grepping for a >, which starts each identification line. Use a pipe and some downstream unix command or python parsing for counting, etc.)

For example, only bin 1, (12+17+86+6)/4104*100=2.95%

Question 3C: In your README, comment on whether you think the sizes of each bin look about right, based on what you know about the size of prokaryotic genomes?
Most prokaryotic genomes are less than 5 Mb in size, which is what I see in the file sizes.

Question 3D:In your README, describe how you might estimate how complete and how contaminated each bin is?

(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]grep '>'  assembly.fasta | wc -l
    4103

(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/83/bins_dir $]grep '>'  bin.1.fa | wc -l
      12
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/83/bins_dir $]grep '>'  bin.2.fa | wc -l
      17
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/83/bins_dir $]grep '>'  bin.3.fa | wc -l
      86
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/83/bins_dir $]grep '>'  bin.4.fa | wc -l
       6
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/86/bins_dir $]grep '>'  bin.1.fa | wc -l
     100
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/86/bins_dir $]grep '>'  bin.2.fa | wc -l
       6
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/88/bins_dir $]grep '>'  bin.1.fa | wc -l
       3
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/88/bins_dir $]grep '>'  bin.2.fa | wc -l
       3
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/88/bins_dir $]grep '>'  bin.3.fa | wc -l
      88
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/89/bins_dir $]grep '>'  bin.1.fa | wc -l
      96
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/89/bins_dir $]grep '>'  bin.2.fa | wc -l
       3
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/89/bins_dir $]grep '>'  bin.3.fa | wc -l
       3
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/90/bins_dir $]grep '>'  bin.1.fa | wc -l
       6
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/90/bins_dir $]grep '>'  bin.2.fa | wc -l
      80
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/93/bins_dir $]grep '>'  bin.1.fa | wc -l
      88
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/93/bins_dir $]grep '>'  bin.2.fa | wc -l
      40
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/93/bins_dir $]grep '>'  bin.3.fa | wc -l
       3
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/93/bins_dir $]grep '>'  bin.4.fa | wc -l
       3
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/93/bins_dir $]grep '>'  bin.5.fa | wc -l
      10
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/94/bins_dir $]grep '>'  bin.1.fa | wc -l
     141
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/94/bins_dir $]grep '>'  bin.2.fa | wc -l
      12
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/94/bins_dir $]grep '>'  bin.3.fa | wc -l
       6
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/97/bins_dir $]grep '>'  bin.1.fa | wc -l
       8
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/97/bins_dir $]grep '>'  bin.2.fa | wc -l
      50
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/97/bins_dir $]grep '>'  bin.3.fa | wc -l
      88
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/97/bins_dir $]grep '>'  bin.4.fa | wc -l
       3
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/97/bins_dir $]grep '>'  bin.5.fa | wc -l
      12
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/97/bins_dir $]grep '>'  bin.6.fa | wc -l
       3

(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/83/bins_dir $]ls -l
total 15712
-rw-r--r--  1 cmdb  staff  2518697 16 Dec 07:40 bin.1.fa
-rw-r--r--  1 cmdb  staff   235740 16 Dec 07:40 bin.2.fa
-rw-r--r--  1 cmdb  staff  2372125 16 Dec 07:40 bin.3.fa
-rw-r--r--  1 cmdb  staff  2910800 16 Dec 07:40 bin.4.fa
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/86/bins_dir $]ls -l
total 10592
-rw-r--r--  1 cmdb  staff  2507051 16 Dec 07:01 bin.1.fa
-rw-r--r--  1 cmdb  staff  2910800 16 Dec 07:01 bin.2.fa
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/88/bins_dir $]ls -l
total 10504
-rw-r--r--  1 cmdb  staff  2260359 16 Dec 07:02 bin.1.fa
-rw-r--r--  1 cmdb  staff   650441 16 Dec 07:02 bin.2.fa
-rw-r--r--  1 cmdb  staff  2463055 16 Dec 07:02 bin.3.fa
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/89/bins_dir $]ls -l
total 10560
-rw-r--r--  1 cmdb  staff  2493334 16 Dec 07:03 bin.1.fa
-rw-r--r--  1 cmdb  staff  2260359 16 Dec 07:03 bin.2.fa
-rw-r--r--  1 cmdb  staff   650441 16 Dec 07:03 bin.3.fa
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/90/bins_dir $]ls -l
total 10280
-rw-r--r--  1 cmdb  staff  2910800 16 Dec 07:05 bin.1.fa
-rw-r--r--  1 cmdb  staff  2349498 16 Dec 07:05 bin.2.fa
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/93/bins_dir $]ls -l
total 16880
-rw-r--r--  1 cmdb  staff  2394708 16 Dec 07:06 bin.1.fa
-rw-r--r--  1 cmdb  staff  1310179 16 Dec 07:06 bin.2.fa
-rw-r--r--  1 cmdb  staff  2260359 16 Dec 07:06 bin.3.fa
-rw-r--r--  1 cmdb  staff   650441 16 Dec 07:06 bin.4.fa
-rw-r--r--  1 cmdb  staff  2021193 16 Dec 07:06 bin.5.fa
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/94/bins_dir $]ls -l
total 20528
-rw-r--r--  1 cmdb  staff  5078611 16 Dec 07:07 bin.1.fa
-rw-r--r--  1 cmdb  staff  2518697 16 Dec 07:07 bin.2.fa
-rw-r--r--  1 cmdb  staff  2910800 16 Dec 07:07 bin.3.fa
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/97/bins_dir $]ls -l
total 23792
-rw-r--r--  1 cmdb  staff  1683938 16 Dec 07:07 bin.1.fa
-rw-r--r--  1 cmdb  staff  1573186 16 Dec 07:07 bin.2.fa
-rw-r--r--  1 cmdb  staff  3484410 16 Dec 07:07 bin.3.fa
-rw-r--r--  1 cmdb  staff   650441 16 Dec 07:07 bin.4.fa
-rw-r--r--  1 cmdb  staff  2518697 16 Dec 07:07 bin.5.fa
-rw-r--r--  1 cmdb  staff  2260359 16 Dec 07:07 bin.6.fa -->





Question 3A: In your README, answer: How many bins did you get?
6 bins

Question 3B: In your README, comment on roughly what percentage of the assembly do they represent?

(Hint: You can see how many and which contigs are in each bin fasta file by grepping for a >, which starts each identification line. Use a pipe and some downstream unix command or python parsing for counting, etc.)

For each bin, 55/4103=1.23%, 78/4301, 8/4301, 37/4301, 13/4301, 6/4301

Question 3C: In your README, comment on whether you think the sizes of each bin look about right, based on what you know about the size of prokaryotic genomes?
Most prokaryotic genomes are less than 5 Mb in size, which are what I see with ls -l

Question 3D:In your README, describe how you might estimate how complete and how contaminated each bin is?
Blast against predicted taxa

(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]jgi_summarize_bam_contig_depths --outputDepth depth.txt sorted_SRR492183.bam sorted_SRR492186.bam sorted_SRR492188.bam sorted_SRR492189.bam sorted_SRR492190.bam sorted_SRR492193.bam sorted_SRR492194.bam sorted_SRR492197.bam 
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]metabat2 -i assembly.fasta -a depth.txt -o bins_dir/bin

(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]grep '>'  assembly.fasta | wc -l
    4103
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]grep '>'  ./bins_dir/bin.1.fa | wc -l
      55
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]grep '>'  ./bins_dir/bin.2.fa | wc -l
      78
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]grep '>'  ./bins_dir/bin.3.fa | wc -l
       8
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]grep '>'  ./bins_dir/bin.4.fa | wc -l
      37
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]grep '>'  ./bins_dir/bin.5.fa | wc -l
      13
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]grep '>'  ./bins_dir/bin.6.fa | wc -l
       6
(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata $]ls -l ./bins_dir/
total 26224
-rw-r--r--  1 cmdb  staff  2752195 16 Dec 09:40 bin.1.fa
-rw-r--r--  1 cmdb  staff  2292366 16 Dec 09:40 bin.2.fa
-rw-r--r--  1 cmdb  staff  1683938 16 Dec 09:40 bin.3.fa
-rw-r--r--  1 cmdb  staff  1249747 16 Dec 09:40 bin.4.fa
-rw-r--r--  1 cmdb  staff  2525551 16 Dec 09:40 bin.5.fa
-rw-r--r--  1 cmdb  staff  2910800 16 Dec 09:40 bin.6.fa


Question 4: 
(A) Within your README, record your predictions for each bin?
Bin 1 Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus aureus
Bin 2 Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus epidermidis
Bin 3 Firmicutes;Tissierellia or Clostridia???
2 Clostridiaceae
5 Peptoniphilaceae
1 Streptococcaceae
Bin 4 Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus haemolyticus
Bin 5 Actinobacteria;Propionibacteriales;Propionibacteriaceae;Cutibacterium;Cutibacterium avidum;Cutibacterium avidum 44067
Bin 6 Firmicutes;Bacilli;Lactobacillales;Enterococcaceae;Enterococcus;Enterococcus faecalis
(B) This approach to classification is fast, but not very quantitative. Within your README, propose one method to more robustly infer the taxonomy of a metagenomic bin.







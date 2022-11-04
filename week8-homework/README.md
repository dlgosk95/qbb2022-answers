What does "phase" mean?
haplotagging, assigning haplotypes to each variants for each individual
ex. 0/1 -> 0|1

Do you expect each region in H1 or H2 to correspond to the same parent of origin (i.e. the same haplotype)? Explain your reasoning?
We tried to assign haplotypes (group variants into two chromosomes of hopefully same parental origin) based on overlaps within chromosome but there is no overlap between chromosomes.
Therefore I do not expect each region to correspond to the same parent of origin

Part 1 

    -i  input bam of reads aligned to ref. Read groups are currently ignored,
        so the bam should only contain reads from a single sample.
    -s  medaka model for initial SNP calling from mixed reads prior to phasing,
        (default: r941_prom_snp_g360).
    -m  medaka model for final variant calling from phased reads,
        (default: r941_prom_variant_g360).
    -p  output phased vcf.
    -r  region string(s). If providing multiple regions, wrap them in quotes.
        If not provided, will process all contigs in bam. 
    -o  output folder (default: medaka_variant).
medaka_variant [-h] -i <bam>
Only one region can be specified for Medaka at a time so you will need to generate a phased vcf file for each region in regions.bed using the format chr:start-end to specify the region.
4 regions
chr11	1900000	2800000
chr14	100700000	100990000
chr15	23600000	25900000
chr20	58800000	58912000
Reads for four regions have been extracted along with their corresponding methylation calls. If you look at the entries in the bam file, you will see that there is an additional pair of tags, MM and ML, followed by a series of comma-separated numbers. These values are the base counts between methylated bases and methylation call probabilities, respectively.

medaka_variant -i methylation.bam -f hg38.fa -p -r [a region from regions.bed] -o [your preferred output folder] 
medaka_variant -i methylation.bam -f hg38.fa -p -r chr11:1900000-2800000 -o ./chr11
medaka_variant -i methylation.bam -f hg38.fa -p -r chr14:100700000-100990000 -o ./chr14
medaka_variant -i methylation.bam -f hg38.fa -p -r chr15:23600000-25900000 -o ./chr15
medaka_variant -i methylation.bam -f hg38.fa -p -r chr20:58800000-58912000 -o ./chr20
chr:start-end


Part 2 

whatshap haplotag -o haplotagged.bam --reference reference.fasta phased.vcf.gz alignments.bam
(medaka) [~/qbb2022-answers/week8-homework $]whatshap haplotag --help
usage: whatshap haplotag [-h] [-o OUTPUT] [--reference FASTA]
                         [--regions REGION] [--ignore-linked-read]
                         [--linked-read-distance-cutoff LINKEDREADDISTANCE]
                         [--ignore-read-groups] [--sample SAMPLE]
                         [--output-haplotag-list HAPLOTAG_LIST]
                         [--tag-supplementary]
                         VCF ALIGNMENTS

Tag reads by haplotype

Sequencing reads are read from file ALIGNMENTS (in BAM format) and tagged reads
are written to stdout.

positional arguments:
  VCF                   VCF file with phased variants (must be gzip-compressed
                        and indexed)
  ALIGNMENTS            File (BAM/CRAM) with read alignments to be tagged by
                        haplotype

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file. If omitted, use standard output.
  --reference FASTA, -r FASTA
                        Reference file. Provide this to detect alleles through
                        re-alignment. If no index (.fai) exists, it will be
                        created
  --regions REGION      Specify region(s) of interest to limit the tagging to
                        reads/variants overlapping those regions. You can
                        specify a space-separated list of regions in the form
                        of chrom:start-end, chrom (consider entire
                        chromosome), or chrom:start (consider region from this
                        start to end of chromosome).
  --ignore-linked-read  Ignore linkage information stored in BX tags of the
                        reads.
  --linked-read-distance-cutoff LINKEDREADDISTANCE, -d LINKEDREADDISTANCE
                        Assume reads with identical BX tags belong to
                        different read clouds if their distance is larger than
                        LINKEDREADDISTANCE (default: 50000).
  --ignore-read-groups  Ignore read groups in BAM/CRAM header and assume all
                        reads come from the same sample.
  --sample SAMPLE       Name of a sample to phase. If not given, all samples
                        in the input VCF are phased. Can be used multiple
                        times.
  --output-haplotag-list HAPLOTAG_LIST
                        Write assignments of read names to haplotypes (tab
                        separated) to given output file. If filename ends in
                        .gz, then output is gzipped.
  --tag-supplementary   Also tag supplementary alignments. Supplementary
                        alignments are assigned to the same haplotype the
                        primary alignment has been assigned to (default: only
                        tag primary alignments).
For the methylation.bam file, you want the original file because you’re tagging and going to split the original reads from the original bam file
chr:start:end
whatshap haplotag -o chr11_hap.bam --reference hg38.fa --regions chr11:1900000:2800000 --output-haplotag-list chr11_haplist.tsv ./chr11/round_0_hap_mixed_phased.vcf.gz methylation.bam
whatshap haplotag -o chr14_hap.bam --reference hg38.fa --regions chr14:100700000:100990000 --output-haplotag-list chr14_haplist.tsv ./chr14/round_0_hap_mixed_phased.vcf.gz methylation.bam
whatshap haplotag -o chr15_hap.bam --reference hg38.fa --regions chr15:23600000:25900000 --output-haplotag-list chr15_haplist.tsv ./chr15/round_0_hap_mixed_phased.vcf.gz methylation.bam
whatshap haplotag -o chr20_hap.bam --reference hg38.fa --regions chr20:58800000:58912000 --output-haplotag-list chr20_haplist.tsv ./chr20/round_0_hap_mixed_phased.vcf.gz methylation.bam


Part 3 

Once you have tagged the reads, you will need to split the bam file into two bam files, one for each haplotype. 
(medaka) [~/qbb2022-answers/week8-homework $]whatshap split --help
usage: whatshap split [-h] [--output-h1 OUTPUT_H1] [--output-h2 OUTPUT_H2]
                      [--output-untagged OUTPUT_UNTAGGED] [--add-untagged]
                      [--only-largest-block] [--discard-unknown-reads]
                      [--read-lengths-histogram READ_LENGTHS_HISTOGRAM]
                      READS LIST

Split reads by haplotype.

Reads FASTQ/BAM file and a list of haplotype assignments (such as generated by
whatshap haplotag --output-haplotag-list). Outputs one FASTQ/BAM per haplotype.
BAM mode is intended for unmapped BAMs (such as provided by PacBio).

positional arguments:
  READS                 Input FASTQ/BAM file with reads (FASTQ can be gzipped)
  LIST                  Tab-separated list with (at least) two columns
                        <readname> and <haplotype> (can be gzipped).
                        Currently, the two haplotypes have to be named H1 and
                        H2 (or none). Alternatively, the output of the
                        "haplotag" command can be used (4 columns), and this
                        is required for using the "--only-largest-block"
                        option (need phaseset and chromosome info).

optional arguments:
  -h, --help            show this help message and exit
  --output-h1 OUTPUT_H1
                        Output file to write reads from Haplotype 1 to. Use
                        ending .gz to create gzipped file.
  --output-h2 OUTPUT_H2
                        Output file to write reads from Haplotype 2 to. Use
                        ending .gz to create gzipped file.
  --output-untagged OUTPUT_UNTAGGED
                        Output file to write untagged reads to. Use ending .gz
                        to create gzipped file.
  --add-untagged        Add reads without tag to both H1 and H2 output
                        streams.
  --only-largest-block  Only consider reads to be tagged if they belong to the
                        largest phased block (in terms of read count) on their
                        respective chromosome
  --discard-unknown-reads
                        Only check the haplotype of reads listed in the
                        haplotag list file. Reads (read names) not contained
                        in this file will be discarded. In the default case (=
                        keep unknown reads), those reads would be considered
                        untagged and end up in the respective output file.
                        Please be sure that the read names match between the
                        input FASTQ/BAM and the haplotag list file.
  --read-lengths-histogram READ_LENGTHS_HISTOGRAM
                        Output file to write read lengths histogram to in tab
                        separated format.

whatshap split --output-h1 chr11_h1.bam --output-h2 chr11_h2.bam chr11_hap.bam chr11_haplist.tsv
whatshap split --output-h1 chr14_h1.bam --output-h2 chr14_h2.bam chr14_hap.bam chr14_haplist.tsv
whatshap split --output-h1 chr15_h1.bam --output-h2 chr15_h2.bam chr15_hap.bam chr15_haplist.tsv
whatshap split --output-h1 chr20_h1.bam --output-h2 chr20_h2.bam chr20_hap.bam chr20_haplist.tsv

You’ll use chr11_hap.bam this time since whatshap haplotag output that one and it was given methylation.bam (the original reads)
the new bam file has tags for the reads saying which haplotype they’re from, so it’s built off of the original bam file, but has new info that split wants

For that, run the whatshap haplotag subcommand on your phased VCF file. It tags each read in a BAM file with HP:i:1 or HP:i:2 depending on which haplotype it belongs to, and also adds a PS tag that describes in which haplotype block the read is. With your aligned reads in alignments.bam, run

While you can complete the igv part of the assignment with the region- and haplotype-specific bam files, it is easy to concatenate them into one bam file per haplotype using

samtools cat -o h1_cat.bam chr11_h1.bam chr14_h1.bam chr15_h1.bam chr20_h1.bam
samtools cat -o h2_cat.bam chr11_h2.bam chr14_h2.bam chr15_h2.bam chr20_h2.bam

samtools index h1_cat.bam
samtools index h2_cat.bam

samtools cat [-b list] [-h header.sam] [-o out.bam] in1.bam in2.bam
-b FOFN
Read the list of input BAM or CRAM files from FOFN. These are concatenated prior to any files specified on the command line. Multiple -b FOFN options may be specified to concatenate multiple lists of BAM/CRAM files.

-h FILE
Uses the SAM header from FILE. By default the header is taken from the first file to be concatenated.

-o FILE
Write the concatenated output to FILE. By default this is sent to stdout.

--no-PG
Do not add a @PG line to the header of the output file.

-@, --threads INT
Number of input/output compression threads to use in addition to main thread [0].


Part 4 

You will need to install a new version of IGV for this assignment as the functionality for viewing methylation data without reprocessing bam files was only recently added. To do this, you will be creating a new conda environment, cloning the IGV repo and building the application.

conda deactivate
conda create -n igv gradle openjdk=11 -y
conda activate igv
git clone https://github.com/igvteam/igv.git
Once you have cloned the repo, change into the igv directory and use the following command to build the program:

cd igv
./gradlew createDist
cd ../
This will create a new executable in the folder igv/build/IGV-dist/igv.sh. For convenience, I suggest creating a symlink (like an alias) in your homework directory.

ln -s ${PWD}/igv/build/IGV-dist/igv.sh ./
Now, when you want to start IGV, simply type ./igv.sh.

samtools index h1_cat.bam


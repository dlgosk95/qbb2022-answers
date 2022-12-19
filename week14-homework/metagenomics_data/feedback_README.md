Good work Hannah! I would recommend that you try to keep your README a little more organized just so it's easier to come back later and try to figure out what you did, but this is fine! A few comments:

1. For Step 1, It's not clear what the `...` mean in your for loops in your README, but I see the correct commands, so no points deducted
2. For Step 2, it looks like you have the right `jgi_summarize_bam_contig_depths` and `metabat2` commands, but you crossed them out! Just to clarify, you DO want to run the `jgi_summarize_bam_contig_depths` on all the bam files at once, and then run `metabat2` on the output of this command
3. Interesting strategy for finding the length of the contigs in the bins! This only works because characters take up about one byte, but you could be more careful by using `wc -l`.  Also, this will include the headers and new line characters (no points deducted)
4. For step 3:Your code and answer for 4A look great (nice work!) but I don't have your answer for 4b (-0.5 point)

Good work!

(9.5/10)

# Week 1 Genome Assembly -- Feedback

1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 10 points out of 10 possible points


1. Question 1.1, 1.4 how many reads (0.5 pts each)

  * great! --> +1

2. Question 1.2, 1.4 simulation script(s)

  * nice! Consider using a single script that accepts command line/user input or a function that you can pass generalized variables to rather than having repetitive code --> +1

3. Question 1.2, 1.4 plotting script(s)

  * nice! --> +1

4. Question 1.2, 1.4 histograms with overlaid Poisson distributions (0.5 pts each)

  * great plots overall! --> +1
  * consider adding titles or making the name of the plot more informative in order to distinguish the 5x from the 15x coverage.
  * Re your question in your README about the mismatch between the poisson and the histogram, you corrected that mismatch both by setting the number of bins and multiplying by a million when using the `poisson.pmf`. Very good

5. Question 1.3, 1.4 how much of genome not sequenced/comparison to Poisson expectations (0.5 pts each, 0.25 for answer and 0.25 for code)

  * very good --> +1

6. Question 2 De novo assembly (0.5 pts each, 0.25 for answer and 0.25 for code)

  * number of contigs --> +0.5
  * total length of contigs --> +0.5; Fantastic use of `awk`!

7. Question 2 De novo assembly cont (0.5 pts each, 0.25 for answer and 0.25 for code)

  * size of largest contig --> +0.5
  * contig n50 size --> +0.5; fantastic work and explanation!

8. whole genome alignment (0.33 pts each, 0.33/2 for answer and 0.33/2 for code)

  * average identity --> +0.33
  * length of longest alignment --> +0.33
  * how many insertions and deletions in assembly --> +0.33; Giving you full credit because I can see how you got to the answer you did, and you provide the output of the report. However, based on your displayed report, I'd say there were 5 deletions and 1 insertion in the query. Insertions in R are Deletions in Q. So we have 1 insertion in Q and 5 deletions in Q. This thought process is outlined [here](https://github.com/marbl/MUMmer3/blob/master/docs/dnadiff.README)

9. decoding the insertion (0.5 pts each, 0.25 for answer and 0.25 for code)

  * position of insertion in assembly --> +0.5
  * length of novel insertion --> +0.5

10. decoding the insertion cont (0.5 pts each, 0.25 for answer and 0.25 for code)

  * DNA sequence of encoded message --> +0.5
  * secret message --> +0.5

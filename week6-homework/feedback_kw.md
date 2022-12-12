## Week 6 -- 10 points possible

0 + 0 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 11 of 10 points possible

1. Given data question: What percentage of reads are valid interactions?

* Didn't see an answer to this question in the README

2. Given data question: What constitutes the majority of invalid 3C pairs?/What does it mean?

* Didn't see an answer to this question in the README

3. Script set up to (0.5 pts each)

  * read in data  
  * Filter data based on location  

4. Script set up to log transform the scores

  * you don't need to use a `for` loop for this, like the following. `data1['score'] = numpy.log(data1['score'])`. It applies the log to all the scores in the array/along the axis.

5. Script set up to shift the data by subtracting minimum value
  * what you have works
  * You can find the minimum without a for loop:
    `minimum1 = np.amin(data1['score'])`. It finds the minimum value in the whole array.
  * then you can subtract the minimum without a `for` loop: `data1['score'] -= minimum1`. It subtracts the minimum value from each of the scores in the array

6. Script set up to convert sparse data into square matrix

7. Script set up to (0.33 pts each)

  * remove distance dependent signal
  * smooth
  * subtract

  Overall, I like the code you used here, but you can do `empty3 = numpy.subtract(smooth_matrix(remove_dd_bg(empty2)), smooth_matrix(remove_dd_bg(empty1)))`. This will remove the distance dependent signal first for empty1 and empty2. This is called evaluating the inner function. Then the next outer function, smooth_matrix is applied on the result of removing the distance dependent signal. Finally, the most outer function, subtract is applied on the two smoothing results.

8. Turned in the plot of the 3 heatmaps (ddCTCF, dCTCF, and difference) for subset dataset (0.33 pts each ddCTCF/dCTCF/difference)

9. Turned in the plot of the 3 heatmaps (ddCTCF, dCTCF, and difference) for full dataset (0.33 pts each ddCTCF/dCTCF/difference)

10. Heatmap questions (0.33 pts each)

  * See the highlighted difference from the original figure?
  * impact of sequencing depth?
  * highlighted signal indicates?

Possible Bonus points:

1. Insulation script set up to (0.25 pts each)

  * read in data
  * filter data based on location
  * log transform the data
  * shift the data by subtracting minimum value

2. Insulation script set up to (0.5 pts each)

  * convert sparse data into square matrix
  * find the insulation score by taking mean of 5x5 squares of interactions around target

3. Turned in the plot of the heatmap + insulation scores below (0.5 pts each panel)

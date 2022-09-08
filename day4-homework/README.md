Part A 

numpy.arange(0.55, 1.05, 0.05)
means list of numbers starting from 0.55 increased by 0.05
so there would be 10 values in the list

numpy.around( ,decimals=2)
rounds to two decimal digits

HOWEVER, for this version of numpy it is not necessary to use numpy.around
print(numpy.arange(0.55, 1.05, 0.05))
[0.55 0.6  0.65 0.7  0.75 0.8  0.85 0.9  0.95 1.  ]

But it is a good practice for float because floats often result in rounding errors.

[::-1]
goes in opposite (decreasing) direction
[1.   0.95 0.9  0.85 0.8  0.75 0.7  0.65 0.6  0.55]


Part B 

```
(base) [~/qbb2022-answers/day4-homework $]python binomial_power_interactive_lecture.py 
```

```
def run_experiment(prob_heads, n_toss, n_iters = 100, seed = 389, correct_the_pvalues = False):
    '''
    Input: prob_heads, a float, the probability of a simulated coin toss returning heads
           n_toss, an integer, the number of coin tosses to simulate
           n_iters, an integer, the number of iterations for each simulation. default is 100
           seed, an integer, the random seed that you will set for the whole simulation experiment. default is 389
           correct_the_pvalues, a boolean, whether or not to perform multiple hypothesis testing correction
    Output: power, a float, the power of the experiment
    '''
    numpy.random.seed(seed)
    
    tosses = numpy.array([10, 50, 100, 250, 500, 1000])
    probs = numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)[::-1]
    power_matrix = numpy.zeros((10, 6))

    for i, p in enumerate(probs):
        for j, n in enumerate(tosses):
            pvals = [] 
            for k in range(n_iters):
                results_arr = simulate_coin_toss(n_toss, prob_heads = prob_heads)
                n_success = numpy.sum(results_arr)
                pvals.append(perform_hypothesis_test(n_success, n_toss))
            if correct_the_pvalues:
                pvals = correct_pvalues(pvals)
            pvals_translated_to_bools = interpret_pvalues(pvals)
            power = compute_power(numpy.sum(pvals_translated_to_bools), n_iters)
            power_matrix[i,j] = power
    return(power_matrix)

# or we can have power as function and make another function including toss and prob
```
If I print it:

[[0.85 0.75 0.83 0.77 0.86 0.85]
 [0.87 0.83 0.85 0.86 0.87 0.83]
 [0.83 0.86 0.78 0.82 0.84 0.86]
 [0.87 0.83 0.86 0.81 0.86 0.76]
 [0.84 0.76 0.8  0.82 0.81 0.82]
 [0.79 0.81 0.86 0.85 0.73 0.82]
 [0.86 0.82 0.86 0.84 0.84 0.86]
 [0.86 0.83 0.78 0.88 0.86 0.81]
 [0.85 0.84 0.85 0.85 0.84 0.81]
 [0.83 0.88 0.87 0.81 0.83 0.86]]


Part C 

```
(base) [~/qbb2022-answers/day4-homework $]python binomial_power_interactive_lecture.py 
correction1.png
no_correction1.png
```

```
def plot_heatmap(power_matrix, xticklabels, yticklabels, f_name):
    fig, ax = plt.subplots()
    sns.heatmap(power_matrix, vmin = 0, vmax = 1, xticklabels = xticklabels, yticklabels = yticklabels, ax = ax, cmap = color)
    #what is ax=ax doing? I can run the same without it.
    ax.set_xlabel('Number of Tosses')
    ax.set_ylabel('Probability of Heads')
    ax.title.set_text('Heatmap of Powers')
    #plt.show()
    fig.savefig(f_name)

tosses = numpy.array([10, 50, 100, 250, 500, 1000])
probs = numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)[::-1]
color = sns.color_palette("mako", as_cmap=True)



power1 = run_experiment(tosses, probs, correct_the_pvalues = True)
power2 = run_experiment(tosses, probs, correct_the_pvalues = False)
plot_heatmap(power1, tosses, probs, "correction1.png")
plot_heatmap(power2, tosses, probs, "no_correction1.png")
```

Trend : 
Lower the number of tosses, less power it has. Closer the probabiility to 0.5, less power.


Part D 

This study developed a quantitative method to test a transmission distortion (TD) of alleles in humans, in which a selfish allele is transmitted to next generation higher than the expected mandellian ratio. 

(Testing transmission distortion in humans remained as a challenge due to small size of human family and weak statistic power detecting weak TD.)

There are many common aspects between this study and today's homework exercise. First, they are both a heatmap testing the null hypothesis that the ratio of inheritance of two alleles are 50:50. Second, they both use binomial test and simulated dataset. Binomial test is performed when an experiment has two possible outcome with expected probability. They both show heatmaps with and without multiple testing correction(Bonferroni). The trends of heatmaps are also similar.  

The transmission rate axis would correspond to the probability of heads in our exercise.
The number of sperms would correspond to the number of tosses in our exercise. 
The number of simulation (n_iter) is 1000 in this figure while our homework exercise had 100 simulations.

0 power is a lot of false negatives.
the more data more power
corrected data required less number of tosses. increases p values to decrease number of false positive
more false negative because we are controlling decreasing the false positive. 
tradeoff
Power heatmap is good at determining what sample size is needed (min) to distinguish signal for a specific affect size of interest (like weak TD vs strong TD).
0.8 power standard

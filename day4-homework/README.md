numpy.arange(0.55, 1.05, 0.05)
means list of numbers starting from 0.55 increased by 0.05
so there would be 10 values in the list

numpy.around( ,decimals=2)
rounds to two decimal digits

HOWEVER, for this version of numpy it is not necessary to use numpy.around
print(numpy.arange(0.55, 1.05, 0.05))
[0.55 0.6  0.65 0.7  0.75 0.8  0.85 0.9  0.95 1.  ]

[::-1]
goes in opposite (decreasing) direction
[1.   0.95 0.9  0.85 0.8  0.75 0.7  0.65 0.6  0.55]

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
 
 def plot_heatmap(power_matrix, xticklabels, yticklabels):
     fig, ax = plt.subplots()
     # plt.xlabel('Number of Tosses', fontsize = 15) # how to set axis name? not working
	 # plt.ylabel('Probability of Heads', fontsize = 15) # not working
     ax.set_xlabel('Number of Tosses') # not working
     ax.set_ylabel('Probability of Heads') # not working
     ax.title.set_text('Heatmap of Powers')
     sns.heatmap(power_matrix, vmin = 0, vmax = 1, xticklabels = xticklabels, yticklabels = yticklabels, ax = ax, cmap = color)
     #is ax = ax doing something?? I am confused
     plt.show()

 tosses = numpy.array([10, 50, 100, 250, 500, 1000])
 probs = numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)[::-1]
 color = sns.color_palette("mako", as_cmap=True)


power1 = run_experiment(tosses, probs, correct_the_pvalues = True)
power2 = run_experiment(tosses, probs, correct_the_pvalues = False)
plot_heatmap(power1, tosses, probs) 
plot_heatmap(power2, tosses, probs) 


Lower the number of tosses, less poweer it has. Closer the probabiility to 0.5, more power.

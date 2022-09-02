(base) [~/qbb2022-answers/day5-lunch $]grep "father" $6 aau1043_dnm.csv| cut -d, -f 5-6 | sort -n | uniq -c | less -S > father_proband_count.sh
(base) [~/qbb2022-answers/day5-lunch $]grep "mother" $6 aau1043_dnm.csv| cut -d, -f 5-6 | sort -n | uniq -c | less -S > mother_proband_count.sh

(base) [~/qbb2022-answers/day5-lunch $]sed -e 's/,/\ /g' father_proband_count.sh > father_modified.sh
(base) [~/qbb2022-answers/day5-lunch $]sed -e 's/,/\ /g' mother_proband_count.sh > mother_modified.sh

(base) [~/qbb2022-answers/day5-lunch $]join -1 2 -2 2 father_modified.sh mother_modified.sh | cut -d ' ' -f 1-2,4 > joined_proband.txts

(base) [~/qbb2022-answers/day5-lunch $]sed -e 's/ /\,/g' joined_proband.txt > joined_modified.csv

(base) [~/qbb2022-answers/day5-lunch $]grep -v 'Proband_id' aau1043_parental_age.csv > no_head_age.csv

(base) [~/qbb2022-answers/day5-lunch $]join -t, -1 1 -2 1 joined_modified.csv no_head_age.csv > proband_fm_count_age.csvq









Ttest_indResult(statistic=-34.727245819690495, pvalue=3.6551794700990466e-161)

                            OLS Regression Results                            
==============================================================================
Dep. Variable:           mother_count   R-squared:                       0.228
Model:                            OLS   Adj. R-squared:                  0.226
Method:                 Least Squares   F-statistic:                     116.0
Date:                Fri, 02 Sep 2022   Prob (F-statistic):           6.88e-24
Time:                        14:10:53   Log-Likelihood:                -1158.1
No. Observations:                 396   AIC:                             2320.
Df Residuals:                     394   BIC:                             2328.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      2.5040      0.981      2.553      0.011       0.576       4.432
mother_age     0.3776      0.035     10.772      0.000       0.309       0.446
==============================================================================
Omnibus:                       51.143   Durbin-Watson:                   2.090
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               75.501
Skew:                           0.845   Prob(JB):                     4.03e-17
Kurtosis:                       4.310   Cond. No.                         121.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

For Mom:
The result is significant because the pvalue is extremely small (pvalue=3.6551794700990466e-161).
c




Ttest_indResult(statistic=26.675255607555535, pvalue=2.765837479277908e-112)
(base) [~/qbb2022-answers/day5-lunch $]./linear_regression.py 
                            OLS Regression Results                            
==============================================================================
Dep. Variable:           father_count   R-squared:                       0.619
Model:                            OLS   Adj. R-squared:                  0.618
Method:                 Least Squares   F-statistic:                     639.6
Date:                Fri, 02 Sep 2022   Prob (F-statistic):           1.55e-84
Time:                        14:19:59   Log-Likelihood:                -1406.6
No. Observations:                 396   AIC:                             2817.
Df Residuals:                     394   BIC:                             2825.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     10.3263      1.702      6.066      0.000       6.979      13.673
father_age     1.3538      0.054     25.291      0.000       1.249       1.459
==============================================================================
Omnibus:                        7.687   Durbin-Watson:                   1.795
Prob(Omnibus):                  0.021   Jarque-Bera (JB):                8.185
Skew:                           0.256   Prob(JB):                       0.0167
Kurtosis:                       3.483   Cond. No.                         127.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.


For Dad:
The result is significant because the pvalue is extremely small (pvalue=2.765837479277908e-112).
y=1.3538x + 10.3263
The relationship: As father's age increase by 1, father's proband count increases by 1.3538.
Note both coefficients are larger than mother's.












(base) [~/qbb2022-answers/day5-lunch $]grep -E 'father|mother' aau1043_dnm.csv | cut -d, -f 5-6 | sort -n | uniq -c > father_mother.txt

(base) [~/qbb2022-answers/day5-lunch $]tr "," " " < father_mother.txt > father_mother_modified.txt

df2 = np.genfromtxt("father_mother_modified.txt", dtype = None, encoding = None, names = ["count", "proband_id", "sex"])
 # print(df2["count"]) # to check if it was ok to read with 2 or 3 spaces in the front.

mom_dad = smf.ols(formula = "count ~ 1 + sex", data = df2)
results_mom_dad = mom_dad.fit()
print(results_mom_dad.summary())


                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  count   R-squared:                       0.783
Model:                            OLS   Adj. R-squared:                  0.783
Method:                 Least Squares   F-statistic:                     2852.
Date:                Fri, 02 Sep 2022   Prob (F-statistic):          2.20e-264
Time:                        15:26:27   Log-Likelihood:                -2972.8
No. Observations:                 792   AIC:                             5950.
Df Residuals:                     790   BIC:                             5959.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
=================================================================================
                    coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------
Intercept        52.0152      0.520    100.125      0.000      50.995      53.035
sex[T.mother]   -39.2348      0.735    -53.404      0.000     -40.677     -37.793
==============================================================================
Omnibus:                      133.813   Durbin-Watson:                   1.715
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              374.697
Skew:                           0.850   Prob(JB):                     4.32e-82
Kurtosis:                       5.910   Cond. No.                         2.62
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

P-value is extremely small, so
the number of maternally inherited de novo mutations per proband is significantly different than the number of paternally inherited de novo mutations per proband.

y=1.3538x + 10.3263
x=50.5

print(1.3538*50.5+10.3263)

78.6932

The number of paternal de novo mutations for a proband with a father who was 50.5 years old at the proband’s time of birth is 79.

new_data = df[0]
new_data.fill(0)
new_data['father_age'] = 50.5
print(results_dad.predict(new_data))

/Users/cmdb/miniconda3/lib/python3.9/site-packages/statsmodels/base/model.py:1147: ValueWarning: nan values have been dropped
  warnings.warn('nan values have been dropped', ValueWarning)
0    78.018535
dtype: float64

The decimal point is dropped because dtype=none set age automatically as integer not float, so it could not read it properly. 












#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
from scipy import stats

df = np.genfromtxt("proband_fm_count_age.csv", delimiter = ",", dtype = None, encoding = None, names = 'proband_id, father_count, mother_count, father_age, mother_age')

fig, ax = plt.subplots()
ax.scatter(df["mother_age"], df["mother_count"] , alpha = 0.5, label = 'mother')
ax.legend()
ax.set_xlabel("Age")
ax.set_ylabel("Count of Proband")
# plt.show()
fig.savefig("ex2_a.png")
plt.close(fig) # to avoid confusion among multiple plots

fig, ax = plt.subplots()
ax.scatter(df["father_age"], df["father_count"] , alpha = 0.5, label = 'father')
ax.legend()
ax.set_xlabel("Age")
ax.set_ylabel("Count of Proband")
# plt.show()
fig.savefig("ex2_b.png")
plt.close(fig)

# mom_count_age = df[["mother_count", "mother_age"]] # not necessary
# dad_count_age = df[["father_count", "father_age"]] # not necessary
# print(mom_count_age)

# print(stats.ttest_ind(df['mother_count'], df['mother_age']))
# print(stats.ttest_ind(df['father_count'], df['father_age']))

mom_count_age = smf.ols(formula = "mother_count ~ 1 + mother_age", data = df)
results_mom = mom_count_age.fit()
# print(results_mom.summary())

dad_count_age = smf.ols(formula = "father_count ~ 1 + father_age", data = df)
results_dad = dad_count_age.fit()
# print(results_dad.summary())


fig, ax = plt.subplots()
ax.hist(df['father_count'], alpha = 0.5, label = 'Father')
ax.hist(df['mother_count'], alpha = 0.5, label = 'Mother')
ax.legend()
ax.set_xlabel("Count of de novo mutations")
ax.set_ylabel("Number of proband individuals")
# plt.show()
fig.savefig("ex2_c.png") # it is safer practice to specify what you're saving, which is fig, not plt
plt.close(fig)


df2 = np.genfromtxt("father_mother_modified.txt", dtype = None, encoding = None, names = ["count", "proband_id", "sex"])
# print(df2["count"]) # to check if it was ok to read with 2 or 3 spaces in the front.

mom_dad = smf.ols(formula = "count ~ 1 + sex", data = df2)
results_mom_dad = mom_dad.fit()
# print(results_mom_dad.summary())

# print(1.3538*50.5+10.3263)


new_data = df[0]
new_data.fill(0)
new_data['father_age'] = 50.5
print(results_dad.predict(new_data))
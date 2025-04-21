# **Module 4. Bivariate analysis:** **qualitative variables**
### **Data Science**

**Sabine De Vreese** **Lieven Smits** **Pieter Van Der Helst** **Bert Van Vreckem**

**2024–2025**


1/43


-----

# **Contents**

Bivariate analysis

Contingency tables

The chi-squared statistic
Cramér’s V

Chi-squared test for independence

Goodness-of-fit test

Testing procedure for goodness of fit test

Standardized residuals

Cochran’s rules

2/43


-----

# **Learning goals**

   - Dependent/independent variable

   - Apply suitable analysis techniques for each combination of
measurement levels

   - Contingency tables and Cramér’s 𝑉

   - Visualization

3/43


-----

# **Bivariate analysis: overview**

**Independent** **Dependent** **Test/Metric**

Qualitative Qualitative 𝜒 [2] -test
Cramér’s 𝑉

Qualitative Quantitative two-sample 𝑡-test
Cohen’s 𝑑

—
Quantitative Quantitative
Regression, correlation

4/43


-----

# **Bivariate analysis**


5/43


-----

# **Bivariate analysis**

   - …is determining whether there is an association between two
stochastic variables (𝑋 and 𝑌).

   - **Association** = you can predict (to some extent) the value of 𝑌 from
the value of 𝑋

   - 𝑋 — Independent variable

   - 𝑌 — Dependent variable

   - **Important!** Finding an association does **NOT** imply a causal relation!

6/43


-----

# **Example research questions**

   - Is there a difference in taste preference between two beverage
brands?

   - Is there a difference in spending at the campus restaurant between
students and staff?

   - Do smokers die more often of lung cancer than non-smokers?

   - Do men and women have a different opinion on a survey question?

   - …

We will use data/rlanders.csv from the Github repo for lab
assignments to explore the last question.

7/43


-----

# **Contingency tables**


8/43


-----

# **Contingency tables**

**(also: crosstab)**

See Python example code in demo-4.01-chi-squared.ipynb

**Gender** **Female** **Male**

**Survey**

Strongly disagree 0 4
Disagree 17 45
Neutral 23 91

Agree 12 53
Strongly agree 0 5

9/43


-----

# **Visualization**

A clustered bar chart


A mosaic plot


-----

# **Marginal totals**

**Gender** **Female** **Male** **Total**

**Survey**

Strongly disagree 0 4 4
Disagree 17 45 62
Neutral 23 91 114

Agree 12 53 65
Strongly agree 0 5 5

**Total** 52 198 250

11/43


-----

# **Expected values**

If there is no difference (association), we expect the same ratios in each
column of the table!

**Gender** **Female** **Male** **Total**

**Survey**

Strongly disagree 0.832 3.168 4
Disagree 12.896 49.104 62
Neutral 23.712 90.288 114

Agree 13.520 51.480 65
Strongly agree 1.040 3.960 5

**Total** 52 198 250

In each cell: (row total × column total) / 𝑛


-----

# **Measuring dispersion**

How far is the observed value 𝑜 from the expected 𝑒?

( 𝑜−𝑒 ) [2]

𝑒

**Gender** **Female** **Male**

**Survey**

Strongly disagree 0.832 0.219
Disagree 1.306 0.343
Neutral 0.021 0.006

Agree 0.171 0.045
Strongly agree 1.040 0.273

13/43


-----

# **The chi-squared statistic**

The sum of all these values is notated:


𝜒 [2] = ∑
𝑖

- 𝜒 is the Greek letter *chi*


(𝑜 𝑖 −𝑒 𝑖 ) [2]

≈4.255
𝑒
𝑖



- 𝑜 𝑖 = number of observations in the 𝑖’th cell of the contingency table

- 𝑒 𝑖 = expected frequency

- Small value ⇒ no association

- Large value ⇒ association


14/43


-----

# When is 𝜒 [2] large enough?

   - 2 × 2-table with 𝜒 [2] = 10

     - Relatively large difference

     - Indicates association

   - 5 × 5-table with 𝜒 [2] = 10

     - Relatively small difference

     - Does NOT indicate association

We need a metric independent of table size!

15/43


-----

# **Cramér’s V**

𝑉= √


𝜒 [2]

𝑛(𝑘−1) [= ] ~~[√]~~


4.255
250(2 −1) [≈0.130]


with 𝑛 the number of observations, 𝑘= min(𝑛𝑢𝑚𝑅𝑜𝑤𝑠, 𝑛𝑢𝑚𝐶𝑜𝑙𝑠)

**Cramér’s V** **Interpretation**

≈0 no association

≈0.1 weak association

≈0.25 moderate association

≈0.5 strong association
≈0.75 very strong association
≈1 complete association


16/43


-----

# **Chi-squared test for** **independence**


17/43


-----

# 𝜒 [2] test for independence

   - = Alternative to Cramér’s V to investigate association between
qualitative variables.

   - Value of 𝜒 [2] distributed according to the 𝜒 [2] distribution

18/43


-----

# 𝜒 [2] -distribution in Python

Import scipy.stats
For a 𝜒 [2] -distribution with df degrees of freedom:

**Function** **Purpose**

chi2.pdf(x, df=d) Probability density for x
chi2.cdf(x, df=d) Left-tail probability 𝑃(𝑋< x)
chi2.sf(x, df=d) Right-tail probability 𝑃(𝑋> x)
chi2.isf(1-p, df=d) p% of observations is expected
to be lower than this value

19/43


-----

# **Test procedure**

   - **Step 1.** Formulate hypotheses:

   - 𝐻 0 : there is no association (𝜒 [2] is “small”)

   - 𝐻 1 : there is an association (𝜒 [2] is “large”)

   - **Step 2.** Choose significance level, e.g. 𝛼= 0.05

   - **Step 3.** Calculate the test statistic, 𝜒 [2] = 4.255

20/43


-----

# **Test procedure (cont.)**

   - **Step 4.** Use 𝑑𝑓= (𝑛𝑢𝑚𝑅𝑜𝑤−1) × (𝑛𝑢𝑚𝐶𝑜𝑙−1) and either:

     - Determine critical value 𝑔 so 𝑃(𝜒 [2]     - 𝑔) = 𝛼

     - Calculate the 𝑝-value

   - **Step 5.** Draw conclusion:

    - 𝜒 [2] < 𝑔: do not reject 𝐻 0 ; 𝜒 [2]    - 𝑔: reject 𝐻 0

     - 𝑝> 𝛼: do not reject 𝐻 0 ; 𝑝< 𝛼: reject 𝐻 0

21/43


-----

# **Example (Gender vs Survey)**

   - g = stats.chi2.isf(0.05, df=4) (result: 9.4877)

   - p = stats.chi2.sf(4.2555, df=4) (result: 0.3725)

**Conclusion** : we do not reject the null hypothesis. Differences between
expected and observed values are not significantly large.
We found no association between variables *Gender* and *Survey*


-----

# **Test for independence in Python**

SciPy has a function to calculate 𝜒 [2] and 𝑝-value from a contingency table:

3

23/43


-----

# **Goodness-of-fit test**


24/43


-----

# **Goodness-of-fit test**

The 𝜒 [2] test can also be used to determine whether a sample is
**representative** for the population.




25/43


-----

# **Example**

26/43


**Type** **# sample** **# population**

Mutant 127 35%

Human 75 17%

Alien 98 23%

God 27 8%

Demon 73 17%

**Total** 400 100%


-----

# **Example**

Is the distribution of the sample (𝑛= 400) representative for the full
population (all superheroes)?

   - What numbers would you *expect* if the sample is representative?

   - How large are the differences from the *observed* numbers?

     - small ⇒ distribution is representative

     - large ⇒ distribution is **not** representative

27/43


-----

# **Example**

Is the distribution of the sample (𝑛= 400) representative for the full
population (all superheroes)?

   - What numbers would you *expect* if the sample is representative?

   - How large are the differences from the *observed* numbers?

     - small ⇒ distribution is representative

     - large ⇒ distribution is **not** representative

Can you see the link with contingency tables and Cramer’s V?

27/43


-----

# **Goodness of fit test**

   - Exactly representative ⇒ 35% of superheroes in the sample is a

mutant

   - The expected number therefore is 𝑒= 0.35 × 400 = 140.

Therefore:

𝑒= 𝑛× 𝜋

If the differences 𝑜−𝑒 are relatively small they can be attributed to
random sampling errors.

28/43


-----

# **Goodness of fit test**

Consider 𝜒 [2] :


(𝑜 𝑖 −𝑒 𝑖 ) [2]

𝑒
𝑖


𝜒 [2] =


𝑛
∑
𝑖=1


Draw a conclusion based on the value of 𝜒 [2] :

 - small ⇒ distribution is representative

 - large ⇒ distribution is **not** representative

𝜒 [2] measures the degree of conflict with the null hypothesis


29/43


-----

# **Goodness of fit test**

( 𝑜−𝑒 ) [2]
**Superhero type** 𝑜 𝜋 𝑒

𝑒

Mutant 127 35% 140 1.21

Human 75 17% 68 0.72

Alien 98 23% 92 0.39

God 27 8% 32 0.78

Demon 73 17% 68 0.37

𝜒 [2] = 3.47

30/43


-----

# **Goodness of fit test**

   - The test statistic 𝜒 [2] follows the 𝜒 [2] distribution.

   - Critical value 𝑔 from the 𝜒 [2] distribution: this is dependent on the
number of degrees of freedom (𝑑𝑓). In general:

𝑑𝑓= 𝑘−1

with 𝑘 the number of categories.

   - The critical value 𝑔 for a given significance level 𝛼 and number of
degrees of freedom 𝑑𝑓 can be calculated in Python using the
function isf().

𝑃(𝜒 [2] < 𝑔) = 1 −𝛼

31/43


-----

# **Goodness of fit test**

**Testing Procedure**

1. **Formulate hypotheses**

   - 𝐻 0 : sample is representative for the population

   - 𝐻 1 : sample is not representative for the population

2. **Choose significance level** : 𝛼= 0.05

32/43


-----

# **Goodness of fit test**

**Testing Procedure**

1. **Calculate test statistic** :


(𝑜 𝑖 −𝑒 𝑖 ) [2]

𝑒
𝑖


𝜒 [2] =


𝑛
∑
𝑖=1


1.1 **Critical area** : Calculate 𝑔 so that 𝑃(𝜒 [2] < 𝑔) = 1 −𝛼
1.2 **Probability value** : Calculate 𝑝= 1 −𝑃(𝑋< 𝜒 [2] )
2. Conclusion (the test is always right-tailed):

2.1 𝜒 [2] < 𝑔⇒ do not reject 𝐻 0, 𝜒 [2]   - 𝑔⇒ reject 𝐻 0
2.2 𝑝> 𝛼⇒ do not reject 𝐻 0, 𝑝< 𝛼⇒ reject 𝐻 0


33/43


-----

# **Example**

   - g = stats.chi2.isf(0.05, df=4) (result: 9.4877)

   - p = stats.chi2.sf(3.4679, df=4) (result: 0.4828)

**Conclusion.** 𝜒 [2] ≈3.47 < 𝑔≈9.4877, so we don’t reject the null hypothesis.
This sample is representative for the population.

34/43


-----

# **Goodness-of-fit test in Python**

5

35/43


-----

# **Standardized residuals**


36/43


-----

# **Example: families**

Consider all families with exactly 5 children in a given community.


-----

# **Example: families**

Consider all families with exactly 5 children in a given community. When
we look at the number of boys/girls, there are 6 possible combinations:

1. 5 boys

2. 4 boys, 1 girl

3. 3 boys, 2 girls

4. 2 boys, 3 girls

5. 1 boy, 4 girls

6. 5 girls

A survey was conducted regarding 1022 families with exactly 5 children

Are the observed numbers in the 6 classes representative for a
population in which the probability of having a boy is equal to the
probability of having a girl, or more concrete 0.5?


-----

# **Example**

38/43


i 0 1 2 3 4 5

𝑜 58 149 305 303 162 45
𝑖


-----

# **Example**

i 0 1 2 3 4 5

𝑜 58 149 305 303 162 45
𝑖

If the assumption is true, the probability 𝜋 𝑖 to have 𝑖 boys is determined
by a binomial distribution with parameters 𝑛= 5 and 𝑝= 0.5. For example,
the probability to have 2 boys out of 5 children is equal to:

(0.5) [2] × (1 −0.5) [5−2]
× (2 [5][)]

In general (you don’t have to know why):

5!
𝜋
𝑖 = ( [5] 𝑖 [) × 0.5] [𝑖] [× 0.5] [5−𝑖] [=] 𝑖!(5 −𝑖)! [× 0.5] [𝑖]

38/43


-----

# **Example**

𝑖 0 1 2 3 4 5 Total

𝑜 58 149 305 303 162 45 1022
𝑖
𝜋 𝑖 0,031 0,156 0,313 0,313 0,156 0,031 1
𝑒 𝑖 31,9 159,7 319,4 319,4 159,7 31,9 1022
( 𝑜−𝑒 ) [2]

21,268 0,715 0,647 0,840 0,033 5,343 28,846
𝑒
𝑟 𝑖 4,686 -0,921 -0,970 -1,105 0,199 2,348

39/43


-----

# **Example**

1. **Formulate both hypotheses**

   - 𝐻 0 : the sample is representative for the population

   - 𝐻 1 : the sample is not representative for the population

2. **Determine** 𝛼 **and** 𝑛: 𝛼= 0.01 and 𝑛= 1022.

3. **Value of the test statistic in the sample** :


(𝑜 𝑖 −𝑒 𝑖 ) [2]

≈28.846
𝑒
𝑖


𝜒 [2] =


𝑛
∑
𝑖=1


4. **Calculate and plot critical area** : The critical value is 15.0863. Our test
statistic is inside the critical area, so we can reject 𝐻 0 .


40/43


-----

# **Standardized Residuals**




𝑜 −𝑛𝜋
𝑖 𝑖
𝑟 =
𝑖

~~√~~ [𝑛𝜋] 𝑖 [(1 −𝜋] 𝑖 [)]

 - 𝑟 𝑖 ∈[−2, 2] ⇒ “acceptable” values

 - 𝑟 𝑖 < −2 ⇒ underrepresented

 - 𝑟 𝑖 - 2 ⇒ overrepresented

**Conclusion:** families in which all children are of the same gender are
overrepresented.


-----

# **Cochran’s rules**


42/43


-----

# **Conditions**

In order to apply the 𝜒 [2] -test, the following conditions must be met (Rule
of Cochran)

1. For all categories, the expected frequency 𝑒 must be greater than 1.

2. In a maximum of 20 % of the categories, the expected frequency 𝑒
may be less than 5.

43/43


-----


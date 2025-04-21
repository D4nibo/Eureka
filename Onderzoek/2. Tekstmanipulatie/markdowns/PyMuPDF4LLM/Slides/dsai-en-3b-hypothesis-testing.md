# **Module 3b. Hypothesis testing**
## **Data Science**

**Sabine De Vreese** **Lieven Smits** **Pieter Van Der Helst** **Bert Van Vreckem**

**2024–2025**


1/37


-----

# **Contents**

Testing procedure

Probability Value

Critical Region

Examples

Student’s t-test

Errors in Hypothesis Tests

2/37


-----

# **Learning Goals**

   - Statistical hypothesis testing concepts

   - Hypothesis testing procedure

   - Apply the 𝑧- and 𝑡-test

3/37


-----

# **Testing procedure**


4/37


-----

# **Statistical Hypothesis Testing**

**Hypothesis** Idea that has yet to be proven: statement regarding the
numeric value of a population parameter

**Hypothesis Test** verification of a statement about the values of one or
multiple population parameters

**Null Hypothesis (** 𝐻 0 **)** Base hypothesis, we start with assuming it is true

**Alternative Hypothesis (** 𝐻 1 **,** 𝐻 𝑎 **)** Conclusion if the null hypothesis is
unlikely to be true

5/37


-----

# **Elements of a testing procedure**

**Test Statistic** The value that is calculated from the sample

**Region of Acceptance** The region of values supporting the null
hypothesis

**Critical Region / Region of Rejection** The region of values rejecting the
null hypothesis

**Significance Level** The probability of rejecting a true null hypothesis 𝐻 0

6/37


-----

# **Testing procedure**

1. Formulate both hypotheses (𝐻 0 and 𝐻 1 )

2. Determine the significance level (𝛼)

3. Calculate the test statistic

4. Determine the critical region or the probability value

5. Draw conclusions

7/37


-----

# **Hypotheses about superheroes**


-----

# **A superhero rescues 3.3 persons** **a day**

[Source: http://www.cracked.com/quick-fixes/](http://www.cracked.com/quick-fixes/4-people-who-saved-day-while-dressed-as-superheroes/)
[4-people-who-saved-day-while-dressed-as-superheroes/](http://www.cracked.com/quick-fixes/4-people-who-saved-day-while-dressed-as-superheroes/)

9/37


-----

Assume that, over a period of 30 days, on average 3.483 people were
saved each day (𝑥= 3.483, 𝑛= 30)

1. Hypothesis: 𝐻 0 ∶𝜇= 3.3; 𝐻 1 ∶𝜇> 3.3

2. Significance level: 𝛼= 0.05

3. Test statistic: 𝑥= 3.483

Standard deviation of the population (assumed to be known): 𝜎= 0.55


10/37


-----

# **Calculate test statistic**

Based on the central limit theorem, we know that:
𝑀∼𝑁𝑜𝑟(𝜇= 3.3; 𝜎= [0.55] √30 [= 0.1)]

4

3

2

1



3 3.1 3.2 3.3 3.4 3.5 3.6


11/37


-----

# **Probability Value**


12/37


-----

# **Probability Value**





- 𝑝-value < 𝛼⇒ reject 𝐻 0 : the discovered value of 𝑥 is too extreme;

- 𝑝-value ≥𝛼⇒ do not reject 𝐻 0 : the discovered value of 𝑥 can still be
explained by coincidence.


13/37


-----

# **Probability Value**

0.4

0.3

0.2

0.1



−3 −2 −1 0 1 2 3

1.822

𝜎

𝑃(𝑀> 3.483) = 𝑃(𝑍> [3.483 −3.3] √𝑛 ) = 𝑃(𝑍> 1.822) = 0.0344


14/37


-----

# **Critical Region**


15/37


-----

# **Critical Region**




We look for a critical value 𝑔 for which:

𝑃(𝑀> 𝑔) = 𝛼

Determine 𝑧 for which:
𝛼

𝑃(𝑍> 𝑧 𝛼 ) = 𝛼⇒𝑔= 𝜇+ 𝑧 𝛼 . √𝑛 [𝜎]

 - Left of 𝑔: region of acceptance (do not reject 𝐻 0 )

 - Right of 𝑔: critical region (reject 𝐻 0 )


16/37


-----

# **Critical Region**

0.4

0.3

0.2

0.1



|gion|Col2|
|---|---|
|𝛼= 0.05||
|−3 −2 −1 0 1|2 3|


𝑧 =
𝛼
1.645

significance level 𝛼= 0.05 ⇒ critical value 𝑧 𝛼 =1.645
(𝑧 𝛼 =stats.norm.isf(1 - 0.95))
17/37


-----

# **Left-tailed testing**

What would you have to change in the equation in order to calculate the
correct critical value?

18/37


-----

# **Left-tailed testing**

What would you have to change in the equation in order to calculate the
correct critical value? Answer:

𝑔= 𝜇 − 𝑧× [𝜎]

√𝑛

because

[𝑔] [−] [𝜇]

𝜎

𝑃(𝑀< 𝑔) = 𝑃(𝑍< √𝑛 ) = 0.05

18/37


-----

# **Left-tailed testing**

Because of symmetry:

𝜎

𝑃(𝑍> −( [𝑔] √𝑛 [−] [𝜇] )) = 0.05

The corresponding 𝑧-value is 1.645, and therefore:


𝑧= [−] [𝑔] [+ ] [𝜇]


√𝑛 𝑧 𝛼 −𝜇


~~√~~ 𝜎 [+ ] 𝑛 [𝜇] ⇔−𝑔= √𝑛 [𝜎]


𝜎
⇔𝑔= 𝜇−𝑧 𝛼 √𝑛


19/37


-----

# **Two-tailed testing**

Sometimes it can be necessary to perform a two-tailed test. In this case,
two critical values need to be calculated, namely the left and right critical
value.


𝑔= 𝜇± 𝑧 𝛼/2 × √𝑛 [𝜎]


(1)


20/37


-----

# **Summary**




Table: Summary of Testing Procedures


-----

# 𝑧 -test **Requirements for**

   - The sample needs to be random

   - The sample size needs to be sufficiently large (𝑛≥30)

   - The test statistic needs to have a normal distribution

   - The standard deviation of the population, 𝜎, is known

Sometimes these assumptions will not hold and in this case we can *not*
use the 𝑍-test!

22/37


-----

# **Examples**


23/37


-----

# **Example 1**

When drawing a random sample consisting of 50 observations from a
population with variance 𝜎 [2] = 55 we obtain as sample mean 𝑥= 25.
We now want to find out if there is a reason to assume that the
population mean is smaller than 27.

24/37


-----

# **Example 1**

**1** Formulate both hypotheses

𝐻 en 𝐻 .
0 ∶𝜇= 27 1 ∶𝜇< 27

**2** Determine significance level 𝛼 and sample size 𝑛
𝛼= 0.05 en 𝑛= 50

**3** Test statistic & value: sample mean 𝑥= 25

25/37


-----

# **Example 1 (cont.)**

**4a** Probability Value
According to the central limit theorem:

𝑀∼𝑁𝑜𝑟(𝜇= 27, [𝜎] [2] )

√𝑛



[𝑥−] [𝜇] = [25 −27]

𝜎

55

√𝑛 √ 50


𝑧= [𝑥−] [𝜇]


√


≈−1.91


55

50


We therefore have a probability value of 0.0281.
Using a significance level of 0.05, we can reject 𝐻 0 .


26/37


-----

# **Example 1 (cont.)**

**4b** Calculate and plot the critical region

𝑔= 𝜇−𝑧× [𝜎]

~~√~~ 𝑛

𝜎

= 27 −1.645 × √ 𝑛

= 25.27470944

We have that 𝑥< 𝑔 and therefore we can reject 𝐻 0 .

27/37


-----

# **Example 1 (cont.)**

0.3

0.2

0.1

24 25 26 27 28 29 30

25.27

28/37


-----

# **Example 1 (cont.)**

**5** Conclusion

We can conclude, based on the sample, that 𝜇< 27 for a
significance level of 0.05

29/37


-----

# **Example 2**

In a reseach about the amount of change in the pockets of our
superheroes, researchers state that on average a superhero carries €25
of cash. We assume that the standard deviation of the population 𝜎= 7.
For a random sample of size 𝑛= 64, the average amount of money a
superhero carries is 𝑥= €23. For the significance level, 𝛼= 0.05 is selected.

30/37


-----

# **Example 2**

**1** Formulate both hypotheses
𝐻 0 ∶𝜇= 25 en 𝐻 1 ∶𝜇≠25

**2** Determine significance level 𝛼 and sample size 𝑛
𝛼= 0.05 en 𝑛= 64.

**3** Test statistic & value: 𝑥= 23

31/37


-----

# **Example 2 (cont.)**

**4b** Calculate the critical region

𝑔 1 = 𝜇−𝑧× [𝜎] = 23.28

√𝑛

𝑔 2 = 𝜇+ 𝑧× [𝜎] = 26.72

√𝑛

We have that 𝑥 is inside the critical region (because
23 < 23.28) so we can reject 𝐻 0 .

**5** Based on this sample we can conclude that superheroes
carry on average *less* than 25 €, using a significance level of
5%

32/37


-----

# **Student’s t-test**


33/37


-----

# **Student’s t-test**

What if the requirements for a 𝑧-test are not met? E.g.

   - Sample size too small

   - Population stdev (𝜎) unknown

If the variable is normally distributed, you can use the 𝑡-test

34/37


-----

# The 𝑡 -test

Determine critical value:


𝑔= 𝜇± 𝑡× [𝑠]

√𝑛



- 𝑡-value is derived from the Student’s 𝑡-distribution, based on the
number of *degrees of freedom*, 𝑛−1

- Look for value using the function t.isf() in Python

- Apart from this, the procedure is identical to the procedure of the

𝑧-test


35/37


-----

# **Errors in Hypothesis Tests**


36/37


-----

# **Errors in Hypothesis Tests**

P(type I error) = 𝛼 (= significance level)
P(type II error) = 𝛽
Calculating 𝛽 is ***not*** trivial, but if 𝛼↘ then 𝛽↗

37/37


-----


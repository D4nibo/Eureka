## **Module 5. Bivariate analysis:** **qualitative — quantitative**
### **Data Science**

**Sabine De Vreese** **Lieven Smits** **Pieter Van Der Helst** **Bert Van Vreckem**

**2024–2025**


1/28


-----

## **Contents**

Data visualization

Two-sample t-test

Paired samples

Effect size

2/28


-----

## **Learning goals**

   - Apply the 𝑡-test for two samples

   - Calculate effect size using Cohen’s 𝑑

   - Visualization

3/28


-----

## **Bivariate analysis: overview**

**Independent** **Dependent** **Test/Metric**

Qualitative Qualitative 𝜒 [2] -test
Cramér’s 𝑉

Qualitative Quantitative two-sample 𝑡-test
Cohen’s 𝑑

—
Quantitative Quantitative
Regression, correlation

4/28


-----

## **Example research questions**

   - Are male penguins larger than females?

   - Do men get a higher salary than women?

   - Does a new vaccine protect against a disease?

   - Does “retrieval practice” improve learning outcomes (i.e. student
grades)?

   - …

In these examples, what is the independent/dependent variable?

5/28


-----

## **Data visualization**


6/28


-----

## **Data visualization**

   - Chart types for quantitative data

   - Grouped by qualitative variable

7/28


-----

## **Data visualization**

   - Chart types for quantitative data

   - Grouped by qualitative variable

Suitable chart types:

   - Grouped boxplot

   - Grouped density plot

   - Bar chart with error bars

   - …

7/28


-----

## **Grouped boxplot**

(source code: see demo-5.01-2sample-t.ipynb)

8/28


-----

## **Grouped violin plot**

9/28


-----

## **Grouped density plot**

10/28


-----

## **Beware! Bar chart of group** **means**

11/28


-----

## **Beware! Bar chart of group** **means**

11/28


-----

## **Bar chart with error bars**

   - Always add error bars!

   - Only makes sense for normally distributed data

   - Example: 1 standard deviation:

12/28


-----

## **Two-sample t-test**


13/28


-----

## **Comparing two population** **means**

Are the population means of two populations different?

We use two *samples* to perform an appropriate statistical test.

Correct test depends on:

   - Independent samples

   - Paired samples

14/28


-----

## **Independent samples**

In a clinical study, the aim is to determine whether a new drug has a
delayed (i.e. higher) reaction time as a side effect.

   - Control group: 6 participants receive placebo

   - Intervention group: 6 participants receive medicine

15/28


-----

## **Independent samples**

In a clinical study, the aim is to determine whether a new drug has a
delayed (i.e. higher) reaction time as a side effect.

   - Control group: 6 participants receive placebo

   - Intervention group: 6 participants receive medicine

Next, the reaction time (in ms) is measured:

   - Control group: 91, 87, 99, 77, 88, 91 (𝑥= 88.83)

   - Intervention group: 101, 110, 103, 93, 99, 104 (𝑦= 101.67)

Are there significant differences between the intervention and control
group?

15/28


-----

## **Independent samples**

**Testing procedure**

1. Hypotheses:

   - 𝐻 0 : 𝜇 1 −𝜇 2 = 0

   - 𝐻 1 : 𝜇 1 −𝜇 2 < 0

2. Significance level: 𝛼= 0.05

3. Test statistic is based on:

     - 𝑥−𝑦= −12.833

     - 𝑥= estimation for 𝜇 1 (control group)

     - 𝑦= estimation for 𝜇 2 (intervention group)

     - Takes the variances of the samples into account. For completeness the
test statistic is

𝑥− 𝑦
𝑡= .

~~√~~ [𝑠] 𝑥 [2] [/𝑛] 𝑥 [+ 𝑠] 𝑦 [2] [/𝑛] 𝑦

4. Calculate 𝑝

16/28


-----

## **Independent samples**

**Calculation in Python**

The calculation of the test statistic and the associated 𝑝-value is done by
stats.ttest_ind()

control = np.array([91, 87, 99, 77, 88, 91])
treatment = np.array([101, 110, 103, 93, 99, 104])
stats.ttest_ind(a=control, b=treatment,
alternative='less', equal_var=False)

Result:

Ttest_indResult(statistic=-3.445612673536487,
pvalue=0.003391230079206901)

17/28


-----

## **Independent samples**

**Testing procedure (continued)**

5. Draw conclusion based on 𝑝-value.
𝑝≈0.00339 < 𝛼= 0.05. We reject the null hypothesis. In this sample,
there is reason to assume that the drug does indeed increase
reaction time.

18/28


-----

## **Paired samples**


19/28


-----

## **Paired samples**

A study examined whether cars that run on petrol with additives have a
lower consumption, i.e. a higher miles per gallon.
For 10 cars, the consumption was measured (expressed in miles per
gallon) for both fuel types:

**Car** 1 2 3 4 5 6 7 8 9 10

**Regular petrol** 16 20 21 22 23 22 27 25 27 28
**With additives** 19 22 24 24 25 25 25 26 28 32

20/28


-----

## **Paired samples**

**Testing procedure**
1. Hypotheses:

   - 𝐻 0 : 𝜇 𝑋−𝑌 = 0

   - 𝐻 1 : 𝜇 𝑋−𝑌 < 0
2. Significance level: 𝛼= 0.05
3. Test statistic:

     - Based on the mean of the difference 𝑑= 𝑥−𝑦

Regular petrol 16 20 21 22 23 22 27 25 27 28
With additives 19 22 24 24 25 25 25 26 28 32

Difference -3 -2 -3 -2 -2 -3 2 -1 -1 -4

     - For completeness, the test statistic i s

𝑑
𝑡=

𝑠 𝑑 /√𝑛

4. Calculate 𝑝

21/28


-----

## **Paired samples**

**Calculation in Python**

regular = np.array([16, 20, 21, 22, 23, 22, 27, 25, 27, 28])
additives = np.array([19, 22, 24, 24, 25, 25, 26, 26, 28, 32])
stats.ttest_rel(regular, additives, alternative='less')

Result:

Ttest_relResult(statistic=-4.47213595499958,
pvalue=0.00077494295585091)

22/28


-----

## **Paired samples**

**Testing procedure**

5. Draw conclusion based on 𝑝-value.
𝑝≈0.0007749 < 𝛼= 0.05. We reject the null hypothesis. In this sample,
there is reason to assume that the fuel with additives leads to lower

fuel consumption, i.e. higher miles per gallon.

23/28


-----

## **Effect size**


24/28


-----

## **Effect size**





- Control group vs. intervention group

- Can be used in addition to hypothesis test

- Often used in educational sciences

- There are several definitions, here: *Cohen’s* 𝑑


25/28


-----

## Cohen’s 𝑑


𝑑=


𝑥 −𝑥
1 2

𝑠


where 𝑥 𝑥
1 and 2 represent the sample means
and 𝑠 the pooled standard deviation, i.e. standard deviation of both
groups combined:


𝑠= √


(𝑛 1 −1)𝑠 1 [2] [+ (𝑛] 2 [−1)𝑠] 2 [2]

𝑛
1 + 𝑛 2 −2


with 𝑛 1, 𝑛 2 the sample sizes, and 𝑠 1, 𝑠 2 the standard deviations
of both groups


26/28


-----

## Interpretation Cohen’s 𝑑


|𝑑| **Effect Size**

0.01 Very small
0.2 Small

0.5 Average
0.8 Large
1.2 Very large
2.0 Huge


In educational sciences (John
Hattie):

 - 0,4 = tipping point for desired
effects

 - effect size 𝑑= 1: process
material that would normally
take 1 year in 6 months!


[E.g. https://visible-learning.org/](https://visible-learning.org/backup-hattie-ranking-256-effects-2017/)
[backup-hattie-ranking-256-effects-2017/](https://visible-learning.org/backup-hattie-ranking-256-effects-2017/)


27/28


-----

## **Typical approach research in** **education**

   - Research question: Is X a good learning strategy, in other words,
does this have a positive effect on final results?

   - Control group uses “traditional” approach

   - Intervention group uses X

   - Followed by an evaluation moment

   - Determine scores, calculate 𝑑

28/28


-----


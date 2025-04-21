#### **Module 4. Bivariate analysis: qualitative variables Data Science**

**Sabine De Vreese Lieven Smits Pieter Van Der Helst Bert Van Vreckem 2024–2025**

Bivariate analysis

Contingency tables The chi-squared statistic Cramér's V

Chi-squared test for independence

Goodness-of-fit test Testing procedure for goodness of fit test

Standardized residuals

Cochran's rules

# **Learning goals**

- Dependent/independent variable
- Apply suitable analysis techniques for each combination of measurement levels
- Contingency tables and Cramér's
- Visualization

## **Bivariate analysis: overview**

| Independent  | Dependent    | Test/Metric             |
|--------------|--------------|-------------------------|
| Qualitative  | Qualitative  | 2<br>𝜒<br>-test         |
|              |              | Cramér's<br>𝑉           |
| Qualitative  | Quantitative | 𝑡-test<br>two-sample    |
|              |              | Cohen's<br>𝑑            |
| Quantitative | Quantitative | —                       |
|              |              | Regression, correlation |

#### **Bivariate analysis**

## **Bivariate analysis**

- …is determining whether there is an association between two stochastic variables ( and ).
- **Association** = you can predict (to some extent) the value of from the value of
	- Independent variable
	- Dependent variable
- **Important!** Finding an association does **NOT** imply a causal relation!

## **Example research questions**

- Is there a difference in taste preference between two beverage brands?
- Is there a difference in spending at the campus restaurant between students and staff?
- Do smokers die more often of lung cancer than non-smokers?
- Do men and women have a different opinion on a survey question?

We will use data/rlanders.csv from the Github repo for lab assignments to explore the last question.

● …

#### **Contingency tables**

## **Contingency tables**

**(also: crosstab)**

See Python example code in demo-4.01-chi-squared.ipynb

| Gender<br>Survey  | Female | Male |
|-------------------|--------|------|
| Strongly disagree | 0      | 4    |
| Disagree          | 17     | 45   |
| Neutral           | 23     | 91   |
| Agree             | 12     | 53   |
| Strongly agree    | 0      | 5    |

## **Visualization**

A mosaic plot

A clustered bar chart

## **Marginal totals**

| Gender<br>Survey  | Female | Male | Total |
|-------------------|--------|------|-------|
| Strongly disagree | 0      | 4    | 4     |
| Disagree          | 17     | 45   | 62    |
| Neutral           | 23     | 91   | 114   |
| Agree             | 12     | 53   | 65    |
| Strongly agree    | 0      | 5    | 5     |
| Total             | 52     | 198  | 250   |

#### **Expected values**

If there is no difference (association), we expect the same ratios in each column of the table!

| Gender<br>Survey  | Female | Male   | Total |
|-------------------|--------|--------|-------|
| Strongly disagree | 0.832  | 3.168  | 4     |
| Disagree          | 12.896 | 49.104 | 62    |
| Neutral           | 23.712 | 90.288 | 114   |
| Agree             | 13.520 | 51.480 | 65    |
| Strongly agree    | 1.040  | 3.960  | 5     |
| Total             | 52     | 198    | 250   |

In each cell: (row total × column total) /

#### **Measuring dispersion**

How far is the observed value from the expected ?

$$\frac{(\text{o} - \text{e})^2}{\text{e}}$$

| Gender<br>Survey  | Female | Male  |
|-------------------|--------|-------|
| Strongly disagree | 0.832  | 0.219 |
| Disagree          | 1.306  | 0.343 |
| Neutral           | 0.021  | 0.006 |
| Agree             | 0.171  | 0.045 |
| Strongly agree    | 1.040  | 0.273 |

## **The chi-squared statistic**

The sum of all these values is notated:

$$\chi^2 = \sum\_{i} \frac{(\mathbf{o}\_i - \mathbf{e}\_i)^2}{\mathbf{e}\_i} \approx 4.255$$

- is the Greek letter *chi*
- = number of observations in the 'th cell of the contingency table
- = expected frequency
- Small value ⇒ no association
- Large value ⇒ association

#### **When is** 2 **large enough?**

- 2 × 2-table with 2 = 10
	- Relatively large difference ○ Indicates association
- 5 × 5-table with 2 = 10
	- Relatively small difference
	- Does NOT indicate association

We need a metric independent of table size!

#### **Cramér's V**

$$\mathbf{V} = \sqrt{\frac{\mathbf{x}^2}{n(\hbar - \mathbf{1})}} = \sqrt{\frac{4.255}{250(2 - \mathbf{1})}} \approx \mathbf{0.130}$$

with the number of observations, = min(, )

| Cramér's V | Interpretation          |
|------------|-------------------------|
| ≈ 0        | no association          |
| ≈ 0.1      | weak association        |
| ≈ 0.25     | moderate association    |
| ≈ 0.5      | strong association      |
| ≈ 0.75     | very strong association |
| ≈ 1        | complete association    |

## **Chi-squared test for independence**

#### 2 **test for independence**

- = Alternative to Cramér's V to investigate association between qualitative variables.
- Value of <sup>2</sup> distributed according to the <sup>2</sup> distribution

#### 2 **-distribution in Python**

Import scipy.stats For a 2 -distribution with df degrees of freedom:

| Function                                     | Purpose                                                              |
|----------------------------------------------|----------------------------------------------------------------------|
| chi2.pdf(x,<br>df=d)<br>chi2.cdf(x,<br>df=d) | Probability density for<br>x<br>Left-tail probability<br>𝑃(𝑋 <<br>x) |
| chi2.sf(x,<br>df=d)                          | 𝑃(𝑋 ><br>x)<br>Right-tail probability                                |
| chi2.isf(1-p,<br>df=d)                       | p% of observations is expected<br>to be lower than this value        |

#### **Test procedure**

- **Step 1.** Formulate hypotheses:
	- <sup>0</sup> : there is no association ( 2 is "small")
	- <sup>1</sup> : there is an association ( 2 is "large")
- **Step 2.** Choose significance level, e.g. = 0.05
- **Step 3.** Calculate the test statistic, 2 = 4.255

## **Test procedure (cont.)**

- **Step 4.** Use = ( − 1) × ( − 1) and either:
	- Determine critical value so (<sup>2</sup> > ) =
	- Calculate the -value
- **Step 5.** Draw conclusion:
	- 2 < : do not reject <sup>0</sup> ; 2 > : reject <sup>0</sup> ○ > : do not reject <sup>0</sup> ; < : reject <sup>0</sup>

## **Example (Gender vs Survey)**

- g = stats.chi2.isf(0.05, df=4) (result: 9.4877)
- p = stats.chi2.sf(4.2555, df=4) (result: 0.3725)

**Conclusion**: we do not reject the null hypothesis. Differences between expected and observed values are not significantly large. We found no association between variables *Gender* and *Survey*

# **Test for independence in Python**

SciPy has a function to calculate and -value from a contingency table:

 observed = pd.crosstab(rlanders.Survey, rlanders.Gender) chi2, p, df, expected = stats.chi2\_contingency(observed) print("Chi-squared : **%.4f**" % chi2) print("Degrees of freedom: **%d**" % df) print("P-value : **%.4f**" % p)

#### **Goodness-of-fit test**

#### **Goodness-of-fit test**

The 2 test can also be used to determine whether a sample is **representative** for the population.

#### **Goodness-of-fit test**

**This test indicates to what degree a sample corresponds to a null hypothesis regarding the distribution of a qualitative variable over mutually exclusive classes.**

| Type   | # sample | # population |
|--------|----------|--------------|
| Mutant | 127      | 35%          |
| Human  | 75       | 17%          |
| Alien  | 98       | 23%          |
| God    | 27       | 8%           |
| Demon  | 73       | 17%          |
| Total  | 400      | 100%         |

Is the distribution of the sample ( = 400) representative for the full population (all superheroes)?

- What numbers would you *expect* if the sample is representative?
- How large are the differences from the *observed* numbers? ○ small ⇒ distribution is representative ○ large ⇒ distribution is **not** representative

Can you see the link with contingency tables and Cramer's V?

Is the distribution of the sample ( = 400) representative for the full population (all superheroes)?

- What numbers would you *expect* if the sample is representative?
- How large are the differences from the *observed* numbers? ○ small ⇒ distribution is representative ○ large ⇒ distribution is **not** representative

Can you see the link with contingency tables and Cramer's V?

- Exactly representative ⇒ 35% of superheroes in the sample is a mutant
- The expected number therefore is = 0.35 × 400 = 140. Therefore:

= ×

If the differences − are relatively small they can be attributed to random sampling errors.

Consider 2 :

$$\chi^2 = \sum\_{i=1}^n \frac{(\mathbf{o}\_i - \mathbf{e}\_i)^2}{\mathbf{e}\_i}.$$

Draw a conclusion based on the value of 2 :

- small ⇒ distribution is representative
- large ⇒ distribution is **not** representative
- <sup>2</sup> measures the degree of conflict with the null hypothesis

| Superhero type | 𝑜   | 𝜋   | 𝑒           | (𝑜−𝑒)2<br>𝑒 |
|----------------|-----|-----|-------------|-------------|
| Mutant         | 127 | 35% | 140         | 1.21        |
| Human          | 75  | 17% | 68          | 0.72        |
| Alien          | 98  | 23% | 92          | 0.39        |
| God            | 27  | 8%  | 32          | 0.78        |
| Demon          | 73  | 17% | 68          | 0.37        |
|                |     |     | 2<br>𝜒<br>= | 3.47        |

- The test statistic 2 follows the <sup>2</sup> distribution.
- Critical value from the <sup>2</sup> distribution: this is dependent on the number of degrees of freedom (). In general:

$$df = h - 1$$

with the number of categories.

● The critical value for a given significance level and number of degrees of freedom can be calculated in Python using the function isf().

$$P(\chi^2 < g) = \mathbb{1} - \alpha$$

**Testing Procedure**

#### 1. **Formulate hypotheses**

- <sup>0</sup> : sample is representative for the population
- <sup>1</sup> : sample is not representative for the population
- 2. **Choose significance level**: = 0.05

**Testing Procedure**

1. **Calculate test statistic**:

$$\chi^2 = \sum\_{i=1}^n \frac{(\mathbf{o}\_i - \mathbf{e}\_i)^2}{\mathbf{e}\_i}$$

- 1.1 **Critical area**: Calculate so that (<sup>2</sup> < ) = 1 −
- 1.2 **Probability value**: Calculate = 1 − ( < <sup>2</sup> )
- 2. Conclusion (the test is always right-tailed): 2.1 2 < ⇒ do not reject <sup>0</sup> , 2 > ⇒ reject <sup>0</sup> 2.2 > ⇒ do not reject <sup>0</sup> , < ⇒ reject <sup>0</sup>

$$\mathbf{H}\_{\mathbf{H}}$$

- g = stats.chi2.isf(0.05, df=4) (result: 9.4877)
- p = stats.chi2.sf(3.4679, df=4) (result: 0.4828)

**Conclusion.** 2 ≈ 3.47 < ≈ 9.4877, so we don't reject the null hypothesis. This sample is representative for the population.

#### **Goodness-of-fit test in Python**

```
1 observed = np.array([127, 75, 98, 27, 73])
2 expected_p = np.array([.35, .17, .23, .08, .17])
3 expected = expected_p * sum(observed)
4 chi2, p = stats.chisquare(f_obs=observed, f_exp=expected)
5
6 print("χ² = %.4f" % chi2)
7 print("p = %.4f" % p)
```
#### **Standardized residuals**

#### **Example: families**

Consider all families with exactly 5 children in a given community.

When

we look at the number of boys/girls, there are 6 possible combinations:

A survey was conducted regarding 1022 families with exactly 5 children

Are the observed numbers in the 6 classes representative for a population in which the probability of having a boy is equal to the probability of having a girl, or more concrete 0.5?

1. 5 boys

6. 5 girls

2. 4 boys, 1 girl 3. 3 boys, 2 girls 4. 2 boys, 3 girls 5. 1 boy, 4 girls

#### **Example: families**

Consider all families with exactly 5 children in a given community. When we look at the number of boys/girls, there are 6 possible combinations:

- 1. 5 boys
- 2. 4 boys, 1 girl
- 3. 3 boys, 2 girls
- 4. 2 boys, 3 girls
- 5. 1 boy, 4 girls
- 6. 5 girls

A survey was conducted regarding 1022 families with exactly 5 children

Are the observed numbers in the 6 classes representative for a population in which the probability of having a boy is equal to the probability of having a girl, or more concrete 0.5?

| i      | 0  | 1   | 2   | 3   | 4   | 5  |  |
|--------|----|-----|-----|-----|-----|----|--|
| 𝑜<br>𝑖 | 58 | 149 | 305 | 303 | 162 | 45 |  |

If the assumption is true, the probability

In general (you don't have to know why):

 = ( 5 ) × 0.5 × 0.5 5− =

by a binomial distribution with parameters = 5 and = 0.5. For example,

× (1 − 0.5)

5−2 × ( 5 2 )

> 5! !(5 − )!

× 0.5 

the probability to have 2 boys out of 5 children is equal to:

(0.5) 2 to have boys is determined

| i      | 0  | 1   | 2   | 3   | 4   | 5  |  |
|--------|----|-----|-----|-----|-----|----|--|
| 𝑜<br>𝑖 | 58 | 149 | 305 | 303 | 162 | 45 |  |

If the assumption is true, the probability to have boys is determined by a binomial distribution with parameters = 5 and = 0.5. For example, the probability to have 2 boys out of 5 children is equal to:

$$(\mathbf{0.5})^2 \ast (\mathbf{1} - \mathbf{0.5})^{5-2} \ast \begin{pmatrix} 5\\2 \end{pmatrix}$$

In general (you don't have to know why):

$$\mathbf{m}\_i = \begin{pmatrix} \mathbf{5} \\ \mathbf{i} \end{pmatrix} \ast \mathbf{0}.\mathbf{5}^i \ast \mathbf{0}.\mathbf{5}^{5-i} = \frac{\mathbf{5!}}{\mathbf{i!(5-i)!}} \ast \mathbf{0}.\mathbf{5}^i$$

| 𝑖                          | 0                   | 1                     | 2                     | 3                     | 4                     | 5                   | Total             |
|----------------------------|---------------------|-----------------------|-----------------------|-----------------------|-----------------------|---------------------|-------------------|
| 𝑜<br>𝑖<br>𝜋<br>𝑖<br>𝑒<br>𝑖 | 58<br>0,031<br>31,9 | 149<br>0,156<br>159,7 | 305<br>0,313<br>319,4 | 303<br>0,313<br>319,4 | 162<br>0,156<br>159,7 | 45<br>0,031<br>31,9 | 1022<br>1<br>1022 |
| (𝑜−𝑒)2<br>𝑒<br>𝑟<br>𝑖      | 21,268<br>4,686     | 0,715<br>-0,921       | 0,647<br>-0,970       | 0,840<br>-1,105       | 0,033<br>0,199        | 5,343<br>2,348      | 28,846            |

#### 1. **Formulate both hypotheses**

- <sup>0</sup> : the sample is representative for the population ○ <sup>1</sup> : the sample is not representative for the population
- 2. **Determine and** : = 0.01 and = 1022.
- 3. **Value of the test statistic in the sample**:

$$\chi^2 = \sum\_{i=1}^{n} \frac{(\mathbf{o}\_i - \mathbf{e}\_i)^2}{\mathbf{e}\_i} = \mathbf{28.846}$$

4. **Calculate and plot critical area**: The critical value is 15.0863. Our test statistic is inside the critical area, so we can reject <sup>0</sup> .

#### **Standardized Residuals**

#### **Standardized Residuals**

**The standardized residuals indicate which classes make the greatest contribution to the value of** 2 **.**

$$r\_i = \frac{\mathbf{o}\_i - n\boldsymbol{\pi}\_i}{\sqrt{n\boldsymbol{\pi}\_i(1-\boldsymbol{\pi}\_i)}}$$

- ∈ [−2, 2] ⇒ "acceptable" values
- < −2 ⇒ underrepresented
- > 2 ⇒ overrepresented

**Conclusion:** families in which all children are of the same gender are overrepresented.

#### **Cochran's rules**

#### **Conditions**

In order to apply the 2 -test, the following conditions must be met (Rule of Cochran)

- 1. For all categories, the expected frequency must be greater than 1.
- 2. In a maximum of 20 % of the categories, the expected frequency may be less than 5.
#### **Module 5. Bivariate analysis: qualitative — quantitative Data Science**

**Sabine De Vreese Lieven Smits Pieter Van Der Helst Bert Van Vreckem 2024–2025**

#### **Contents**

Data visualization

Two-sample t-test

Paired samples

Effect size

# **Learning goals**

- Apply the -test for two samples
- Calculate effect size using Cohen's
- Visualization

# **Bivariate analysis: overview**

| Independent  | Dependent    | Test/Metric             |
|--------------|--------------|-------------------------|
| Qualitative  | Qualitative  | 2<br>𝜒<br>-test         |
|              |              | 𝑉<br>Cramér's           |
| Qualitative  | Quantitative | two-sample<br>𝑡-test    |
|              |              | Cohen's<br>𝑑            |
| Quantitative | Quantitative | —                       |
|              |              | Regression, correlation |

### **Example research questions**

- Are male penguins larger than females?
- Do men get a higher salary than women?
- Does a new vaccine protect against a disease?
- Does "retrieval practice" improve learning outcomes (i.e. student grades)?
- …

In these examples, what is the independent/dependent variable?

#### **Data visualization**

# **Data visualization**

- Chart types for quantitative data
- Grouped by qualitative variable

Suitable chart types: ● Grouped boxplot

● …

● Grouped density plot ● Bar chart with error bars

# **Data visualization**

- Chart types for quantitative data
- Grouped by qualitative variable

Suitable chart types:

- Grouped boxplot
- Grouped density plot
- Bar chart with error bars

● …

#### **Grouped boxplot**

(source code: see demo-5.01-2sample-t.ipynb)

## **Grouped violin plot**

# **Grouped density plot**

# **Beware! Bar chart of group**

#### **means**

**FAIL**

# **Beware! Bar chart of group**

#### **means**

## **Bar chart with error bars**

- Always add error bars!
- Only makes sense for normally distributed data
- Example: 1 standard deviation:

#### **Two-sample t-test**

# **Comparing two population means**

Are the population means of two populations different?

We use two *samples* to perform an appropriate statistical test.

Correct test depends on:

- Independent samples
- Paired samples

In a clinical study, the aim is to determine whether a new drug has a delayed (i.e. higher) reaction time as a side effect.

- Control group: 6 participants receive placebo
- Intervention group: 6 participants receive medicine

Next, the reaction time (in ms) is measured:

group?

● Control group: 91, 87, 99, 77, 88, 91 ( = 88.83)

● Intervention group: 101, 110, 103, 93, 99, 104 ( = 101.67)

Are there significant differences between the intervention and control

In a clinical study, the aim is to determine whether a new drug has a delayed (i.e. higher) reaction time as a side effect.

- Control group: 6 participants receive placebo
- Intervention group: 6 participants receive medicine

Next, the reaction time (in ms) is measured:

- Control group: 91, 87, 99, 77, 88, 91 ( = 88.83)
- Intervention group: 101, 110, 103, 93, 99, 104 ( = 101.67)

Are there significant differences between the intervention and control group?

#### **Testing procedure**

- 1. Hypotheses:
	- <sup>0</sup> : <sup>1</sup> − <sup>2</sup> = 0 ○ <sup>1</sup> : <sup>1</sup> − <sup>2</sup> < 0
- 2. Significance level: = 0.05
- 3. Test statistic is based on:
	- − = −12.833
	- = estimation for <sup>1</sup> (control group)
	- = estimation for <sup>2</sup> (intervention group)
	- Takes the variances of the samples into account. For completeness the test statistic is

$$\mathbf{t} = \frac{\overline{\mathbf{x}} \mathbf{-} \overline{\mathbf{y}}}{\sqrt{\mathbf{s}\_{\mathbf{x}}^{2}/n\_{\mathbf{x}} \star \mathbf{s}\_{\mathbf{y}}^{2}/n\_{\mathbf{y}}}} \cdot \mathbf{t}$$

#### 4. Calculate

#### **Calculation in Python**

The calculation of the test statistic and the associated -value is done by stats.ttest\_ind()

control = np.array([91, 87, 99, 77, 88, 91]) treatment = np.array([101, 110, 103, 93, 99, 104]) stats.ttest\_ind(a=control, b=treatment, alternative='less', equal\_var=False)

Result:

```
Ttest_indResult(statistic=-3.445612673536487,
pvalue=0.003391230079206901)
```
**Testing procedure (continued)**

5. Draw conclusion based on -value.

 ≈ 0.00339 < = 0.05. We reject the null hypothesis. In this sample, there is reason to assume that the drug does indeed increase reaction time.

A study examined whether cars that run on petrol with additives have a lower consumption, i.e. a higher miles per gallon. For 10 cars, the consumption was measured (expressed in miles per gallon) for both fuel types:

| Car            | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 |
|----------------|----|----|----|----|----|----|----|----|----|----|
| Regular petrol | 16 | 20 | 21 | 22 | 23 | 22 | 27 | 25 | 27 | 28 |
| With additives | 19 | 22 | 24 | 24 | 25 | 25 | 25 | 26 | 28 | 32 |

#### **Testing procedure** 1. Hypotheses:

- - <sup>0</sup> : − = 0 ○ <sup>1</sup> : − < 0
- 2. Significance level: = 0.05
- 3. Test statistic:

○ Based on the mean of the difference = −

| Regular petrol | 16 | 20 | 21 | 22 | 23 | 22 | 27 | 25 | 27 | 28 |
|----------------|----|----|----|----|----|----|----|----|----|----|
| With additives | 19 | 22 | 24 | 24 | 25 | 25 | 25 | 26 | 28 | 32 |
| Difference     | -3 | -2 | -3 | -2 | -2 | -3 | 2  | -1 | -1 | -4 |

○ For completeness, the test statistic is

$$\mathbf{t} = \frac{d}{\mathbf{s}\_d / \sqrt{n}}$$

#### 4. Calculate

**Calculation in Python**

regular = np.array([16, 20, 21, 22, 23, 22, 27, 25, 27, 28]) additives = np.array([19, 22, 24, 24, 25, 25, 26, 26, 28, 32]) stats.ttest\_rel(regular, additives, alternative='less')

Result:

Ttest\_relResult(statistic=-4.47213595499958, pvalue=0.00077494295585091)

**Testing procedure**

5. Draw conclusion based on -value.

 ≈ 0.0007749 < = 0.05. We reject the null hypothesis. In this sample, there is reason to assume that the fuel with additives leads to lower fuel consumption, i.e. higher miles per gallon.

#### **Effect size**

## **Effect size**

#### **Effect size**

**The effect size is a metric which expresses how great the difference between two groups is**

- Control group vs. intervention group
- Can be used in addition to hypothesis test
- Often used in educational sciences
- There are several definitions, here: *Cohen's*

#### **Cohen's**

$$d = \frac{\overline{\mathbf{x}\_1} - \overline{\mathbf{x}\_2}}{\mathbf{s}}$$

where <sup>1</sup> and <sup>2</sup> represent the sample means and the pooled standard deviation, i.e. standard deviation of both groups combined:

$$\mathbf{s} = \sqrt{\frac{(n\_1 - 1)\mathbf{s}\_1^2 + (n\_2 - 1)\mathbf{s}\_2^2}{n\_1 + n\_2 - 2}}$$

with <sup>1</sup> , <sup>2</sup> the sample sizes, and <sup>1</sup> , <sup>2</sup> the standard deviations of both groups

#### **Interpretation Cohen's**

| d    | Effect Size |
|------|-------------|
| 0.01 | Very small  |
| 0.2  | Small       |
| 05   | Average     |
| 08   | Large       |
| 1.2  | Very large  |
| 2.0  | Huge        |

In educational sciences (John Hattie):

- 0,4 = tipping point for desired effects
- effect size = 1: process material that would normally take 1 year in 6 months!

E.g. https://visible-learning.org/ backup-hattie-ranking-256-effects-2017/

# **Typical approach research in education**

- Research question: Is X a good learning strategy, in other words, does this have a positive effect on final results?
- Control group uses "traditional" approach
- Intervention group uses X
- Followed by an evaluation moment
- Determine scores, calculate
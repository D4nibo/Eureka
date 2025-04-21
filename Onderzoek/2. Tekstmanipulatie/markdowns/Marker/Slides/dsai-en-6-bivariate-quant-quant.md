## **Module 6. Bivariate analysis: quantitative—quantitative Data Science**

**Sabine De Vreese Lieven Smits Pieter Van Der Helst Bert Van Vreckem 2024–2025**

# **Contents**

Data visualization

Linear regression

Covariance

Pearson's correlation coefficient

Coefficient of determination

# **Learning goals**

- Determine the equation of the regression line and plot it;
- Calculate the covariance , the correlation coefficient and the coefficient of determination 2
- Interpret these values using the correct terms;
- Visualization

# **Bivariate analysis: overview**

| Independent  | Dependent    | Test/Metric                          |
|--------------|--------------|--------------------------------------|
| Qualitative  | Qualitative  | 2<br>𝜒<br>-test<br>𝑉<br>Cramér's     |
| Qualitative  | Quantitative | two-sample<br>𝑡-test<br>Cohen's<br>𝑑 |
| Quantitative | Quantitative | —<br>Regression, correlation         |

# **Data visualization**

# **Data visualization**

To visualize quantitative data, we use a *scatter plot*

- X-axis: independent variable
- Y-axis: dependent variable
- Each point corresponds to an observation

## **Data visualization**

**Scatterplot**

Source: Horst A., et al. (2020) palmerpenguins: Palmer Archipelago (Antarctica) penguin data, https://allisonhorst.github.io/palmerpenguins/

With **regression** we will try to find a **consistent** and **systematic** relationship between two quantitative variables.

- 1. **Monotonic:** consistent direction of the relationship between the two variables: increasing or decreasing
- 2. **Non-monotonic:** value of dependent variable changes systematically with value of independent variable, but the direction is not consistent

A *linear* relationship between an independent and dependent variable.

Characteristics:

- Presence: is there a relationship?
- Direction: increasing or decreasing?
- Strength of the relationship: strong, moderate, weak, nonexistent, …

|   | X     | y                                                 | (x-x)     | (y-y)                             | (x-x)(y-y)                                                     | (x-x) -   |
|---|-------|---------------------------------------------------|-----------|-----------------------------------|----------------------------------------------------------------|-----------|
| 0 |       |                                                   |           |                                   | 187.0 3250.00000 -12.823529 -641.274510 8223.402537 164.442907 |           |
| 1 | 191.0 | 3400.000000                                       |           | -8.823529 -491.274510 4334.775087 |                                                                | 77.854671 |
| വ | 193.0 |                                                   |           |                                   | 3741.666667 -6.823529 -149.607843 1020.853518 46.560554        |           |
| ന | 194.0 | 3775.0000000                                      | -5.823529 | -116.274510                       | 677.128028                                                     | 33.913495 |
| ব | 195.0 | 4000.000000 - -4.823529 - 108.725490 - 524.440600 |           |                                   |                                                                | 23.266436 |
| ഗ | 196.0 | 3725.000000 - -3.823529                           |           | -166,274510 635,755479            |                                                                | 14.619377 |
| ് | 197.0 | 3675.000000                                       |           | -216.274510 610.657439            |                                                                | 7.972318  |
|   |       | 2700 000000                                       | 4000000   | 104 371010                        | 240 704001                                                     | 2 235000  |

…

#### **Equation**

The regression line has the following equation:

$$
\hat{\mathbf{y}} = \mathcal{B}\_1 \mathbf{x} + \mathcal{B}\_0 \mathbf{y}
$$

with:

$$\mathcal{B}\_1 = \frac{\sum\_{i=1}^n (\chi\_i - \overline{\chi})(\chi\_i - \overline{\chi})}{\sum\_{i=1}^n (\chi - \overline{\chi})^2} = \frac{29375.49}{756.47} = 38.83$$

$$\mathcal{B}\_0 = \overline{\chi} - \mathcal{B}\_1 \overline{\chi} = 38971.27 - 38.83 \times 199.82 = -3868.333$$

$$\hat{\mathcal{Y}} = 38.83 \times -3868.33$$

Note: ̂ indicates "an estimation for "

| HO GENT |
|---------|
|         |

#### **Covariance**

**Covariance is a measure that indicates whether a relationship between two variables is increasing or decreasing.**

$$\mathsf{Cov}(\mathsf{X}, \mathsf{Y}) = \frac{1}{n - 1} \sum\_{i=1}^{n} (\mathsf{x}\_i - \overline{\mathsf{x}})(\mathsf{y}\_i - \overline{\mathsf{y}})$$

Cov > 0: increasing Cov ≈ 0: no relationship Cov < 0: decreasing **Note** Covariance of population (denominator ) vs. sample (denominator − 1)

19/28

$$\mathsf{Cov}(\mathsf{X}, \mathsf{Y}) \simeq \frac{2\mathsf{P375.49}}{17 - 1} \simeq \mathsf{1835.97}$$

- > 0 ⇒ increasing relationship
- What if body mass was expressed in kg instead of g?

**Covariance has limited use as a measure of the relationship between two variables.**

# **Pearson's correlation coefficient**

# **Pearson correlation coefficient**

**Pearson's Correlation Coefficient**

**Pearson's product-moment correlation coefficient is a measure for the strength of a linear correlation between and**

 = (, ) (1) = ∑ =1( − )( − ) √∑ =1( − )<sup>2</sup>√∑ =1( − )<sup>2</sup> (2) ∈ [−1, +1]

# **Correlation coefficient**

**Some datasets and their R-value**

Source: Wikipedia https://en.wikipedia.org/wiki/Pearson\_correlation\_coefficient

# **Coefficient of determination**

# **Coefficient of determination**

### **Coefficient of determination**

**The coefficient of determination** <sup>2</sup> **explains the percentage of the variance of the observed values relative to the regression line.**

 2 : percentage variance observations explained by the regression line 1 − <sup>2</sup> : percentage variance observations *not* explained by regression

## **Interpretation of and** <sup>2</sup> **values**

| 𝑅           | 2<br>𝑅     | Explained variance | Interpretation |
|-------------|------------|--------------------|----------------|
| < 0.3       | < 0.1      | < 10%              | very weak      |
| 0.3 − 0.5   | 0.1 − 0.25 | 10 − 25%           | weak           |
| 0.5 − 0.7   | 0.25 − 0.5 | 25 − 50%           | moderate       |
| 0.7 − 0.85  | 0.5 − 0.75 | 50 − 75%           | strong         |
| 0.85 − 0.95 | 0.75 − 0.9 | 75 − 90%           | very strong    |
| > 0.95      | > 0.9      | > 90%              | exceptional(!) |

# **Strength of relationship**

**Example chinstrap penguins**

$$\begin{aligned} \mathsf{Cov}(\mathsf{X}, \mathsf{Y}) &\approx \frac{2\mathsf{P3}\overline{\mathsf{T}}\overline{\mathsf{T}}\overline{\mathsf{A}}\mathsf{9}}{\mathsf{1}\mathsf{T}-\mathsf{1}} \approx \mathsf{1835.97} \\\ R &= \frac{\mathsf{Cov}(\mathsf{X}, \mathsf{Y})}{\sigma\_{\mathsf{x}}\sigma\_{\mathsf{y}}} \\ &\approx \frac{\mathsf{1835.968}}{\mathsf{6.876} \times \mathsf{322.935}} \approx \mathsf{0.827} \\\ R^{2} &\approx \mathsf{0.827^{2}} \approx \mathsf{0.684} \end{aligned}$$

**Conclusion:** There is a strong linear and increasing relationship between flipper length and body mass of male chinstrap penguins. 68.4% of the variance in body mass can be explained by the variance in flipper length.

# **Considerations**

- The correlation coefficient only looks at the relationship between **two variables**. Interactions with other variables are not considered.
- The correlation coefficient explicitly does **not** assume a **causal** relationship.
- Pearson's correlation coefficient only expresses **linear** relationships.
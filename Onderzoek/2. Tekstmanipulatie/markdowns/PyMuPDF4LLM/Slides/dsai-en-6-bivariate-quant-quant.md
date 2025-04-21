# **Module 6. Bivariate analysis:** **quantitative—quantitative**
### **Data Science**

**Sabine De Vreese** **Lieven Smits** **Pieter Van Der Helst** **Bert Van Vreckem**

**2024–2025**


1/28


-----

# **Contents**

Data visualization

Linear regression

Covariance

Pearson’s correlation coefficient

Coefficient of determination

2/28


-----

# **Learning goals**

   - Determine the equation of the regression line and plot it;

   - Calculate the covariance 𝐶𝑜𝑣, the correlation coefficient 𝑅 and the
coefficient of determination 𝑅 [2]

   - Interpret these values using the correct terms;

   - Visualization

3/28


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

4/28


-----

# **Data visualization**


5/28


-----

# **Data visualization**

To visualize quantitative data, we use a *scatter plot*

   - X-axis: independent variable

   - Y-axis: dependent variable

   - Each point corresponds to an observation


-----

# **Data visualization**

**Scatterplot**

Source: Horst A., et al. (2020) palmerpenguins: Palmer Archipelago (Antarctica) penguin data,

[https://allisonhorst.github.io/palmerpenguins/](https://allisonhorst.github.io/palmerpenguins/)


-----

# **Linear regression**


8/28


-----

# **Linear Regression**

With **regression** we will try to find a **consistent** and **systematic**
relationship between two quantitative variables.

1. **Monotonic:** consistent direction of the relationship between the two
variables: increasing or decreasing

2. **Non-monotonic:** value of dependent variable changes
systematically with value of independent variable, but the direction
is not consistent

9/28


-----

# **Linear Regression**

A *linear* relationship between an independent and dependent variable.

Characteristics:

   - Presence: is there a relationship?

   - Direction: increasing or decreasing?

   - Strength of the relationship: strong, moderate, weak, nonexistent, …

10/28


-----

# **Linear Regression**


-----

# **Linear Regression**


-----

# **Method of least squares**

13/28


-----

# **Method of least squares**

14/28


-----

# **Method of least squares**

…

15/28


-----

# **Method of least squares**

**Equation**

The regression line has the following equation:

̂𝑦= 𝛽 1 𝑥+ 𝛽 0

with:


∑ [𝑛] 𝑖=1 [(𝑥] 𝑖 [−𝑥)(𝑦] 𝑖 [−𝑦)]
𝛽 1 =

[𝑛] [2]


≈38.83
756.47



[(𝑥] 𝑖 [−𝑥)(𝑦] 𝑖 [−𝑦)]

≈ [29375.49]
∑ [𝑛] 𝑖=1 [(𝑥−𝑥)] [2] 756.47


𝛽 0 = 𝑦−𝛽 1 𝑥≈3891.27 −38.83 × 199.82 ≈−3868.33

̂𝑦= 38.83𝑥−3868.33

Note: ̂𝑦 indicates “an estimation for 𝑦”


16/28


-----

# **Covariance**


17/28


-----

# **Covariance**




1
Cov(𝑋, 𝑌) =
𝑛−1


𝑛
∑(𝑥 𝑖 −𝑥)(𝑦 𝑖 −𝑦)
𝑖=1


Cov > 0: increasing
Cov ≈0: no relationship
Cov < 0: decreasing
**Note** Covariance of population (denominator 𝑛)
vs. sample (denominator 𝑛−1)


18/28


-----

# **Covariance**

19/28


-----

# **Covariance**

𝐶𝑜𝑣(𝑋, 𝑌) ≈ [29375.49] ≈1835.97

17 −1

  - 𝐶𝑜𝑣> 0 ⇒ increasing relationship

   - What if body mass was expressed in kg instead of g?



20/28


-----

# **Pearson’s correlation coefficient**


21/28


-----

# **Pearson correlation coefficient**




𝑅= [𝐶𝑜𝑣] [(] [𝑋, 𝑌] [)] (1)

𝜎 𝜎
𝑥 𝑦

∑ [𝑛] 𝑖=1 [(𝑥] 𝑖 [−𝑥)(𝑦] 𝑖 [−𝑦)]
=

(2)
√∑ 𝑖=1 [𝑛] [(𝑥] 𝑖 [−𝑥)] [2] ~~[√]~~ [∑] [𝑛] 𝑖=1 [(𝑦] 𝑖 [−𝑦)] [2]

𝑅∈[−1, +1]


22/28


-----

# **Correlation coefficient**

**Some datasets and their R-value**

[Source: Wikipedia https://en.wikipedia.org/wiki/Pearson_correlation_coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)


-----

# **Coefficient of determination**


24/28


-----

# **Coefficient of determination**




𝑅 [2] : percentage variance observations explained by the regression line
1 −𝑅 [2] : percentage variance observations *not* explained by regression


25/28


-----

# Interpretation of 𝑅 and 𝑅 [2] values

|𝑅| 𝑅 [2] Explained variance Interpretation

< 0.3 < 0.1 < 10% very weak
0.3 −0.5 0.1 −0.25 10 −25% weak

0.5 −0.7 0.25 −0.5 25 −50% moderate

0.7 −0.85 0.5 −0.75 50 −75% strong
0.85 −0.95 0.75 −0.9 75 −90% very strong

           - 0.95           - 0.9           - 90% exceptional(!)

26/28


-----

# **Strength of relationship**

**Example chinstrap penguins**

𝐶𝑜𝑣(𝑋, 𝑌) ≈ [29375.49] ≈1835.97

17 −1

𝑅= [𝐶𝑜𝑣] [(] [𝑋, 𝑌] [)]

𝜎 𝜎
𝑥 𝑦

1835.968
≈
6.876 × 322.935 [≈0.827]

𝑅 [2] ≈0.827 [2] ≈0.684

**Conclusion:** There is a strong linear and increasing relationship between
flipper length and body mass of male chinstrap penguins. 68.4% of the
variance in body mass can be explained by the variance in flipper length.


-----

# **Considerations**

   - The correlation coefficient only looks at the relationship between
**two variables** . Interactions with other variables are not considered.

   - The correlation coefficient explicitly does **not** assume a **causal**
relationship.

   - Pearson’s correlation coefficient only expresses **linear** relationships.

28/28


-----


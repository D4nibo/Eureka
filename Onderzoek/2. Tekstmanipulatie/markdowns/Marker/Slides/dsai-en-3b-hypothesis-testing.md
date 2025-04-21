#### **Module 3b. Hypothesis testing Data Science**

**Sabine De Vreese Lieven Smits Pieter Van Der Helst Bert Van Vreckem 2024–2025**

Testing procedure

Probability Value

Critical Region

Examples

Student's t-test

Errors in Hypothesis Tests

# **Learning Goals**

- Statistical hypothesis testing concepts
- Hypothesis testing procedure
- Apply the and -test

#### **Testing procedure**

# **Statistical Hypothesis Testing**

**Hypothesis** Idea that has yet to be proven: statement regarding the numeric value of a population parameter **Hypothesis Test** verification of a statement about the values of one or multiple population parameters **Null Hypothesis (**<sup>0</sup> **)** Base hypothesis, we start with assuming it is true

**Alternative Hypothesis (**<sup>1</sup> **, )** Conclusion if the null hypothesis is unlikely to be true

## **Elements of a testing procedure**

**Test Statistic** The value that is calculated from the sample **Region of Acceptance** The region of values supporting the null hypothesis **Critical Region / Region of Rejection** The region of values rejecting the null hypothesis **Significance Level** The probability of rejecting a true null hypothesis <sup>0</sup>

# **Testing procedure**

- 1. Formulate both hypotheses (<sup>0</sup> and <sup>1</sup> )
- 2. Determine the significance level ()
- 3. Calculate the test statistic
- 4. Determine the critical region or the probability value
- 5. Draw conclusions

#### **Hypotheses about superheroes**

#### **A superhero rescues 3.3 persons a day**

Source: http://www.cracked.com/quick-fixes/ 4-people-who-saved-day-while-dressed-as-superheroes/ Assume that, over a period of 30 days, on average 3.483 people were saved each day ( = 3.483, = 30)

- 1. Hypothesis: <sup>0</sup> ∶ = 3.3; <sup>1</sup> ∶ > 3.3
- 2. Significance level: = 0.05
- 3. Test statistic: = 3.483

Standard deviation of the population (assumed to be known): = 0.55

#### **Calculate test statistic**

#### **Probability Value**

# **Probability Value**

#### **-value**

**The -value is the probability, if the null hypothesis is true, to obtain a value for the test statistic that is at least as extreme as the observed value.**

- -value < ⇒ reject <sup>0</sup> : the discovered value of is too extreme;
- -value ≥ ⇒ do not reject <sup>0</sup> : the discovered value of can still be explained by coincidence.

#### **Probability Value**

$$P\{\mathsf{M} > \mathsf{3.483}\} = P\left(Z > \frac{\mathsf{3.483} - \mathsf{3.3}}{\frac{\sigma}{\sqrt{n}}}\right) = P\{Z > \mathsf{3.822}\} = 0.0344 \quad \begin{array}{c} \mathsf{H} \\ \mathsf{O} \\ \mathsf{G} \boxminus \mathsf{N} \mathsf{T} \end{array}$$

# **Critical Region**

# **Critical Region**

#### **Critical region**

**The critical region is the collection of all values of the test statistic for which we can reject the null hypothesis.**

We look for a critical value for which:

( > ) =

Determine for which:

$$\mathcal{P}(\mathbb{Z} > \mathbf{z}\_{\alpha}) = \alpha \Rightarrow g = \mu \star \mathbf{z}\_{\alpha} \cdot \frac{\sigma}{\sqrt{n}}$$

- Left of : region of acceptance (do not reject <sup>0</sup> )
- Right of : critical region (reject <sup>0</sup> )

## **Left-tailed testing**

What would you have to change in the equation in order to calculate the correct critical value?

Answer:

because

= − ×

( < ) = ( <

 √

 − √

) = 0.05

### **Left-tailed testing**

What would you have to change in the equation in order to calculate the correct critical value? Answer:

$$\mathbf{g} = \boldsymbol{\mu} - \mathbf{z} \ast \frac{\boldsymbol{\sigma}}{\sqrt{n}}$$

because

$$P(\mathsf{M} < \mathsf{g}) = P\left(Z < \frac{\mathsf{g} - \mu}{\frac{\sigma}{\sqrt{n}}}\right) = \mathbf{0}.\mathbf{0}\mathbf{5}$$

#### **Left-tailed testing**

Because of symmetry:

$$P\left(Z > -\left(\frac{g-\mu}{\frac{\sigma}{\sqrt{n}}}\right)\right) = 0.05$$

The corresponding -value is 1.645, and therefore:

$$\begin{aligned} \mathbf{z} = \frac{-\mathbf{g} + \mu}{\frac{\sigma}{\sqrt{n}}} &\Leftrightarrow -\mathbf{g} = \frac{\sigma}{\sqrt{n}} \mathbf{z}\_a - \mu \\ &\Leftrightarrow \mathbf{g} = \mu - \mathbf{z}\_a \frac{\sigma}{\sqrt{n}} \end{aligned}$$

$$\mathbf{E}\_{\mathbf{B}}$$

### **Two-tailed testing**

Sometimes it can be necessary to perform a two-tailed test. In this case, two critical values need to be calculated, namely the left and right critical value.

$$\mathbf{g} = \mu \pm \mathbf{z}\_{a/2} \times \frac{\sigma}{\sqrt{n}}\tag{l}$$

$$\mathbf{F}\_{\mathbf{B}}^{\mathbf{B}}$$

### **Summary**

| Goal                                                  | Test regarding the value of the population mean<br>𝜇<br>using a sample of<br>𝑛<br>independent values |                                           |                                                          |
|-------------------------------------------------------|------------------------------------------------------------------------------------------------------|-------------------------------------------|----------------------------------------------------------|
| Prerequisite                                          | De population has a random distribution,<br>𝑛<br>is suffi<br>ciently large                           |                                           |                                                          |
| Test Type                                             | Two-tailed                                                                                           | Left-tailed                               | Right-tailed                                             |
| 𝐻<br>0<br>𝐻<br>1<br>Critical Region<br>Test statistic | 𝜇 = 𝜇<br>0<br>𝜇 ≠ 𝜇<br>0<br> 𝑥 <br>> 𝑔                                                               | 𝜇 = 𝜇<br>0<br>𝜇 < 𝜇<br>0<br>𝑥 < −𝑔<br>𝑧 = | 𝜇 = 𝜇<br>0<br>𝜇 > 𝜇<br>0<br>𝑥 > 𝑔<br>𝑥−𝜇<br>0<br>𝜎<br>√𝑛 |

Table: Summary of Testing Procedures

### **Requirements for -test**

- The sample needs to be random
- The sample size needs to be sufficiently large ( ≥ 30)
- The test statistic needs to have a normal distribution
- The standard deviation of the population, , is known

Sometimes these assumptions will not hold and in this case we can *not* use the -test!

#### **Examples**

#### **Example 1**

When drawing a random sample consisting of 50 observations from a population with variance 2 = 55 we obtain as sample mean = 25. We now want to find out if there is a reason to assume that the population mean is smaller than 27.

### **Example 1**

- **1** Formulate both hypotheses 0 ∶ = 27 en <sup>1</sup> ∶ < 27.
- **2** Determine significance level and sample size = 0.05 en = 50
- **3** Test statistic & value: sample mean = 25

**4a** Probability Value According to the central limit theorem:

$$\mathcal{M} \sim \mathcal{M}or(\mu = \mathcal{Z}\mathcal{T}, \frac{\sigma^2}{\sqrt{n}})$$

$$\mathbf{z} = \frac{\overline{\mathbf{x}} - \mu}{\frac{\sigma}{\sqrt{n}}} = \frac{2\mathbf{5} - 2\mathbf{7}}{\sqrt{\frac{5\mathbf{5}}{50}}} \approx -1.91$$

We therefore have a probability value of 0.0281. Using a significance level of 0.05, we can reject <sup>0</sup> .

**4b** Calculate and plot the critical region

$$\begin{aligned} g &= \mu - \mathbf{z} \ast \frac{\sigma}{\sqrt{n}} \\ &= 27 - 1.645 \ast \sqrt{\frac{\sigma}{n}} \\ &= 25.27470944 \end{aligned}$$

We have that < and therefore we can reject <sup>0</sup> .

**5** Conclusion

We can conclude, based on the sample, that < 27 for a significance level of 0.05

#### **Example 2**

In a reseach about the amount of change in the pockets of our superheroes, researchers state that on average a superhero carries €25 of cash. We assume that the standard deviation of the population = 7. For a random sample of size = 64, the average amount of money a superhero carries is = €23. For the significance level, = 0.05 is selected.

### **Example 2**

- **1** Formulate both hypotheses
	- 0 ∶ = 25 en <sup>1</sup> ∶ ≠ 25
- **2** Determine significance level and sample size = 0.05 en = 64.
- **3** Test statistic & value: = 23

**4b** Calculate the critical region

$$\begin{aligned} g\_1 &= \mu - \mathbf{z} \ast \frac{\sigma}{\sqrt{n}} = 23.28 \\ g\_2 &= \mu + \mathbf{z} \ast \frac{\sigma}{\sqrt{n}} = 26.72 \end{aligned}$$

We have that is inside the critical region (because 23 < 23.28) so we can reject <sup>0</sup> .

**5** Based on this sample we can conclude that superheroes carry on average *less* than 25 €, using a significance level of 5%

#### **Student's t-test**

#### **Student's t-test**

What if the requirements for a -test are not met? E.g.

- Sample size too small
- Population stdev () unknown

If the variable is normally distributed, you can use the -test

#### **The -test**

Determine critical value:

$$\mathbf{g} = \mu \star \mathbf{t} \ast \frac{\mathbf{s}}{\sqrt{n}}$$

- -value is derived from the Student's -distribution, based on the number of *degrees of freedom*, − 1
- Look for value using the function t.isf() in Python
- Apart from this, the procedure is identical to the procedure of the -test

#### **Errors in Hypothesis Tests**

# **Errors in Hypothesis Tests**

|                                              | Reality                                            |                                                     |  |
|----------------------------------------------|----------------------------------------------------|-----------------------------------------------------|--|
| Conclusion                                   | 𝐻<br>True<br>0                                     | 𝐻<br>True<br>1                                      |  |
| 𝐻<br>not rejected<br>0<br>𝐻<br>rejected<br>0 | Correct inference<br>Type I error (false positive) | Type II error (false negative)<br>Correct inference |  |

P(type I error) = (= significance level) P(type II error) = Calculating is *not* trivial, but if ↘ then ↗
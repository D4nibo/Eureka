#### **Module 2. Univariate statistics Data Science**

**Sabine De Vreese Lieven Smits Pieter Van Der Helst Bert Van Vreckem 2024–2025**

#### **Contents**

Central Tendency and Dispersion Measure of Central Tendency Measures of Dispersion Summary

Data visualisation Simple Graphs Interpretation of Charts

## **Learning Goals**

- Descriptive statistics
- Central tendency and dispersion for each measurement level
- Know formulas, being able to calculate
- Suitable visualization techniques for each measurement level

## **Central Tendency and Dispersion**

## **How tall are my friends?**

#### Remember our superheroes:

#### **Measure of Central Tendency**

What value is representative of the entire group?

#### **Mean or Average**

#### **Arithmetic mean**

**The arithmetic mean (notation: ) is the sum of all values divided by the number of values**

$$\overline{\mathbf{x}} = \frac{1}{n} \sum\_{\mathbf{x}=\mathbf{1}}^{n} \mathbf{x}\_{\bar{i}}$$

| 𝑥   | 𝑥   | 𝑥   | 𝑥   | 𝑥   |
|-----|-----|-----|-----|-----|
| 1   | 2   | 3   | 4   | 5   |
| 141 | 198 | 143 | 201 | 184 |

#### **Mean or Average**

**Q1** What happens if Ant-Man shrinks to a size of 10 cm? **Q2** The arithmetic mean of 15 numbers is 12. What number

should be added to get a mean of 13?

## **Median**

#### **Median**

**To find the median, sort all values and pick the middle number**

- Odd number of values: no problem
- Even number of values: average of the middle two

| 𝑥   | 𝑥   | 𝑥   | 𝑥   | 𝑥   |
|-----|-----|-----|-----|-----|
| 1   | 2   | 3   | 4   | 5   |
| 141 | 198 | 143 | 201 | 184 |

### **Median**

**Q1** What happens if Ant-Man shrinks to a size of 10 cm? **Q2** What is the median of the number of people saved by Batman during the last eight years?

#### **Mode**

#### **Mode**

**The mode is the value that appears most often in a dataset.**

Number of people saved by Superman during the last 15 years:

Number of people saved by Batman during the last 8 years:

#### **Measures of Dispersion**

#### How large are the differences within the group?

#### **Range**

**The range of a dataset is the absolute value of the difference between the highest and the lowest value.**

| 𝑥   | 𝑥   | 𝑥   | 𝑥   | 𝑥   |
|-----|-----|-----|-----|-----|
| 1   | 2   | 3   | 4   | 5   |
| 141 | 198 | 143 | 201 | 184 |

## **Quartiles**

#### **Quartiles**

**The quartiles of a sorted set of numbers are the three values that divide the set into 4 equally large subsets. Notation:** <sup>1</sup> **,** <sup>2</sup> **,** <sup>3</sup>

Number of people saved by Superman during the last 15 years:

# **Calculating Quartiles**

- Different software programs have slightly different ways of calculating quartiles.
- The following method is easy to perform by hand. Start by sorting the values.
	- When is odd.
		- The median (<sup>2</sup> ) is the middle value (as before).
		- Leave out the median. <sup>1</sup> is the median of the first half, <sup>3</sup> is the median of the second half.
	- When is even.
		- The median (<sup>2</sup> ) is the average of the two middle values.
		- <sup>1</sup> is the median of the first half, <sup>3</sup> is the median of the second half.

# **Interquartile Range (IQR)**

#### **Interquartile Range**

**The interquartile range is the difference between the third and first quartile** |<sup>3</sup> − <sup>1</sup> |**.**

### **Variance and Standard Deviation**

#### **Variance**

**The variance (** <sup>2</sup> **or** 2 **) is the mean squared difference between the values of a data set and the arithmetic mean.**

$$\mathbf{s}^2 = \frac{1}{n-1} \sum\_{i=1}^{n} (\mathbf{x}\_i - \overline{\mathbf{x}})^2$$

**Standard deviation**

**The standard deviation ( or ) is the square root of the variance**

● Can the standard deviation be negative?

● What is the smallest possible value? What does this imply? ● What effect do outliers have on the standard deviation?

the variable)?

average?

● What is the unit of the standard deviation (in relation to the unit of

● How do you interpret the standard deviation combined with the

- Can the standard deviation be negative?
- What is the smallest possible value? What does this imply?

● What effect do outliers have on the standard deviation?

the variable)?

average?

● What is the unit of the standard deviation (in relation to the unit of

● How do you interpret the standard deviation combined with the

- Can the standard deviation be negative?
- What is the smallest possible value? What does this imply?
- What effect do outliers have on the standard deviation?

● What is the unit of the standard deviation (in relation to the unit of

● How do you interpret the standard deviation combined with the

the variable)?

average?

- Can the standard deviation be negative?
- What is the smallest possible value? What does this imply?
- What effect do outliers have on the standard deviation?
- What is the unit of the standard deviation (in relation to the unit of the variable)?

● How do you interpret the standard deviation combined with the

average?

- Can the standard deviation be negative?
- What is the smallest possible value? What does this imply?
- What effect do outliers have on the standard deviation?
- What is the unit of the standard deviation (in relation to the unit of the variable)?
- How do you interpret the standard deviation combined with the average?

Why − 1 in the denominator and not ? You can prove the reason for the change mathematically, but we will investigate it empirically

See Python example code in demo-analysis-1-var.ipynb

This news item reports on high prices for houses and flats. Do the numbers give a good idea of the situation?

#### **Remember!**

#### **Providing only a center value is never sufficient!**

- What is the dispersion?
- How is the data distributed? Normal distribution?
- Is the group sufficiently homogeneous?

## **Central Tendency and Dispersion: Summary**

| Measurement Level | Center                 | Spread Distribution                                        |
|-------------------|------------------------|------------------------------------------------------------|
| Qualitative       | Mode                   | —                                                          |
| Quantitative      | Average/Mean<br>Median | Variance, Standard Deviation<br>Range, Interquartile Range |

## **Summary of Symbols**

|                    | Population                           | Sample                                 |
|--------------------|--------------------------------------|----------------------------------------|
| number of elements | 𝑁                                    | 𝑛                                      |
| average or mean    | 𝜇                                    | 𝑥                                      |
| variance           | −𝜇)2<br>∑(𝑥<br>2<br>𝑖<br>𝜎<br>=<br>𝑁 | −𝑥)2<br>∑(𝑥<br>2<br>𝑖<br>𝑠<br>=<br>𝑛−1 |
| standard deviation | 𝜎                                    | 𝑠                                      |

#### **Data visualisation**

## **Chart type overview**

| Measurement level | Chart type                           |
|-------------------|--------------------------------------|
| Qualitative       | Bar chart                            |
| Quantitative      | Boxplot<br>Histogram<br>Density plot |

See Python-example code in demo-analysis-1-var.ipynb

## **Pie Chart**

#### **Attention!**

**Avoid using a pie chart!**

Disadvantages:

- Comparing angles is harder than comparing length
- Unusable for data with many categories

## **Pie Chart**

## **Interpretation of Charts**

Tips:

- Label the axes
- Add a clear title
- Name the unit (and, if necessary, order of magnitude)
- Add a label that clarifies the chart

### **Data distortion**

**= misrepresenting data so that invalid conclusions are drawn**

### **Data distortion**

## **Data distraction**

- Avoid bells and whistles
- Minimize "ink to data" ratio

## **The importance of data visualization**

**Anscombe's Quartet** are four completely different datasets with the same measurements of central tendency and dispersion.

"The Datasaurus Dozen" (Source: https://www.autodeskresearch.com/publications/samestats)
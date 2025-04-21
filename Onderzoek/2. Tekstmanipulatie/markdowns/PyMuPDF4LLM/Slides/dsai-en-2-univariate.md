# **Module 2. Univariate statistics**
### **Data Science**

**Sabine De Vreese** **Lieven Smits** **Pieter Van Der Helst** **Bert Van Vreckem**

**2024–2025**


1/33


-----

# **Contents**

Central Tendency and Dispersion

Measure of Central Tendency
Measures of Dispersion
Summary

Data visualisation

Simple Graphs
Interpretation of Charts

2/33


-----

# **Learning Goals**

   - Descriptive statistics

   - Central tendency and dispersion for each measurement level

   - Know formulas, being able to calculate

   - Suitable visualization techniques for each measurement level

3/33


-----

# **Central Tendency and** **Dispersion**


4/33


-----

# **How tall are my friends?**

Remember our superheroes:



200

180

160

140

120

100

80

60

40

20

0





|Col1|198 cm 201 cm 184 cm|
|---|---|
||184 cm|
|||
||141 cm 143 cm|
|||
|||
|||
|||
|||
|||
|||


5/33


-----

# **Measure of Central Tendency**
## What value is representative of the entire group?

6/33


-----

# **Mean or Average**




𝑥= [1]

𝑛


𝑛

𝑥
∑ 𝑖
𝑥=1


|𝑥 1|𝑥 2|𝑥 3|𝑥 4|𝑥 5|
|---|---|---|---|---|
|141|198|143|201|184|


7/33


-----

# **Mean or Average**

**Q1** What happens if Ant-Man shrinks to a size of 10 cm?

**Q2** The arithmetic mean of 15 numbers is 12. What number
should be added to get a mean of 13?

8/33


-----

# **Median**





- Odd number of values: no problem

- Even number of values: average of the middle two

|𝑥 1|𝑥 2|𝑥 3|𝑥 4|𝑥 5|
|---|---|---|---|---|
|141|198|143|201|184|


9/33


-----

# **Median**

**Q1** What happens if Ant-Man shrinks to a size of 10 cm?

**Q2** What is the median of the number of people saved by
Batman during the last eight years?

10/33


-----

# **Mode**




Number of people saved by Superman during the last 15 years:

Number of people saved by Batman during the last 8 years:


11/33


-----

# **Measures of Dispersion**
## How large are the differences within the group?

12/33


-----

# **Range**




|𝑥 1|𝑥 2|𝑥 3|𝑥 4|𝑥 5|
|---|---|---|---|---|
|141|198|143|201|184|


13/33


-----

# **Quartiles**




Number of people saved by Superman during the last 15 years:


14/33


-----

# **Calculating Quartiles**

   - Different software programs have slightly different ways of
calculating quartiles.

   - The following method is easy to perform by hand. Start by sorting
the values.

     - When 𝑛 is odd.

– The median (𝑄 2 ) is the middle value (as before).
– Leave out the median. 𝑄 1 is the median of the first half, 𝑄 3 is the median
of the second half.

     - When 𝑛 is even.

– The median (𝑄 2 ) is the average of the two middle values.

–
𝑄 1 is the median of the first half, 𝑄 3 is the median
of the second half.

15/33


-----

# **Interquartile Range (IQR)**




16/33


-----

# **Variance and Standard Deviation**




1
𝑠 [2] =
𝑛−1


𝑛
∑(𝑥 𝑖 −𝑥) [2]
𝑖=1




|𝑥 1|𝑥 2|𝑥 3|𝑥 4|𝑥 5|
|---|---|---|---|---|
|141|198|143|201|184|


17/33


-----

# **Properties of the Standard** **Deviation**

   - Can the standard deviation be negative?

18/33


-----

# **Properties of the Standard** **Deviation**

   - Can the standard deviation be negative?

   - What is the smallest possible value? What does this imply?

18/33


-----

# **Properties of the Standard** **Deviation**

   - Can the standard deviation be negative?

   - What is the smallest possible value? What does this imply?

   - What effect do outliers have on the standard deviation?

18/33


-----

# **Properties of the Standard** **Deviation**

   - Can the standard deviation be negative?

   - What is the smallest possible value? What does this imply?

   - What effect do outliers have on the standard deviation?

   - What is the unit of the standard deviation (in relation to the unit of
the variable)?

18/33


-----

# **Properties of the Standard** **Deviation**

   - Can the standard deviation be negative?

   - What is the smallest possible value? What does this imply?

   - What effect do outliers have on the standard deviation?

   - What is the unit of the standard deviation (in relation to the unit of
the variable)?

   - How do you interpret the standard deviation combined with the
average?

18/33


-----

# **Properties of the Standard** **Deviation**

Why 𝑛−1 in the denominator and not 𝑛?
You can prove the reason for the change mathematically, but we will
investigate it empirically

See Python example code in demo-analysis-1-var.ipynb

19/33


-----

This news item reports on high prices for houses and flats. Do the
numbers give a good idea of the situation?


-----

# **Remember!**




- What is the dispersion?

- How is the data distributed? Normal distribution?

- Is the group sufficiently homogeneous?


21/33


-----

# **Central Tendency and Dispersion:** **Summary**

**Measurement Level** **Center** **Spread Distribution**

Qualitative Mode —

Quantitative Average/Mean Variance, Standard Deviation
Median Range, Interquartile Range

22/33


-----

# **Summary of Symbols**

**Population** **Sample**

number of elements 𝑁 𝑛

average or mean 𝜇 𝑥


𝑖 −𝜇) [2] 𝑠 [2] = ∑(𝑥 𝑖 −𝑥) [2]

𝑁 𝑛−1


variance 𝜎 [2] = ∑(𝑥 𝑖 −𝜇) [2]


𝑁 𝑛−1

standard deviation 𝜎 𝑠


23/33


-----

# **Data visualisation**


24/33


-----

# **Chart type overview**

**Measurement level** **Chart type**

Qualitative Bar chart

Quantitative Boxplot
Histogram
Density plot

See Python-example code in demo-analysis-1-var.ipynb

25/33


-----

# **Pie Chart**




Disadvantages:

 - Comparing angles is harder than comparing length

 - Unusable for data with many categories


26/33


-----

# **Pie Chart**

27/33


-----

# **Interpretation of Charts**

Tips:

                  - Label the axes

                  - Add a clear title

                  - Name the unit (and, if
necessary, order of magnitude)

                  - Add a label that clarifies the
chart

28/33


-----

# **Data distortion**

**= misrepresenting data so that invalid conclusions are drawn**

29/33


-----

# **Data distortion**

30/33


-----

# **Data distraction**

   - Avoid bells and whistles

   - Minimize “ink to data” ratio

31/33


-----

# **The importance of data** **visualization**

**Anscombe’s Quartet** are four completely different datasets with the
same measurements of central tendency and dispersion.

32/33


-----

“The Datasaurus Dozen” (Source:
[https://www.autodeskresearch.com/publications/samestats)](https://www.autodeskresearch.com/publications/samestats)


-----


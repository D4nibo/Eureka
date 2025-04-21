# **Module 7. Time series analysis**
## **Data Science**

**Sabine De Vreese** **Lieven Smits** **Pieter Van Der Helst** **Bert Van Vreckem**

**2024–2025**


1/39


-----

# **Contents**

Time series and predictions

Time series models

Mathematical model

General

Estimating the parameters

Moving average

Simple moving average
Weighted moving average
Double exponential smoothing
Forecasting
Triple exponential smoothing

2/39


-----

# **Learning goals**

   - Concepts, time series models

   - Moving average

   - Exponential smoothing
## **Remark**

You should not memorize the formulas in this module, but you should
understand them!

3/39


-----

# **Time series and predictions**


4/39


-----

# **Time series and predictions**





- Monthly demand for milk

- Annual intake of students at HOGENT

- Price of a share or bond on the stock exchange (hourly, daily, …)

- Number of HTTP requests per second for a website

- Evolution of disk usage on a backup server


5/39


-----

# **Time series and predictions**

May decisions in business operations depend on a forecast of some
quantity

   - General development of future plans (investments, capacity …)

   - Budget planning to avoid shortcomings (operating budget,
marketing budget …)

   - Procurement planning (e.g. storage capacity)

   - Support for financial objectives

   - Avoid uncertainty

6/39


-----

# **Time series and predictions**

Time series are a **statistical** problem: observations vary with time

Figure: Number of heavily wounded in car accidents in Flanders.


-----

# **Time series components**

   - Level

   - Trend

   - Seasonal fluctuations

   - Cyclic patterns

   - Random noise (residuals)

8/39


-----

# **Time series decomposition**

9/39


-----

# **Time series models**


10/39


-----

# **Mathematical model time series**

**The simplest model:**

𝑋 𝑡 = 𝑏+ 𝜀 𝑡 (1)

  - 𝑋 𝑡 : estimate for time series, at time 𝑡

   - 𝑏: the level (a constant), based on **observations** 𝑥 𝑡

  - 𝜀 𝑡 : random **noise** . We assume that 𝜀 𝑡 ∼𝑁𝑜𝑟(𝜇= 0; 𝜎)

11/39


-----

# **Mathematical model time series**

We could also assume that there is a linear relationship:

𝑋 𝑡 = 𝑏 0 + 𝑏 1 𝑡+ 𝜀 𝑡 (2)

with **level** 𝑏 0 and **trend** 𝑏 1 .

Equation 1 and 2 are special cases of the **polynomial** case:

𝑋 𝑡 = 𝑏 0 + 𝑏 1 𝑡+ 𝑏 2 𝑡 [2] + ⋯+ 𝑏 𝑛 𝑡 [𝑛] + 𝜀 𝑡 (3)

12/39


-----

# **General expression time series**

𝑋 𝑡 = 𝑓(𝑏 0, 𝑏 1, 𝑏 2, …, 𝑏 𝑛, 𝑡) + 𝜀 𝑡 (4)

We make these assumptions:

   - We consider two components of variability:

     - the mean of the predictions changes with time

     - the variations to this mean vary randomly

   - The residuals of the model (𝑋 𝑡 −𝑥 𝑡 ) have a constant variance in time
( **homoscedastic** )

13/39


-----

# **Estimating the parameters**

Make **predictions** based on the time series model:

1. select the most suitable model

2. estimation for parameters 𝑏 𝑖 (𝑖∶1, …, 𝑛) based on observations

The estimations ̂𝑏 𝑖 are selected so that they approximate the observed
values as close as possible.

14/39


-----

# **Example**

**Number of heavily wounded in car accidents in Flanders**

15/39


-----

# **Example: parameter estimation**

   - We select the constant model of Equation 1

   - You choose which observations you use to determine 𝑏 [̂], e.g.

1

     - First 70 observations: 𝑏= [̂] 70 [∑] 𝑡=1 [70] [𝑥] 𝑡 [= 346.4]

1

     - Last 50 observations: 𝑏= [̂] 50 [∑] 𝑡=47 [96] [𝑥] 𝑡 [= 290.68]

16/39


-----

# **Example: parameter estimation**

If we want to model the observations with a linear function
𝑋 𝑡 = 𝑏 0 + 𝑏 1 𝑡+ 𝜀 𝑡, then we can use linear regression!

17/39


-----

# **Moving average**


18/39


-----

# **Moving average**





- Notation: SMA

- Hide short-term fluctuations and show long-term trends

- Parameter 𝑚 is the time window


𝑆𝑀𝐴(𝑡) =


𝑡
∑

𝑖=𝑘


𝑥
𝑖
(5)
𝑚


with 𝑘= 𝑡−𝑚+ 1.


19/39


-----

# **Example**

20/39


-----

# **Example: “Golden cross”**

Moving averages are used in the **technical analysis** of stock prices to
discover trends:


-----

# **Weighted moving average**

   - For 𝑆𝑀𝐴, the weights of the observations are equal

   - For a weighted moving average (𝑊𝑀𝐴), more recent observations
gain relatively more weight

   - A specific form of this is single exponential smoothing or the
**exponential moving average** (EMA):

𝑋 𝑡 = 𝛼𝑥 𝑡−1 + (1 −𝛼)𝑋 𝑡−1 (6)

with 𝛼 the smoothing constant (0 < 𝛼< 1), and 𝑡≥3

22/39


-----

# **Exponential smoothing**

Equation 6 is only valid from 𝑡= 3. Hence, we need to choose a suitable
value for 𝑋
2 ourselves. There are several options:

  - 𝑋
2 = 𝑥 1

  - 𝑋 [1]
2 = 𝑚 [∑] 𝑖=1 [𝑚] [𝑥] 𝑖 [(so the mean of the first][ 𝑚] [observations)]

   - make 𝑋
2 equal to a specific objective

   - …

23/39


-----

# **Exponential Smoothing**

**Example of calculation (** 𝛼= 0.1 **)**

𝑡 1 2 3 4 …

𝑥 8 10 11 13 …
𝑡

𝑡

𝑋 1 = undefined

𝑋 = 𝑥
2 1

𝑋 = 0.1 × 10 + 0.9 × 8 = 8.2
3

𝑋 = 0.1 × 13 + 0.9 × 8.2 = 8.68
4

24/39


-----

# **Why “ exponential ”?**

𝑋 𝑡 = 𝛼𝑥 𝑡−1 + (1 −𝛼)𝑋 𝑡−1
= 𝛼𝑥 𝑡−1 + (1 −𝛼) [𝛼𝑥 𝑡−2 + (1 −𝛼)𝑋 𝑡−2 ]

= 𝛼𝑥 𝑡−1 + 𝛼(1 −𝛼)𝑥 𝑡−2 + (1 −𝛼) [2] 𝑋 𝑡−2
or in general:


= 𝛼


𝑡−2
∑(1 −𝛼) [𝑖−1] 𝑥 𝑡−𝑖 + (1 −𝛼) [𝑡−𝑖] 𝑋 𝑡−𝑖, 𝑡≥2
𝑖=1


In other words: older observations have an exponentially
smaller weight.


25/39


-----

# **Exponential smoothing**

𝛼 (1 −𝛼) (1 −𝛼) [2] (1 −𝛼) [3] (1 −𝛼) [4]

0.9 0.1 0.01 0.001 0.0001

0.5 0.5 0.25 0.125 0.062

0.1 0.9 0.81 0.729 0.6561

Table: Values for 𝛼 and (1 −𝛼) [𝑛]

The speed at which the old observations are “forgotten” depends on the
value of 𝛼. For a value of 𝛼 close to 1, old observations are quickly
forgotten, whereas for 𝛼 close to 0, this goes less fast.

26/39


-----

# **Example**

Figure: Single exponential smoothing with 𝛼= 0.1, 0.5

27/39


-----

# **Forecasting**

As a forecast for time 𝑡+ 𝑚 (𝑚 time units in the “future”), we always take
the last estimate of the level:

𝐹(𝑡+ 𝑚) = 𝑋 𝑡

28/39


-----

# **Double exponential smoothing**

Basic exponential smoothing does not work well if there is a trend in the
data

Figure: Exponential smoothing with a trend: the errors keep getting bigger


-----

# **Double exponential smoothing**

We add an additional term to model the trend. We use 𝑏 for the
𝑡
estimation of the trend at time 𝑡> 1:

𝑋 𝑡 = 𝛼𝑥 𝑡 + (1 −𝛼)(𝑋 𝑡−1 + 𝑏 𝑡−1 )

𝑏 𝑡 = 𝛽(𝑋 𝑡 −𝑋 𝑡−1 ) + (1 −𝛽)𝑏 𝑡−1

with 0 < 𝛼< 1 and 0 < 𝛽< 1

  - 𝑏 𝑡 is an estimate for the slope of the trend line

   - Added to the first equation to ensure that the trend is followed

  - 𝑋 𝑡 −𝑋 𝑡−1 is positive or negative, this corresponds to an
increasing/decreasing trend

30/39


-----

# **Double exponential smoothing**

Again, there are different options for selecting the initial values:

𝑋
1 = 𝑥 1

𝑏
1 = 𝑥 2 −𝑥 1

𝑏
1 = [1]

3 [[(𝑥] [2] [ −𝑥] [1] [) + (𝑥] [1] [ −𝑥] [2] [) + (𝑥] [4] [ −𝑥] [3] [)]]

𝑥 −𝑥
𝑏 𝑛 1
1 =

𝑛−1

31/39


-----

# **Predicting (forecasting)**

To make a prediction (forecast) 𝐹(𝑡+ 1) for time 𝑡+ 1 we use:

𝐹(𝑡+ 1) = 𝑋 𝑡 + 𝑏 𝑡

or in general for time 𝑡+ 𝑚:

𝐹(𝑡+ 𝑚) = 𝑋 𝑡 + 𝑚𝑏 𝑡

32/39


-----

# **Example**

**Comparison of Single/Double Exponential Smoothing forecasts**

33/39


-----

# **Triple exponential smoothing**

Some time series have recurring (seasonal) patterns, e.g.

34/39


-----

# **Triple exponential smoothing**

**Or Holt-Winter’s Method**

Notation:

   - 𝐿: length of the seasonal cycle (number of time units)

  - 𝑐 : term that models the seasonal variations
𝑡

  - 𝛾 (gamma): smoothing factor for the seasonal variation

𝑥
𝑡
𝑋 𝑡 = 𝛼 + (1 −𝛼)(𝑋 𝑡−1 + 𝑏 𝑡−1 ) Smoothing
𝑐
𝑡−𝐿

𝑏 𝑡 = 𝛽(𝑋 𝑡 −𝑋 𝑡−1 ) + (1 −𝛽)𝑏 𝑡−1 Trend smoothing

𝑥
𝑡
𝑐 𝑡 = 𝛾 𝑋 + (1 −𝛾)𝑐 𝑡−𝐿 Seasonal smoothing
𝑡

35/39


-----

# **Triple exponential smoothing**

Prediction at time 𝑡+ 𝑚:

𝐹 𝑡+𝑚 = (𝑋 𝑡 + 𝑚𝑏 𝑡 )𝑐 𝑡−𝐿+𝑚

36/39


-----

# **Example**

37/39


-----

# **Quality of a time series model**

38/39


-----

# **Quality of a time series model**

Compare forecast results with actual observations, when they become
available:

   - Mean absolute error: 𝑀𝐴𝐸= 𝑚 [1] [∑] 𝑖=𝑡+1 [𝑡+𝑚] [|𝑥] 𝑖 [−𝐹] 𝑖 [|]

   - Mean squared error 𝑀𝑆𝐸= 𝑚 [1] [∑] 𝑖=𝑡+1 [𝑡+𝑚] [(𝑥] 𝑖 [−𝐹] 𝑖 [)] [2]

If square root of MSE is well below standard deviation over all
observations, you have a good model!

39/39


-----


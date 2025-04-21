#### **Module 7. Time series analysis Data Science**

**Sabine De Vreese Lieven Smits Pieter Van Der Helst Bert Van Vreckem 2024–2025**

Time series models Mathematical model General Estimating the parameters

Moving average Simple moving average Weighted moving average Double exponential smoothing Forecasting Triple exponential smoothing

# **Learning goals**

- Concepts, time series models
- Moving average
- Exponential smoothing

#### **Remark**

You should not memorize the formulas in this module, but you should understand them!

#### **Time series**

**A time series is a sequence of observations of some variable over time.**

- Monthly demand for milk
- Annual intake of students at HOGENT
- Price of a share or bond on the stock exchange (hourly, daily, …)
- Number of HTTP requests per second for a website
- Evolution of disk usage on a backup server

May decisions in business operations depend on a forecast of some quantity

- General development of future plans (investments, capacity …)
- Budget planning to avoid shortcomings (operating budget, marketing budget …)
- Procurement planning (e.g. storage capacity)
- Support for financial objectives
- Avoid uncertainty

Time series are a **statistical** problem: observations vary with time

Figure: Number of heavily wounded in car accidents in Flanders.

# **Time series components**

- Level
- Trend
- Seasonal fluctuations
- Cyclic patterns
- Random noise (residuals)

## **Time series decomposition**

#### **Time series models**

#### **Mathematical model time series**

**The simplest model:**

$$
\lambda\_\mathbf{t} = \mathbf{b} + \varepsilon\_\mathbf{t} \tag{l}
$$

- : estimate for time series, at time
- : the level (a constant), based on **observations**
- : random **noise**. We assume that ∼ ( = 0; )

$$\mathbf{H}$$

#### **Mathematical model time series**

We could also assume that there is a linear relationship:

$$\mathbf{X}\_{\mathbf{t}} = \mathbf{b}\_0 \mathbf{+} \mathbf{b}\_1 \mathbf{t} \star \mathbf{e}\_{\mathbf{t}} \tag{2}$$

with **level** <sup>0</sup> and **trend** <sup>1</sup> .

Equation 1 and 2 are special cases of the **polynomial** case:

 = <sup>0</sup> + <sup>1</sup> + <sup>2</sup> 2 + ⋯ + + (3)

### **General expression time series**

$$\chi\_{\mathbf{t}} = f(\mathbf{b}\_0, \mathbf{b}\_1, \mathbf{b}\_2, \dots, \mathbf{b}\_n, \mathbf{t}) \star \varepsilon\_{\mathbf{t}}$$

We make these assumptions:

- We consider two components of variability:
	- the mean of the predictions changes with time ○ the variations to this mean vary randomly
- The residuals of the model ( − ) have a constant variance in time (**homoscedastic**)

(4)

# **Estimating the parameters**

Make **predictions** based on the time series model:

- 1. select the most suitable model
- 2. estimation for parameters ( ∶ 1, … , ) based on observations

The estimations ̂ are selected so that they approximate the observed values as close as possible.

#### **Example**

#### **Number of heavily wounded in car accidents in Flanders**

#### **Example: parameter estimation**

- We select the constant model of Equation 1
- You choose which observations you use to determine ̂, e.g.
	- First 70 observations: =̂ 1 <sup>70</sup> ∑ 70 =1 = 346.4

## **Example: parameter estimation**

If we want to model the observations with a linear function = <sup>0</sup> + <sup>1</sup> + , then we can use linear regression!

### **Moving average**

# **Moving average**

#### **Moving Average**

**The moving average is a series of averages (means) of the last observations**

- Notation: SMA
- Hide short-term fluctuations and show long-term trends
- Parameter is the time window

$$\mathsf{SMA(t)} = \sum\_{i=k}^{t} \frac{\mathsf{x}\_i}{m}$$

with = − + 1.

### **Example**

### **Example: "Golden cross"**

Moving averages are used in the **technical analysis** of stock prices to discover trends:

# **Weighted moving average**

- For , the weights of the observations are equal
- For a weighted moving average (), more recent observations gain relatively more weight
- A specific form of this is single exponential smoothing or the **exponential moving average** (EMA):

$$
\lambda \chi\_t = \alpha \chi\_{t-1} + (1 - \alpha) \chi\_{t-1} \tag{6}
$$

with the smoothing constant (0 < < 1), and ≥ 3

## **Exponential smoothing**

Equation 6 is only valid from = 3. Hence, we need to choose a suitable value for <sup>2</sup> ourselves. There are several options:

- <sup>2</sup> = <sup>1</sup>
- <sup>2</sup> = 1 ∑ =1 (so the mean of the first observations)
- make <sup>2</sup> equal to a specific objective
- …

## **Exponential Smoothing**

**Example of calculation (** = 0.1**)**

$$\begin{array}{rcl} \mathsf{X}\_{1} & = & \mathsf{undefinced} \\ \mathsf{X}\_{2} & = & \mathsf{x}\_{1} \\ \mathsf{X}\_{3} & = & \mathsf{0}.\mathsf{I} \times \mathsf{I}\mathsf{0} \star \mathsf{0}.\mathsf{9} \star \mathsf{8} = \mathsf{8.2} \\ \mathsf{X}\_{4} & = & \mathsf{0}.\mathsf{I} \times \mathsf{I}\mathsf{3} \star \mathsf{0}.\mathsf{9} \star \mathsf{8.2} = \mathsf{8.68} \end{array}$$

# **Why "***exponential***"?**

$$\begin{aligned} \mathsf{X}\_{\mathsf{t}} &= \alpha \mathsf{x}\_{\mathsf{t}-\mathsf{1}} + (\mathsf{1} - \alpha) \mathsf{X}\_{\mathsf{t}-\mathsf{1}} \\ &= \alpha \mathsf{x}\_{\mathsf{t}-\mathsf{1}} + (\mathsf{1} - \alpha) \left[ \alpha \mathsf{x}\_{\mathsf{t}-\mathsf{2}} + (\mathsf{1} - \alpha) \mathsf{X}\_{\mathsf{t}-\mathsf{2}} \right] \\ &= \alpha \mathsf{x}\_{\mathsf{t}-\mathsf{1}} + \alpha (\mathsf{1} - \alpha) \mathsf{x}\_{\mathsf{t}-\mathsf{2}} + (\mathsf{1} - \alpha)^{2} \mathsf{X}\_{\mathsf{t}-\mathsf{2}} \\ &\quad \text{or in general:} \\ &= \bot \end{aligned}$$

$$\mathbf{t} = \alpha \sum\_{i=1}^{t-2} (\mathbb{1} - \alpha)^{i-1} \mathbf{x}\_{t-i} + (\mathbb{1} - \alpha)^{t-i} \mathbf{x}\_{t-i}, \mathbf{t} \ge \mathbf{2}$$

In other words: older observations have an exponentially smaller weight.

# **Exponential smoothing**

| 𝛼   | (1 − 𝛼) | (1 − 𝛼)2 | (1 − 𝛼)3 | (1 − 𝛼)4 |
|-----|---------|----------|----------|----------|
| 0.9 | 0.1     | 0.01     | 0.001    | 0.0001   |
| 0.5 | 0.5     | 0.25     | 0.125    | 0.062    |
| 0.1 | 0.9     | 0.81     | 0.729    | 0.6561   |

Table: Values for and (1 − )

The speed at which the old observations are "forgotten" depends on the value of . For a value of close to 1, old observations are quickly forgotten, whereas for close to 0, this goes less fast.

# **Example**

Figure: Single exponential smoothing with = 0.1, 0.5

**Forecasting** As a forecast for time + ( time units in the "future"), we always take the last estimate of the level:

$$F(\mathbf{t} \star m) = \mathbf{x}\_{\mathbf{t}}$$

## **Double exponential smoothing**

Basic exponential smoothing does not work well if there is a trend in the data

Figure: Exponential smoothing with a trend: the errors keep getting bigger

# **Double exponential smoothing**

We add an additional term to model the trend. We use for the estimation of the trend at time > 1:

$$\begin{aligned} \mathsf{X}\_{\mathsf{t}} &= \alpha \mathsf{x}\_{\mathsf{t}} + (\mathsf{1} - \alpha)(\mathsf{X}\_{\mathsf{t-1}} + \mathsf{b}\_{\mathsf{t-1}})\\ \mathsf{b}\_{\mathsf{t}} &= \beta(\mathsf{X}\_{\mathsf{t}} - \mathsf{X}\_{\mathsf{t-1}}) + (\mathsf{1} - \beta)\mathsf{b}\_{\mathsf{t-1}} \end{aligned}$$

with 0 < < 1 and 0 < < 1

- is an estimate for the slope of the trend line
- Added to the first equation to ensure that the trend is followed
- − −1 is positive or negative, this corresponds to an increasing/decreasing trend

# **Double exponential smoothing**

Again, there are different options for selecting the initial values:

$$\begin{aligned} \mathsf{X}\_{\mathsf{1}} &= \mathsf{x}\_{\mathsf{1}} \\ \mathsf{b}\_{\mathsf{1}} &= \mathsf{x}\_{2} - \mathsf{x}\_{\mathsf{1}} \\ \mathsf{b}\_{\mathsf{1}} &= \frac{1}{3} \left[ (\mathsf{x}\_{2} - \mathsf{x}\_{\mathsf{1}}) + (\mathsf{x}\_{1} - \mathsf{x}\_{2}) + (\mathsf{x}\_{4} - \mathsf{x}\_{3}) \right] \\ \mathsf{b}\_{\mathsf{1}} &= \frac{\mathsf{x}\_{n} - \mathsf{x}\_{\mathsf{1}}}{n - 1} \end{aligned}$$

# **Predicting (forecasting)**

To make a prediction (forecast) ( + 1) for time + 1 we use:

$$F(\mathbf{t} + \mathbf{1}) = \mathbf{x\_t} + \mathbf{b\_t}$$

or in general for time + :

( + ) = +

#### **Example**

#### **Comparison of Single/Double Exponential Smoothing forecasts**

# **Triple exponential smoothing**

Some time series have recurring (seasonal) patterns, e.g.

# **Triple exponential smoothing**

#### **Or Holt-Winter's Method**

Notation:

- : length of the seasonal cycle (number of time units)
- : term that models the seasonal variations
- (gamma): smoothing factor for the seasonal variation

$$\begin{aligned} \mathsf{X}\_{t} &= \alpha \frac{\mathsf{X}\_{t}}{\mathsf{c}\_{t-\mathsf{L}}} + (\mathsf{1} - \alpha) \mathsf{X}\_{t-\mathsf{1}} + \mathsf{b}\_{t-\mathsf{1}} \\ \mathsf{b}\_{t} &= \beta (\mathsf{X}\_{t} - \mathsf{X}\_{t-\mathsf{1}}) + (\mathsf{1} - \beta) \mathsf{b}\_{t-\mathsf{1}} \\ \mathsf{c}\_{t} &= \mathsf{y} \frac{\mathsf{X}\_{t}}{\mathsf{K}\_{t}} + (\mathsf{1} - \mathsf{y}) \mathsf{c}\_{t-\mathsf{L}} \end{aligned} \qquad \begin{aligned} \mathsf{Smooththing} \\ \mathsf{Trends smoothing} \\ \mathsf{Sesasonal smoothing} \end{aligned}$$

# **Triple exponential smoothing**

Prediction at time + :

+ = ( + )−+

### **Example**

# **Quality of a time series model**

# **Quality of a time series model**

Compare forecast results with actual observations, when they become available:

- Mean absolute error: = <sup>1</sup> ∑ + =+1 | − |
- Mean squared error = <sup>1</sup> ∑ + =+1( − ) 2

If square root of MSE is well below standard deviation over all observations, you have a good model!
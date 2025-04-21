#### **Module 3a. Probability, The Central Limit Theorem, Confidence Intervals Data Science**

**Sabine De Vreese Lieven Smits Pieter Van Der Helst Bert Van Vreckem 2024–2025**

#### **Contents**

#### Probability

Discrete random variables Expectation and variance of a random variable Continuous Random Variables The (Standard) Normal Distribution Probabilities in the Normal Distribution Other Continuous Distributions

From Sample to Population The Central Limit Theorem Confidence Intervals Confidence Interval for a Large Sample Confidence Interval for a Small Sample

### **Learning Goals**

- Probability distribution of a sample
- The normal and Student- distribution
- Formulate the central limit theorem and explain its importance for statistical analysis
- Calculate confidence intervals

#### **Probability**

## **Probability**

Informally, probabilities represent beliefs of how likely it is that a certain event will happen when performing a certain experiment.

In the frequentist view, **probability** represents the **relative frequency** of the occurrence of the event at hand (when performing a large number of independent experiments).

## **Probability: (Simple) Examples**

A fair six-sided die is thrown once.

- What is the probability of getting a "1"?
- What is the probability of throwing an even number?
- What is the probability of getting a number in the set {1, 2, 3, 4, 5, 6}?

Answers: 1/6, 1/2 and 1

## **Probability: (Simple) Examples**

A fair six-sided die is thrown once.

- What is the probability of getting a "1"?
- What is the probability of throwing an even number?
- What is the probability of getting a number in the set {1, 2, 3, 4, 5, 6}?

Answers: 1/6, 1/2 and 1

6/63

## **Probability: Example**

Two games of chance:

- 1. Bet on: at least one six when throwing a fair die 4 consecutive times.
	- You will *win* in the long run when playing this game.
- 2. Bet on: at least one "double six" when throwing two fair dice 24 times.
	- You will *lose* in the long run when playing this game, even though in some sense the two bets seem equivalent. (Probability divided by six but number of throws multiplied by six.)

#### **Probability: Example**

#### **Probability: Observations**

- Probabilities are numbers assigned to sets.
- These sets are part of some all-encompassing set, the "universe", typically denoted .
- The numbers (probabilities) assigned to the sets have to satisfy three simple rules (see later) in order to correspond to our intuition about how probabilities should behave.

For the first game: at least one six when throwing a fair die 4 consecutive times.

● What is the universe?

Answer:

Answer

= {(1, 1, 1, 1), (1, 1, 1, 2), (1, 1, 1, 3), … , (6, 6, 6, 4), (6, 6, 6, 5), (6, 6, 6, 6)}

= {(6, 1, 1, 1), (6, 1, 1, 2), … , (5, 5, 5, 6), (6, 6, 1, 1), …

● What set corresponds to the event: "you win" or "at least one 6"?

(6, 6, 5, 5), (1, 6, 6, 1), … , (6, 6, 6, 6)}

For the first game: at least one six when throwing a fair die 4 consecutive times.

● What is the universe? Answer:

= {(1, 1, 1, 1), (1, 1, 1, 2), (1, 1, 1, 3), … , (6, 6, 6, 4), (6, 6, 6, 5), (6, 6, 6, 6)}

● What set corresponds to the event: "you win" or "at least one 6"?

(6, 6, 5, 5), (1, 6, 6, 1), … , (6, 6, 6, 6)}

= {(6, 1, 1, 1), (6, 1, 1, 2), … , (5, 5, 5, 6), (6, 6, 1, 1), …

Answer

For the first game: at least one six when throwing a fair die 4 consecutive times.

● What is the universe? Answer:

= {(1, 1, 1, 1), (1, 1, 1, 2), (1, 1, 1, 3), … , (6, 6, 6, 4), (6, 6, 6, 5), (6, 6, 6, 6)}

● What set corresponds to the event: "you win" or "at least one 6"?

Answer

= {(6, 1, 1, 1), (6, 1, 1, 2), … , (5, 5, 5, 6), (6, 6, 1, 1), …

(6, 6, 5, 5), (1, 6, 6, 1), … , (6, 6, 6, 6)}

For the first game: at least one six when throwing a fair die 4 consecutive times.

● What is the universe? Answer:

= {(1, 1, 1, 1), (1, 1, 1, 2), (1, 1, 1, 3), … , (6, 6, 6, 4), (6, 6, 6, 5), (6, 6, 6, 6)}

● What set corresponds to the event: "you win" or "at least one 6"? Answer

$$\mathcal{A} = \{ \langle \mathbf{6}, \mathbb{1}, \mathbb{1}, \mathbb{1} \rangle, \langle \mathbf{6}, \mathbb{1}, \mathbb{1}, \mathbb{2} \rangle, \dots, \langle \mathbf{5}, \mathbb{5}, \mathbb{5}, \mathbb{6} \rangle, \langle \mathbf{6}, \mathbb{6}, \mathbb{1}, \mathbb{1} \rangle, \dots \}$$

$$\langle \mathbf{6}, \mathbf{6}, \mathbb{5}, \mathbb{5} \rangle, \langle \mathbb{1}, \mathbb{6}, \mathbb{6}, \mathbb{1} \rangle, \dots, \langle \mathbf{6}, \mathbb{6}, \mathbb{6}, \mathbb{6} \rangle \}$$

## **Axioms (Rules) of Probability**

#### **Axioms of Probability**

- 1. **Probabilities are non-negative:** () ≥ 0 **for each .**
- 2. **The universe has probability** 1**:** () = 1
- 3. *Sum rule***: When and are** *disjoint* **events (i.e.** ∩ = ∅**) then it holds that**

( ∪ ) = () + ()

### **Properties of Probabilities**

From the three axioms of probability, we can derive *all* properties of probabilities. Some important ones are listed below:

● **Complement rule**: for each it holds that

() = 1 − ()

where represents the event "A does not occur".

- The impossible event has probability zero: (∅) = 0.
- The **general sum rule**:

$$P(\mathsf{A}\cup\mathsf{B}) = P(\mathsf{A}) + P(\mathsf{B}) - P(\mathsf{A}\cap\mathsf{B})$$

$$\mathbf{H}\_{\mathbf{H}}$$

- 1. A coin is tampered with such that (head) = 0.6. What is (tail)?
- 2. From the 250 students enrolled in this course, 200 own a PlayStation game console, while 100 own a Nintendo Switch. There are 75 students who own both game consoles. What is the probability, when you pick a random student, that
	- this student does not own a PlayStation
	- this student owns a PlayStation or a Nintendo Switch (or both)
	- this student owns neither a PlayStation nor a Nintendo Switch.

Answers: 1 − 200/250 = 1/5, (200 + 100 − 75)/250 = 225/250 = 9/10,

1 − 9/10 = 1/10

- 1. A coin is tampered with such that (head) = 0.6. What is (tail)?
- 2. From the 250 students enrolled in this course, 200 own a PlayStation game console, while 100 own a Nintendo Switch. There are 75 students who own both game consoles. What is the probability, when you pick a random student, that
	- this student does not own a PlayStation
	- this student owns a PlayStation or a Nintendo Switch (or both)
	- this student owns neither a PlayStation nor a Nintendo Switch.

Answers: 1 − 200/250 = 1/5, (200 + 100 − 75)/250 = 225/250 = 9/10, 1 − 9/10 = 1/10

When events are **independent** it means that the occurrence of one event (or knowing that the event occurred) does **not change** the probability of the other event occurring.

As an example: draw a card from a standard deck of cards and consider the following events:

= a ♣ was drawn

and

= an ace was drawn

When I tell you that occurred, this will not change your opinion about the probability of occurring, this will still be 13/52 = 1/4. (Note: this also works the other way around!)

#### **Independent Events: Definition**

**Independent events**

**Mathematically, two events and are independent when**

( ∩ ) = ()()

Consider the events from before where students own either a PlayStation, a Nintendo Switch or both. Let be the event that a student owns a PlayStation, while represents the fact that a student owns a Nintendo Switch. From the numbers above we see that

$$P(\text{A}) = \frac{200}{250} = 0.8, \quad \text{and} \quad P(\text{B}) = \frac{100}{250} = 0.44$$

when we multiply these two probabilities we get

()() = 0.8 × 0.4 = 0.32

However, the probability that a student owns both a PlayStation and a Nintendo Switch, i.e. ∩ is given by

$$P(\mathsf{A} \cap \mathsf{B}) = \frac{75}{250} = \mathsf{0.3} \neq \mathsf{0.32}$$

Hence,

( ∩ ) ≠ ()()

and the two events are **dependent**.

In practical terms this means that e.g. knowing that a student owns a PlayStation gives you additional information about his or her ownership of a Nintendo Switch.

Before you know that the student owns a PlayStation the probability that this student owns a Nintendo Switch is

$$P(B) = \frac{100}{250} = 0.44$$

However, once you know that that the student owns a PlayStation you know that this students belongs to the group of 200 PlayStation owners, of which 75 also own a Nintendo Switch. With fancy notation we write this as

$$P(B \mid A) = \frac{75}{200} = 0.375$$

so the probability now is slightly lower.

On the other hand, when you know that a student owns a Nintendo Switch, what is the probability of this student owning a PlayStation?

Answer:

( | ) =

75 100

= 0.75

On the other hand, when you know that a student owns a Nintendo Switch, what is the probability of this student owning a PlayStation?

Answer:

$$P(\mathsf{A} \mid B) = \frac{\mathsf{75}}{\mathsf{100}} = \mathsf{0.75}$$

#### **Discrete Random Variable**

#### **Example**

A player draws a card from a standard deck of cards. She gets 1 € when drawing a jack, 2 € when drawing a queen and 3 € when drawing a king. In all other cases she receives nothing. We can formalise this be defining a mapping from to ℝ:

 ∶ → ℝ ∶ ↦ () = { when drawing a jack when drawing a queen when drawing a king in all other cases.

We have done nothing else but associate a *number* with different events.

#### **Probability Mass Function**

Using the rules of probability we can assign probabilities to the different numerical outcomes

$$\begin{aligned} f\_X(\mathbf{3}) &= P(\mathbf{X} = \mathbf{3}) = P(\text{ki}\text{in}\mathbf{g}) = \frac{4}{52} = \frac{1}{13}, \\ f\_X(\mathbf{2}) &= P(\mathbf{X} = \mathbf{2}) = P(\text{q}\text{u}\text{e}\text{en}\mathbf{n}) = \frac{4}{52} = \frac{1}{13}, \\ f\_X(\mathbf{1}) &= P(\mathbf{X} = \mathbf{1}) = P(\text{j2c}\text{ck}) = \frac{4}{52} = \frac{1}{13}, \\ f\_X(\mathbf{0}) &= P(\mathbf{X} = \mathbf{0}) = P(\text{any other card}) = \frac{40}{52} = \frac{10}{13}. \end{aligned}$$

#### **Note:**

- It holds that (0) + (1) + (2) + (3) = 1.
- And also: 0 ≤ ( ) ≤ 1.

# **Probability Mass Function** To make things more explicit we can put the probability mass function in

a table:

| 𝑥                        | 0        | 1       | 2       | 3       |
|--------------------------|----------|---------|---------|---------|
| 𝑓<br>(𝑥) = 𝑃(𝑋 = 𝑥)<br>𝑋 | 10<br>13 | 1<br>13 | 1<br>13 | 1<br>13 |

We can also represent this probability mass function in a graph:

#### **Probability Distribution: 1 die**

What is the probability of each outcome when rolling a single die?

| 𝑥 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |

1/6

 ()

() = ( = )

1 6 1 6

1 2 3 4 5 6

1 6 1 6 1 6 1 6

### **Probability Distribution: 1 die**

What is the probability of each outcome when rolling a single die?

#### **Probability Distribution: 2 dice**

| 𝑥 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|----|----|----|
|   |   |   |   |   |   |   |   |   |    |    |    |

() = ( = )

()

 

1/36 2/36 3/36 4/36 5/36 6/36

 

 

 

 

4 6 8 10 12

 

 

 

 

 

 

#### **Probability Distribution: 2 dice**

Once you have a probability mass function, you can compute other probabilities.

With the card game, what is the probability that you gain at most 2 EUR?

Answer:

( ≤ 2) = ( = 0) + ( = 1) + ( = 2) =

We could also have used the complement rule in this case:

( ≤ 2) = 1 − ( > 2) = 1 − ( = 3) = 1 −

10 13 + 1 13 + 1 13 = 12 13

> 1 13 = 12 13 .

Once you have a probability mass function, you can compute other probabilities.

With the card game, what is the probability that you gain at most 2 EUR? Answer:

$$P(\mathbb{X} \le \mathbb{Z}) = P(\mathbb{X} = \mathbb{O}) + P(\mathbb{X} = \mathbb{1}) + P(\mathbb{X} = \mathbb{Z}) = \frac{\mathbb{1}\mathbb{O}}{\mathbb{1}\mathbb{3}} + \frac{\mathbb{1}}{\mathbb{1}\mathbb{3}} + \frac{\mathbb{1}}{\mathbb{1}\mathbb{3}} = \frac{\mathbb{1}\mathbb{2}}{\mathbb{1}\mathbb{3}}$$

We could also have used the complement rule in this case:

( ≤ 2) = 1 − ( > 2) = 1 − ( = 3) = 1 − <sup>1</sup> <sup>13</sup> <sup>=</sup> 12 13.

When throwing two dice, what is the probability that the sum of the results is between 4 and 7, boundaries included

Answer:

(4 ≤ ≤ 7) = ( = 4) + ( = 5) + ( = 6) + ( = 7) =

We could also compute this using left-tail probabilities only:

(4 ≤ ≤ 7) = ( ≤ 7) − ( < 4) = ( ≤ 7) − ( ≤ 3) =

18 36 = 1 2

21 36 − 3 36 = 1 2

When throwing two dice, what is the probability that the sum of the results is between 4 and 7, boundaries included Answer:

$$P(\{4 \le X \le 7\}) = P(X = 4) + P(X = 5) + P(X = 6) + P(X = 7) = \frac{18}{36} = \frac{1}{2}$$

We could also compute this using left-tail probabilities only:

$$P(4 \le X \le 7) = P(X \le 7) - P(X < 4) = P(X \le 7) - P(X \le 3) = \frac{2 \cdot 1}{3 \cdot 6} - \frac{3}{3 \cdot 6} = \frac{1}{2}$$
 
$$\begin{array}{c} \mathbf{HOP} \\ \mathbf{GEND} \end{array}$$

#### **Expectation of a R.V.**

Consider the random variable associated with playing the card game with the following probability distribution function

$$\begin{aligned} f\_{\chi} \{\mathfrak{Z}\} &= P \{\mathfrak{X} = \mathfrak{Z}\} = \frac{\mathfrak{I}}{\mathfrak{I}\mathfrak{Z}}, & f\_{\chi} \{\mathfrak{Z}\} &= P \{\mathfrak{X} = \mathfrak{Z}\} = \frac{\mathfrak{I}}{\mathfrak{I}\mathfrak{Z}}, \\ f\_{\chi} \{\mathfrak{I}\} &= P \{\mathfrak{X} = \mathfrak{I}\} = \frac{\mathfrak{I}}{\mathfrak{I}\mathfrak{Z}}, & f\_{\chi} \{\mathfrak{O}\} &= P \{\mathfrak{X} = \mathfrak{O}\} = \frac{\mathfrak{I}\mathfrak{O}}{\mathfrak{I}\mathfrak{Z}}. \end{aligned}$$

If somebody played this game a very large number of times, what would their average earnings be? I.e. what is the **expected value** of this random variable?

#### **Expectation of a R.V.**

#### **Expectation of a random variable**

**The expectation of a random variable is denoted by or E**() **and is given by**

$$
\mu\_{\chi} = \sum\_{l} \times\_{l} P(\chi = \chi\_{l}) = \sum\_{l} \times\_{l} f\_{\chi}(\chi\_{l}).
$$

Note the similarity between this formula and the way you calculate the sample mean when a frequency table is given. We often write instead of .

#### **Expectation of a R.V.**

The expected value of the random variable associated with the card game is given by:

$$\begin{split} \mu\_{\chi} &= \sum\_{i} \times\_{i} f\_{\chi}(\chi\_{i}) \\ &= \mathbf{0} \cdot f\_{\chi}(\mathbf{0}) + \mathbf{1} \cdot f\_{\chi}(\mathbf{1}) + 2 \cdot f\_{\chi}(\mathbf{2}) + \mathbf{3} \cdot f\_{\chi}(\mathbf{3}) \\ &= \mathbf{0} \cdot \frac{\mathbf{1}\mathbf{0}}{\mathbf{1}\mathbf{3}} + \mathbf{1} \cdot \frac{\mathbf{1}}{\mathbf{1}\mathbf{3}} + 2 \cdot \frac{\mathbf{1}}{\mathbf{1}\mathbf{3}} + \mathbf{3} \cdot \frac{\mathbf{1}}{\mathbf{1}\mathbf{3}} \\ &= \frac{\mathbf{6}}{\mathbf{1}\mathbf{3}} . \end{split}$$

#### **Variance of a R.V.**

The variance of a R.V. is a measure of dispersion that resembles the sample variance very closely.

#### **Variance of a random variable**

**The variance of a random variable is defined by:**

$$
\sigma\_\chi^2 = \sum\_i \left(\chi\_i - \mu\_\chi\right)^2 \\
\mathbb{P}(\mathbf{X} = \mathbf{x}\_i) = \sum\_i \left(\chi\_i - \mu\_\chi\right)^2 f\_\chi(\chi\_i).
$$

Note: the **standard deviation** is the positive square root of the variance.

$$
\sigma\_\chi = \sqrt{\sigma\_\chi^2}
$$

$$\mathbf{H}\_{\mathbf{H}}$$

#### **Variance: Intuition**

Consider two random variables variables and . The random variable represents the number of received emails per day for a first office worker. This person receives either 48 or 52 emails per day, each with a 50 percent probability. The random variable represents the number of received emails of a second office worker. This second person receives no emails at all with 50 percent probability and with 50 percent chance receives 100 emails.

- Determine the probability mass function of and of .
- Compute the expected value of and . What do you notice?
- Who is experiencing a larger variability w.r.t. the number of emails received?
- Compute the variance of and .

#### **Continuous Random Variable**

- A continuous random variable takes on an uncountably infinite number of possible values.
- In this case it doesn't make a lot of sense to consider the probability that equals some number **exactly**, because this probability is always zero.
- What does make sense is to consider the probability that takes on a value in some interval [, ].
- This probability can be found be *integrating* (i.e. "summing up") the **probability density function** of the random variable.

#### **Continuous Random Variable**

Measurements of length, time, … are examples of continuous random variables.

The leftmost histogram illustrates that most of the 5000 men were between 175cm and 180cm tall.

#### **Continuous Random Variable**

- From left to right the number of intervals is increased, but the total area of all the bars always equals 1.
- If the number of intervals is increased even more, the intervals would eventually get so small that we no longer have a histogram, but rather a curve (by connecting the 'dots' at the tops of the very tiny rectangles).
- The heights of people often follow an approximate **Normal Distribution**. The Normal Distribution is a type of **continuous probability distribution**.
- There are also other continuous probability distributions, e.g. the Exponential Distribution and the continuous Uniform Distribution.

### **Continuous Probability Distr.**

The reaction speed of Superman (in ms) can also be represented as a normal distribution:

#### **Expectation and Variance**

Also for continuous R.V.'s there are formulas for expectation and variance. The expectation is given by

$$
\mu\_\chi = \int\_{-\infty}^{+\infty} \times f\_\chi(\mathbf{x}) \, \mathbf{d} \mathbf{x},
$$

while the variance 2 is given by

$$
\sigma\_\chi^2 = \int\_{-\infty}^{\cdot \infty} \left(\mathbf{x} - \boldsymbol{\mu}\_\chi\right)^2 f\_\chi(\mathbf{x}) \, \mathbf{d} \mathbf{x} \, \mathbf{d}
$$

**Note:** these are essentially the same formulas as for discrete R.V.'s but with integrals instead of summations.

**Note:** you are **not** expected to know how to calculate integrals!

#### *Standard* **Normal Distribution**

 and have a similar position on the Gaussian bell curve. What is the mathematical relationship between and ?

= + . and =

− 

#### *Standard* **Normal Distribution**

normal distribution ∈ ∼ (, ) 0.3

**standard** normal distribution

 and have a similar position on the Gaussian bell curve. What is the mathematical relationship between and ?

$$\mathbf{x} = \mu \mathbf{+z}.\sigma \quad \text{and} \quad \mathbf{z} = \frac{\mathbf{x} - \mu}{\sigma}$$

#### **Standard Normal Distribution**

## **Python functions**

#### Import scipy.stats

For a normal distribution with mean m and standard deviation s:

| Function                                                                                                                                          | Purpose                                                                                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| norm.pdf(x,<br>loc=m,<br>scale=s)<br>norm.cdf(x,<br>loc=m,<br>scale=s)<br>norm.sf(x,<br>loc=m,<br>scale=s)<br>norm.isf(1-p,<br>loc=m,<br>scale=s) | Probability density at<br>x<br>Left-tail probability<br>𝑃(𝑋 <<br>x)<br>Right-tail probability<br>𝑃(𝑋 ><br>x)<br>p% of observations are<br>expected to be lower than result |

## **Calculating Probabilities**

What is the probability that Superman's observed reaction speed is over 6 ms?

Mathematical Notation:

( > 6) = ? with ∼ ( = 5, = 1, 5)

#### **Calculating Probabilities: -table**

( > 6) = ? with ∼ ( = 5, = 1, 5)

(Old) calculation method using z-table, e.g. http://sixsigmastudyguide.com/wp-content/uploads/2014/04/ z-table.jpg

1. Calculate the -score

2. Convert to a *left* tail probability

= 0, 667 so ( > 6) = ( > 0, 667)

○ 100% probability rule: ( > 0, 667) = 1 − ( < 0, 667) ○ or symmetry rule: ( > 0, 667) = ( < −0, 667) 3. look for the corresponding value in the -table

 = 6−5 1,5

#### **Calculating Probabilities: -table**

( > 6) = ? with ∼ ( = 5, = 1, 5)

(Old) calculation method using z-table, e.g. http://sixsigmastudyguide.com/wp-content/uploads/2014/04/ z-table.jpg

- 1. Calculate the -score = 6−5 1,5 = 0, 667 so ( > 6) = ( > 0, 667)
- 2. Convert to a *left* tail probability ○ 100% probability rule: ( > 0, 667) = 1 − ( < 0, 667) ○ or symmetry rule: ( > 0, 667) = ( < −0, 667)
- 3. look for the corresponding value in the -table

## **Calculating Probabilities: using Python**

( > 6) = ? with ∼ ( = 5, = 1, 5) Calculated directly using Python:

> import scipy.stats as stats stats.norm.sf(6, loc=5, scale=1.5)

- 1. What is the probability that Superman reacts in less than 4 ms?
- 2. What is the probability that he reacts in less than 7 ms?
- 3. What is the probability that he reacts in less than 3 ms?
- 4. What is the probability that he reacts between 2 en 6.5 ms?
- 5. What interval contains 80% of his reaction speed?

#### **Question 3:** ( < 3)

#### **Question 4:** (2 < < 6, 5)

#### **Question 5**

For what value of is ( < ) = 80%?

## **Exponentional Distribution**

Besides the Normal Distribution, there are other often used continuous distributions, e.g. the **Exponentional Distribution**.

Values for an exponential random variable occur when there are fewer large values and more small values. For example, the amount of money customers spend in a trip to the supermarket follows an exponential distribution. There are more people who spend small amounts of money and fewer people who spend large amounts of money. Another examples is the length, in minutes, of long distance business

telephone calls.

# **Exponentional Distribution** Another example is the amount of time (in minutes) a postal clerk

spends with his or her customers. In the image below, the time is known to have an exponential distribution with an average amount of time equal to four minutes.

## **Continuous Uniform Distribution**

The continuous **Uniform Distribution** describes an experiment where there is an arbitrary outcome that lies between certain bounds. It is the simplest of all continuous probability distributions. The density function is constant where every value has an equal chance of occurring. Imagine you live in a building that has an elevator that will take you to your floor. From experience, once you push the button to call the elevator, it takes between ten and twenty seconds to arrive at your floor. This means the elevator arrival time is uniformly distributed between 10 and 20 seconds once you hit the button.

#### **Continuous Uniform Distribution**

(13 < < 18) = area under () between 13 & 18 = 5 × 0.1 = 0.5 Note: (13 < < 18) = (13 < ≤ 18) = (13 ≤ < 18) = (13 ≤ ≤ 18) and it also holds that (10 ≤ ≤ 20) = 1

so the total area under the probability density function is always equal to 1.

#### **From Sample to Population**

### **The Central Limit Theorem**

#### **Central limit theorem**

**If the size of the sample is sufficiently large, the probability distribution of the sample mean will approximate a normal distribution, regardless of the probability distribution of the underlying population.**

- 1 test
- 25 tests
- 100 tests

Demo: https://www.zoology.ubc.ca/~whitlock/Kingfisher/CLT.htm

#### **The Central Limit Theorem**

Consider a random sample of observations drawn from a population with expected value and standard deviation . If is sufficiently large, the probability distribution of the sample mean will approximate a normal distribution with mean = and standard deviation = √ .

The larger the sample, the better the probability distribution of will approximate the expected value of the population, .

#### **Point Estimate**

#### **Point estimate**

**A Point Estimate for a population parameter is a formula or equation that allows us to calculate a value to estimate that parameter.**

Example: sample variance/standard deviation, sample mean.

#### **Confidence Interval**

#### **confidence interval**

**A confidence interval is an equation or formula that allows us to construct an interval that will contain the parameter to be estimated with a certain level of confidence.**

Demo:

https://www.zoology.ubc.ca/~whitlock/Kingfisher/CIMean.htm

#### **Conf. Int. - Large Sample**

Given a sample with mean . We are looking for an interval [ − , + ] for which we can say with a level of confidence (1 − ) of e.g. 95% that is inside this interval.

$$\mathcal{P}\left(\overline{\mathbf{x}} - \mathbf{b} < \mu < \overline{\mathbf{x}} + \mathbf{b}\right) = \mathbf{1} - \mathbf{a} = \mathbf{0}, \mathbf{9.5}$$

#### **Conf. Int. - Large Sample**

Because of the central limit theorem we know that: ∈ ∼ (, √ ) And because of the symmetry we can say:

$$\mathcal{P}\left\{\overline{\mathbf{x}} - \mathbf{b} < \boldsymbol{\mu} < \overline{\boldsymbol{\lambda}} + \mathbf{b}\right\} = \mathcal{P}\left\{\boldsymbol{\mu} - \mathbf{b} < \overline{\boldsymbol{\lambda}} < \boldsymbol{\mu} + \mathbf{b}\right\}.$$

#### **Conf. Int. - Large Sample**

We now calculate the -score for : = − 

√ We lookup (or calculate) the value 2 for which:

#### **Conf. Int. - Large Sample** The result is: (−1, 96 < − √ < 1, 96) = 0, 95 ( − 1, 96 √ <sup>&</sup>lt; < + 1, 96 √ ) = 0, 95

Because of symmetry we can swap and :

$$\mathcal{P}\left(\overline{\mathbf{x}} - \mathbf{1}, \mathbf{96}\frac{\sigma}{\sqrt{n}} < \mu < \overline{\mathbf{x}} + \mathbf{1}, \mathbf{96}\frac{\sigma}{\sqrt{n}}\right) = \mathbf{0}, \mathbf{95}$$

Now we can say with 95% confidence that:

$$\mu \in \left[ \overline{\mathbf{x}} - \mathfrak{I}, \mathfrak{M}. \frac{\sigma}{\sqrt{n}}, \overline{\mathbf{x}} + \mathfrak{I}, \mathfrak{M}. \frac{\sigma}{\sqrt{n}} \right]^2$$

(in practice we will use as a point estimate for ) 59/63

#### **Conf. Int. - Small Sample**

For a *small* sample the central limit theorem is **no longer** valid.

Instead we can say:

If a population has a normal distribution ( ∼ (, )) and you take a *small* sample with mean and standard deviation , then

$$\mathbf{t} = \frac{\overline{\mathbf{x}} - \mu}{\frac{\overline{\mathbf{s}}}{\sqrt{n}}}$$

will behave as a t-distribution with − 1 degrees of freedom

#### **Student t-distribution**

### **Student -distribution in Python**

Import scipy.stats For a -distribution with df degrees of freedom: (df = degrees of freedom)

| Functie                                 | Betekenis                                                               |
|-----------------------------------------|-------------------------------------------------------------------------|
| t.pdf(x,<br>df=d)<br>t.cdf(x,<br>df=d)  | Probability density for<br>x<br>Left-tail probability<br>𝑃(𝑋 <<br>x)    |
| t.sf(x,<br>df=d)<br>t.isf(1-p,<br>df=d) | Right-tail probability<br>𝑃(𝑋 ><br>x)<br>p% of observations is expected |
|                                         | to be lower than this value                                             |

#### **Conf. Int.: Small Sample**

To determine the confidence interval for the mean of a population, based on a *small* sample, we first calculate 2 , .

With a confidence level of 95% we have 2 = 0, 025 Assume for example = 5 (so df=4), then we have

$$\mathbf{t}\_{\frac{a}{2},df} = \texttt{sts.t.}\,\texttt{isf(1-0.975, df=4)} = \texttt{2.776}$$

We can say with a confidence of 95% that:

$$\mu \in \left[ \overline{\mathbf{x}} - \mathbf{t}\_{\frac{a}{2}, df} . \frac{\mathbf{s}}{\sqrt{n}}, \,\overline{\mathbf{x}} + \mathbf{t}\_{\frac{a}{2}, df} . \frac{\mathbf{s}}{\sqrt{n}} \right].$$
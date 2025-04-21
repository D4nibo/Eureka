# **Module 3a. Probability, The** **Central Limit Theorem,** **Confidence Intervals**
### **Data Science**

**Sabine De Vreese** **Lieven Smits** **Pieter Van Der Helst** **Bert Van Vreckem**

**2024–2025**


1/63


-----

# **Contents**

Probability

Discrete random variables

Expectation and variance of a random variable
Continuous Random Variables

The (Standard) Normal Distribution
Probabilities in the Normal Distribution

Other Continuous Distributions

From Sample to Population

The Central Limit Theorem
Confidence Intervals
Confidence Interval for a Large Sample
Confidence Interval for a Small Sample

2/63


-----

# **Learning Goals**

   - Probability distribution of a sample

   - The normal and Student-𝑡 distribution

   - Formulate the central limit theorem and explain its importance for
statistical analysis

   - Calculate confidence intervals

3/63


-----

# **Probability**


4/63


-----

# **Probability**

Informally, probabilities represent beliefs of how likely it is that a certain
event will happen when performing a certain experiment.

In the frequentist view, **probability** represents the **relative frequency** of
the occurrence of the event at hand (when performing a large number
of independent experiments).

5/63


-----

# **Probability: (Simple) Examples**

A fair six-sided die is thrown once.

   - What is the probability of getting a “1”?

   - What is the probability of throwing an even number?

   - What is the probability of getting a number in the set {1, 2, 3, 4, 5, 6}?

6/63


-----

# **Probability: (Simple) Examples**

A fair six-sided die is thrown once.

   - What is the probability of getting a “1”?

   - What is the probability of throwing an even number?

   - What is the probability of getting a number in the set {1, 2, 3, 4, 5, 6}?

Answers: 1/6, 1/2 and 1

6/63


-----

# **Probability: Example**

Two games of chance:

1. Bet on: at least one six when throwing a fair die 4 consecutive times.

     - You will *win* in the long run when playing this game.
2. Bet on: at least one “double six” when throwing two fair dice 24
times.

     - You will *lose* in the long run when playing this game, even though in
some sense the two bets seem equivalent. (Probability divided by six
but number of throws multiplied by six.)

7/63


-----

# **Probability: Example**

8/63


-----

# **Probability: Observations**

   - Probabilities are numbers assigned to sets.

   - These sets are part of some all-encompassing set, the “universe”,
typically denoted 𝛺.

   - The numbers (probabilities) assigned to the sets have to satisfy three
simple rules (see later) in order to correspond to our intuition about
how probabilities should behave.

9/63


-----

# **Example**

For the first game: at least one six when throwing a fair die 4
consecutive times.

   - What is the universe?

10/63


-----

# **Example**

For the first game: at least one six when throwing a fair die 4
consecutive times.

   - What is the universe? Answer:

𝛺= {(1, 1, 1, 1), (1, 1, 1, 2), (1, 1, 1, 3), …, (6, 6, 6, 4), (6, 6, 6, 5), (6, 6, 6, 6)}

10/63


-----

# **Example**

For the first game: at least one six when throwing a fair die 4
consecutive times.

   - What is the universe? Answer:

𝛺= {(1, 1, 1, 1), (1, 1, 1, 2), (1, 1, 1, 3), …, (6, 6, 6, 4), (6, 6, 6, 5), (6, 6, 6, 6)}

   - What set corresponds to the event: “you win” or “at least one 6”?

10/63


-----

# **Example**

For the first game: at least one six when throwing a fair die 4
consecutive times.

   - What is the universe? Answer:

𝛺= {(1, 1, 1, 1), (1, 1, 1, 2), (1, 1, 1, 3), …, (6, 6, 6, 4), (6, 6, 6, 5), (6, 6, 6, 6)}

   - What set corresponds to the event: “you win” or “at least one 6”?

Answer

𝐴= {(6, 1, 1, 1), (6, 1, 1, 2), …, (5, 5, 5, 6), (6, 6, 1, 1), …

(6, 6, 5, 5), (1, 6, 6, 1), …, (6, 6, 6, 6)}

10/63


-----

# **Axioms (Rules) of Probability**




11/63


-----

# **Properties of Probabilities**

From the three axioms of probability, we can derive *all* properties of
probabilities. Some important ones are listed below:

   - **Complement rule** : for each 𝐴 it holds that

𝑃(𝐴) = 1 −𝑃(𝐴)

where 𝐴 represents the event “A does not occur”.

   - The impossible event has probability zero: 𝑃(∅) = 0.

   - The **general sum rule** :

𝑃(𝐴∪𝐵) = 𝑃(𝐴) + 𝑃(𝐵) −𝑃(𝐴∩𝐵)

12/63


-----

# **Examples**

1. A coin is tampered with such that 𝑃(head) = 0.6. What is 𝑃(tail)?
2. From the 250 students enrolled in this course, 200 own a PlayStation
game console, while 100 own a Nintendo Switch. There are 75
students who own both game consoles. What is the probability,
when you pick a random student, that

     - this student does not own a PlayStation

     - this student owns a PlayStation or a Nintendo Switch (or both)

     - this student owns neither a PlayStation nor a Nintendo Switch.

13/63


-----

# **Examples**

1. A coin is tampered with such that 𝑃(head) = 0.6. What is 𝑃(tail)?
2. From the 250 students enrolled in this course, 200 own a PlayStation
game console, while 100 own a Nintendo Switch. There are 75
students who own both game consoles. What is the probability,
when you pick a random student, that

     - this student does not own a PlayStation

     - this student owns a PlayStation or a Nintendo Switch (or both)

     - this student owns neither a PlayStation nor a Nintendo Switch.
Answers: 1 −200/250 = 1/5, (200 + 100 −75)/250 = 225/250 = 9/10,
1 −9/10 = 1/10

13/63


-----

# **Independent Events: Example**

When events are **independent** it means that the occurrence of one
event (or knowing that the event occurred) does **not change** the
probability of the other event occurring.

As an example: draw a card from a standard deck of cards and consider
the following events:

𝐴= a ♣ was drawn

and

𝐵= an ace was drawn

When I tell you that 𝐵 occurred, this will not change your opinion about
the probability of 𝐴 occurring, this will still be 13/52 = 1/4.
(Note: this also works the other way around!)


-----

# **Independent Events: Definition**




15/63


-----

# **Dependent Events: Example**

Consider the events from before where students own either a

PlayStation, a Nintendo Switch or both. Let 𝐴 be the event that a student
owns a PlayStation, while 𝐵 represents the fact that a student owns a
Nintendo Switch. From the numbers above we see that


𝑃(𝐴) = [200]


250 [= 0.4]



[200] and 𝑃(𝐵) = [100]

250 [= 0.8,] 250


when we multiply these two probabilities we get

𝑃(𝐴)𝑃(𝐵) = 0.8 × 0.4 = 0.32


16/63


-----

However, the probability that a student owns both a PlayStation and a
Nintendo Switch, i.e. 𝐴∩𝐵 is given by


Hence,


𝑃(𝐴∩𝐵) = [75]

250 [= 0.3 ≠0.32]

𝑃(𝐴∩𝐵) ≠𝑃(𝐴)𝑃(𝐵)


and the two events are **dependent** .


17/63


-----

# **Dependent Events: Example**

In practical terms this means that e.g. knowing that a student owns a
PlayStation gives you additional information about his or her ownership
of a Nintendo Switch.

Before you know that the student owns a PlayStation the probability
that this student owns a Nintendo Switch is

𝑃(𝐵) = [100]

250 [= 0.4]

However, once you know that that the student owns a PlayStation you
know that this students belongs to the group of 200 PlayStation owners,
of which 75 also own a Nintendo Switch. With fancy notation we write
this as

𝑃(𝐵| 𝐴) = [75]

200 [= 0.375]

so the probability now is slightly lower.

18/63


-----

# **Dependent Events: Example**

On the other hand, when you know that a student owns a Nintendo
Switch, what is the probability of this student owning a PlayStation?

19/63


-----

# **Dependent Events: Example**

On the other hand, when you know that a student owns a Nintendo
Switch, what is the probability of this student owning a PlayStation?

Answer:

𝑃(𝐴| 𝐵) = [75]

100 [= 0.75]

19/63


-----

# **Discrete Random Variable**

**Example**

A player draws a card from a standard deck of cards. She gets 1 € when
drawing a jack, 2 € when drawing a queen and 3 € when drawing a king.
In all other cases she receives nothing.
We can formalise this be defining a mapping 𝑋 from 𝛺 to
ℝ:

1 when drawing a jack

2 when drawing a queen

3 when drawing a king

𝑋∶𝛺→ℝ∶𝜔↦𝑋(𝜔) = {0 in all other cases.

We have done nothing else but associate a *number* with different events.


-----

# **Probability Mass Function**

Using the rules of probability we can assign probabilities to the different
numerical outcomes


𝑓 𝑋 (3) = 𝑃(𝑋= 3) = 𝑃(king) = [4]


13 [,]



[4] [1]

52 [=] 13


𝑓 𝑋 (2) = 𝑃(𝑋= 2) = 𝑃(queen) = [4]


13 [,]



[4] [1]

52 [=] 13


𝑓 𝑋 (1) = 𝑃(𝑋= 1) = 𝑃(jack) = [4]


13 [,]



[4] [1]

52 [=] 13


𝑓 𝑋 (0) = 𝑃(𝑋= 0) = 𝑃(any other card) = [40]



[40]

52 [= 10] 13


13 [.]


**Note:**

 - It holds that 𝑓 𝑋 (0) + 𝑓 𝑋 (1) + 𝑓 𝑋 (2) + 𝑓 𝑋 (3) = 1.

 - And also: 0 ≤𝑓 𝑋 (𝑥 𝑖 ) ≤1.


21/63


-----

# **Probability Mass Function**

To make things more explicit we can put the probability mass function in
a table:





|𝑥|0|1|2|3|
|---|---|---|---|---|
|𝑓 (𝑥) = 𝑃(𝑋 = 𝑥) 𝑋|10 13|1 13|1 13|1 13|


We can also represent this probability mass function in a graph:

10/13

1/13


0 1 2 3

𝑥


22/63


-----

# **Probability Distribution: 1 die**

What is the probability of each outcome when rolling a single die?

23/63

|𝑥|1|2|3|4|5|6|
|---|---|---|---|---|---|---|
||||||||


-----

# **Probability Distribution: 1 die**

What is the probability of each outcome when rolling a single die?







|𝑥|1|2|3|4|5|6|
|---|---|---|---|---|---|---|
|𝑓 (𝑥) = 𝑃(𝑋 = 𝑥) 𝑋|1 6|1 6|1 6|1 6|1 6|1 6|


1/6


1 2 3 4 5 6

𝑥


23/63


-----

# **Probability Distribution: 2 dice**

24/63

|𝑥|2|3|4|5|6|7|8|9|10|11|12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||


-----

# **Probability Distribution: 2 dice**












|𝑥|2|3|4|5|6|7|8|9|10|11|12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|𝑓 (𝑥) = 𝑃(𝑋 = 𝑥) 𝑋|1 36|2 36|3 36|4 36|5 36|6 36|5 36|4 36|3 36|2 36|1 36|


6/36
5/36
4/36
3/36
2/36
1/36


2 4 6 8 10 12

𝑥


24/63


-----

# **Using Probability Mass Func.**

Once you have a probability mass function, you can compute other
probabilities.

With the card game, what is the probability that you gain at most 2 EUR?

25/63


-----

# **Using Probability Mass Func.**

Once you have a probability mass function, you can compute other
probabilities.

With the card game, what is the probability that you gain at most 2 EUR?
Answer:


𝑃(𝑋≤2) = 𝑃(𝑋= 0) + 𝑃(𝑋= 1) + 𝑃(𝑋= 2) = [10]



[1] [1]

13 [+] 13



[10] [1]

13 [+] 13



[1]

13 [= 12] 13


13 13 13 13

We could also have used the complement rule in this case:



[1]

13 [= 12] 13


𝑃(𝑋≤2) = 1 −𝑃(𝑋> 2) = 1 −𝑃(𝑋= 3) = 1 − [1]


13 [.]


25/63


-----

# **Using Probability Mass Func.**

When throwing two dice, what is the probability that the sum of the
results is between 4 and 7, boundaries included

26/63


-----

# **Using Probability Mass Func.**

When throwing two dice, what is the probability that the sum of the
results is between 4 and 7, boundaries included

Answer:


𝑃(4 ≤𝑋≤7) = 𝑃(𝑋= 4) + 𝑃(𝑋= 5) + 𝑃(𝑋= 6) + 𝑃(𝑋= 7) = [18]



[18]

36 [= 1] 2


36 2

We could also compute this using left-tail probabilities only:


𝑃(4 ≤𝑋≤7) = 𝑃(𝑋≤7) −𝑃(𝑋< 4) = 𝑃(𝑋≤7) −𝑃(𝑋≤3) = [21]



[21]

36 [−3] 36



[−3] 36 [= 1] 2


2


26/63


-----

# **Expectation of a R.V.**

Consider the random variable associated with playing the card game
with the following probability distribution function


𝑓 𝑋 (3) = 𝑃(𝑋= 3) = 13 [1]

𝑓 𝑋 (1) = 𝑃(𝑋= 1) = [1]


13 [1] [,] 𝑓 𝑋 (2) = 𝑃(𝑋= 2) = 13 [1]


13 [.]


13 [,]


13 [1] [,] 𝑓 𝑋 (0) = 𝑃(𝑋= 0) = 13 [10]


If somebody played this game a very large number of times, what would
their average earnings be? I.e. what is the **expected value** of this
random variable?


27/63


-----

# **Expectation of a R.V.**




Note the similarity between this formula and the way you calculate the
sample mean when a frequency table is given.
We often write 𝜇 instead of 𝜇 𝑋 .


28/63


-----

# **Expectation of a R.V.**

The expected value of the random variable associated with the card
game is given by:

𝜇 𝑋 = ∑ 𝑥 𝑖 𝑓 𝑋 (𝑥 𝑖 )
𝑖

= 0 ⋅𝑓 𝑋 (0) + 1 ⋅𝑓 𝑋 (1) + 2 ⋅𝑓 𝑋 (2) + 3 ⋅𝑓 𝑋 (3)


= 0 ⋅ [10]


13 [+ 2 ⋅1] 13



[10]

13 [+ 1 ⋅1] 13


13 [+ 3 ⋅1] 13


13


= [6]

13 [.]


29/63


-----

# **Variance of a R.V.**

The variance of a R.V. is a measure of dispersion that resembles the
sample variance very closely.



Note: the **standard deviation** is the positive square root of the variance.

𝜎 𝑋 = ~~√~~ 𝜎 𝑋 [2]


30/63


-----

# **Variance: Intuition**

Consider two random variables variables 𝑋 and 𝑌.

The random variable 𝑋 represents the number of received emails per day
for a first office worker. This person receives either 48 or 52 emails per
day, each with a 50 percent probability. The random variable 𝑌
represents the number of received emails of a second office worker.
This second person receives no emails at all with 50 percent probability
and with 50 percent chance receives 100 emails.

   - Determine the probability mass function of 𝑋 and of 𝑌.

   - Compute the expected value of 𝑋 and 𝑌. What do you notice?

   - Who is experiencing a larger variability w.r.t. the number of emails
received?

   - Compute the variance of 𝑋 and 𝑌.

31/63


-----

# **Continuous Random Variable**

   - A continuous random variable takes on an uncountably infinite
number of possible values.

   - In this case it doesn’t make a lot of sense to consider the probability
that 𝑋 equals some number 𝑎 **exactly**, because this probability is
always zero.

   - What does make sense is to consider the probability that 𝑋 takes on
a value in some interval [𝑎, 𝑏].

   - This probability can be found be *integrating* (i.e. “summing up”) the
**probability density function** of the random variable.

32/63


-----

# **Continuous Random Variable**

Measurements of length, time, … are examples of continuous random
variables.

The leftmost histogram illustrates that most of the 5000 men were
between 175cm and 180cm tall.


-----

# **Continuous Random Variable**

   - From left to right the number of intervals is increased, but the total
area of all the bars always equals 1.

   - If the number of intervals is increased even more, the intervals would
eventually get so small that we no longer have a histogram, but
rather a curve (by connecting the ’dots’ at the tops of the very tiny
rectangles).

   - The heights of people often follow an approximate **Normal**
**Distribution** . The Normal Distribution is a type of **continuous**
**probability distribution** .

   - There are also other continuous probability distributions, e.g. the
Exponential Distribution and the continuous Uniform Distribution.


-----

# **Continuous Probability Distr.**

The reaction speed 𝑥 of Superman (in ms) can also be represented as a
normal distribution:

𝑦

𝑥 (ms)
3.5 5 6.5

𝜇

35/63


-----

# **Expectation and Variance**

Also for continuous R.V.’s there are formulas for expectation and variance.
The expectation is given by


𝜇 𝑋
= ∫ −∞


+∞


𝑥𝑓 𝑋 (𝑥) d𝑥,

−∞


while the variance 𝜎 [2]
𝑋 [is given by]


𝜎 [2]
𝑋 [= ∫]

−∞


+∞


2
(𝑥−𝜇 𝑋 ) 𝑓 𝑋 (𝑥) d𝑥.

−∞


**Note:** these are essentially the same formulas as for discrete R.V.’s but
with integrals instead of summations.
**Note:** you are **not** expected to know how to calculate integrals!


-----

# **Standard Normal Distribution**


normal distribution 𝑥∈𝑋∼𝑁𝑜𝑟(𝜇, 𝜎)

𝜇−𝜎 𝜇 𝑥 𝜇+ 𝜎


**standard** normal distribution
𝑧∈𝑍∼𝑁𝑜𝑟(0, 1)

0.3

0.2

0.1


0
−1 0 𝑧 1


𝑍


𝑥 and 𝑧 have a similar position on the Gaussian bell curve.
What is the mathematical relationship between 𝑥 and 𝑧?


37/63


-----

# **Standard Normal Distribution**


normal distribution 𝑥∈𝑋∼𝑁𝑜𝑟(𝜇, 𝜎)

𝜇−𝜎 𝜇 𝑥 𝜇+ 𝜎


**standard** normal distribution
𝑧∈𝑍∼𝑁𝑜𝑟(0, 1)

0.3

0.2

0.1


0
−1 0 𝑧 1


𝑍


𝑥 and 𝑧 have a similar position on the Gaussian bell curve.
What is the mathematical relationship between 𝑥 and 𝑧?
## 𝑥= 𝜇+ 𝑧.𝜎 and 𝑧= [𝑥−] [𝜇]

𝜎


37/63


-----

# **Standard Normal Distribution**

68.3%

|Col1|Col2|95.|4%|Col5|Col6|
|---|---|---|---|---|---|
|||99.|7%|||
|2.1%|13.6%|34.1%|34.1%|13.6%|2.1%|



−3 −2 −1 0 1 2 3

38/63


-----

# **Python functions**

Import scipy.stats
For a normal distribution with mean m and standard deviation s:

**Function** **Purpose**

norm.pdf(x, loc=m, scale=s) Probability density at x
norm.cdf(x, loc=m, scale=s) Left-tail probability 𝑃(𝑋< x)
norm.sf(x, loc=m, scale=s) Right-tail probability 𝑃(𝑋> x)
norm.isf(1-p, loc=m, scale=s) p% of observations are
expected to be lower than result

39/63


-----

# **Calculating Probabilities**

What is the probability that Superman’s observed reaction speed is over
6 ms?

Mathematical Notation:

𝑥

|tation: ith 𝑋∼𝑁𝑜𝑟(𝜇= 5, 𝜎= 1, 5)|Col2|
|---|---|
|𝑃(𝑋||
|3.5 5|6.5|


6

40/63


-----

# Calculating Probabilities: 𝑧 -table

𝑃(𝑋> 6) = ? with 𝑋∼𝑁𝑜𝑟(𝜇= 5, 𝜎= 1, 5)

(Old) calculation method using z-table, e.g.
[http://sixsigmastudyguide.com/wp-content/uploads/2014/04/](http://sixsigmastudyguide.com/wp-content/uploads/2014/04/z-table.jpg)
[z-table.jpg](http://sixsigmastudyguide.com/wp-content/uploads/2014/04/z-table.jpg)

41/63


-----

# Calculating Probabilities: 𝑧 -table

𝑃(𝑋> 6) = ? with 𝑋∼𝑁𝑜𝑟(𝜇= 5, 𝜎= 1, 5)

(Old) calculation method using z-table, e.g.
[http://sixsigmastudyguide.com/wp-content/uploads/2014/04/](http://sixsigmastudyguide.com/wp-content/uploads/2014/04/z-table.jpg)
[z-table.jpg](http://sixsigmastudyguide.com/wp-content/uploads/2014/04/z-table.jpg)

1. Calculate the 𝑧-score
𝑧= [6] 1,5 [−] [5] [= 0, 667][ so][ 𝑃(𝑋> 6) = 𝑃(𝑍> 0, 667)]

2. Convert to a ***left*** tail probability

     - 100% probability rule: 𝑃(𝑍> 0, 667) = 1 −𝑃(𝑍< 0, 667)

     - or symmetry rule: 𝑃(𝑍> 0, 667) = 𝑃(𝑍< −0, 667)

3. look for the corresponding value in the 𝑧-table

41/63


-----

# **Calculating Probabilities: using** **Python**

𝑃(𝑋> 6) = ? with 𝑋∼𝑁𝑜𝑟(𝜇= 5, 𝜎= 1, 5)
Calculated directly using Python:

import scipy.stats as stats
stats.norm.sf(6, loc=5, scale=1.5)

42/63


-----

# **Examples**

1. What is the probability that Superman reacts in less than 4 ms?

2. What is the probability that he reacts in less than 7 ms?

3. What is the probability that he reacts in less than 3 ms?

4. What is the probability that he reacts between 2 en 6.5 ms?

5. What interval contains 80% of his reaction speed?

43/63


-----

# Question 3: 𝑃(𝑋< 3)

0.3

0.2

0.1

−4 −2 0 2 4

-1.33

44/63


-----

# Question 4: 𝑃(2 < 𝑋< 6, 5)

0.3

0.2

0.1

−4 −2 0 2 4

1

45/63


-----

# **Question 5**

For what value of 𝑥 is 𝑃(𝑋< 𝑥) = 80%?

0.3

0.2

0.1

−4 −2 0 2 4

.84

46/63


-----

# **Exponentional Distribution**

Besides the Normal Distribution, there are other often used continuous
distributions, e.g. the **Exponentional Distribution** .
Values for an exponential random variable occur when there are fewer
large values and more small values. For example, the amount of money
customers spend in a trip to the supermarket follows an exponential
distribution. There are more people who spend small amounts of money
and fewer people who spend large amounts of money.
Another examples is the length, in minutes, of long distance business
telephone calls.

47/63


-----

# **Exponentional Distribution**

Another example is the amount of time (in minutes) a postal clerk
spends with his or her customers. In the image below, the time is known
to have an exponential distribution with an average amount of time
equal to four minutes.

48/63


-----

# **Continuous Uniform Distribution**

The continuous **Uniform Distribution** describes an experiment where
there is an arbitrary outcome that lies between certain bounds.
It is the simplest of all continuous probability distributions. The density
function is constant where every value has an equal chance of occurring.
Imagine you live in a building that has an elevator that will take you to
your floor. From experience, once you push the button to call the
elevator, it takes between ten and twenty seconds to arrive at your floor.
This means the elevator arrival time is uniformly distributed between 10
and 20 seconds once you hit the button.

49/63


-----

# **Continuous Uniform Distribution**

𝑃(13 < 𝑋< 18) = area under 𝑓 𝑋 (𝑥) between 13 & 18

= 5 × 0.1

= 0.5


0.1

0
0 5 10 15 20


Note:

𝑃(13 < 𝑋< 18) = 𝑃(13 < 𝑋≤18) = 𝑃(13 ≤𝑋< 18)

= 𝑃(13 ≤𝑋≤18)

and it also holds that

𝑃(10 ≤𝑋≤20) = 1


𝑥

so the total area under the

probability density function is
50/63 always equal to 1.


-----

# **From Sample to Population**


51/63


-----

# **The Central Limit Theorem**





           - 1 test

           - 25 tests

           - 100 tests

Demo:
[https://www.zoology.ubc.ca/~whitlock/Kingfisher/CLT.htm](https://www.zoology.ubc.ca/~whitlock/Kingfisher/CLT.htm)


52/63


-----

# **The Central Limit Theorem**

Consider a random sample of 𝑛 observations drawn from a population
with expected value 𝜇 and standard deviation 𝜎. If 𝑛 is sufficiently large,
the probability distribution of the sample mean 𝑥 will approximate a

𝜎
normal distribution with mean ~~𝜇~~ 𝑥 = 𝜇 and standard deviation ~~𝜎~~ 𝑥 = ~~√~~ 𝑛 [.]

The larger the sample, the better the probability distribution of 𝑥 will
approximate the expected value of the population, 𝜇.

53/63


-----

# **Point Estimate**




Example: sample variance/standard deviation, sample mean.


54/63


-----

# **Confidence Interval**




Demo:
[https://www.zoology.ubc.ca/~whitlock/Kingfisher/CIMean.htm](https://www.zoology.ubc.ca/~whitlock/Kingfisher/CIMean.htm)


55/63


-----

# **Conf. Int. - L a rge Sample**

Given a sample with mean 𝑥.
We are looking for an interval [ 𝑥−𝑏, 𝑥+ 𝑏] for which we can say with a
level of confidence (1 −𝛼) of e.g. 95% that 𝜇 is inside this interval.

𝑃(𝑥−𝑏< 𝜇< 𝑥+ 𝑏) = 1 −𝛼= 0, 95





|95% 2,5% 2,5% (1 −𝛼) ( 𝛼) ( 𝛼) 2 2|Col2|
|---|---|
|𝑥−𝑏 𝑥|𝑥+ 𝑏|


𝜇


56/63


-----

# **Conf. Int. - Large Sample**

Because of the central limit theorem we know that: 𝑥∈𝑋∼𝑁𝑜𝑟(𝜇, [𝜎]

~~√~~ 𝑛 [)]

And because of the symmetry we can say:

𝑃(𝑥−𝑏< 𝜇< 𝑥+ 𝑏) = 𝑃(𝜇−𝑏< 𝑥< 𝜇+ 𝑏)





√𝑛

|2,5% ( 𝛼) 2|95% 2,5 (1 −𝛼) ( 𝛼 2 𝑋 𝜇 𝜎 𝜇+ 𝑏|
|---|---|
|𝜇−𝑏||


𝑥


57/63


-----

# **Conf. Int. - Large Sample**


We now calculate the 𝑧-score for 𝑥: 𝑧= [𝑥−] 𝜎 [𝜇]

~~√~~ 𝑛
We lookup (or calculate) the value 𝑧 𝛼

2 [for which:]


𝛼
𝑃(−𝑧 2



[𝛼]

2 [) = 1 −𝛼= 0.95]


𝛼

2 [< 𝑧< 𝑧] [𝛼] 2


𝛼
𝑃(𝑧< 𝑧 2


𝛼

2 [) = 1 −𝛼] 2


2 [= 0.975]


𝑧 𝛼

2 [=][ stats.norm.isf(1-0.975)][ ≈1.96]






-𝑧 𝛼


𝛼 -1 0 1 𝑧 𝛼

2 2


𝛼

2


58/63


-----

# **Conf. Int. - Large Sample**

The result is:

𝜎

𝑃(−1, 96 < [𝑥−] ~~√~~ 𝑛 [𝜇] < 1, 96) = 0, 95



[𝜎]
𝑃(𝜇−1, 96 √𝑛



[𝜎]

~~√~~ 𝑛 ) = 0, 95



[𝜎] < 𝑥< 𝜇+ 1, 96 [𝜎]

√𝑛 ~~√~~


Because of symmetry we can swap 𝜇 and 𝑥:



[𝜎]
𝑃(𝑥−1, 96 ~~√~~



[𝜎]

√𝑛 ) = 0, 95



[𝜎] < 𝜇< 𝑥+ 1, 96 [𝜎]

~~√~~ 𝑛 √𝑛


Now we can say with 95% confidence that:



[𝜎]
𝜇∈[ 𝑥−1, 96. √𝑛



[𝜎]

~~√~~ 𝑛 ]



[𝜎], 𝑥+ 1, 96. [𝜎]

√𝑛 ~~√~~


(in practice we will use 𝑠 as a point estimate for 𝜎 )
59/63 𝑠𝑎𝑚𝑝𝑙𝑒 𝑝𝑜𝑝𝑢𝑙𝑎𝑡𝑖𝑜𝑛


-----

# **Conf. Int. - Small Sample**

For a ***small*** sample the central limit theorem is **no longer** valid.

Instead we can say:

If a population 𝑋 has a normal distribution (𝑋∼𝑁𝑜𝑟(𝜇, 𝜎)) and you take a
*small* sample with mean 𝑥 and standard deviation 𝑠, then

𝑡= [𝑥−] [𝜇]

𝑠
√𝑛

will behave as a t-distribution with 𝑛−1 degrees of freedom

60/63


-----

# **Student t-distribution**

61/63


-----

# Student 𝑡 **-distribution in Python**

Import scipy.stats
For a 𝑡-distribution with df degrees of freedom:
(df = degrees of freedom)

**Functie** **Betekenis**

t.pdf(x, df=d) Probability density for x
t.cdf(x, df=d) Left-tail probability 𝑃(𝑋< x)
t.sf(x, df=d) Right-tail probability 𝑃(𝑋> x)
t.isf(1-p, df=d) p% of observations is expected
to be lower than this value

62/63


-----

# **Conf. Int.: Small Sample**

To determine the confidence interval for the mean 𝜇 of a population,
based on a *small* sample, we first calculate 𝑡 𝛼

2 [,𝑑𝑓] [.]

With a confidence level of 95% we have [𝛼] 2 [= 0, 025]

Assume for example 𝑛= 5 (so df=4), then we have

𝑡 𝛼

2 [,𝑑𝑓] [=][ stats.t.isf(1-0.975, df=4)][ = 2.776]

We can say with a confidence of 95% that:


𝛼

2

𝜇∈[ 𝑥−𝑡


𝛼 [𝑠]

2 [,𝑑𝑓] [.] √𝑛


𝛼 [𝑠]

2 [,𝑑𝑓] [.] ~~√~~


, 𝑥+ 𝑡 𝛼
√𝑛 2



[𝑠]

~~√~~ 𝑛 ]


63/63


-----


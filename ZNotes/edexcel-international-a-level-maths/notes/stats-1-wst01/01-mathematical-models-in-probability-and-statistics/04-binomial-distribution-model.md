## Binomial Distribution Model

* We use the Binomial Distribution model from a manageable sample size to make mathematical predictions about a much larger population

* Testing an entire population (like every single person in a country or every smartphone made in a factory) is usually impossible due to inefficiency

* Notation of Binomial distribution:

  * X$\sim$B(n,p) where n is the total number of independent trials and p is the fixed probability

* To get our $(p)$ fixed probability, we start by testing a smaller, controlled sample size (e.g., testing 50 patients/ n= 50)

* From this sample, we observe how many times a binary outcome occurs (success vs. failure) to establish the baseline probability $(p)$ of that event happening

* In this case, let’s imagine that the probability of the tested patients being able to recover within 2 days is 20%

  * In this case, X$\sim$B(50,0.2)$ would denote that there is a sample size of 50 (50 patients) and 20% (10 patients) are able to recover within 2 days

* Through a binomial distribution model, we can change our "number of trials" $(n)$ in the binomial formula to match a much larger target population. Instead of physically testing 10,000 items, we let $n= 10000 $ once we have the baseline probability

![](https://images.znotes.org/allimages/558a5cce56db2cfd1f97b876.webp =796x)

* **Key Assumptions Made:**

  * There is a fixed number of trials

  * Each trial has only two outcomes: success or failure.

  * The probability of success is identical for every single trial

  * Each trial is statistically independent.

* **Why It May Be Inaccurate:**

  * The probability of success rarely stays completely constant.
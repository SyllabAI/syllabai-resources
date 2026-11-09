# as-statistics-1-data-collection — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Population, sample, and good data

![Population shown as a large group, sample as a highlighted subset, strata boxes, and a numbered list with every fifth member selected from a random start](../assets/001-20156c56-a3d1-42d6-8a9e-a99f6e0ee4e3.jpeg)

In statistics, the population is the whole group we want information about, while a sample is the smaller group we actually collect data from. A census means collecting data from every member of the population.

A good sample should be representative, so it reflects the population fairly. If some types of people are more likely to be included than others, the results can be biased.

Sampling saves time and money, but the choice of method matters. In AS questions, you often need to say not just the method name but exactly how the sample would be taken.

## Simple random sampling

A sampling frame is a complete list of the population. A simple random sample gives every possible sample of the chosen size an equal chance of being selected.

Suppose a club has 180 members and needs a sample of 15. Write a list of all 180 members, number them from 1 to 180, and use a random number generator to choose 15 different numbers.

This is usually done without replacement, so if a number repeats, you ignore it and generate another. In an exam, saying choose 15 at random is too vague, so mention the list, numbering, and random numbers.

## Stratified random sampling

A stratified random sample is useful when the population is split into clear groups, called strata, and you want each group represented in the right proportion. Use: 
$$\text{sample from stratum} = \frac{\text{stratum size}}{\text{population size}} \times \text{overall sample size}$$
This keeps each group in the same proportion as in the population.

A college has 96 Year 12 students and 84 Year 13 students, so the total population is $96+84=180$. For a sample of 30, the number from Year 12 is: 
$$\frac{96}{180}\times 30 = 16$$

The number from Year 13 is: 
$$\frac{84}{180}\times 30 = 14$$
Now number the students within each year group and use random numbers to choose 16 Year 12 students and 14 Year 13 students.

Finally, check that the selected numbers add to the required total, here $16+14=30$. The common error is forgetting the random part, because taking the right proportions alone is not enough.

## Systematic sampling

In systematic sampling, you use an ordered list, choose a random start, and then take every $k$th member. The sampling interval is determined by the ratio of the population size to the sample size.

$$$k = \frac{N}{n}$$ In this formula, $N$ represents the population size and $n$ is the sample size.

If a business has 150 employees and wants a sample of 30, the interval $k$ is $150/30 = 5$. By picking a random starting number from 1 to 5, say 4, you then select employees numbered 4, 9, 14, 19, and so on.

This technique spreads the sample across the list and is quick to carry out. However, you must use a random start, and if the list has a repeating pattern, the sample can become biased.

## When random methods are not possible

Stratified random sampling needs accurate group sizes and a way to randomly identify individuals inside each group. If you only have estimates, or there is no complete sampling frame, true stratified random sampling cannot be done.

Suppose a pond is estimated to contain 240 perch, 360 trout, 120 eels and 180 tench, and a researcher wants 100 fish. The estimated total is $900$, and a perch quota is $\frac{240}{900}\times 100 \approx 26.7$, so about $27$ perch; similar calculations give $40$ trout, $13$ eels, and $20$ tench.

This is quota sampling, because the sample is made to match the group proportions without random selection from a full list. It can look fairer than just taking whoever is nearby, but it can still be biased.

Another non-random method is opportunity sampling, where you use the people or items that are easiest to access, such as the first 35 visitors to arrive. Volunteer sampling is also non-random because people choose themselves to take part.

## Full-mark descriptions

To get full marks in a describe how question, imagine someone else following your instructions exactly. Name the method first, then give the practical steps in order.

For simple random sampling, mention the sampling frame, numbering, random number generator, and ignoring repeats. For stratified random sampling, add the calculation for each stratum and then say random numbers are used within each stratum.

For systematic sampling, calculate $k$, choose a random starting number from $1$ to $k$, and then take every $k$th member. If a random method is impossible, explain why using phrases such as no sampling frame or only estimated group sizes.

## Check yourself

1. A sports centre has 520 members and asks 40 of them to complete a questionnaire. Which statement is correct?

   - The 520 members are the sample and the 40 members are the population

   - The 520 members are the population and the 40 members are the sample ✔

   - It is a census because 40 members are being asked

   - Any sample of 40 must be representative

   _Explanation:_ The population is the whole group being studied, here all 520 members, and the sample is the 40 selected members. The common wrong answer flips these definitions, but the sample is always the smaller group actually observed.

2. Which description gives a valid simple random sample of 15 from 180 club members?

   - Ask the first 15 members you see

   - Number the 180 members from 1 to 180 and use a random number generator to choose 15 different numbers ✔

   - Put the members in alphabetical order and choose every 12th member

   - Ask 15 volunteers from a noticeboard advert

   _Explanation:_ Numbering the full list and using 15 different random numbers gives a simple random sample. The common wrong answer is choosing every 12th member, but that is a fixed-interval method from an ordered list, not a simple random sample, and it also misses the random-start detail.

3. A researcher knows only estimated numbers of each fish species in a pond and has no list of individual fish. Which method is most suitable for a roughly proportional sample of 100 fish?

   - Stratified random sampling

   - Quota sampling ✔

   - Simple random sampling

   - Systematic sampling

   _Explanation:_ Quota sampling can match the estimated species proportions even when there is no full list of individual fish. The common wrong answer is stratified random sampling, but that needs a sampling frame and random selection within each species.

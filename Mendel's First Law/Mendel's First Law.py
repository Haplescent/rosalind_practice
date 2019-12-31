"""
Probability is the mathematical study of randomly occurring phenomena. We will
model such a phenomenon with a random variable, which is simply a variable that
can take a number of different distinct outcomes depending on the result of an
underlying random process.

For example, say that we have a bag containing 3 red balls and 2 blue balls.
If we let X represent the random variable corresponding to the color of a
drawn ball, then the probability of each of the two outcomes is given by
Pr(X=red)=35 and Pr(X=blue)=25.

Random variables can be combined to yield new random variables. Returning to
the ball example, let Y model the color of a second ball drawn from the bag
(without replacing the first ball). The probability of Y being red depends on
whether the first ball was red or blue. To represent all outcomes of X and Y,
we therefore use a probability tree diagram. This branching diagram represents
all possible individual probabilities for X and Y, with outcomes at the
endpoints ("leaves") of the tree. The probability of any outcome is given by
the product of probabilities along the path from the beginning of the tree;
see Figure 2 for an illustrative example.

An event is simply a collection of outcomes. Because outcomes are distinct,
the probability of an event can be written as the sum of the probabilities
of its constituent outcomes. For our colored ball example, let A be the event
"Y is blue." Pr(A) is equal to the sum of the probabilities of two different
outcomes: Pr(X=blue and Y=blue)+Pr(X=red and Y=blue), or 3/10+1/10= 2/5
(see Figure 2 above).

Given: Three positive integers k, m, and n, representing a population
containing k+m+n organisms: k individuals are homozygous dominant for
a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms
will produce an individual possessing a dominant allele (and thus displaying
 the dominant phenotype). Assume that any two organisms can mate.

 Sample Dataset
2 2 2

Sample Output
0.78333

frequency of alleles can be modeled as
1 = p^2 + 2pq + q^2
where p is the frequency of the dominant allele and q is the frequency of the
recessive allele

k is the population of  homozygous dominant individual for
a factor, m is the population of heterozygous, and n is the population
of homozygous recessive, t is the total population size (k + m + n)

p^2 is the frequency of homozygous dominant (k/t)
2pq is the frequency of heterozygous dominat (m/t)
q^2 is the frequency of homozygous recessive (n/t)

p^2 is the chances that newborn will get two dominant alleles
2pq is the chances that the newborn will get one dominant allele and one
recessive allele
q^2 is the frequency that the newborn will get two recessive alleles


There is a 1/3 chance that mate 1 will be a k, 1/3 chance that mate 1 will be
a .  This means that there are only 5
individuls left in the population.  this means that there is a 1/5 chance
mate 2 will be a k
"""


from sys import argv
from math import pow
from math import sqrt

script, k, m, n = argv

k = int(k)
m = int(m)
n = int(n)


def calculate_mate_prob(k, m, n):
    #calculates the mate percentages
    t = k + m + n
    kk_mate_prob = (k / t) * ((k - 1) / (t - 1))
    km_mate_prob = (k / t) * ((m) / (t - 1))
    kn_mate_prob = (k / t) * ((n) / (t - 1))

    mk_mate_prob = (m / t) * ((k) / (t - 1))
    mm_mate_prob = (m / t) * ((m - 1) / (t - 1))
    mn_mate_prob = (m / t) * ((n) / (t - 1))

    nk_mate_prob = (n / t) * ((k) / (t - 1))
    nm_mate_prob = (n / t) * ((m) / (t - 1))
    nn_mate_prob = (n / t) * ((n - 1) / (t - 1))

    dominat_prob = kk_mate_prob + km_mate_prob + kn_mate_prob + mk_mate_prob + (3/4)*mm_mate_prob + (1/2)*mn_mate_prob + nk_mate_prob + (1/2)*nm_mate_prob

    return dominat_prob



t = k + m + n

q = ((2 * n) + m) / (t * 2)

p = 1 - q

print(p)

print(pow(p, 2) + (2 * p * q))

print(calculate_mate_prob(k, m, n))

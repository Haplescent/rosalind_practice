""""
any given month will contain the rabbits that were alive the previous
month, plus any new offspring.

The population begins in the first month with a pair of newborn rabbits.
Rabbits reach reproductive age after one month.
In any given month, every rabbit of reproductive age mates with another rabbit
of reproductive age.
Exactly one month after two rabbits mate, they produce one male and one female
rabbit.
Rabbits never die or stop reproducing

we obtain the Fibonacci sequence having terms Fn that are defined by the
recurrence relation Fn=Fn−1+Fn−2 (with F1=F2=1 to initiate the sequence).
"""

from sys import argv

script, n, k = argv
n = int(n)
k = int(k)

total = []
reproduction_age = []
non_reproductive_age = []
unborn = []


def rabbit_growth_logic(n ,pairs_per_mate, count = 0, repro_pop = 0, non_repro_pop = 1,
    non_born = 0):
    """function defining how rabbits grow with each month
    where n = months past
    """
    if n == count:
        pass
    else:
        #appending population numbers to results list
        reproduction_age.append(repro_pop)
        non_reproductive_age.append(non_repro_pop)
        unborn.append(non_born)
        total.append(repro_pop + non_repro_pop)
        #changing populations numbers for next month through mating and growing up

        #reproductive bunnies mate and are added to non_born population
        non_born = repro_pop * pairs_per_mate


        repro_pop = non_repro_pop + repro_pop
        #bunnies grow up

        non_repro_pop = repro_pop * pairs_per_mate


def three_state_growth(months, pairs_per_mate, count = 0 , repro = 0, nonrepro = 1, nonborn = 0):
    if count == 0:
        reproduction_age.append(repro)
        non_reproductive_age.append(nonrepro)
        unborn.append(nonborn)


        next_repro = nonrepro + repro
        next_nonrepro = nonborn
        next_nonborn = repro * pairs_per_mate

        reproduction_age.append(next_repro)
        non_reproductive_age.append(next_nonrepro)
        unborn.append(next_nonborn)

        count += 1
        three_state_growth(months, pairs_per_mate, count, next_repro, next_nonrepro, next_nonborn)

    elif count > 0 and count <= months:

        next_repro = nonrepro + repro
        next_nonrepro = nonborn
        next_nonborn = repro * pairs_per_mate

        reproduction_age.append(next_repro)
        non_reproductive_age.append(next_nonrepro)
        unborn.append(next_nonborn)

        count += 1
        three_state_growth(months, pairs_per_mate, count, next_repro, next_nonrepro, next_nonborn)

    elif count > months:

        print(repro + nonrepro)

    else:
        print('error with logic')



def two_state_growth(months, pairs_per_mate, count = 0 , repro = 0, nonrepro = 1):
    if count == 0:
        reproduction_age.append(repro)
        non_reproductive_age.append(nonrepro)

        next_repro = nonrepro + repro
        next_nonrepro = repro * pairs_per_mate

        reproduction_age.append(next_repro)
        non_reproductive_age.append(next_nonrepro)

        count += 1
        two_state_growth(months, pairs_per_mate, count, next_repro, next_nonrepro)

    elif count > 0 and count < months:

        next_repro = nonrepro + repro
        next_nonrepro = repro * pairs_per_mate

        reproduction_age.append(next_repro)
        non_reproductive_age.append(next_nonrepro)

        count += 1
        two_state_growth(months, pairs_per_mate, count, next_repro, next_nonrepro)

    elif count == months:

        print(repro + nonrepro)
        print(repro)
    else:
        print('error with logic')


two_state_growth(n, k)

print(reproduction_age)
print(non_reproductive_age)

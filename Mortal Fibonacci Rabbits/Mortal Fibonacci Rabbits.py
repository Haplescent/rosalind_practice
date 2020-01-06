from sys import argv

script, n, k, l = argv

n = int(n)
k = int(k)
l = int(l)

n = n-1
total = []
reproduction_age = []
non_reproductive_age = []


def two_state_growth(months, pairs_per_mate, lifespan, count = 0 , repro = 0, nonrepro = 1):
    if count == 0:
        reproduction_age.append(repro)
        non_reproductive_age.append(nonrepro)

        next_repro = nonrepro + repro
        next_nonrepro = repro * pairs_per_mate

        reproduction_age.append(next_repro)
        non_reproductive_age.append(next_nonrepro)

        count += 1
        two_state_growth(months, pairs_per_mate, lifespan, count, next_repro, next_nonrepro)


    elif count > 0 and count < months and (count+1) < (lifespan):

        next_repro = nonrepro + repro
        next_nonrepro = repro * pairs_per_mate

        reproduction_age.append(next_repro)
        non_reproductive_age.append(next_nonrepro)

        count += 1
        two_state_growth(months, pairs_per_mate, lifespan, count, next_repro, next_nonrepro)

    elif count > 0 and count < months and (count+1) >= (lifespan):

        next_repro = nonrepro + repro - (non_reproductive_age[count + 1 - (lifespan)])
        next_nonrepro = repro * pairs_per_mate

        reproduction_age.append(next_repro)
        non_reproductive_age.append(next_nonrepro)

        count += 1
        two_state_growth(months, pairs_per_mate, lifespan, count, next_repro, next_nonrepro)


    elif count == months:

        print(repro + nonrepro)
        print(repro)
        print(nonrepro)
    else:
        print('error with logic')

two_state_growth(n,k,l)
print(reproduction_age)
print(non_reproductive_age)

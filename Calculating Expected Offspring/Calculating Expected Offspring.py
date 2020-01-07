"""
Given: Six nonnegative integers, each of which does not exceed 20,000. The
integers correspond to the number of couples in a population possessing each
 genotype pairing for a given factor. In order, the six given integers represent
  the number of couples having the following genotypes:

AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa

Return: The expected number of offspring displaying the dominant phenotype in
the next generation, under the assumption that every couple has exactly two
offspring.

Sample Dataset
1 0 0 1 0 1
Sample Output
3.5
"""

from sys import argv
import numpy as np

script, a ,b, c, d, e, f = argv

"""
list_file_opened = open(list_file, 'r')
list_file_read = list_file_opened.read()
list_file_opened.close()
print(type(list_file_read))
print(list_file_read.split(' '))
"""

list_file_read = [a,b,c,d,e,f]
for each in list_file_read:
    each = int(each)
    print(type(each))
    print(each)



def calculate_num_offstring_with_dominant(couple_pair_list):
    """couple_pair_list is a list comprising of number of couples in a population
    possessing eachn genotype pairing for a given factor
    AA-AA
    AA-Aa
    AA-aa
    Aa-Aa
    Aa-aa
    aa-aa
    calculate the num of offstring expected to have dominant phenotype in
    population given the couple_pair_list
    """
    #unpacking the couple_pair_list population into a list

    AA_AA = [couple_pair_list[0],1]
    AA_Aa = [couple_pair_list[1],1]
    AA_aa = [couple_pair_list[2],1]
    Aa_Aa = [couple_pair_list[3],.75]
    Aa_aa = [couple_pair_list[4],.50]
    aa_aa = [couple_pair_list[5],0]

    #giving each couple_pair their own probability of dominant phenotype
    """
    AA_AA.append(1)
    AA_Aa.append(1)
    AA_aa.append(1)
    Aa_Aa.append(.75)
    Aa_aa.append(.50)
    aa_aa.append(0)
    """

    temp_list = [AA_AA,AA_Aa,AA_aa,Aa_Aa,Aa_aa,aa_aa]
    """
    since each couple will have two offspring, the amount of offspring in the
    next generation that will be dominant will be

    (AA_AA[0]*2*AA_AA[1] + AA_Aa*2*AA_Aa[1] + ...)
    """
    offspring = int(0)
    for couple_pair in temp_list:
        couple_pair[0], couple_pair[1] = int(couple_pair[0]), float(couple_pair[1])
        offspring += couple_pair[0] * 2 * couple_pair[1]

    return offspring

print(calculate_num_offstring_with_dominant(list_file_read))

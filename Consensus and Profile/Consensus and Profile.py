"""
A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns. Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.

Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4×n matrix P in which P1,j represents the number of times that 'A' occurs in the jth position of one of the strings, P2,j represents the number of times that C occurs in the jth position, and so on (see below).

A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.

DNA Strings

A T C C A G C T
G G G C A A C T
A T G G A T C T
A A G C A A C C
T T G G A A C T
A T G C C A T T
A T G G C A C T

Profile
A   5 1 0 0 5 5 0 0
C   0 0 1 4 2 0 6 1
G   1 1 6 3 0 1 0 0
T   1 5 0 0 0 1 1 6

Consensus
A T G C A A C T


Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

Sample Dataset
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
"""

from sys import argv
from rosalind_merritt_module import fasta_file_to_fasta_dict, count_ACGT
import numpy as np

script, fasta_file = argv


def checkEqual(iterator):
   return len(set(iterator)) <= 1

def same_length(fasta_dict):
    #return true if all fasta_labels have nucleotides the same same_length
    length_list = []
    for string_label in fasta_dict:
        length_list.append(len(fasta_dict[string_label]))
    if checkEqual(length_list):
        return [True, length_list[0]]
    else:
        return [False, None]

def nucleotide_from_every_string_label(fasta_dict, n):
    #gets nucleotide from every string label in fasta_dict at index n
    nucleotide_list = []
    for string_label in fasta_dict:
        nucleotide_list.append(fasta_dict[string_label][n])
    else:
        return nucleotide_list
    return nucleotide_list

def array_into_list_of_list(array):
    newdata=list()
    for line in array:
        line = list(line)
        newdata.append(line)
    return newdata

def print_profile(ATGC_count_list, consensus_string):
    print(consensus_string)
    header = ['A:','C:','G:','T:']
    ATGC_count_list.insert(0, header)
    a = np.array(ATGC_count_list)
    b = np.transpose(a)
    c = array_into_list_of_list(b)
    for list in c:
        row = ' '.join(list)
        print(row)


def ATGC_count_list_to_consensus_string(ATGC_count_list):
    consensus_list = []
    for count_list in ATGC_count_list:
        nucleotide_num = count_list.index(max(count_list))
        if nucleotide_num == 0:
            consensus_list.append('A')
        elif nucleotide_num == 1:
            consensus_list.append('C')
        elif nucleotide_num == 2:
            consensus_list.append('G')
        elif nucleotide_num == 3:
            consensus_list.append('T')
    consensus_string = ''.join(consensus_list)
    return consensus_string

def profile(fasta_dict):
    length_list = same_length(fasta_dict)
    if length_list[0] == True:
        profile_list = []
        for nucleotide_index in range(0, length_list[1]):
            profile_list.append(nucleotide_from_every_string_label(fasta_dict, nucleotide_index))
    #print(profile_list)
    ATGC_count_list = []
    for nucleotides in profile_list:
        count_these_string = ''.join(nucleotides)
        ATGC_count_list.append(count_ACGT(count_these_string))
    #print(ATGC_count_list)
    consensus_string = ATGC_count_list_to_consensus_string(ATGC_count_list)
    print_profile(ATGC_count_list, consensus_string)





fasta_dict = (fasta_file_to_fasta_dict(fasta_file))
profile(fasta_dict)

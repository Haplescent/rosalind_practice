"""
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
"""

from sys import argv
script, seq_string_1, seq_string_2 = argv

def seq_string_to_seq_list(seq_string):
    seq_list = []
    for char in seq_string:
        seq_list.append(char)
    return seq_list

def calculate_hamming_distance(seq_string_1, seq_string_2):
    seq_list_1 = seq_string_to_seq_list(seq_string_1)
    seq_list_2 = seq_string_to_seq_list(seq_string_2)

    index = 0
    hamming_distance = 0
    for each in seq_list_1:
        if seq_list_1[index] != seq_list_2[index]:
            hamming_distance += 1
            index += 1
        else:
            index += 1

    return hamming_distance

print(calculate_hamming_distance(seq_string_1, seq_string_2))

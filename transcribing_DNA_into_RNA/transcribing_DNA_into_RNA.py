"""
Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and
 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string
u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.

Sample Dataset
GATGGAACTTGACTACGTAAATT
Sample Output
GAUGGAACUUGACUACGUAAAUU
"""

from sys import argv
script , filename = argv

txt_file = open(filename, "r")
txt = txt_file.read()
txt_file.close()

print(txt)

def transcribe(t):
    rna_list = []
    for char in t:
        if char == "T":
            rna_list.append("U")
        elif char == "A":
            rna_list.append("A")
        elif char == "G":
            rna_list.append("G")
        elif char == "C":
            rna_list.append("C")
    return "".join(rna_list)

print(transcribe(txt))

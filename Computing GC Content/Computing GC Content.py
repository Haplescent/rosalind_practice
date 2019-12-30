"""
The GC-content of a DNA string is given by the percentage of symbols in the string
that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note
that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A
commonly used method of string labeling is called FASTA format. In this format,
the string is introduced by a line that begins with '>', followed by some labeling
information. Subsequent lines contain the string itself; the first line to begin
with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the
ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the
GC-content of that string. Rosalind allows for a default error of 0.001 in all
decimal answers unless otherwise stated; please see the note on absolute error
below.
"""

from sys import argv
script, fasta_file = argv

fasta_opened = open(fasta_file, 'r')
fasta_txt = fasta_opened.read()
fasta_opened.close()

def fasta_txt_to_fasta_dict(fasta_txt):
    fasta_list = fasta_txt.split('>')
    del(fasta_list[0])
    fasta_dict = {}
    for each in fasta_list:
        n_split_list = each.split("\n")
        del(n_split_list[-1])
        fasta_dict[n_split_list[0]] = ''.join(n_split_list[1:])
    return fasta_dict

def gc_content(fasta_dict, key):
    """
    takes key from fasta_dict and returns percent gc content of the dna
    sequence that is associated with that key
    """
    #print(type(fasta_dict[key]))
    sequence = fasta_dict[key]
    seq_len = len(sequence)
    #print(seq_len)
    gc_count = 0
    for nucleotide in sequence:
        if nucleotide == 'G' or nucleotide == 'C':
            gc_count += 1
        else:
            pass
    return gc_count / seq_len * 100

#print(gc_content(fasta_dict, 'Rosalind_7463'))

def highest_gc_content_string(fasta_dict):
    """
    calculates which string in fasta_dict has the highest GC content
    """
    gc_percent_dict = {}
    for key in fasta_dict:
        gc_percent_dict[key] = gc_content(fasta_dict, key)

    max_index = max(gc_percent_dict, key = gc_percent_dict.get)
    return [max_index, gc_content(fasta_dict, max_index)]


fasta_dict = fasta_txt_to_fasta_dict(fasta_txt)
#print(fasta_dict['Rosalind_7463'])

print(highest_gc_content_string(fasta_dict))

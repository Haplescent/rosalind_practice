"""
Module containing functions from previous problems that can be used to solve
additional problems.
"""

def fasta_file_to_fasta_dict(fasta_file):
    fasta_opened = open(fasta_file, 'r')
    fasta_txt = fasta_opened.read()
    fasta_opened.close()
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

def highest_gc_content_string(fasta_dict):
    """
    calculates which string in fasta_dict has the highest GC content
    """
    gc_percent_dict = {}
    for key in fasta_dict:
        gc_percent_dict[key] = gc_content(fasta_dict, key)

    max_index = max(gc_percent_dict, key = gc_percent_dict.get)
    return [max_index, gc_content(fasta_dict, max_index)]

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

def count_ACGT(s):

    num_A, num_T, num_C, num_G = 0, 0, 0, 0

    for char in s:
        if char == "A":
            num_A += 1
        elif char == "T":
            num_T += 1
        elif char == "C":
            num_C += 1
        elif char == "G":
            num_G += 1

    return [num_A, num_C, num_G, num_T]


def subunit_check(s, t):
    len_t = len(t)
    len_s = len(s)
    subunit_s = []
    subunit_count = 0
    for subunit_index in range(0, len_s +1):
        if subunit_index + 1 + len_t - 1 <= len_s:
            subunit_s.append(s[subunit_index:subunit_index+len(t)])
            subunit_count += 1
        else:
            pass
    t_substring_positions = []
    for subunit_num in range(0, subunit_count + 1):
        if subunit_s[subunit_num - 1] == t:
            t_substring_positions.append(str(subunit_num))

    return ' '.join(t_substring_positions)

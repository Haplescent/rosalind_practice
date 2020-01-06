from sys import argv
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from rosalind_merritt_module import fasta_file_to_fasta_dict
script, fasta_file = argv

fasta_dict = fasta_file_to_fasta_dict(fasta_file)
print(fasta_dict)

"""
We would like to find the overlap in each string_label's sequence
"""

def add_prefix_to_fasta_dict(fasta_dict, k):
    #gets the prefix (k nucleotides) for each fasta string label
    for string_label in fasta_dict:
        prefix = fasta_dict[string_label][0][0:k]
        fasta_dict[string_label].append(prefix)
    return fasta_dict

def add_suffix_to_fasta_dict(fasta_dict, k):
    #gets the prefix (k nucleotides) for each fasta string label
    for string_label in fasta_dict:
        suffix = fasta_dict[string_label][0][-1:-(k+1):-1][::-1]
        #messy indexing to get last k letters of a string
        fasta_dict[string_label].append(suffix)
    return fasta_dict

def compare_label_suffix_with_other_prefix(fasta_dict, label):
    #compares prefix of a fasta_dict label with suffix of other labels
    #returns a list to use to make overlap edges
    overlap_edges = []
    for string_label in fasta_dict:
        if string_label == label:
            pass
        elif fasta_dict[string_label][1] == fasta_dict[label][2]:
            overlap_edges.append((label, string_label))
        else:
            pass
    return overlap_edges

def create_overlap_graph(fasta_dict):
    G = nx.DiGraph()
    for string_label in fasta_dict:
        label_edges = compare_label_suffix_with_other_prefix(fasta_dict,string_label)
        fasta_dict[string_label].append(label_edges)
        G.add_edges_from(label_edges)
    return G

def print_directed_overlap_graph(fasta_dict):
    for string_label in fasta_dict:
        for tuple_edge in fasta_dict[string_label][3]:
            print(' '.join(tuple_edge))

fasta_dict = add_prefix_to_fasta_dict(fasta_dict,3)
fasta_dict = add_suffix_to_fasta_dict(fasta_dict,3)

print(fasta_dict)

G = create_overlap_graph(fasta_dict)

print_directed_overlap_graph(fasta_dict)

nx.draw(G)
nx.draw(G, pos=nx.spring_layout(G))

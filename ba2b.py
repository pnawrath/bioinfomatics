"""
Bioinformatics 101
Assignment 2
Philipp Nawrath
Rosalind problem: BA2B
"""

import sys

SymbolToNumber = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
NumberToSymbol = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

#dna = ["TGATGATAACGTGACGGGACTCAGCGGCGATGAAGGATGAGT", "CAGCGACAGACAATTTCAATAATATCCGCGGTAAGCGGCGTA", "TGCAGAGGTTGGTAACGCCGGCGACTCGGAGAGCTTTTCGCT", "TTTGTCATGAACTCAGATACCATAGAGCACCGGCGAGACTCA", "ACTGGGACTTCACATTAGGTTGAACCGCGAGCCAGGTGGGTG", "TTGCGGACGGGATACTCAATAACTAAGGTAGTTCAGCTGCGA", "TGGGAGGACACACATTTTCTTACCTCTTCCCAGCGAGATGGC", "GAAAAAACCTATAAAGTCCACTCTTTGCGGCGGCGAGCCATA", "CCACGTCCGTTACTCCGTCGCCGTCAGCGATAATGGGATGAG", "CCAAAGCTGCGAAATAACCATACTCTGCTCAGGAGCCCGATG"]
dna = ["AAATTGACGCAT", "GACGACCACGTT", "CGTCAGCGCCTG", "GCTGAGCACCGG", "AGTACGGGACAG"]
k = 3


def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError()
    else:
        return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))


def number_to_pattern(index, k):
    if k == 1:
        return NumberToSymbol[index]
    prefix_index = index // 4
    r = index % 4
    prefix_pattern = number_to_pattern(prefix_index, k - 1)
    return prefix_pattern + NumberToSymbol[r]


def distance_between_pattern_and_strings(pattern, dna):
    distance = 0
    k = len(pattern)
    for x in dna:
        ham = sys.maxsize
        for i in range(len(x)-k+1):
            if ham > hamming_distance(pattern, x[i:i+k]):
                ham = hamming_distance(pattern, x[i:i+k])
        distance += ham
    return distance


def median_string(dna, k):
    distance = sys.maxsize
    median = ""
    for i in range(0, 4 ** (k-1)):
        pattern = number_to_pattern(i, k)
        if distance > distance_between_pattern_and_strings(pattern, dna):
            distance = distance_between_pattern_and_strings(pattern, dna)
            median = pattern
    return median


print(median_string(dna, k))

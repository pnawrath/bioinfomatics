"""
Bioinformatics 101
Assignment 2
Philipp Nawrath
Rosalind problem: BA2H
"""

import sys


def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError()
    else:
        return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))


def distance_between_pattern_and_strings(pattern, dna):
    distance = 0
    k = len(pattern)
    for x in dna:
        ham = sys.maxsize
        for i in range(len(x) - k + 1):
            if ham > hamming_distance(pattern, x[i:i+k]):
                ham = hamming_distance(pattern, x[i:i+k])
        distance += ham
    return distance


dna = ['TTACCTTAAC',  'GATATCTGTC', 'ACGGCGTTCG', 'CCCTAAAGAG', 'CGTCAGAGGT']
pattern = "AAA"


print(distance_between_pattern_and_strings(pattern, dna))

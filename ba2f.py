"""
Bioinformatics 101
Assignment 2
Philipp Nawrath
Rosalind problem: BA2F
"""

import sys
import random

SymbolToNumber = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
NumberToSymbol = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}


def pattern_to_number(text):
    symboltonumber = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    result = 0
    for k in range(len(text)):
        result = 4 * result + symboltonumber[text[k]]
    return result


def number_to_pattern(index, k):
    if k == 1:
        return NumberToSymbol[index]
    prefix_index = index // 4
    r = index % 4
    prefix_pattern = number_to_pattern(prefix_index, k - 1)
    return prefix_pattern + NumberToSymbol[r]


def profile_probable(text, k, profile):
    maxprob = 0
    kmer = text[0:k]
    for i in range(0, len(text) - k + 1):
        prob = 1
        pattern = text[i:i+k]
        for j in range(k):
            l = SymbolToNumber[pattern[j]]
            prob *= profile[l][j]
        if prob > maxprob:
            maxprob = prob
            kmer = pattern
    return kmer


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
        for i in range(len(x)-k+1):
            if ham > hamming_distance(pattern, x[i:i+k]):
                ham = hamming_distance(pattern, x[i:i+k])
        distance += ham
    return distance


def profile_form(motifs):
    k = len(motifs[0])
    profile = [[1 for i in range(k)] for j in range(4)]
    for x in motifs:
        for i in range(len(x)):
            j = SymbolToNumber[x[i]]
            profile[j][i] += 1
    for x in profile:
        for i in range(len(x)):
            x[i] = x[i]/len(motifs)
    return profile


def consensus(profile):
    str = ""
    for i in range(len(profile[0])):
        max = 0
        loc = 0
        for j in range(4):
            if profile[j][i] > max:
                loc = j
                max = profile[j][i]
        str += NumberToSymbol[loc]
    return str


def score(motifs):
    profile = profile_form(motifs)
    cons = consensus(profile)
    score = 0
    for x in motifs:
        for i in range(len(x)):
            if cons[i] != x[i]:
                score += 1
    return score


def random_motif_search(dna, k, t):
    bestMotifs = []
    motifs = []
    for x in range(0, t):
        random.seed()
        i = random.randint(0, len(dna[x])-k)
        motifs.append(dna[x][i:i+k])
    bestMotifs = motifs.copy()
    count = 0
    while True:
        profile = profile_form(motifs)
        for x in range(t):
            motifs[x] = profile_probable(dna[x], k, profile)
        if score(motifs) < score(bestMotifs):
            bestMotifs = motifs.copy()
            count += 1
        else:
            print(count)
        return bestMotifs


k = 8
t = 5
dna = ["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA", "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG", "TAGTACCGAGACCGAAAGAAGTATACAGGCGT", "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC", "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]
best = random_motif_search(dna, k, t)
min = score(best)
for x in range(10000):
    print(x)
    if score(random_motif_search(dna, k, t)) < score(best):
        best = random_motif_search(dna, k, t)
        min = score(random_motif_search(dna, k, t))
print(min)
for x in best:
    print(x)

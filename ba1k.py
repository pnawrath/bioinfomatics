"""
Bioinformatics 101
Assignment 2
Philipp Nawrath
Rosalind problem: BA1K
"""

SymbolToNumber = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
NumberToSymbol = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}


def pattern_to_number(pattern):
    symboltonumber = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    result = 0
    for k in range(len(pattern)):
        result = 4 * result + symboltonumber[pattern[k]]
    return result


def computingfrequencies(text, k):
    for i in range(0, 4 ** k - 1):
        frequencyarray = [0] * 4**k
    for i in range(0, (len(text)-k+1)):
        pattern = text[i:i+k]
        j = int(pattern_to_number(pattern))
        frequencyarray[j] = frequencyarray[j] + 1
    return frequencyarray


print(computingfrequencies(input("Enter a DNA Sequence: "), int(input("Enter k: "))))

"""
Bioinformatics 101
Assignment 2
Philipp Nawrath
Rosalind problem: BA1L
"""

SymbolToNumber = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
NumberToSymbol = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}


def pattern_to_number(pattern):
    result = 0
    for k in range(len(pattern)):
        result = 4 * result + SymbolToNumber[pattern[k]]
    return result


print(pattern_to_number(input("Enter a DNA Sequence: ")))

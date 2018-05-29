"""
Bioinformatics 101
Assignment 2
Philipp Nawrath
Rosalind problem: BA1M
"""

SymbolToNumber = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
NumberToSymbol = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}


def num2dna(index, k):
    if k == 1:
        return NumberToSymbol[index]
    prefix_index = index // 4
    r = index % 4
    prefix_pattern = num2dna(prefix_index, k - 1)
    return prefix_pattern + NumberToSymbol[r]


print(num2dna(int(input("Please enter the index Number: ")), int(input("Enter the lenght of the k-mer: "))))

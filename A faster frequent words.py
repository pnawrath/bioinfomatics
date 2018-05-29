"""
Bioinformatics 101
Assignment 2
Philipp Nawrath
A faster frequentwords
"""

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


def computingfrequencies(text, k):
    for i in range(0, 4 ** k - 1):
        frequencyarray[i] = 0
    for i in range(0, (len(text)-k)):
        pattern = text(i, k)
        j = int(pattern_to_number(pattern))
        frequencyarray[j] = frequencyarray[j] + 1
    return frequencyarray


def faster_frequentwords(text, k):
    frequent_patterns = []
    frequencyarray = computingfrequencies(text, k)
    max_count = max(frequencyarray)
    for i in range(0, (4 ** k) - 1):
        if frequencyarray[i] == max_count:
            pattern = number_to_pattern(i, k)
            frequent_patterns.extend(pattern)
    return frequent_patterns


print(faster_frequentwords(input("text"), int(input("k"))))

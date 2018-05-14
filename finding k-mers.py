# Find the most frequent k-mers in a DNA string

import collections

# Asking for the DNA string

dna = input("DNA string?")
print("Length of DNA string:", len(dna))

# Asking for the length of k


def input_k (message):
    while True:
        try:
            user_input = int(input(message))
        except ValueError:
            print("Not a valid number.")
            print("Please enter a number!")
            continue
        else:
            return user_input
        break


k = input_k("Please enter the length of k:")

# Asking for the allowed error


def input_m(message):
    while True:
        try:
            user_input = int(input(message))
        except ValueError:
            print("Not a valid number.")
            print("Please enter a number!")
            continue
        else:
            return user_input
        break


m = input_m ("Please enter the allowed error:")

# Counting function
in_mistake = m
out_result = []
kmer_list = []


def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError()
    else:
        return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))


for i in range(len(dna)-k + 1):
    v = dna[i:i + k]
    out_result.append(v)


for i in range(len(out_result) - 1):
    for j in range(i+1, len(out_result)):
        if hamming_distance(str(out_result[i]), str(out_result[j])) <= in_mistake:
            kmer_list.extend([out_result[i], out_result[j]])


kmer_count = collections.Counter(kmer_list).most_common(2)

print("Most frequent kmers:", (kmer_count))




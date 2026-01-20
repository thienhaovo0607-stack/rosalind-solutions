s = input().strip()

# map
complement = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

reverse_complement = ''.join(complement[base] for base in reversed(s))

# result
print(reverse_complement)

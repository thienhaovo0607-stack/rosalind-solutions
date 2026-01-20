MOD = 1_000_000

codon_count = {
    'F': 2, 'L': 6, 'I': 3, 'M': 1, 'V': 4,
    'S': 6, 'P': 4, 'T': 4, 'A': 4,
    'Y': 2, 'H': 2, 'Q': 2, 'N': 2,
    'K': 2, 'D': 2, 'E': 2, 'C': 2,
    'W': 1, 'R': 6, 'G': 4
}

protein = input().strip()

result = 1
for aa in protein:
    result = (result * codon_count[aa]) % MOD

# nhân số codon STOP
result = (result * 3) % MOD

print(result)

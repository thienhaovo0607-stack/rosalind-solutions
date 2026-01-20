import sys

lines = sys.stdin.read().strip().splitlines()

dna_strings = []
current = []

for line in lines:
    if line.startswith(">"):
        if current:
            dna_strings.append("".join(current))
            current = []
    else:
        current.append(line)

# thêm chuỗi cuối
dna_strings.append("".join(current))

L = len(dna_strings[0])

# Khởi tạo profile
profile = {
    'A': [0] * L,
    'C': [0] * L,
    'G': [0] * L,
    'T': [0] * L
}

# Đếm
for s in dna_strings:
    for i, base in enumerate(s):
        profile[base][i] += 1

# Tạo consensus
consensus = []

for i in range(L):
    max_base = max("ACGT", key=lambda b: profile[b][i])
    consensus.append(max_base)

consensus = "".join(consensus)

# GHI RA FILE
with open("output.txt", "w") as f:
    f.write(consensus + "\n")
    for base in "ACGT":
        f.write(base + ": " + " ".join(map(str, profile[base])) + "\n")

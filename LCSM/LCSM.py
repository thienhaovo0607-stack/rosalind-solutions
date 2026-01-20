import sys

# Parse FASTA
lines = sys.stdin.read().strip().splitlines()

seqs = []
current = []

for line in lines:
    if line.startswith(">"):
        if current:
            seqs.append("".join(current))
            current = []
    else:
        current.append(line)

seqs.append("".join(current))

# Chọn chuỗi ngắn nhất
seqs.sort(key=len)
base = seqs[0]
others = seqs[1:]

# Tìm longest common substring
for length in range(len(base), 0, -1):
    for i in range(len(base) - length + 1):
        sub = base[i:i+length]
        if all(sub in s for s in others):
            print(sub)
            sys.exit()

import sys

lines = sys.stdin.read().strip().splitlines()

seqs = {}
current_id = None
current_seq = []

# Parse FASTA
for line in lines:
    if line.startswith(">"):
        if current_id is not None:
            seqs[current_id] = "".join(current_seq)
        current_id = line[1:]
        current_seq = []
    else:
        current_seq.append(line)

# Lưu sequence cuối
seqs[current_id] = "".join(current_seq)

k = 3

# Tạo overlap graph
for id1, s in seqs.items():
    suffix = s[-k:]
    for id2, t in seqs.items():
        if id1 != id2 and suffix == t[:k]:
            print(id1, id2)

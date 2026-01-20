import sys

data = sys.stdin.read().strip().splitlines()

sequences = {}
current_id = ""
current_seq = []

for line in data:
    if line.startswith(">"):
        if current_id:
            sequences[current_id] = "".join(current_seq)
        current_id = line[1:]  # bỏ dấu '>'
        current_seq = []
    else:
        current_seq.append(line)

# lưu sequence cuối
sequences[current_id] = "".join(current_seq)

# Tính GC-content
max_gc = 0
max_id = ""

for seq_id, seq in sequences.items():
    gc_count = seq.count("G") + seq.count("C")
    gc_content = gc_count / len(seq) * 100

    if gc_content > max_gc:
        max_gc = gc_content
        max_id = seq_id

# Output
print(max_id)
print(f"{max_gc:.6f}")

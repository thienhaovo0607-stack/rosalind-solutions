import sys

# RNA codon table
codon_table = {
    "UUU":"F","UUC":"F","UUA":"L","UUG":"L",
    "UCU":"S","UCC":"S","UCA":"S","UCG":"S",
    "UAU":"Y","UAC":"Y","UAA":"Stop","UAG":"Stop",
    "UGU":"C","UGC":"C","UGA":"Stop","UGG":"W",
    "CUU":"L","CUC":"L","CUA":"L","CUG":"L",
    "CCU":"P","CCC":"P","CCA":"P","CCG":"P",
    "CAU":"H","CAC":"H","CAA":"Q","CAG":"Q",
    "CGU":"R","CGC":"R","CGA":"R","CGG":"R",
    "AUU":"I","AUC":"I","AUA":"I","AUG":"M",
    "ACU":"T","ACC":"T","ACA":"T","ACG":"T",
    "AAU":"N","AAC":"N","AAA":"K","AAG":"K",
    "AGU":"S","AGC":"S","AGA":"R","AGG":"R",
    "GUU":"V","GUC":"V","GUA":"V","GUG":"V",
    "GCU":"A","GCC":"A","GCA":"A","GCG":"A",
    "GAU":"D","GAC":"D","GAA":"E","GAG":"E",
    "GGU":"G","GGC":"G","GGA":"G","GGG":"G"
}

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
        current.append(line.strip())

seqs.append("".join(current))

# DNA gốc
dna = seqs[0]

# Loại introns
for intron in seqs[1:]:
    dna = dna.replace(intron, "")

# Phiên mã DNA -> RNA
rna = dna.replace("T", "U")

# Dịch mã RNA -> protein
protein = ""
for i in range(0, len(rna), 3):
    codon = rna[i:i+3]
    aa = codon_table[codon]
    if aa == "Stop":
        break
    protein += aa

print(protein)

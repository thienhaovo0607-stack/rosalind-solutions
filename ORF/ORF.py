import sys

# Codon table
codon_table = {
    "TTT":"F","TTC":"F","TTA":"L","TTG":"L",
    "CTT":"L","CTC":"L","CTA":"L","CTG":"L",
    "ATT":"I","ATC":"I","ATA":"I","ATG":"M",
    "GTT":"V","GTC":"V","GTA":"V","GTG":"V",
    "TCT":"S","TCC":"S","TCA":"S","TCG":"S",
    "CCT":"P","CCC":"P","CCA":"P","CCG":"P",
    "ACT":"T","ACC":"T","ACA":"T","ACG":"T",
    "GCT":"A","GCC":"A","GCA":"A","GCG":"A",
    "TAT":"Y","TAC":"Y","TAA":"Stop","TAG":"Stop",
    "CAT":"H","CAC":"H","CAA":"Q","CAG":"Q",
    "AAT":"N","AAC":"N","AAA":"K","AAG":"K",
    "GAT":"D","GAC":"D","GAA":"E","GAG":"E",
    "TGT":"C","TGC":"C","TGA":"Stop","TGG":"W",
    "CGT":"R","CGC":"R","CGA":"R","CGG":"R",
    "AGT":"S","AGC":"S","AGA":"R","AGG":"R",
    "GGT":"G","GGC":"G","GGA":"G","GGG":"G"
}

# Reverse complement
def reverse_complement(s):
    comp = {'A':'T','T':'A','C':'G','G':'C'}
    return "".join(comp[c] for c in reversed(s))

# Parse FASTA
lines = sys.stdin.read().strip().splitlines()
dna = ""
for line in lines:
    if not line.startswith(">"):
        dna += line.strip()

proteins = set()

# Process both strands
for strand in (dna, reverse_complement(dna)):
    for frame in range(3):
        for i in range(frame, len(strand) - 2, 3):
            if strand[i:i+3] == "ATG":
                protein = ""
                for j in range(i, len(strand) - 2, 3):
                    codon = strand[j:j+3]
                    aa = codon_table[codon]
                    if aa == "Stop":
                        proteins.add(protein)
                        break
                    protein += aa

# Output
for p in proteins:
    print(p)

def leArq(arquivo):
    dna=""
    f=open(arquivo,"r")
    linhas=f.readlines()
    for linha in linhas:
        linha=linha.strip()
        dna+=linha
    return dna

def reverse_complement(dna):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    reverse_dna = dna[::-1]
    complement_dna = [complement[base] for base in reverse_dna]
    return ''.join(complement_dna)

dna = leArq('content/rosalind_revc.txt')
print(reverse_complement(dna))
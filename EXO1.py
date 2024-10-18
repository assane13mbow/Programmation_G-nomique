# EXO

# Verification des nuc A, C, G et T dans la seq 
def valid_nuc(sequence):
    
    for nucleotide in sequence :

        if nucleotide not in "ATCG":

            return False
        
    return True

# Fonction qui fait la transcription ADN -> ARN (remplace T par U)
def transcribe_dna_to_rna(sequence):

    return sequence.replace("T", "U")   # Remplacer T par U

def main() :

    dna_seq = input("SVP, veuillez taper une sequence d'ADN : ").upper()

    if not valid_nuc(dna_seq) :

        print("La sequence contient des nucleotides valides")

        return
    
    rna_seq = transcribe_dna_to_rna(dna_seq)

    print(rna_seq)

if __name__ == "__main__":
    main()  # Appelle la fonction principale


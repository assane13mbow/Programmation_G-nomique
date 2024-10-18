"""BCM2550 - TP1 - ASSANE MBOW."""


import sys

from tp1_data import GENETIC_CODE


def main():
    """BCM2550 - TP1 - ASSANE MBOW."""
    # Get the DNA sequence
    dna_sequence = get_dna_sequence()

    # Check the DNA sequence, exit if invalid
    if not is_valid_dna(dna_sequence):
        sys.exit("Not a valid DNA sequence")

    # Generate the RNA sequence
    rna_sequence = dna_to_rna(dna_sequence)

    # Check the RNA sequence, exit if invalid
    if not is_valid_rna(rna_sequence):
        sys.exit("Not a valid RNA sequence")

    # Create the peptide
    peptide = rna_to_peptide(rna_sequence)
    print("Peptide:", peptide)

    # Print the peptide to the standard output


def get_dna_sequence() -> str:
    """Get DNA sequence from the user."""
    # Demander à l'utilisateur d'entrer la séquence d'ADN et
    # la convertir en majuscule
    dna_seq = input("Veuillez entrer une séquence d'ADN : ").upper()
    return dna_seq


def is_valid_dna(dna_seq: str) -> bool:
    """Check if the sequence is a DNA sequence."""
    valid_nucleotides = {"A", "C", "G", "T"}  # Nucléotides valides dans l'ADN

    # Vérifier si chaque nucléotide est valide
    for nucleotide in dna_seq:
        if nucleotide not in valid_nucleotides:
            return False

    return True


def dna_to_rna(dna_seq: str) -> str:
    """Convert a DNA sequence to a RNA sequence."""
    # Remplacer la thymine (T) par de l'uracile (U) pour convertir l'ADN en ARN
    return dna_seq.replace("T", "U")


def is_valid_rna(rna_seq: str) -> bool:
    """Check if the RNA sequence is a valid one."""
    # Vérifier si la longueur de la séquence est un multiple de 3
    if len(rna_seq) % 3 != 0:
        return False

    # Vérifier si la séquence commence par le codon de départ AUG (Méthionine)
    if not rna_seq.startswith("AUG"):
        return False

    stop_codons = {"UAA", "UAG", "UGA"}  # Codons d'arrêt

    # Vérifier si la séquence se termine par un codon d'arrêt
    if rna_seq[-3:] not in stop_codons:
        return False

    return True


def rna_to_peptide(rna_seq: str) -> str:
    """Convert an RNA sequence to a peptide (protein sequence)."""
    peptide = ""  # Initialiser la séquence peptidique

    # Parcourir la séquence d'ARN par groupes de trois
    for i in range(0, len(rna_seq), 3):
        codon = rna_seq[i:i + 3]  # Extraire un codon

        # Vérifier si le codon est dans le code génétique et
        # ajouter l'acide aminé correspondant
        if codon in GENETIC_CODE:
            peptide += GENETIC_CODE[codon]
        else:
            break  # Arrêter la traduction en cas de codon inconnu

    return peptide


if __name__ == "__main__":
    main()

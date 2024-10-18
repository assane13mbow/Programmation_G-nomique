"""BCM2550 - TP2 - ASSANE MBOW."""

import csv


def main():
    """BCM2550 - TP2 - ASSANE MBOW."""
    # Étape 1 : Ouvrir et lire le fichier ligne par ligne
    with open("NA12878.vcf", "r", encoding="utf-8") as vcf_file, \
         open("results.csv", "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        # Écrire l'en-tête du fichier CSV
        csv_writer.writerow(['variant_id', 'variant_type'])
        for line in vcf_file:
            # Étape 2 : exlclure les lignes de métadonnées et de titre
            if line.startswith("##"):
                continue
            if line.startswith("#"):  # Ignorer la ligne de titre
                continue
            # Séparer la ligne en colonnes par des tabulations
            columns = line.strip().split("\t")
            # Étape 3 : Extraction de l'information demandée
            chromosome = columns[0]    # Colonne du chromosome
            position = columns[1]      # Colonne de la position
            ref_allele = columns[3]    # Colonne de l'allèle de référence
            alt_allele = columns[4]    # Colonne de l'allèle alternatif
            # Étape 4 : Création de l'identifiant
            variant_id = f"{chromosome}:{position}:{ref_allele}:{alt_allele}"
            # Étape 5 : Déterminer le type de mutation
            if len(ref_allele) == 1 and len(alt_allele) == 1:
                variant_type = "SNV"   # Il s'agit d'un SNV
            else:
                variant_type = "INDEL"  # Il s'agit d'un INDEL
            # Étape 6 : Générer un fichier CSV
            csv_writer.writerow([variant_id, variant_type])

    print("Le fichier results.csv a été généré avec succès.")


if __name__ == "__main__":
    main()

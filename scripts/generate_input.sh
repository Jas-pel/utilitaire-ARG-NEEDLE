#!/bin/sh
# NOTE : Le code permet de de générr les fichiers nécessaire pour ARG_NEEDLE
module load StdEnv/2020

# Message lancement script
echo -e "\n\nÉTAPE 2 : CRÉATION DES 3 FICHIERS D'INPUTS (MAP, SAMPLE ET HAPS)"

# Assigner les arguments à des variables
phased_vcf_file="$1"
start="$2"
stop="$3"
range_file="$4"
file_col_1_path="$5"
file_col_2_path="$6"
output_dir="$7"
LOG_ARG_NEEDLE_DIR="$8"


# Créer le fichier range
echo -e "19\t${start}\t${stop}\t1" > "${range_file}"
echo -e "Fichier range '${range_file}' créé avec succès."


# Générer .haps et .sample using Plink 2
module load plink/2.00-10252019-avx2
plink2 --vcf "${phased_vcf_file}" --extract range "${range_file}" --keep "${file_col_1_path}" --export haps --out "${output_dir}"
if [ $? -ne 0 ]; then
    echo -e "Erreur lors de la génération des fichiers .haps et .sample avec Plink 2."
    exit 1
else
    echo -e "Fichiers ${output_dir}.haps et ${output_dir}.sample générés avec succès."
fi


# Générer .map using Plink 1.9
module load plink/1.9b_6.21-x86_64
plink --vcf "${phased_vcf_file}" --extract range "${range_file}" --keep "${file_col_2_path}" --recode --out "${output_dir}" --double-id
if [ $? -ne 0 ]; then
    echo -e "Erreur lors de la génération du fichier .map avec Plink 1.9."
    exit 1
else
    echo -e "Fichier ${output_dir}.map généré avec succès."
fi


# Déplacer les fichiers inutiles
mv "${output_dir}.nosex" "${output_dir}.ped" "${output_dir}.log" "$LOG_ARG_NEEDLE_DIR"
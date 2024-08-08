#!/bin/sh
# Jasmin Pelletier


# ALLER DANS LA REPOSITERY
cd "/home/jaspel/projects/rrg-girardsi/ARGS/Utilitaire-ARG-NEEDLE"


# ARGUMENT
phased_vcf_file=$1
csv_file=$2
start=$3
stop=$4
terminaison_fichier=$5
lst_sample=$6
cluster=$7
path_venv=$8


# CONSTANTE
# Dossier de travail
SCRIPTS_DIR="scripts/"
RESULTS_DIR="results/"
INPUT_ARG_NEEDLE_DIR="data/INPUT_ARG_NEEDLE/"
LOG_ARG_NEEDLE_DIR="data/LOG_ARG_NEEDLE/"
mkdir -p "${INPUT_ARG_NEEDLE_DIR}" "${LOG_ARG_NEEDLE_DIR}" "${RESULTS_DIR}" # Créer les dossiesrs si ils existent pas
chmod -R 777 "${INPUT_ARG_NEEDLE_DIR}" "${LOG_ARG_NEEDLE_DIR}" "${RESULTS_DIR}" # Donne les permissions à tout le monde

# Autre
sample_col_1="${LOG_ARG_NEEDLE_DIR}patients_1_col_${terminaison_fichier}.lst"
sample_col_2="${LOG_ARG_NEEDLE_DIR}patients_2_col_${terminaison_fichier}.lst"
output_path="${INPUT_ARG_NEEDLE_DIR}${terminaison_fichier}"
map_file="${output_path}.map" 
arg_file="${RESULTS_DIR}${terminaison_fichier}"  


############################################################
# MAIN
############################################################


# ÉTAPE 0 : CONNECTION VENV + AFFICHER LE LOGO
source "${path_venv}/bin/activate"
source "${SCRIPTS_DIR}arg_needle_logo.sh"


# ÉTAPE 1 : CRÉATION DES LISTES DE PATIENTS
echo -e "\n\nÉTAPE 1 : CRÉATION DES LISTES DE PATIENTS"
awk -F',' 'NR > 1 {print $1}' "$csv_file" | awk '!seen[$0]++' > "$sample_col_1"           # Création de sample_col_1 sans doublons
awk -F',' 'NR > 1 {print $1 "\t" $1}' "$csv_file" | awk '!seen[$0]++' > "$sample_col_2"   # Création de sample_col_2 sans doublons, avec colonne supplémentaire
echo "Fichier ${sample_col_1} créé."
echo "Fichier ${sample_col_2} créé."


# ÉTAPE 2 : CRÉER LES 3 FICHIERS D'INPUTS (MAP, SAMPLE ET HAPS)
bash "${SCRIPTS_DIR}generate_input.sh" \
    "${phased_vcf_file}"  \
    "${start}"  \
    "${stop}"  \
    "${LOG_ARG_NEEDLE_DIR}${terminaison_fichier}.snps.range"  \
    "${sample_col_1}"  \
    "${sample_col_2}"  \
    "${output_path}"  \
    "${LOG_ARG_NEEDLE_DIR}"  \


# ÉTAPE 3 : CRÉER CSV EN ORDRE AVEC ID
python "${SCRIPTS_DIR}create_csv_in_order.py" \
    "${output_path}.sample" \
    "${csv_file}" \
    "${csv_file%????}_in_order.csv"

csv_file="${csv_file%????}_in_order.csv"


# ÉTAPE 4 : INTERPOLATION DES POSITIONS GÉNÉTIQUES
echo -e "\n\nÉTAPE 4 : INTERPOLATION DES POSITIONS GÉNÉTIQUES"
module load r/4.4.0
Rscript "${SCRIPTS_DIR}interpolation.R"  -map "${INPUT_ARG_NEEDLE_DIR}${terminaison_fichier}.map" 
echo "Fichier .map mis à jour écrit : ${map_file}"


# ÉTAPE 5 : CRÉATION D'UN OBJET ARG-NEEDLE
echo -e "\n\nÉTAPE 5 : CRÉATION D'UN OBJET ARG-NEEDLE\n"
arg_needle --hap_gz "${output_path}.haps" --map "${map_file}" --out "${arg_file}"
echo "Object arg_needle créer : ${arg_file}"


# Étape 6 : AFFICHAGE INFORMATION
echo -e "\n\nÉTAPE 6 : AFFICHAGE DES INFORMATIONS\n"
python "${SCRIPTS_DIR}analyse_and_visualisation_ARGN/main.py" \
    --path_meta_data "$csv_file" \
    --path_argn "$arg_file.argn" \
    --path_fichier_svg "${RESULTS_DIR}${terminaison_fichier}.svg" \
    --path_fichier_html "${RESULTS_DIR}${terminaison_fichier}.html" \
    --cluster "$cluster" \
    --lst_sample "$lst_sample"
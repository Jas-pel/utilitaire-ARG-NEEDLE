#!/bin/sh
# Jasmin Pelletier

# CONSTANTE
csv_file=$1
path_argn=$2
lst_sample=$3
cluster=$4
terminaison_fichier=$5

# DOSSIER
ARGS_DIR="/lustre03/project/6033529/ARGS/"
RESULTS_DIR="${ARGS_DIR}results/"
SCRIPTS_DIR="${ARGS_DIR}scripts/"


# MAIN
source "${SCRIPTS_DIR}venv/bin/activate"
python "${SCRIPTS_DIR}analyse_and_visualisation_ARGN/main.py" \
    --path_meta_data "$csv_file" \
    --path_argn "$path_argn" \
    --path_fichier_svg "${RESULTS_DIR}${terminaison_fichier}.svg" \
    --path_fichier_html "${RESULTS_DIR}${terminaison_fichier}.html" \
    --cluster "$cluster" \
    --lst_sample "$lst_sample"
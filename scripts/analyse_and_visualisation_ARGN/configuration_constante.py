import argparse
def configurer_constantes():
    """ 
    Reçois des constantes.
    Les retournes dans le main.
    """
    parser = argparse.ArgumentParser(description="Configurer les constantes pour l'analyse et la visualisation ARGN")
    
    parser.add_argument("--path_meta_data", type=str, required=True, help="Chemin vers les métadonnées")
    parser.add_argument("--path_argn", type=str, required=True, help="Chemin vers le fichier ARGN")
    parser.add_argument("--path_fichier_svg", type=str, required=True, help="Chemin de sortie pour le SVG")
    parser.add_argument("--path_fichier_html", type=str, required=True, help="Chemin de sortie pour le HTML")
    parser.add_argument("--lst_sample", type=str, required=True, help="Liste des échantillons")
    parser.add_argument("--cluster", type=str, required=True, help="Cluster, écrire haplotype ou haplogroupe")

    args = parser.parse_args()


    # Transforme les variables et les prints
    PATH_META_DATA: str = args.path_meta_data ; print(f"PATH_META_DATA : {PATH_META_DATA}")
    PATH_ARGN: str  = args.path_argn ; print(f"PATH_ARGN : {PATH_ARGN}")    
    PATH_OUTPUT_SVG: str  = args.path_fichier_svg ; print(f"PATH_OUTPUT_SVG : {PATH_OUTPUT_SVG}")
    PATH_OUTPUT_HTML: str  = args.path_fichier_html ; print(f"PATH_OUTPUT_HTML : {PATH_OUTPUT_HTML}")
    LST_SAMPLE: str  = list(map(int, args.lst_sample.split())) ; print(f"LST_SAMPLE : {LST_SAMPLE}")
    CLUSTER: str  = args.cluster ; print(f"CLUSTER : {CLUSTER}")

    return PATH_META_DATA, PATH_ARGN, PATH_OUTPUT_SVG, PATH_OUTPUT_HTML, LST_SAMPLE, CLUSTER
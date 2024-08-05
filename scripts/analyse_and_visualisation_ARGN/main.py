# Import des bibliothèques
from affichage_figure import create_figure_html, enregistrer_figure_html
from affichage_arbre import creer_enregister_arbre_svg
from data_frame import create_data_frame
from tskit_transformation import obtenir_arbre, obtenir_arbre_simplifier, obtenir_tree_sequence
from configuration_constante import configurer_constantes



def charger_meta_donnee_sample() -> tuple[dict, list]:
    """ 
    Charge les métadonnées à partir d'un fichier CSV (path venant de constante.py).
    Retourne une dictionnaire ou la clé est l'id du noeud et les values les rangées du CSV.
    Retourne les header de CSV
    """
    donnees_dict = {}

    with open(PATH_META_DATA, mode='r', newline='') as file:
        lines = file.readlines()
        header_information = lines[0].lower().strip().split(",")

        for line in lines[1:]:
            informations = line.lower().strip().split(",")
            donnees_dict[int(informations[0])] = informations

    return donnees_dict, header_information


def creer_dict_noeud(arbre: object) -> tuple[dict, list]:
    """
    Ajoute les autres id au dictionnaire.
    Retourne la liste des objets noeuds.
    """
    donnees_dict, header_information = charger_meta_donnee_sample()

    for id_noeud in arbre.nodes():
        if id_noeud not in donnees_dict:
            donnees_dict[id_noeud] = [id_noeud]

            for _ in range(len(header_information)-1):
                donnees_dict[id_noeud].append("")

        id_parent = arbre.parent(id_noeud)
        donnees_dict[id_noeud].insert(3, id_parent) if id_parent != -1 else donnees_dict[id_noeud].insert(3, "")

    header_information.insert(3, "id_parent")
    return donnees_dict, header_information




# DÉBUT DU CODE
if __name__ == "__main__":

    # Configurer les constantes
    PATH_META_DATA, PATH_ARGN, PATH_OUTPUT_SVG, PATH_OUTPUT_HTML, LST_SAMPLE, CLUSTER = configurer_constantes()


    # Création d'objet et analyse préliminaire
    tree_sequence = obtenir_tree_sequence(PATH_ARGN)
    arbre = obtenir_arbre(tree_sequence)
    dict_noeud, header_information = creer_dict_noeud(arbre)
    sample_to_keep = [id_sample for id_sample in arbre.leaves() if dict_noeud[id_sample][2] == "1"]


    # Affiche le html
    data_frame = create_data_frame(arbre, dict_noeud, header_information)
    fig = create_figure_html(data_frame, header_information, CLUSTER)
    enregistrer_figure_html(fig, PATH_OUTPUT_HTML)
    print(f"La figure ({PATH_OUTPUT_HTML}) à bien été enregistrer en HTML")


    # Affiche le SVG
    arbre, probabilite = obtenir_arbre_simplifier(tree_sequence, [i for i in LST_SAMPLE if i in sample_to_keep])
    creer_enregister_arbre_svg(arbre, dict_noeud, PATH_OUTPUT_SVG)
    print(f"L'arbre ({PATH_OUTPUT_SVG}) à bien été enregistrer en SVG, il y a {probabilite}% de chance que l'arbre soit le bon")
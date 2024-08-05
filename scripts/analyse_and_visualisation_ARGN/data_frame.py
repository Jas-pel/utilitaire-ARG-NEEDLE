# Le fichier contient les fonctions en lien avec la création et l'affichage du data_frame
import pandas as pd

def trouver_noeuds_a_pas_afficher(arbre: object, donnees_dict: dict[list]) -> list[int]:
    """ 
    Trouve les nœuds à supprimer dans un arbre.
    Retourne une liste de int.
    """
    noeuds_a_pas_afficher = []
    for id_noeud in arbre.nodes():
        if id_noeud not in noeuds_a_pas_afficher :
            if all(["0" == donnees_dict[id_sample][2] or "testtttt" == donnees_dict[id_sample][4] for id_sample in arbre.leaves(id_noeud)]):
                noeuds_a_pas_afficher.extend(list(arbre.nodes(id_noeud)))
    return noeuds_a_pas_afficher


def create_data_frame(arbre: object, donnees_dict: dict[list], header_information: list) -> object:
    """ 
    Créer un data_frame.
    """
    noeuds_a_pas_afficher = trouver_noeuds_a_pas_afficher(arbre, donnees_dict)
    for id_noeud in noeuds_a_pas_afficher:
        del donnees_dict[id_noeud]
    
    with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
        df = pd.DataFrame.from_dict(donnees_dict, orient='index')
        df.columns = header_information
        print(df.to_string(index=False))
        return df
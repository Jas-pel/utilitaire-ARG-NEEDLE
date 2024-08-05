import arg_needle_lib
from tskit import *


def obtenir_tree_sequence(PATH_ARGN) -> object:
    """
    Désérialise le fichier .argn.
    Le transforme en objet tskit tree_sequence.
    Retourne cet objet.
    """
    arg_object = arg_needle_lib.deserialize_arg(PATH_ARGN)
    return arg_needle_lib.arg_to_tskit(arg_object)


def obtenir_arbre(tree_sequence: object) -> object:
    """
    Reçois un objet tree_sequence.
    Retourne un objet arbre.
    """
    return tree_sequence.at_index(200)


def obtenir_arbre_simplifier(tree_sequence: object, sample_to_keep: list[int]) -> object:
    """
    Reçois une liste d'id de feuille à conserver.
    Retourne l'objet arbre simplifier et la probabilité (float) que ce soit le bon arbre.
    """
    tree_sequence = tree_sequence.simplify(samples=sample_to_keep, filter_nodes=False)  
    return tree_sequence.at_index(0), round(100/tree_sequence.num_trees, 2)
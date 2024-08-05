# Le fichier contient les fonctions en lien avec la création et l'affichage de l'arbre SVG

def creer_enregister_arbre_svg(arbre: object, dict_noeud: dict[list], PATH_OUTPUT_SVG: str):
    """
    Transformer un arbre en format SVG et l'enregistrer dans un fichier.
    """
    nodes_labels = {}
    for id_noeud in arbre.nodes():
        sample = dict_noeud[id_noeud][1]
        if sample : sample = sample[3:]
        else : sample = id_noeud
        nodes_labels[id_noeud] = sample

    node_label_style = (
    ".node > .lab {font-size: 70%}"
    ".leaf > .lab {font-size: 100%; text-anchor: start; transform: rotate(90deg) translate(-70px, -10px)}"
    )
    with open(PATH_OUTPUT_SVG, "w") as file:
        file.write(arbre.draw_svg(size=(850, 480), time_scale="rank", node_labels=nodes_labels, style=node_label_style))


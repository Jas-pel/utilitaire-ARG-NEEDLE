# Le fichier contient les fonctions en lien avec la création et l'affichage de la figure HTML
import plotly.express as px


def create_figure_html(data, header_information, CLUSTER) -> object:
    """ 
    Créer une figure HTML et la retourne .
    """
    fig =  px.sunburst(
        data,
        names='id',
        parents='id_parent',
        color=CLUSTER.lower(),
        color_continuous_scale="Spectral",
        width=1700,
        height=1700,
        hover_data={titre : True for titre in header_information}
    )

    fig.update_traces(textinfo='label+text', text=data['sample'])
    return fig

def enregistrer_figure_html(fig: object, PATH_OUTPUT_HTML: str):
    """
    Transformer une figure en format HTML et l'enregistrer dans un fichier.
    """
    with open(PATH_OUTPUT_HTML, "w") as file:
        file.write(fig.to_html())
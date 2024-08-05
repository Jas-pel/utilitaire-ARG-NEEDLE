# Utilitaire ARG-NEEDLE


## Description

**ARG-NEEDLE** est un package conçu pour inférer des graphiques de recombinaison ancestrale (ARG) à partir de données de génotypage ou de séquençage. Il permet également de réaliser diverses analyses basées sur les ARG, telles que les associations généalogiques.

Cet utilitaire facilite l'utilisation d'ARG-NEEDLE en offrant des fonctionnalités supplémentaires :

- **Visualisation** : Génère des graphiques interactifs ou des arbres pour une visualisation approfondie des données fournies par le package.
- **Association des données** : Associe des données de survols aux échantillons pour une analyse détaillée des clusters, des familles et plus encore.
- **Simplicité d'utilisation** : Nécessite seulement un fichier VCF et un fichier CSV pour fonctionner.
- **Personnalisable** : Les graphiques interactifs et les arbres sont facilement personnalisables pour divers types d'utilisation.


## Arguments nécessaires

Il y a 7 arguments à fournir pour exécuter le script.

#### VCF
- **Description :** Chemin vers un fichier VCF.
- **Exemple :** `/path/to/file.vcf`

#### CSV
- **Description :** Chemin vers un fichier CSV.
- **Exemple :** `/path/to/file.csv`
- **Format requis :** Le fichier CSV doit contenir au moins deux colonnes :
  1. **Échantillon (Sample) :** Doit correspondre aux échantillons du VCF.
  2. **Valeur 0 ou 1 :** Arg-Needle exige qu'il y ait un échantillon pour chaque allèle. Pour les maladies dominantes, l'un des échantillons n'est pas essentiel. Dans ce cas, attribuez la valeur 0 à cet échantillon.

  Le fichier CSV peut également contenir autants de colonnes supplémentaires que nécessaires, telles que l'haplogroupe ou l'haplotype.

- **Exemple de CSV :**
  ```csv
  Sample,Utile,Haplotype
  11128103_11128103,1,H061
  11128103_11128103,0,H061
  FDM007_JM0083,1,H2618
  FDM007_JM0083,0,H2618
  FDM014_JM0725,1,H2843
  ```

- **IMPORTANT :**
Les échantillons doivent toujours apparaître deux fois de suite dans le CSV.

#### START
- **Description :** Borne inférieur à utiliser pour le nombre de Mb.
- **Exemple :** 200000

#### STOP
- **Description :** Borne supérieur à utiliser pour le nombre de Mb.
- **Exemple :** 500000

#### TERMINAISON_FICHIER
- **Description :** Nom de base pour les fichiers qui seront créés.
- **Exemple :** "test"

#### LST_SAMPLE
- **Description :** Liste d'IDs d'échantillons pour visualiser l'arbre menant à leur MRCA (Most Recent Common Ancestor).
- **Exemple :** "10 12 17 26"
- **IMPORTANT :** Les ID doivent être séparer d'une espace et être dans un str.

#### CLUSTER
- **Description :** Indique le type de clustering à afficher.
- **Exemple :** "haplotype"
- **Valeurs possible :** 
N'importe quelle titres des colonnes du CSV.

#### CLUSTER
- **Description :** Dossier menant vers l'environement virtuel.
- **Exemple :** 'dir/vers/venv/'


## Comment exécuter le code ?

Pour exécuter le pipeline ARG-NEEDLE, utilisez la commande suivante dans votre console :

```bash
bash path/vers/pipeline_arg_needle.sh "phased_vcf_file" "csv_file" start stop "terminaison_fichier" "lst_sample" "cluster" "dir/vers/venv/"
```

Pour exécuter l'affichage, il vous suffit d'écrire dans la console ceci :
```bash
bash path/vers/visualisation.sh "csv_file" "path/vers/.argn" "lst_sample" "cluster" "terminaison_fichier"
```


## Comment installer les packages nécessaires ?

Il vous suffit d'activer votre environement virtuel (source venv/bin/activate) et de faire pip install "requirements.txt".


## Bug possible

- **Un ou des samples présents dans le CSV ne sont pas dans le VCF initial.** 
  - **Solution :** S'assurer que les samples sont dans le VCF.

- **Voir l'erreur disant que les positions génétiques doivent augmenter lors de l'étape 4.** 
  - **Solution :** Trouver le fichier `decoders.py`, et mettre un commentaire devant la vérification de l'augmentation des positions génétiques.
  - **Explication :** Selon `arg-needle`, les positions génétiques n'augmentent pas mais elles augmentent bel et bien. Le problème vient de la représentation des nombres nuages en 16 bits.


## Suggestions et Contact

Je suis toujours preneur d'idées pour améliorer ce projet. Si vous avez des suggestions ou des questions, n'hésitez pas à me contacter :

- Par email : [pelletierjasmin7@gmail.com](mailto:votre.email@gmail.com)
- Sur GitHub : [Jas-pel](https://github.com/votre-profil)

Je serai ravi de discuter de toute amélioration ou collaboration possible.


## À propos

Ce projet a été développé au cours de mon stage de trois mois au laboratoire Genopop, associé à l'UQAC. Je tiens à remercier les personnes qui ont apporté leur aide et leurs suggestions tout au long de ce processus.

Ce projet a été subventionné par le gouvernement du Québec dans le cadre du programme BIRSC, ainsi que du soutien du laboratoire Genopop.

Réalisé par Jasmin Pelletier, 2024


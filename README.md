## 1. Arguments nécessaires

Il y a 6 arguments à fournir pour exécuter le script.

### VCF
- **Description :** Chemin vers un fichier VCF standard.
- **Exemple :** `/path/to/file.vcf`

### CSV
- **Description :** Chemin vers un fichier CSV contenant des informations sur les échantillons.
- **Format requis :** Le fichier CSV doit contenir au moins deux colonnes :
  1. **Échantillon (Sample) :** Doit correspondre aux échantillons du VCF.
  2. **Valeur 0 ou 1 :** Arg-Needle exige qu'il y ait un échantillon pour chaque allèle. Pour les maladies dominantes, l'un des échantillons n'est pas essentiel. Dans ce cas, attribuez la valeur 0 à cet échantillon.

  Le fichier CSV peut également contenir des colonnes supplémentaires, telles que l'haplogroupe ou l'haplotype.

- **Exemple de CSV :**
  ```csv
  Sample,Utile,Haplotype
  11128103_11128103,1,H061
  11128103_11128103,0,H061
  FDM007_JM0083,1,H2618
  FDM007_JM0083,0,H2618
  FDM014_JM0725,1,H2843
  
**IMPORTANT :**
Les échantillons doivent toujours apparaître deux fois de suite dans le CSV.

### START
- **Description :** Entier indiquant la taille à partir de laquelle commencer.
- **Exemple :** 20000

### STOP
- **Description :** Entier indiquant la taille jusqu'à laquelle aller.
- **Exemple :** 50000

### TERMINAISON_FICHIER
- **Description :** Nom de base pour les fichiers qui seront créés.
- **Exemple :** "test"

### LST_SAMPLE
- **Description :** Liste d'IDs d'échantillons pour visualiser l'arbre menant à leur MRCA (Most Recent Common Ancestor).
- **IMPORTANT :** Les ID doivent être séparer d'une espace et être dans un str.
- **Exemple :** "10 12 17 26"

### CLUSTER
- **Description :** Indique le type de clustering à afficher.
- **Valeurs possible :** 
N'importe quelle titres des colonnes du CSV.


# 2. Comment exécuter le code ?

Il vous suffit d'écrire dans la console ceci :
bash path/vers/pipeline_arg_needle.sh "phased_vcf_file" "csv_file" start stop "terminaison_fichier" "lst_sample" "cluster"

Cela peux resembler à ceci : 
bash /lustre03/project/6033529/ARGS/scripts/pipeline_arg_needle.sh "/lustre03/project/6033529/DM1/results/genotypes/IBD/dm1_CaG_sag_chr19.vcf.gz" "/lustre03/project/6033529/ARGS/data/meta_data.csv" 42091163 50149813 "test" "6 298 122 126 58 18 8" "haplogroupe"


Pour exécuter l'affichage, il vous suffit d'écrire dans la console ceci :
bash path/vers/visualisation.sh "csv_file" "path/vers/.argn" "lst_sample" "cluster" "terminaison_fichier"

Cela peux resembler à ceci : 
bash /lustre03/project/6033529/ARGS/scripts/visualisation.sh "/lustre03/project/6033529/ARGS/data/meta_data.csv" "/lustre03/project/6033529/ARGS/results/test.argn" "10 12 24" "haplogroupe" "test2"



# 3. Comment installer les packages nécessaires ?

Il vous suffit d'activer votre environement virtuel (source venv/bin/activate) et de faire pip install "requirements.txt".



# 4. Bug possible

- **Un ou des samples présents dans le CSV ne sont pas dans le VCF initial.** 
  - **Solution :** S'assurer que les samples sont dans le VCF.

- **Voir l'erreur disant que les positions génétiques doivent augmenter lors de l'étape 4.** 
  - **Solution :** Trouver le fichier `decoders.py`, et mettre un commentaire devant la vérification de l'augmentation des positions génétiques.
  - **Explication :** Selon `arg-needle`, les positions génétiques n'augmentent pas mais elles augmentent bel et bien. Le problème vient de la représentation des nombres nuages en 16 bits.


import csv
import sys

# Début du script
print("\n\nÉTAPE 4 : CRÉER CSV EN ORDRE AVEC ID")


# Fichiers d'entrée et de sortie
txt_file = sys.argv[1]
csv_file = sys.argv[2]
output_csv_file = sys.argv[3]


# Lire les identifiants depuis la deuxième colonne du fichier CSV, à partir de la troisième ligne
identifiants = []
with open(txt_file, 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    # Ignorer les deux premières lignes
    next(reader)
    next(reader)
    for row in reader:
        if len(row) > 1:  # S'assurer qu'il y a au moins deux colonnes
            identifiants.append(row[1].strip())


# Lire les données du fichier CSV
with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # Lire l'en-tête
    rows = [tuple(row) for row in reader]  # Convertir les lignes en tuples


# Créer un dictionnaire pour stocker les lignes du CSV par identifiant
csv_dict = {}
for row in rows:
    identifiant = row[0]
    if identifiant in csv_dict:
        csv_dict[identifiant].append(row)
    else:
        csv_dict[identifiant] = [row]


# Réorganiser les lignes du CSV en fonction des identifiants du fichier .txt
sorted_rows = []
for identifiant in identifiants:
    if identifiant in csv_dict:
        # Ajouter les lignes correspondantes en conservant l'ordre original
        for row in csv_dict[identifiant]:
            sorted_rows.append(row)



# Ajouter la colonne "id" avec des chiffres croissants à partir de 0
new_header = ['Id'] + header  # Nouveau header avec "id" en première position
sorted_rows_with_id = [(i, *row) for i, row in enumerate(sorted_rows)]


# Écrire les données réorganisées dans le nouveau fichier CSV
with open(output_csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(new_header)  # Écrire l'en-tête avec la nouvelle colonne "id"
    writer.writerows(sorted_rows_with_id)


# Fin du script
print(f'Le fichier CSV réorganisé avec la colonne "id" a été enregistré sous "{output_csv_file}".')

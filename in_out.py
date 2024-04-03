import csv

def ouverture_fichier(fic):
    with open(fic, 'r') as fic:
        txt = fic.read()
    return txt

def csv_file(rows, fichier_out):
    with open(fichier_out, 'w') as csv_out:
        csv_output = csv.writer(csv_out)
        for row in rows:
            csv_output.writerow(row)
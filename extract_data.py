import re
import argparse
import csv

def parse_fic():
    parser = argparse.ArgumentParser()
    parser.add_argument('fichier') # ajout argument positionnel
    return parser.parse_args()

def extract_info(chaine, type_info):
    info = re.findall(r'(M.+)(?<!RC)' + type_info + r'Value = (\d+(\.\d+)?)', chaine)
    return info

def ouverture_fichier():
    with open(parse_fic().fichier, 'r') as fic:
        txt = fic.read()
    return txt

def sortie_resultat(data):
    return [(el[0], float(el[1])) for el in data]

def csv_file(rows, fichier_out):
    with open(fichier_out, 'w') as csv_out:
        csv_output = csv.writer(csv_out)
        for row in rows:
            csv_output.writerow(row)

def do_it():
    txt = ouverture_fichier()
    suv = extract_info(txt, 'SUV')
    hu = extract_info(txt, 'HU')
    dic_suv = sortie_resultat(suv)
    csv_file(dic_suv, 'output_suv.csv')
    dic_hu = sortie_resultat(hu)
    csv_file(dic_hu, 'output_hu.csv')
    print("SUV :\t", dic_suv)
    print("HU  :\t", dic_hu)

if __name__ == '__main__':
    do_it()
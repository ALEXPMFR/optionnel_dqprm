import re
import argparse
from in_out import ouverture_fichier, csv_file

def parse_fic():
    parser = argparse.ArgumentParser()
    parser.add_argument('fichier') # ajout argument positionnel
    parser.add_argument('-o')
    return parser.parse_args()

def extract_info(chaine, type_info):
    info = re.findall(r'(M.+)(?<!RC)' + type_info + r'Value = (\d+(\.\d+)?)', chaine)
    return info

def sortie_resultat(data):
    return [(el[0], float(el[1])) for el in data]

def do_it(fic, output):
    txt = ouverture_fichier(fic)
    suv = extract_info(txt, 'SUV')
    hu = extract_info(txt, 'HU')
    dic_suv = sortie_resultat(suv)
    csv_file(dic_suv, output + '_suv.csv')
    dic_hu = sortie_resultat(hu)
    csv_file(dic_hu, output + '_hu.csv')
    print("SUV :\t", dic_suv)
    print("HU  :\t", dic_hu)



if __name__ == '__main__':
    p = parse_fic()
    do_it(p.fichier, p.o)
import re
import argparse

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

def do_it():
    txt = ouverture_fichier()
    suv = extract_info(txt, 'SUV')
    hu = extract_info(txt, 'HU')
    dic_suv = {el[0]: float(el[1]) for el in suv}
    dic_hu = {el[0]: float(el[1]) for el in hu}
    print("SUV :\t", dic_suv)
    print("HU  :\t", dic_hu)

if __name__ == '__main__':
    do_it()
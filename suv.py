import re
import argparse

def parse_fic():
    parser = argparse.ArgumentParser()
    parser.add_argument('fichier') # ajout argument positionnel
    return parser.parse_args()

def extract_SUV(chaine):
    suv = re.findall(r'(M.+)(?<!RC)SUVValue = (\d+\.\d+)', chaine)
    return suv

def do_it():
    with open(parse_fic().fichier, 'r') as fic:
        txt = fic.read()
    suv = extract_SUV(txt)
    d = {el[0]: float(el[1]) for el in suv}
    print(d)

if __name__ == '__main__':
    do_it()
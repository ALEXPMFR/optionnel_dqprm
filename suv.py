import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('fichier') # ajout argument positionnel
arg = parser.parse_args()

def do_it():
    with open(arg.fichier, 'r') as fic:
        txt = fic.read()

    suv = re.findall(r'(M.+)(?<!RC)SUVValue = (\d+\.\d+)', txt)

    d = {el[0]: float(el[1]) for el in suv}
    print(d)

if __name__ == '__main__':
    do_it()
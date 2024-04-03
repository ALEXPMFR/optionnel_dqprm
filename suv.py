import re

with open('20200527152905.861802.ig.tum', 'r') as fic:
    txt = fic.read()

suv = re.findall(r'(M.+)(?<!RC)SUVValue = (\d+\.\d+)', txt)

d = {el[0]: float(el[1]) for el in suv}
print(d)
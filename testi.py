# -*- coding: utf-8 -*-
__author__ = 'eeneku'

numerot = [2.0, 2.5, 0.5, 12.2, 4.3]
pienin = suurin = numerot[0]
yhteensa = 0

for numero in numerot:
    yhteensa += numero

    if numero < pienin:
        pienin = numero
    elif numero > suurin:
        suurin = numero

print("pienin = " + str(pienin) + ", suurin = " + str(suurin) + ", yhteensa = " + str(yhteensa-suurin-pienin))
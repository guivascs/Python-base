#!/usr/bin/env python3
__version__ = "0.0.1" 


# base = [1,2,3,4,5,6,7,8,9,10]
numeros = list(range(1,11))

#Itarable (precorrivel)
for numero in numeros: 
    print("Tabuada do:", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print ("-----------------")
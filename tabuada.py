#!/usr/bin/env python3
__version__ = "0.1.1" 


# base = [1,2,3,4,5,6,7,8,9,10]
numeros = list(range(1,11))

#Itarable (precorrivel)
for n1 in numeros:
    print()
    print("{:-^18}".format(f"Tabuada do {n1}"))
    print()
    bloco = ""
    for n2 in numeros:
        resultado = n1 * n2
        #operacao= f"{n1} x {n2} = {n1 * n2}"
        #print("{n1} x {n2} = {resultado}\n")
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print()
    print("\U0001F600" * 18)

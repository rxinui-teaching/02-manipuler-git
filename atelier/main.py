"""Main program - Circular

@author Rxinui
"""
from circular import Circular
from random import randint

TAILLE : int = 5

if __name__ == "__main__":
    datastructure = Circular(TAILLE)
    print("+ Ajout des éléments")
    for _ in range(TAILLE):
        datastructure.add(randint(-100,100))
        print("\t",datastructure)
    print("+ Shift left des éléments")
    for _ in range(TAILLE):
        datastructure.shift_left()
        print("\t",datastructure)
    print("+ Suppression des éléments")
    for _ in range(TAILLE):
        datastructure.pop()
        print("\t",datastructure)
    print("+ La structure de données doit être vide :",datastructure.is_empty())
    exit(0) if datastructure.is_empty() else exit(1)
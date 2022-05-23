"""Circula data structure.

Structure:
    Circular (ordered) array with a fixed length.

Methods:
    add(e): add element to the data structure
    pop(): remove the 1st element of data structure
    shift_right(): shift all elements to the right 
    shift_left(): shift all elements to the left
    clean(): remove all elements
"""
from typing import *


class Circular:
    
    class PrivArray:
        """NE PAS TOUCHER CETTE CLASSE"""
        def __init__(self, length: int = 0) -> None:
            self.__struct = [None] * length

        def __getitem__(self, key):
            return self.__struct.__getitem__(key)

        def __setitem__(self, key, value):
            return self.__struct.__setitem__(key, value)

        def __iter__(self):
            return self.__struct.__iter__()

        def __len__(self) -> int:
            return len(self.__struct)

        def __repr__(self) -> str:
            return self.__struct.__repr__()

        def __contains__(self, item) -> bool:
            return self.__struct.__contains__(item)

    def __len__(self) -> int:
        return len(self.structure)

    def __repr__(self) -> str:
        return self.structure.__repr__()

    def __contains__(self, item) -> bool:
        return self.structure.__contains__(item)

    @property
    def structure(self) -> PrivArray:
        """Accède à la structure de données qui sert de base pour la Circular."""
        return self.__structure

    def __init__(self, length: int) -> None:
        """Initialise la structure Circular

        Attributes:
            structure: contient les éléments
            nb_element: contient le nombre d'element dans la structure
        """
        self.__structure = Circular.PrivArray(length)
        self.nb_element = 0

    """
    AIDE - Utiliser la syntaxe suivante pour :
        self.structure: acceder à la structure de données 
        self.nb_element: le nombre d'élément dans la structure de données (différent de 'None')

    Vous pouvez consulter le fichier de test 'circular/test_circular.py'.
    """

    def is_empty(self) -> bool:
        """Verifie si la structure de données est vide.

        Vide signifit ici que toutes les valeurs sont définient à 'None'

        Return:
            bool: True si toutes les valeurs sont égales à 'None', sinon False.

        Example:
            Circular(length=3): [None,None,None]
        """
        # TODO
        return False

    def is_full(self) -> bool:
        """Verifie si la structure de données est pleine.

        Pleine signifit ici que toutes les valeurs sont toutes différentes de 'None'

        Return:
            bool: True si toutes les valeurs sont différentes de 'None', sinon False.

        Example:
            Circular(length=3): [0,"hello",3.14]
        """
        # TODO
        return False

    def add(self, e: Any) -> "Circular":
        """Ajoute l'element e dans la structure de données.

        Si la structure de données est pleine, alors on n'ajoute pas l'element.

        Args:
            e (Any): un element de tout type (int, str, ...)

        Return:
            Circular: la structure de données avec le nouvel élément.

        Example:
            Circular(length=3): [None,None,None] --> add("test") --> ["test",None,None]
            Circular(length=3): ["test",None,None] --> add(24) --> ["test",24,None]
        """
        # TODO
        return self.structure

    def clean(self) -> "Circular":
        """Supprime tous les éléments (mise à 'None')

        Return:
            Circular: la structure de données vide

        Example:
            Circular(length=3): [110,"world",None] --> clean() --> [None,None,None]
        """
        # TODO
        return self.structure

    def shift_left(self) -> "Circular":
        """Pivote les éléments par la gauche.

        Le 1er element devient dernier, le 2e devient 1e, ..., le dernier devient avant-dernier.

        Return:
            Circular: la structure de données mis-à-jour

        Example:
            Circular(length=3): [0,"hello",3.14] --> ["hello",3.14,0]
        """
        # TODO
        return self.structure

    def pop(self) -> "Circular":
        """Supprime le 1er element dans la structure de données.

        La suppression s'exprime par la valeur 'None' puis un shift vers la gauche.
        Si la structure de données est vide, alors on ne fait rien.

        Return:
            Circular: la structure de données avec un element en moins.

        Example:
            Circular(length=3): [0,"hello",3.14] --> pop() --> ["hello",3.14,None]
            Circular(length=3): ["hello",3.14,None] --> pop() --> [3.14,None,None]
        """
        # TODO
        return self.structure

"""Atelier 1 python main program

@author Rxinui
"""
from pathlib import Path
from typing import *

##### BEGIN Functions #####
def get_files_path(folder: str) -> List[Path[str]]:
    """Renvoie la liste des noms de fichier contenu dans {folder}
    
    Args:
        folder (str): chemin du dossier à parcourir

    Return:
        List[Path[str]]: liste contenant les chemins des fichiers de {folder}
    """
    return list(Path(folder).iterdir())

def get_file_content(path: Path[str]) -> str:
    """Renvoie le contenu d'un fichier
    
    Args:
        path (Path(str)): chemin du fichier à lire

    Return:
        (str): contenu du fichier
    """
    return open(path).read()

def analyze_files(folder: str) -> None:
    """Analyse les fichier contenu dans {folder}

    Args:
        folder (str): chemin du dossier à analyser
    """
    data = dict.fromkeys(["file","extension","chars","lines"])
    paths = get_files_path(folder)
    for path in paths:
        content = get_file_content(path)
        data["file"], data["extension"], data["chars"], data["lines"] = path.name, path.suffix,len(content),len(content.splitlines())
        print(content,"-"*10,data,sep="\n",end="\n\n")
    return
##### END Functions #####

if __name__ == "__main__":
    ##### BEGIN Main Program #####
    print("Hello atelier 1 !\n")
    analyze_files("./rsc")
    ##### END Main Program #####
"""Télécharger les deux versions OpenML utilisées dans les notebooks."""

import hashlib
from pathlib import Path
from urllib.request import urlopen


# Le chemin reste valable si le projet change de dossier.
dossier = Path(__file__).resolve().parents[1] / "data" / "raw"
dossier.mkdir(parents=True, exist_ok=True)

fichiers = [
    (
        "freMTPL2freq.arff",
        "https://openml.org/data/v1/download/20649148/freMTPL2freq.arff",
        "a45363e056e2ea56408b38eeb9d4d04d7f6c6982eb7a14ed5e807c7c71807cdd",
    ),
    (
        "freMTPL2sev.arff",
        "https://openml.org/data/v1/download/20649149/freMTPL2sev.arff",
        "047632016b87e132247124f449a95d6d0e9f8ba05f2fe0947ef76ab8aaa10e0a",
    ),
]

for nom, url, empreinte_attendue in fichiers:
    chemin = dossier / nom

    if chemin.exists():
        contenu = chemin.read_bytes()
    else:
        print(f"Téléchargement de {nom}...")
        with urlopen(url, timeout=120) as reponse:
            contenu = reponse.read()

    # Vérifier le fichier avant de l'utiliser ou de l'enregistrer.
    empreinte = hashlib.sha256(contenu).hexdigest()
    if empreinte != empreinte_attendue:
        raise ValueError(
            f"Empreinte inattendue pour {nom}. "
            "Aucun fichier existant n'a été remplacé. Vérifier data/SOURCES.md."
        )

    if not chemin.exists():
        chemin.write_bytes(contenu)

    print(f"{nom} : empreinte vérifiée, fichier prêt.")

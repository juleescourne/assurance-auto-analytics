"""Exécuter les trois notebooks et enregistrer leurs résultats."""
from pathlib import Path
import time

import nbformat
from nbclient import NotebookClient

racine = Path(__file__).resolve().parent
for nom in ['data_quality.ipynb', 'analyse_globale.ipynb', 'analyse_approfondie.ipynb']:
    chemin = racine / 'notebook' / nom
    debut = time.time()
    notebook = nbformat.read(chemin, as_version=4)
    print(f'Exécution de {nom}...', flush=True)
    NotebookClient(
        notebook, timeout=600, kernel_name='python3',
        resources={'metadata': {'path': str(racine / 'notebook')}}
    ).execute()
    nbformat.validate(notebook)
    nbformat.write(notebook, chemin)
    print(f'{nom} : OK ({time.time() - debut:.0f} secondes)', flush=True)

print('Notebooks exécutés ; quatre CSV disponibles dans data/processed.', flush=True)

# Sources des données

Les fichiers utilisés viennent des deux jeux **OpenML version 1** ci-dessous. Métadonnées et empreintes vérifiées le **01/10/2026**.

| Fichier | Jeu OpenML | Fichier OpenML | Lignes de données | Licence indiquée |
|---|---|---|---:|---|
| freMTPL2freq.arff | [41214, version 1](https://www.openml.org/d/41214) | 20649148 | 678 013 | CC0 |
| freMTPL2sev.arff | [41215, version 1](https://www.openml.org/d/41215) | 20649149 | 26 639 | CC0 |

Téléchargements directs : [fréquence](https://openml.org/data/v1/download/20649148/freMTPL2freq.arff) et [sévérité](https://openml.org/data/v1/download/20649149/freMTPL2sev.arff).

Métadonnées de référence : [API fréquence](https://www.openml.org/api/v1/json/data/41214) et [API sévérité](https://www.openml.org/api/v1/json/data/41215). Les empreintes MD5 des fichiers locaux correspondent à celles de ces fiches.

```text
freMTPL2freq.arff
MD5    f8875568bf0ca622929105197e2db613
SHA256 a45363e056e2ea56408b38eeb9d4d04d7f6c6982eb7a14ed5e807c7c71807cdd

freMTPL2sev.arff
MD5    24cc74449e3931cb1aad0d43a12e7a6e
SHA256 047632016b87e132247124f449a95d6d0e9f8ba05f2fe0947ef76ab8aaa10e0a
```

Le script [telecharger_donnees.py](../scripts/telecharger_donnees.py) vérifie les SHA-256 avant de conserver un téléchargement. Cela permet de retrouver les mêmes données et les mêmes résultats.

**Attention aux versions :** la description historique de fréquence et la version actuelle de CASdatasets peuvent annoncer des effectifs différents. Les nombres de ce projet sont ceux réellement comptés dans les fichiers OpenML dont les empreintes sont données ici. Ne pas remplacer silencieusement ces fichiers par une autre version.

Les définitions métier sont tirées de [CASdatasets — freMTPL](https://dutangc.github.io/CASdatasets/reference/freMTPL.html). La documentation situe approximativement les observations entre 2011 et 2013, sans dates exploitables dans nos fichiers. L'[exemple scikit-learn](https://scikit-learn.org/stable/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html) présente également le chargement de ces données. Les montants sont exprimés en euros, comme dans l'étude [Machine Learning and Frequency–Severity Decomposition for Insurance Pricing](https://www.mdpi.com/2227-7390/14/10/1640). Les traitements et résultats de ce projet sont ceux de ses notebooks.

Citation fournie par OpenML : **C. Dutang and A. Charpentier (2018), CASdatasets: Insurance datasets.**

Les fichiers bruts ne sont pas modifiés. Les CSV de `processed` sont produits par la dernière section d'[analyse_approfondie.ipynb](../notebook/analyse_approfondie.ipynb). Données brutes et exports sont exclus de Git, mais restent présents localement.

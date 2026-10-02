# Assurance automobile : comprendre les sinistres et les limites des données

**Projet personnel de Data Analyst junior — Jules Courné**
Python · Pandas · Matplotlib · Power Query · Power BI · DAX

Je pars de deux tables publiques d'assurance automobile pour identifier les segments à investiguer en priorité. Le projet couvre le cadrage, le contrôle des données, l'analyse exploratoire et la préparation d'un rapport Power BI.

La question métier est simple : **quels groupes concentrent les sinistres, et lesquels ont une fréquence élevée une fois leur exposition prise en compte ?** Il s'agit d'une mission fictive, sans lien avec un assureur commanditaire.

## Ce que je retiens

- **B12 / véhicules de 0 an : l'écart persiste à durée proche.** Entre 0,50 et 1 an d'exposition, la fréquence est de 21,33 contre 9,68 pour les autres marques. La forte part de montants absents impose encore une vérification des sources.
- **R24 : une moyenne basse peut masquer des profils à étudier.** Les véhicules de 1-2 ans / bonus-malus 76-100 ont une fréquence de 16,96 contre 12,81 pour les mêmes tranches hors R24, sur 1 531 contrats locaux.
- **R11 : la priorité dépend du profil.** À densité 1 001-5 000 et bonus-malus 51-75, la fréquence est de 14,77 contre 12,26 ailleurs. D'autres tranches deviennent proches de leur comparateur.
- **Les coûts restent partiels et sensibles aux gros montants.** 26,76 % des contrats sinistrés sont sans montant retrouvé ; un seul sinistre représente 21,37 % des coûts observés de R24.

Ce sont des comparaisons descriptives, pas des preuves causales. Les effectifs, les sensibilités et les actions proposées sont dans [la synthèse des analyses](docs/Analyse.md).

## Quelques chiffres

| Indicateur | Résultat |
|---|---:|
| Contrats conservés | 678 013 |
| Exposition totale | 358 499,45 années |
| Sinistres déclarés | 36 102 |
| Sinistres avec montant rapproché | 26 444 |
| Fréquence pour 100 années assurées | 10,07 |
| Montant observé et rapproché | 59 909 216,50 € |
| Coût moyen / médian observé | 2 265,51 € / 1 172,00 € |
| Contrats sinistrés sans montant retrouvé | 9 116, soit 26,76 % |

**Fréquence = 100 × somme des sinistres déclarés / somme des expositions.** Ce n'est pas un pourcentage de contrats. Le coût moyen utilise uniquement le nombre de sinistres correspondant aux montants rapprochés.

## Parcourir le projet

| Fichier | Rôle |
|---|---|
| [docs/Cadrage.md](docs/Cadrage.md) | Question métier, périmètre et livrables |
| [docs/Dictionnaire.md](docs/Dictionnaire.md) | Grain, colonnes, segments et définitions des KPI |
| [data_quality.ipynb](notebook/data_quality.ipynb) | Contrôles des deux sources et décisions de traitement |
| [docs/Qualité.md](docs/Qualité.md) | Résumé de l'audit des données |
| [analyse_globale.ipynb](notebook/analyse_globale.ipynb) | Volumes, fréquences, coûts, couverture et gros sinistres |
| [analyse_approfondie.ipynb](notebook/analyse_approfondie.ipynb) | Croisements des segments repérés, puis export des CSV |
| [docs/Analyse.md](docs/Analyse.md) | Résultats, limites et priorités |
| [powerbi/Assurance.pbip](powerbi/Assurance.pbip) | Point d'entrée du rapport Power BI |
| [powerbi/LISEZ_MOI.txt](powerbi/LISEZ_MOI.txt) | Ouverture, modèle, mesures et contrôles dans Desktop |
| [data/SOURCES.md](data/SOURCES.md) | Versions des données, licences et empreintes des fichiers |

Les sorties et les graphiques sont conservés dans les notebooks pour permettre leur lecture directement sur GitHub.

GitHub Actions vérifie la syntaxe Python, les sorties enregistrées des notebooks, les liens locaux et les références aux champs Power BI. Ces contrôles de livrables ne remplacent pas l'exécution des analyses et le contrôle visuel du rapport. Ils se lancent aussi avec `python scripts/verifier_livrables.py`.

## Modèle et rapport Power BI

```text
Contrats (1 ligne par IDpol)  1 ────> *  Sinistres (1 ligne par sinistre rapproché)

Orphelins : table indépendante, pour suivre les sinistres sans contrat dans freq.
```

Le filtre circule des contrats vers les sinistres. L'exposition reste au grain contrat ; les coûts moyens et médians sont calculés sur les sinistres individuels. Les **6 contrats orphelins**, soit **195 lignes et 788 714,18 €**, restent hors des coûts rapprochés et sont présentés séparément.

Le modèle enregistré par Desktop est au format **TMDL**, dans `powerbi/Assurance.SemanticModel/definition`. Il contient trois tables et 86 mesures. Le contrôle des livrables accepte ce format ainsi que l'ancien format `model.bim`.

Le rapport contient cinq pages :

1. **Vue d'ensemble** : KPI, régions, fréquence par âge et comparaison régionale.
2. **B12 / véhicules de 0 an** : exposition, couverture des coûts et sensibilité.
3. **R24** : profils âge du véhicule / bonus-malus, sensibilité et gros sinistre.
4. **R11** : profils densité / bonus-malus et comparaison au reste du portefeuille.
5. **Qualité et limites** : couverture des montants, écart de dénombrement, orphelins et priorités.

**État au 02/10/2026 :** les deux notebooks d'analyse ont été réexécutés et les CSV régénérés. Les fichiers, références et positions Power BI sont contrôlés. **L'actualisation, l'exécution des nouvelles mesures DAX et l'affichage natif restent à confirmer dans Power BI Desktop.** Le contrôle des fichiers ne remplace pas cette dernière étape.

## Reproduire l'analyse

Environnement utilisé : **Python 3.10.9** et Power BI Desktop de septembre 2026 sur Windows. Les versions Python des bibliothèques sont dans [requirements.txt](requirements.txt). Les notebooks n'ont pas besoin d'une licence Office.

Depuis le dossier de ce projet :

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe scripts/telecharger_donnees.py
.venv\Scripts\python.exe -m ipykernel install --sys-prefix --name python3 --display-name "Python (assurance)"
.venv\Scripts\python.exe main.py
.venv\Scripts\python.exe -m jupyterlab
```

Le script télécharge les deux fichiers OpenML précis dans `data/raw` et vérifie leur empreinte SHA-256. Un fichier déjà présent et identique n'est pas téléchargé à nouveau. Les données sont publiques et les deux fiches OpenML indiquent **CC0** ; voir [les sources](data/SOURCES.md).

`main.py` exécute les trois notebooks dans l'ordre et enregistre leurs sorties. Pour les parcourir manuellement dans Jupyter, choisir le noyau **Python (assurance)** et ouvrir le dossier `notebook/`, puis exécuter depuis la première cellule :

1. `data_quality.ipynb`.
2. `analyse_globale.ipynb`.
3. `analyse_approfondie.ipynb`, jusqu'à la section **Exporter les données pour Power BI**.

Les notebooks retrouvent la racine du projet depuis `notebook/` ou depuis la racine. Le dernier crée dix fichiers dans `data/processed` : `contrats.csv`, `sinistres.csv`, `orphelins.csv`, `controle_kpi.csv` et six tableaux `investigation_*.csv` décrits dans le dictionnaire. Seuls les trois premiers sont importés dans le modèle. Ils utilisent le séparateur `;`, l'encodage UTF-8 avec BOM et le point décimal. Les contrôles de fin doivent afficher `Contrôles des exports : OK`.

### Ouvrir Power BI

1. Ouvrir `powerbi/Assurance.pbip` dans Power BI Desktop. Garder les dossiers `Assurance.Report` et `Assurance.SemanticModel` à côté du fichier.
2. Dans **Transformer les données > Gérer les paramètres**, renseigner `DossierDonnees` avec le chemin absolu de **votre** dossier `data/processed`. Le chemin livré correspond au PC de création et doit être adapté après clonage.
3. Appliquer les changements, puis **Actualiser**. Le dépôt contient les définitions du rapport et du modèle, sans cache de données.
4. Sans filtre, comparer les KPI au tableau ci-dessus et à `controle_kpi.csv`. La requête [Controles_investigations.dax](powerbi/Controles_investigations.dax) permet aussi de vérifier B12, R24 et R11.
5. Parcourir les cinq pages et comparer les croisements aux CSV `investigation_*.csv`. Enregistrer ensuite le projet ; un `.pbix` peut être créé avec **Enregistrer sous**.

Les filtres sont propres à chaque page. Dans les trois pages d’investigation, seuls les menus de filtre agissent sur les autres visuels : les clics sur barres ou tableaux ne réduisent pas le groupe de référence. R24 et R11 sont comparées aux autres régions réunies, sous les mêmes filtres. La table des orphelins reste indépendante des filtres portant sur les caractéristiques des contrats.

## Limites et choix

- Tous les contrats de `freq` sont conservés. Une jointure interne aurait supprimé des contrats utiles au calcul de fréquence.
- Un montant non retrouvé reste inconnu : il n'est pas remplacé par zéro.
- Les lignes répétées de `sev` sont conservées faute d'identifiant de sinistre. Le contrat 4158255 présente 2 sinistres déclarés contre 1 ligne de montant et reste signalé.
- Les expositions supérieures à un an et les âges de 100 ans sont conservés et signalés ; leur signification reste à confirmer.
- Les seuils de sélection servent à prioriser l'exploration. Aucun test statistique ni modèle causal n'a été réalisé.
- Sans dates exploitables, primes ni frais, je ne produis pas d'évolution mensuelle, de rentabilité ou de recommandation tarifaire.

Le [cadrage](docs/Cadrage.md) précise le périmètre réalisé : Python, analyse descriptive et Power BI. Le projet ne contient pas de requêtes SQL ni de tests d'inférence.

## Fichiers suivis dans Git

Le dépôt garde les notebooks avec leurs résultats, la documentation, le script de téléchargement, les dépendances et le projet Power BI au format texte. Les données brutes et les CSV se régénèrent localement : `contrats.csv` dépasse à lui seul la limite GitHub de 100 MiB par fichier. [Limites GitHub](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

Le `.gitignore` exclut les données locales, les caches Power BI, les checkpoints Jupyter, les environnements Python et les copies de travail. Le rapport de référence est **Assurance.pbip** ; l'ancienne entrée `Dashboard_Ventes.pbip` et la copie `Assurance_corrigee` ne font pas partie des fichiers à publier.

Sources : C. Dutang et A. Charpentier (2018), *CASdatasets: Insurance datasets*, versions OpenML [41214](https://www.openml.org/d/41214) et [41215](https://www.openml.org/d/41215).

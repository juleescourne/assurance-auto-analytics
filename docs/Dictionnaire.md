# Dictionnaire des données et KPI

**Projet :** assurance automobile, étude de cas fictive.
**Mise à jour :** 01/10/2026. Les définitions ci-dessous correspondent aux notebooks et aux mesures du projet Power BI.

## 1. Données brutes

### freMTPL2freq : une ligne par contrat

| Colonne | Type / unité | Définition |
|---|---|---|
| IDpol | Identifiant entier | Clé unique du contrat, à ne pas additionner |
| ClaimNb | Entier | Nombre de sinistres déclarés pendant la période d'exposition |
| Exposure | Nombre, années | Durée d'exposition du contrat ; deux contrats de six mois représentent une année assurée |
| Area | Catégorie | Code de zone A à F, de rural à urbain selon la documentation |
| VehPower | Catégorie ordonnée | Catégorie de puissance du véhicule |
| VehAge | Entier, années | Âge du véhicule |
| DrivAge | Entier, années | Âge du conducteur principal |
| BonusMalus | Nombre | Coefficient bonus-malus : 100 est la référence, moins de 100 correspond à un bonus |
| VehBrand | Catégorie | Marque codée ; les codes B1, B2… ne sont pas associés à un nom de constructeur dans cette étude |
| VehGas | Catégorie | Carburant : Regular ou Diesel |
| Density | Nombre, habitants/km² | Densité de population de la commune de résidence |
| Region | Catégorie | Code régional, conservé sans inventer de correspondance avec un nom |

### freMTPL2sev : une ligne par sinistre enregistré

| Colonne | Type / unité | Définition |
|---|---|---|
| IDpol | Identifiant entier | Contrat associé ; il peut apparaître sur plusieurs lignes |
| ClaimAmount | Nombre, euros | Montant individuel du sinistre enregistré sur cette ligne, pas un total par contrat |

Il n'y a pas d'identifiant métier de sinistre. Deux lignes identiques ne suffisent donc pas à prouver un doublon. Les dates de sinistre, les primes et les frais ne sont pas disponibles.

## 2. Tables de travail

Dans les notebooks, `df_unified` conserve les **678 013 contrats**. Avant la jointure, `sev` est regroupée par `IDpol` pour créer `NbSinister` (nombre de lignes rapprochées) et `TotalAmount` (somme de leurs montants). Cette étape évite de multiplier l'exposition d'un contrat ayant plusieurs sinistres.

| Status | Définition | Contrats |
|---|---|---:|
| Sans sinistre | ClaimNb = 0 et aucune ligne dans sev | 643 953 |
| Montant non retrouvé | ClaimNb > 0 et aucune ligne dans sev | 9 116 |
| Nombre concordant | ClaimNb égale le nombre de lignes rapprochées | 24 943 |
| Nombre différent | ClaimNb diffère du nombre de lignes rapprochées | 1 |

Le statut de secours `À vérifier` ne concerne aucun contrat dans les fichiers étudiés. Les six IDpol orphelins ne sont pas dans cette table : ils représentent **195 lignes et 788 714,18 €**, conservées à part.

Les exports Power BI séparent les grains :

| Fichier | Grain et contenu |
|---|---|
| contrats.csv | Un contrat : caractéristiques, exposition, ClaimNb, statut et segments ; sans NbSinister ni TotalAmount |
| sinistres.csv | Un sinistre rapproché : LigneSource, IDpol, ClaimAmount |
| orphelins.csv | Un sinistre non rapproché : mêmes colonnes, table indépendante |
| controle_kpi.csv | Une ligne de totaux de référence, non importée dans le modèle |

`LigneSource` est la position dans les lignes de données de `sev`, à partir de 1. C'est un repère technique, pas un identifiant métier. Dans Power BI, `Contrats[IDpol]` filtre `Sinistres[IDpol]` par une relation **1 vers plusieurs**, à sens unique.

## 3. KPI utilisés

Les montants et dénombrements de sinistres observés ci-dessous concernent uniquement les **26 444 lignes rapprochées**. Les fréquences utilisent tous les contrats de `freq`, y compris ceux sans sinistre ou sans montant retrouvé.

| KPI | Calcul | Unité / intérêt |
|---|---|---|
| Nombre de contrats | Nombre de lignes de Contrats, avec IDpol unique | Taille du groupe |
| Exposition totale | Somme de Exposure | Années assurées |
| Sinistres déclarés | Somme de ClaimNb | Volume déclaré dans freq |
| Sinistres observés | Nombre de lignes de Sinistres | Volume avec montant rapproché |
| Fréquence pour 100 années | 100 × somme de ClaimNb / somme de Exposure | Sinistres pour 100 années ; ce n'est pas un pourcentage |
| Montant observé | Somme de ClaimAmount rapprochés | Euros ; charge disponible, incomplète |
| Coût moyen observé | Montant observé / nombre de sinistres observés | Euros par sinistre observé |
| Coût médian observé | Médiane des ClaimAmount individuels rapprochés | Euros ; complément à la moyenne sensible aux gros montants |
| Coût observé par année | Montant observé / exposition totale | Euros par année assurée ; ne mesure pas la rentabilité |
| Contrats sinistrés | Nombre de contrats avec ClaimNb > 0 | Dénominateur du suivi des montants absents |
| Contrats sans montant | Nombre de contrats avec Status = Montant non retrouvé | Contrats sinistrés sans ligne rapprochée |
| Part sans montant | Contrats sans montant / contrats sinistrés | Pourcentage ; 9 116 / 34 060 = 26,76 % au global |
| Contrats nombre différent | Nombre de contrats avec Status = Nombre différent | Suit séparément le contrat 4158255 : 2 déclarés, 1 observé |

Dans les notebooks et `controle_kpi.csv`, la part sans montant vaut **26,76** après multiplication par 100. La mesure DAX renvoie une fraction proche de **0,2676**, formatée en pourcentage : l'affichage est le même.

Les parts de sinistres ou de montants par segment présentes dans les notebooks utilisent le total du portefeuille complet au dénominateur. Elles s'additionnent à 100 % pour un découpage exhaustif sans chevauchement. Ce n'est pas le cas des neuf groupes prioritaires, qui se recoupent.

Le suivi d'influence compare aussi le maximum, sa part dans le montant observé et la moyenne après retrait d'**une seule occurrence** du maximum. Il s'agit d'un calcul de sensibilité : aucun sinistre n'est retiré de la référence.

## 4. Segments ajoutés

| Colonne | Tranches ou groupes |
|---|---|
| TrancheAgeConducteur | 18-24, 25-34, 35-44, 45-54, 55-64, 65-74, 75-99, 100 et plus |
| TrancheAgeVehicule | 0, 1-2, 3-5, 6-10, 11-20, 21-99, 100 et plus |
| TrancheBonusMalus | 50 ou moins, 51-75, 76-100, 101-125, 126-150, 151-200, 201 et plus |
| TranchePuissance | 5 ou moins, 6-7, 8-9, 10-11, 12 et plus |
| TrancheDensite | 100 ou moins, 101-500, 501-1 000, 1 001-5 000, 5 001-20 000, 20 001 et plus |
| TrancheExposition | ]0 ; 0,10], ]0,10 ; 0,50], ]0,50 ; 1], plus de 1 année |
| GroupeMarque | B12 / autres marques |
| GroupeVehicule | 0 an / 1-99 ans / 100 ans et plus |
| GroupeConducteur | 18-24 ans / 25-99 ans / 100 ans et plus |
| GroupeRegion | R11 / autres régions |

Les noms exacts des colonnes et les libellés sont définis dans `analyse_approfondie.ipynb`. Les colonnes `Ordre_…` servent uniquement à trier les tranches dans Power BI. `ContratSinistre` et `SansMontant` sont des indicateurs booléens pour compter les contrats concernés.

La priorité d'exploration repose sur **10 000 contrats minimum**, **1 000 années d'exposition minimum** et une fréquence **au moins 20 % supérieure à celle du portefeuille complet**. Ces seuils de travail ne sont pas des tests statistiques.

## 5. Règles à garder

- Ne pas faire la moyenne des fréquences individuelles : diviser les sommes.
- Ne pas remplacer un coût non retrouvé par zéro.
- Ne pas utiliser les 36 102 sinistres déclarés pour diviser les seuls montants des 26 444 sinistres rapprochés.
- Garder les expositions supérieures à un an et les âges de 100 ans, en signalant leur interprétation incertaine. Aucune exposition n'a été exclue ici : elles sont toutes strictement positives.
- Garder les répétitions de sev et les gros montants dans les résultats de référence.
- Afficher un ratio vide quand son dénominateur est nul ; cela ne veut pas dire zéro.
- Lire les coûts avec leur couverture : la part sans montant ne mesure pas les sinistres partiellement manquants d'un contrat déjà présent dans sev.

Sources : [versions OpenML et documentation métier](../data/SOURCES.md). Résultats : [Analyse.md](Analyse.md). Contrôles : [Qualité.md](Qualité.md).

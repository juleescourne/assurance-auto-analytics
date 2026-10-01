# Synthèse des analyses — Assurance automobile

**Date :** 01/10/2026
**Projet :** étude de cas fictive sur les données freMTPL2freq et freMTPL2sev
**Sources :** [analyse globale](../notebook/analyse_globale.ipynb) et [analyse approfondie](../notebook/analyse_approfondie.ipynb)
**Contrôles des données :** [rapport qualité](Qualité.md)

## 1. Objectif et périmètre

Je cherche les segments qui concentrent les sinistres et les coûts observés, puis ceux qui présentent une fréquence élevée. L'objectif est de proposer des priorités d'investigation pour un responsable assurance.

L'analyse globale donne une vue du portefeuille. L'analyse approfondie croise plusieurs caractéristiques pour mieux comprendre les premiers écarts.

J'ai conservé les **678 013 contrats de freq**, avec une ligne par contrat après unification. Les **6 contrats orphelins de sev, soit 195 lignes de sinistres**, restent à part. Leurs montants ne sont pas inclus dans les coûts rapprochés présentés ici.

Pour la fréquence, j'utilise les sinistres déclarés dans `ClaimNb` et l'exposition de `freq`. Pour les coûts moyens et médians, j'utilise les montants individuels des sinistres rapprochés de `sev`.

## 2. Indicateurs du portefeuille

| Indicateur | Résultat |
|---|---:|
| Nombre de contrats | 678 013 |
| Exposition totale | 358 499,45 années |
| Sinistres déclarés dans freq | 36 102 |
| Sinistres observés dans sev et rapprochés | 26 444 |
| Montant total observé et rapproché | 59 909 216,50 € |
| Fréquence pour 100 années d'exposition | 10,07 |
| Coût moyen par sinistre observé | 2 265,51 € |
| Coût médian par sinistre observé | 1 172,00 € |
| Coût observé par année d'exposition | 167,11 € |
| Part des contrats sinistrés sans montant retrouvé | 26,76 % |

Les principaux calculs sont :

- **Fréquence :** somme de `ClaimNb` / somme de `Exposure` × 100. Ce n'est pas un pourcentage de contrats.
- **Coût moyen observé :** montant rapproché / nombre de sinistres rapprochés, soit 26 444 au total.
- **Part sans montant :** 9 116 contrats sinistrés absents de sev / 34 060 contrats déclarant au moins un sinistre × 100.

Les coûts sont incomplets. Le coût observé par année d'exposition ne représente donc pas la charge complète du portefeuille.

## 3. Ce que montre l'analyse globale

### Volume et fréquence donnent des lectures différentes

J'ai comparé les contrats selon le carburant, la zone, la marque codée, la région, les âges, le bonus-malus, la puissance et la densité.

| Constat | Ce que j'en retiens |
|---|---|
| R24 concentre 25,49 % des sinistres et 28,65 % de l'exposition ; sa fréquence est de 8,96 | Son volume de sinistres est important, mais sa fréquence reste sous les 10,07 du portefeuille |
| Le bonus-malus 50 ou moins représente 50,01 % des sinistres, avec une fréquence de 8,02 | Un grand groupe peut concentrer beaucoup de sinistres sans avoir une fréquence élevée |
| Les 45-54 ans représentent 26,35 % des sinistres ; les véhicules de 6-10 ans, 27,27 % | Ces groupes pèsent dans le volume à suivre |
| Les 18-24 ans ont une fréquence de 18,93, sur 30 198 contrats et 2 364 sinistres | Ce groupe mérite une comparaison plus détaillée de ses profils |
| Les véhicules de 0 an ont une fréquence de 31,13 | Il faut approfondir ce résultat et vérifier les données associées |

Je garde les effectifs et l'exposition à côté des fréquences. Par exemple, le bonus-malus 201 et plus atteint **253,16 sinistres pour 100 années**, mais avec seulement **4 contrats et 2 sinistres**.

### Les coûts sont sensibles aux gros sinistres et aux montants manquants

R24 représente **31,84 % des montants observés**, soit environ **19,07 millions d'euros**. Les véhicules de 11-20 ans représentent **34,75 %** des montants, contre **26,38 %** pour ceux de 6-10 ans.

Le plus gros sinistre, de **4 075 400,56 €**, représente **6,80 % du montant rapproché total** et **21,37 % des montants de R24**. Sans ce sinistre, uniquement pour mesurer son influence, le coût moyen global passe de **2 265,51 € à 2 111,48 €**. La médiane reste à **1 172 €**. Je conserve ce sinistre dans les résultats de référence.

La couverture des coûts varie aussi entre les groupes : **77,51 %** des contrats sinistrés avec un véhicule de 0 an sont sans montant retrouvé, contre **14,18 %** pour les véhicules de 11-20 ans. Les comparaisons de coûts doivent garder cette limite visible.

## 4. Ce que précise l'analyse approfondie

### Sélection des groupes

J'ai retenu les groupes réunissant trois critères : **au moins 10 000 contrats**, **1 000 années d'exposition** et une fréquence **au moins 20 % supérieure à celle du portefeuille**, soit environ **12,08**.

Les neuf groupes retenus sont : **B12, les zones E et F, le bonus-malus 76-100, les véhicules de 0 an, R11, les conducteurs de 18-24 ans et les densités 5 001-20 000 et 20 001 et plus**.

Ils concernent **359 446 contrats distincts et 20 164 sinistres déclarés**. Un contrat pouvant appartenir à plusieurs groupes, je n'additionne pas leurs effectifs. Les autres contrats restent disponibles pour les comparaisons.

Ces seuils servent à choisir les sujets à approfondir. Ils ne constituent pas un test statistique. Le bonus-malus 101-125 reste intéressant, mais ses 6 987 contrats sont sous le seuil de volume choisi.

### B12 et âge du véhicule

| Âge du véhicule | Fréquence B12 | Fréquence des autres marques |
|---|---:|---:|
| 0 an | 45,16 | 12,39 |
| 1-99 ans | 8,22 | 9,20 |

*Unité : sinistres pour 100 années d'exposition.*

Le groupe **B12 / véhicule de 0 an** compte **37 069 contrats et 4 318 sinistres**. Pourtant, **87,10 % de ses contrats sinistrés sont sans montant retrouvé**.

La fréquence élevée de B12 n'est donc pas présente dans toutes les classes d'âge du véhicule. Ma priorité est de vérifier ce périmètre avant de conclure sur un effet propre à la marque.

### Âge du véhicule et durée d'exposition

Pour les véhicules de **0 an exposés au plus 0,10 année**, la fréquence atteint **133,93**, sur **22 545 contrats**, **1 631 sinistres** et **1 217,77 années d'exposition cumulées**. La part des contrats sinistrés sans montant est de **94,03 %**.

Pour les véhicules de 0 an exposés entre 0,50 et 1 an, la fréquence est de **16,21**.

Une fréquence supérieure à 100 est possible puisqu'il s'agit d'un nombre de sinistres rapporté à une durée. Ce résultat justifie de vérifier que `ClaimNb` et `Exposure` couvrent la même période et le même périmètre. Il ne prouve pas que la courte durée cause les sinistres.

### Âge du conducteur et bonus-malus

| Bonus-malus | Fréquence des 18-24 ans | Fréquence des 25-99 ans |
|---|---:|---:|
| 51-75 | 7,15 | 11,38 |
| 76-100 | 17,85 | 15,25 |
| 101-125 | 42,72 | 34,25 |

*Unité : sinistres pour 100 années d'exposition.*

L'écart entre les âges change selon le bonus-malus. Dans la tranche 76-100, les groupes comptent respectivement **25 006 et 86 045 contrats**. Dans la tranche 51-75, le résultat des 18-24 ans repose sur seulement **74 sinistres** : je reste prudent sur sa stabilité.

Ces comparaisons ne suffisent pas à isoler un effet de l'âge, car les autres caractéristiques peuvent encore différer.

### Région, zone et densité

À densité comprise entre **1 001 et 5 000**, R11 présente une fréquence de **13,45**, contre **11,37** ailleurs. Entre **5 001 et 20 000**, les fréquences sont plus proches : **13,15 et 12,83**.

Les **11 302 contrats de densité supérieure à 20 000** sont tous en R11 : il n'existe donc aucun groupe extérieur pour comparer cette tranche dans le fichier.

Les zones E/F et les fortes densités se recoupent en partie. Je ne les interprète pas automatiquement comme des signaux indépendants.

## 5. Contrôles et limites à conserver

Les contrôles des regroupements ont confirmé la conservation des totaux attendus. Les quatre tableaux de croisement conservent les contrats, les sinistres déclarés, l'exposition et les contrats sinistrés sans montant.

- Les coûts inconnus restent manquants. Leur origine n'est pas expliquée à ce stade.
- Le contrat **4158255** déclare 2 sinistres pour 1 ligne observée dans sev. Cet écart est suivi séparément des contrats entièrement absents de sev.
- Les âges de 100 ans, les expositions supérieures à un an et les lignes de sinistres répétées restent conservés et signalés.
- Les résultats sont descriptifs. Aucun test statistique ni modèle causal n'a été réalisé.
- Les données ne permettent pas une évolution mensuelle ni un calcul de rentabilité complète : les dates nécessaires, les primes et les frais ne sont pas disponibles.

## 6. Priorités et restitution dans Power BI

| Priorité proposée | Pourquoi |
|---|---|
| Vérifier les extractions et les définitions pour B12 / véhicules de 0 an | Fréquence élevée et forte proportion de montants manquants se cumulent |
| Examiner les circonstances des sinistres des profils âge / bonus-malus repérés | Les écarts varient entre les sous-groupes ; une action de prévention demanderait des informations complémentaires |
| Garder la densité et le poids des gros sinistres dans les comparaisons géographiques | Les classements régionaux diffèrent selon la fréquence, le volume et les coûts observés |

Le projet [Assurance.pbip](../powerbi/Assurance.pbip) reprend trois pages :

1. **Vue d'ensemble :** contrats, exposition, sinistres, fréquence, coûts observés et part des contrats sinistrés sans montant.
2. **Comprendre les segments :** comparaisons B12 / âge du véhicule, âge / bonus-malus, âge du véhicule / exposition et région / densité. Les coûts moyens et médians sont consultables dans le tableau régional de la première page.
3. **Qualité et limites :** montants non retrouvés, orphelins, écart de nombre de sinistres et influence du plus gros montant.

Les tables sont exportées dans `data/processed` par la dernière section d'`analyse_approfondie.ipynb`. Les clés et les totaux des CSV ont été contrôlés. Les mesures DAX sont définies à partir des sommes de sinistres et d'exposition, sans moyenne simple des fréquences.

L'actualisation, l'exécution des mesures et le rendu des tableaux restent à confirmer dans Power BI Desktop. Le [guide d'ouverture](../powerbi/LISEZ_MOI.txt) donne les valeurs de référence à comparer, au global et pour B12 / véhicule de 0 an.

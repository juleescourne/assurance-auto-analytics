# Synthèse des analyses — Assurance automobile

**Date :** 02/10/2026
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

Ces seuils servent à choisir les sujets à approfondir. Je complète cette sélection avec R24 pour son poids dans le volume, même si sa fréquence globale est basse. Ils ne constituent pas un test statistique. Le bonus-malus 101-125 reste intéressant, mais ses 6 987 contrats sont sous le seuil de volume choisi.

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

### Investigations complémentaires : B12 / véhicule de 0 an

Je compare B12 aux autres marques **parmi les seuls véhicules codés 0 an**. Le code d'âge ne donne pas la date d'achat ni la date du sinistre.

| Exposition du contrat | Contrats B12 | Sinistres B12 | Exposition B12 (années) | Fréquence B12 | Fréquence autres marques | Sans montant B12 |
|---|---:|---:|---:|---:|---:|---:|
| Jusqu'à 0,10 an | 16 319 | 1 498 | 880,88 | 170,06 | 39,48 | 96,63 % |
| Plus de 0,10 à 0,50 an | 13 501 | 1 750 | 3 649,67 | 47,95 | 13,59 | 86,18 % |
| Plus de 0,50 à 1 an | 7 237 | 1 070 | 5 017,07 | 21,33 | 9,68 | 75,15 % |

La catégorie supérieure à un an reste dans les tableaux complets : seulement 12 contrats B12, aucun sinistre. Je n'en tire pas de conclusion comparative.

**Ce qui change :** la fréquence élevée de B12 ne se limite pas aux durées très courtes. Au-delà de 0,50 an, elle reste à **21,27 contre 9,40** pour les autres marques. Ces valeurs incluent les expositions supérieures à un an, d'où la différence avec la dernière ligne du tableau.

Cela ne prouve pas un effet propre à la marque. D'autres caractéristiques peuvent différer, et la couverture des montants reste faible. Je demande d'abord une vérification des périodes couvertes et du rapprochement des montants, puis des circonstances des sinistres.

### R24 : chercher derrière la moyenne régionale

J'ai comparé R24 aux **autres régions réunies, sans R24**, selon cinq axes : âge du véhicule, âge du conducteur, bonus-malus, densité et exposition. Puis j'ai croisé l'âge du véhicule et le bonus-malus. Chaque ligne présentée comme comparaison retenue a au moins **1 000 contrats et 500 années de chaque côté**. Ce sont des seuils de lecture, pas une garantie statistique.

| Profil en R24 | Contrats | Sinistres | Exposition (années) | Fréquence R24 | Même profil hors R24 | Sans montant R24 |
|---|---:|---:|---:|---:|---:|---:|
| Véhicule 1-2 ans, bonus-malus 76-100 | 1 531 | 117 | 689,87 | 16,96 | 12,81 | 8,49 % |
| Véhicule 1-2 ans, bonus-malus ≤ 50 | 11 886 | 747 | 7 956,24 | 9,39 | 7,23 | 44,34 % |
| Véhicule 6-10 ans, bonus-malus 76-100 | 7 161 | 490 | 3 299,51 | 14,85 | 17,16 | 8,01 % |

Le premier profil mérite une investigation ciblée malgré la moyenne régionale basse. Le deuxième est sous la moyenne du portefeuille, mais au-dessus de la référence correspondant aux mêmes tranches ailleurs. Le troisième rappelle qu'une fréquence élevée en valeur absolue ne signifie pas que R24 est plus élevée que son comparateur. Le notebook conserve tous les profils, y compris ceux dont l'écart est négatif.

Pour les coûts, R24 présente une moyenne de **2 945,92 €** et une médiane de **1 128,12 €**. Un seul sinistre représente **21,37 %** des montants régionaux observés. Sans une occurrence de ce maximum, la moyenne serait de **2 316,87 €**. C'est un diagnostic, pas une suppression de donnée.

### R11 : compléter la densité par le bonus-malus

| Profil en R11 | Contrats | Sinistres | Exposition (années) | Fréquence R11 | Même profil hors R11 | Sans montant R11 |
|---|---:|---:|---:|---:|---:|---:|
| Densité 1 001-5 000, bonus-malus 51-75 | 6 793 | 412 | 2 789,59 | 14,77 | 12,26 | 34,99 % |
| Densité 5 001-20 000, bonus-malus 51-75 | 6 495 | 337 | 2 672,25 | 12,61 | 12,70 | 29,90 % |
| Densité 5 001-20 000, bonus-malus 76-100 | 5 237 | 353 | 1 835,37 | 19,23 | 18,96 | 33,44 % |

L'écart reste visible pour le premier profil, alors qu'il est faible pour les deux suivants. Je ne propose donc pas la même priorité pour tous les contrats R11. Comparer deux caractéristiques ne suffit toutefois pas à rendre les groupes identiques : les autres profils peuvent encore différer.

Au-delà de 20 000 habitants/km², aucun contrat hors R11 n'est disponible. La comparaison reste vide ; elle n'est pas remplacée par zéro. Le maximum représente **4,01 %** des montants observés de R11, bien moins que dans R24.

### Sensibilité des deux régions aux groupes particuliers

J'applique chaque condition aux contrats de la région **et** au comparateur. Les scénarios ne modifient pas les résultats de référence.

| Scénario | Fréquence R24 | Hors R24 | Fréquence R11 | Hors R11 |
|---|---:|---:|---:|---:|
| Portefeuille complet | 8,96 | 10,52 | 13,17 | 9,79 |
| Exposition > 0,10 an | 8,61 | 9,58 | 11,51 | 9,10 |
| Sans B12 / véhicule de 0 an | 8,93 | 9,18 | 10,27 | 9,01 |
| Sans B12 / 0 an et exposition > 0,10 an | 8,59 | 8,76 | 9,74 | 8,62 |

**Interprétation :** l'écart global de R24 avec le reste du portefeuille devient faible dans le dernier scénario. L'écart de R11 se réduit mais reste présent. La composition des portefeuilles compte donc dans la lecture des moyennes ; ces exclusions n'isolent pas un effet causal de la région.

## 5. Contrôles et limites à conserver

Les contrôles des regroupements ont confirmé la conservation des totaux attendus. Les quatre tableaux de croisement conservent les contrats, les sinistres déclarés, l'exposition et les contrats sinistrés sans montant.

- Les coûts inconnus restent manquants. Leur origine n'est pas expliquée à ce stade.
- Le contrat **4158255** déclare 2 sinistres pour 1 ligne observée dans sev. Cet écart est suivi séparément des contrats entièrement absents de sev.
- Les âges de 100 ans, les expositions supérieures à un an et les lignes de sinistres répétées restent conservés et signalés.
- Les résultats sont descriptifs. Aucun test statistique ni modèle causal n'a été réalisé.
- Les données ne permettent pas une évolution mensuelle ni un calcul de rentabilité complète : les dates nécessaires, les primes et les frais ne sont pas disponibles.

## 6. Priorités et restitution dans Power BI

| Priorité | Action proposée et résultat attendu |
|---|---|
| B12 / véhicule de 0 an | Faire vérifier les périodes ClaimNb / Exposure et l'extraction des montants ; recalculer les comparaisons après validation. L'écart persiste entre 0,50 et 1 an : ne pas attribuer tout le signal aux expositions très courtes. |
| R24, véhicules 1-2 ans / bonus-malus 76-100 | Demander les circonstances des 117 sinistres et comparer les autres caractéristiques à celles du même groupe hors R24. Objectif : déterminer si une investigation métier ou une prévention ciblée est justifiée. |
| R24, coûts | Confirmer le gros sinistre et présenter systématiquement moyenne, médiane et influence du maximum. Ne pas interpréter la moyenne seule comme un coût habituel. |
| R11, densité 1 001-5 000 / bonus-malus 51-75 | Examiner ce profil de 6 793 contrats en priorité ; vérifier aussi la couverture des montants. Éviter de généraliser aux tranches où les fréquences sont proches ailleurs. |

Ces actions sont proposées, pas réalisées auprès d'un assureur. Aucun gain financier n'a été mesuré et aucun changement de tarif n'est recommandé sur ces seuls résultats.

Le projet [Assurance.pbip](../powerbi/Assurance.pbip) comporte cinq pages :

1. **Vue d'ensemble** : volumes, fréquence, exposition et couverture du portefeuille.
2. **B12 / véhicules de 0 an** : comparaison des marques selon la durée et scénarios d'exposition.
3. **R24** : profils, croisement âge du véhicule / bonus-malus, sensibilité et coûts.
4. **R11** : profils, croisement densité / bonus-malus, sensibilité et coûts.
5. **Qualité et limites** : montants manquants, orphelins, écart de nombre et priorités.

Les pages d'investigation sont pilotées par leurs menus de filtre. Les clics sur barres ou tableaux ne filtrent pas les autres visuels, pour garder les groupes de comparaison visibles. Les deux régions sont fixées dans leurs mesures ; les menus filtrent simultanément la région et le reste du portefeuille.

Dix CSV sont régénérés dans `data/processed` : trois tables détaillées, un contrôle global et six tableaux d'investigation. Seules les trois tables détaillées sont importées dans Power BI. Les visuels recalculent les ratios et ne font pas de moyenne de fréquences préagrégées.

Les notebooks ont été exécutés. Le contrôle du rendu natif et l'exécution des nouvelles mesures dans Desktop restent à confirmer ; voir le [guide d'ouverture](../powerbi/LISEZ_MOI.txt) et les [requêtes de contrôle](../powerbi/Controles_investigations.dax).

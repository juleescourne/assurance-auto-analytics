# Rapport qualité des données

**Projet :** assurance responsabilité civile automobile
**Date :** 30/09/2026
**Source des résultats :** [data_quality.ipynb](../notebook/data_quality.ipynb)

## 1. Données contrôlées

J'ai contrôlé les fichiers bruts `freMTPL2freq.arff` et `freMTPL2sev.arff`, présents dans `data/raw` et issus d'OpenML.

| Table | Nombre de lignes | Contrats distincts | Grain |
|---|---:|---:|---|
| freq | 678 013 | 678 013 | Une ligne par contrat |
| sev | 26 639 | 24 950 | Une ligne par sinistre enregistré |

Le notebook a été exécuté entièrement dans l'ordre, sans erreur.

## 2. Contrôles réalisés

| Contrôle | Résultat | Décision ou remarque |
|---|---|---|
| Valeurs manquantes | Aucune dans les deux tables | Aucun remplacement effectué |
| Unicité dans freq | Aucun IDpol répété, aucune ligne entièrement répétée | Une ligne par contrat confirmée |
| Lignes entièrement répétées dans sev | 255 répétitions après la première occurrence | Conservées : sans identifiant de sinistre, je ne peux pas confirmer qu'il faut les supprimer |
| Catégories Area, VehGas, VehBrand et Region | Aucune valeur hors des listes contrôlées | Catégories conservées |
| Règles numériques | Aucun cas signalé | Exposition et montants positifs ; ClaimNb entier et non négatif ; âge du véhicule non négatif ; âge du conducteur et densité positifs |

J'ai également regardé le minimum, la moyenne, les quartiles, P95, P99, le maximum et l'écart-type des valeurs numériques.

| Point à vérifier | Résultat | Décision |
|---|---|---|
| Exposition supérieure à un an | 1 224 contrats ; maximum de 2,01 ans | Valeurs conservées, durée couverte à confirmer |
| Âge égal à 100 ans | 25 véhicules et 3 conducteurs | Valeurs conservées, signification à confirmer |
| Montant maximal d'un sinistre | 4 075 400,56 € | Conservé ; un montant élevé ne suffit pas à prouver une erreur |

L'exposition minimale est d'environ **0,00273 année**, et non zéro. L'affichage `0.00` venait de l'arrondi.

## 3. Cohérence entre les tables

| Situation | Résultat | Interprétation |
|---|---:|---|
| Contrats présents dans les deux tables | 24 944 | Rapprochement possible par IDpol |
| Contrats de freq sans sinistre et absents de sev | 643 953 | Absence de ligne de sinistre attendue |
| Contrats de freq avec sinistre et absents de sev | 9 116 | Coûts non disponibles dans le rapprochement |
| Contrats de sev absents de freq | 6 | Exposition et caractéristiques du contrat indisponibles |

Les **9 116 contrats sinistrés sans ligne dans sev** représentent **26,76 % des contrats déclarant au moins un sinistre**. Je les ai conservés dans `freq`.

J'ai comparé `ClaimNb` au nombre de lignes de `sev` pour les contrats communs. Un contrat présente un écart : **IDpol 4158255**, avec **2 sinistres déclarés contre 1 ligne dans sev**. `ClaimNb` a été conservé. Son coût observé peut être incomplet.

## 4. Traitement effectué et limites

J'ai séparé les six contrats absents de `freq` dans `df_sev_orphelins`. Les autres lignes sont dans `df_sev_rapprochable`, pour les analyses nécessitant les caractéristiques ou l'exposition des contrats.

| Périmètre | Lignes de sinistres | Montant |
|---|---:|---:|
| sev initial | 26 639 | 60 697 930,68 € |
| Contrats orphelins mis de côté | 195 | 788 714,18 € |
| Sinistres rapprochables | 26 444 | 59 909 216,50 € |

Les montants mis de côté représentent **1,30 % du montant total de sev**. Les contrôles confirment que les lignes et les montants se retrouvent entièrement dans les deux groupes, au centime près pour les montants. Aucun IDpol de `df_sev_rapprochable` n'est absent de `freq`.

Les tables brutes sont conservées. Aucun coût manquant n'a été remplacé par zéro et les lignes répétées de `sev` n'ont pas été supprimées.

**Conclusion :** les contrôles de base sont réalisés, mais les coûts disponibles ne couvrent pas tous les sinistres déclarés dans `freq`. L'origine des écarts entre les tables reste inconnue. Les durées supérieures à un an et les âges égaux à 100 ans restent également à expliquer.

## 5. Suivi qualité dans les investigations du 02/10/2026

L'audit initial reste inchangé : les investigations n'ont pas permis d'expliquer ni de corriger les écarts entre les sources.

- B12 / véhicules de 0 an : 87,10 % des contrats sinistrés sans montant. Même entre 0,50 et 1 an d'exposition, cette part reste de 75,15 %.
- R24, véhicules de 1-2 ans / bonus-malus 76-100 : 8,49 % sans montant ; la fréquence se calcule toujours depuis freq, indépendamment de la présence du coût.
- R11, densité 1 001-5 000 / bonus-malus 51-75 : 34,99 % sans montant. Les coûts ne couvrent donc pas ce groupe de façon complète.
- Aucun contrat hors R11 au-delà de 20 000 de densité : le comparateur reste manquant, pas nul.
- Les regroupements contrôlent les totaux de contrats, de sinistres et d'exposition. Les montants régionaux retrouvent le total des lignes rapprochées.

Les scénarios d'exclusion et le retrait d'une occurrence du maximum servent uniquement à mesurer la sensibilité. Les tables de référence conservent les 678 013 contrats et les sinistres rapprochés. Les fréquences n'ont pas été corrigées, et aucun montant inconnu n'a été imputé.

Les nouveaux résultats figurent dans [l'analyse approfondie](../notebook/analyse_approfondie.ipynb) et [la synthèse](Analyse.md).

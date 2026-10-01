# Note de cadrage — Assurance responsabilité civile automobile

**Projet :** étude de cas fictive sur les données publiques freMTPL2.
**Mise à jour :** 01/10/2026.
**Échéance cible initiale :** 10 octobre 2026.

## 1. Problème

Je cherche à aider une direction technique fictive à repérer les segments à investiguer en priorité. Un grand nombre de sinistres peut simplement venir d'un grand portefeuille : il faut aussi regarder l'exposition, la fréquence et les coûts observés.

## 2. Acteurs décisionnaires

Dans cette mise en situation, la direction technique valide les définitions et les conclusions. La direction générale arbitre ensuite une éventuelle action nécessitant des moyens. Il ne s'agit pas d'une mission réalisée pour un assureur.

## 3. Questions

- Quels segments concentrent le nombre de sinistres et les montants observés ?
- Comment ces résultats changent-ils lorsque l'on tient compte de l'exposition et du coût moyen ?
- Quels segments faut-il approfondir, compte tenu des effectifs et des limites des données ?

## 4. Périmètre

L'analyse porte sur des contrats d'assurance automobile en France et des sinistres de responsabilité civile automobile. La documentation situe approximativement les observations entre 2011 et 2013. Les fichiers n'ont pas de dates permettant une analyse mensuelle ou annuelle fiable.

L'étude reste descriptive : je ne cherche pas à démontrer une causalité ni à fixer un tarif. Sans primes encaissées et frais, je ne peux pas mesurer la rentabilité des contrats. Les montants étant incomplets, je parle de **coûts observés**.

## 5. Données

Les fichiers viennent d'OpenML. Les versions exactes et leurs empreintes sont précisées dans [les sources](../data/SOURCES.md).

| Dataset | Lignes | IDpol distincts | Grain |
|---|---:|---:|---|
| freMTPL2freq, OpenML 41214 v1 | 678 013 | 678 013 | Un contrat observé sur sa période d'exposition |
| freMTPL2sev, OpenML 41215 v1 | 26 639 | 24 950 | Un enregistrement de sinistre rattaché à un contrat |

Je conserve tous les contrats de `freq`. Les six contrats présents uniquement dans `sev` sont isolés et suivis à part. Les choix détaillés figurent dans le [rapport qualité](Qualité.md).

## 6. Livrables réalisés

- [Dictionnaire des données et KPI](Dictionnaire.md).
- [Rapport qualité](Qualité.md) et [notebook de contrôle](../notebook/data_quality.ipynb).
- [Analyse globale](../notebook/analyse_globale.ipynb) et [analyse approfondie](../notebook/analyse_approfondie.ipynb).
- [Synthèse des résultats, limites et priorités](Analyse.md).
- Quatre CSV régénérables dans `data/processed`, pour Power BI et le contrôle des KPI.
- [Projet Power BI](../powerbi/Assurance.pbip) : modèle et trois pages de rapport.
- [README](../README.md) : présentation et instructions pour reproduire le projet.

Le sujet initial proposait aussi du SQL et des tests statistiques. Ces parties n'ont pas été réalisées dans ce périmètre. Le rapport est fourni au format projet `.pbip` ; aucun fichier `.pbix` n'est fourni.

## 7. Critères de vérification

- Les KPI ont un grain, un dénominateur et une unité explicites.
- La jointure conserve le nombre de contrats, les sinistres déclarés et l'exposition.
- Les montants se répartissent entièrement entre sinistres rapprochés et orphelins.
- Les conclusions distinguent constats, hypothèses et limites.
- Les exports retrouvent les résultats des notebooks.
- Dans Power BI, l'actualisation, le rendu des tableaux et les mesures DAX doivent encore être confirmés dans Desktop. Les contrôles de fichiers ne remplacent pas cette vérification.

## 8. Sources

- [OpenML — fréquence](https://www.openml.org/d/41214) et [sévérité](https://www.openml.org/d/41215).
- [CASdatasets — définitions et période](https://dutangc.github.io/CASdatasets/reference/freMTPL.html).
- [Exemple scikit-learn sur ces données](https://scikit-learn.org/stable/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html).

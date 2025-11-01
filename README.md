# Projet – Analyse de prix d’actions (BNP, LVMH, TotalEnergies)

## Objectif
Ce projet a pour but d’analyser l’évolution des cours de trois entreprises françaises
(BNP Paribas, LVMH, TotalEnergies) à l’aide de **Python** et **R**.  
Nous calculons et visualisons :
- Les rendements journaliers
- La volatilité
- Les corrélations entre actions

## Structure du projet
- `data/` : données brutes et transformées
- `notebooks/` : notebooks Python (Jupyter) et R (RMarkdown)
- `reports/` : graphiques et rapport final
- `src/` : fonctions utilitaires
- `requirements.txt` : packages nécessaires

## Technologies utilisées
- Python : pandas, numpy, matplotlib, seaborn, yfinance
- R : tidyverse, quantmod, ggplot2

## Résultats
- Les 3 actions ont montré une volatilité différente : LVMH > BNP > TotalEnergies
- La corrélation la plus forte observée est entre BNP et TotalEnergies
- Exemple de graphique (rendements journaliers BNP) :

![Exemple de graphique](reports/figures/bnp_returns.png)

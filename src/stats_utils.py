import statistics


def analyser_ventes(transactions):
    """
    Analyse statistique d'une liste de transactions.

    Paramètre
    ---------
    transactions : list
        Liste de montants de ventes en euros.

    Retour
    ------
    dict
        Dictionnaire contenant les indicateurs statistiques.
    """
    # --------------------------------------------------
    # 1. Nettoyage des données
    # --------------------------------------------------
    transactions_valides = [
        montant for montant in transactions
        if montant > 0
    ]

    # --------------------------------------------------
    # 2. Vérification
    # --------------------------------------------------
    if not transactions_valides:
        return {
            "nombre_transactions": 0,
            "somme_totale": 0,
            "moyenne": 0,
            "mediane": 0,
            "ecart_type": 0,
            "minimum": 0,
            "maximum": 0,
            "outliers": []
        }

    # --------------------------------------------------
    # 3. Calcul des indicateurs
    # --------------------------------------------------
    nombre_transactions = len(transactions_valides)
    somme_totale = sum(transactions_valides)
    moyenne = somme_totale / nombre_transactions
    mediane = statistics.median(transactions_valides)
    ecart_type = statistics.stdev(transactions_valides)
    minimum = min(transactions_valides)
    maximum = max(transactions_valides)

    # --------------------------------------------------
    # 4. Détection des outliers
    # --------------------------------------------------
    outliers = [
        montant for montant in transactions_valides
        if montant > 2 * moyenne
    ]

    # --------------------------------------------------
    # 5. Résultat
    # --------------------------------------------------
    return {
        "nombre_transactions": nombre_transactions,
        "somme_totale": somme_totale,
        "moyenne": moyenne,
        "mediane": mediane,
        "ecart_type": ecart_type,
        "minimum": minimum,
        "maximum": maximum,
        "outliers": outliers
    }


def calculer_marge_erreur(liste_nombres):
    """Calcule l'étendue (max - min) d'une liste de nombres."""
    if not liste_nombres:
        return 0
    return max(liste_nombres) - min(liste_nombres)


# ======================================================
# TEST DU SCRIPT
# ======================================================
transactions_test = [
    150,
    200,
    -50,
    300,
    0,
    500,
    1000
]

resultats = analyser_ventes(transactions_test)

print("\n===== RAPPORT STATISTIQUE DES VENTES =====")
print(f"Nombre de transactions valides : "
      f"{resultats['nombre_transactions']}")
print(f"Somme totale des ventes : "
      f"{resultats['somme_totale']:.2f} €")
print(f"Moyenne : "
      f"{resultats['moyenne']:.2f} €")
print(f"Médiane : "
      f"{resultats['mediane']:.2f} €")
print(f"Écart-type : "
      f"{resultats['ecart_type']:.2f} €")
print(f"Minimum : "
      f"{resultats['minimum']:.2f} €")
print(f"Maximum : "
      f"{resultats['maximum']:.2f} €")
print(f"Transactions anormalement élevées : "
      f"{resultats['outliers']}")
print(f"Marge d'erreur (étendue) : "
      f"{calculer_marge_erreur(transactions_test):.2f} €")
print("=======================================\n")
# Création des listes avec les données
ds_data = [
    "BBB6+ $ds",
    "BBB5- $ds",
    "4456-7789/7765 $ds",
    "88T9+/8876+ $ds",
    "Kxxx $ds !RR !A",
    "KQRR $ds (88-)",
    "KQRR $ds (99+)"
]

ss_data = [
    "2234-7789/9987 $ss",
    "889T-JJT9 $ss",
    "QQJT+$ss",
    "9876- $ss",
    "Ne pas over 3B les mains $ss",
    "AKxx $ss As si !B ou !connected",
    "AKxx $ss As $B $connected",
    "AKxx $ss As si $B ou $connected",
    "AKxx $ss Ks si !(B+connected)"
]

rb_data = ["les meilleures mains Rainbow"]

fold_data = [
    "Kxxx $ds !RR !A",
    "2234-7789/9987 $ss",
    "9876- $ss",
    "AKxx $ss As si !B ou !connected",
    "AKxx $ss Ks si !(B+connected)"
]

flat_data = [
    "BBB5- $ds",
    "4456-7789/7765 $ds",
    "KQRR $ds (88-)",
    "889T-JJT9 $ss",
    "AKxx $ss As si $B ou $connected"
]

raise_data = [
    "BBB6+ $ds",
    "88T9+/8876+ $ds",
    "KQRR $ds (99+)",
    "QQJT+$ss",
    "Ne pas over 3B les mains $ss",
    "AKxx $ss As $B $connected",
    "les meilleures mains Rainbow",
]

# Création des listes regroupées
sb_vs_bu_ds_fold = list(set(ds_data) & set(fold_data))
sb_vs_bu_ds_flat = list(set(ds_data) & set(flat_data))
sb_vs_bu_ds_3bet = list(set(ds_data) & set(raise_data))
sb_vs_bu_ss_fold = list(set(ss_data) & set(fold_data))
sb_vs_bu_ss_flat = list(set(ss_data) & set(flat_data))
sb_vs_bu_ss_3bet = list(set(ss_data) & set(raise_data))
sb_vs_bu_rb_fold = list(set(rb_data) & set(fold_data))
sb_vs_bu_rb_flat = list(set(rb_data) & set(flat_data))
sb_vs_bu_rb_3bet = list(set(rb_data) & set(raise_data))


# Fonction pour obtenir les données d'une catégorie et décision spécifiques
def obtenir_donnees(categorie, decision):
    if categorie == "DS":
        if decision == "Fold":
            return sb_vs_bu_ds_fold
        elif decision == "Flat":
            return sb_vs_bu_ds_flat
        elif decision == "3Bet":
            return sb_vs_bu_ds_3bet
    elif categorie == "SS":
        if decision == "Fold":
            return sb_vs_bu_ss_fold
        elif decision == "Flat":
            return sb_vs_bu_ss_flat
        elif decision == "3Bet":
            return sb_vs_bu_ss_3bet
    elif categorie == "RB":
        if decision == "Fold":
            return sb_vs_bu_rb_fold
        elif decision == "Flat":
            return sb_vs_bu_rb_flat
        elif decision == "3Bet":
            return sb_vs_bu_rb_3bet
    return []

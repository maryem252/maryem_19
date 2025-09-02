import math


def calculatrice():
    print("=== CALCULATRICE AVANCÉE ===")
    print("Opérations disponibles:")
    print("+ : Addition")
    print("- : Soustraction")
    print("* : Multiplication")
    print("/ : Division")
    print("** : Puissance")
    print("% : Modulo")
    print("sqrt : Racine carrée")
    print("sin, cos, tan : Fonctions trigonométriques")
    print("log : Logarithme naturel")
    print("q : Quitter")
    print("=" * 30)

    while True:
        operateur = input("\nEntrez votre opération: ").lower().strip()

        # Option pour quitter
        if operateur == 'q':
            print("Au revoir!")
            break

        # Opérations à un seul nombre
        if operateur in ['sqrt', 'sin', 'cos', 'tan', 'log']:
            try:
                num = float(input("Entrez le nombre: "))

                if operateur == 'sqrt':
                    if num < 0:
                        print("Erreur: Racine carrée d'un nombre négatif!")
                        continue
                    result = math.sqrt(num)
                elif operateur == 'sin':
                    result = math.sin(math.radians(num))
                elif operateur == 'cos':
                    result = math.cos(math.radians(num))
                elif operateur == 'tan':
                    result = math.tan(math.radians(num))
                elif operateur == 'log':
                    if num <= 0:
                        print("Erreur: Logarithme d'un nombre négatif ou nul!")
                        continue
                    result = math.log(num)

                print(f"Résultat: {result:.6f}")

            except ValueError:
                print("Erreur: Veuillez entrer un nombre valide!")
                continue

        # Opérations à deux nombres
        elif operateur in ['+', '-', '*', '/', '**', '%']:
            try:
                num1 = float(input("Entrez le premier nombre: "))
                num2 = float(input("Entrez le deuxième nombre: "))

                if operateur == "+":
                    result = num1 + num2
                elif operateur == "-":
                    result = num1 - num2
                elif operateur == "*":
                    result = num1 * num2
                elif operateur == "/":
                    if num2 == 0:
                        print("Erreur: Division par zéro!")
                        continue
                    result = num1 / num2
                elif operateur == "**":
                    result = num1 ** num2
                elif operateur == "%":
                    if num2 == 0:
                        print("Erreur: Division par zéro!")
                        continue
                    result = num1 % num2

                print(f"Résultat: {num1} {operateur} {num2} = {result}")

            except ValueError:
                print("Erreur: Veuillez entrer des nombres valides!")
                continue

        else:
            print("Opération non reconnue! Essayez encore.")

        # Demander si l'utilisateur veut continuer
        continuer = input("\nVoulez-vous faire un autre calcul? (yes/no): ").lower()
        if continuer != 'yes':
            print("Au revoir!")
            break


# Fonction pour un historique des calculs
def calculatrice_avec_historique():
    historique = []

    print("=== CALCULATRICE AVEC HISTORIQUE ===")

    while True:
        print("\nOptions:")
        print("1. Nouveau calcul")
        print("2. Voir l'historique")
        print("3. Effacer l'historique")
        print("4. Quitter")

        choix = input("Votre choix (1-4): ")

        if choix == '1':
            operateur = input("Opération (+, -, *, /): ")
            if operateur in ['+', '-', '*', '/']:
                try:
                    num1 = float(input("Premier nombre: "))
                    num2 = float(input("Deuxième nombre: "))

                    if operateur == "+":
                        result = num1 + num2
                    elif operateur == "-":
                        result = num1 - num2
                    elif operateur == "*":
                        result = num1 * num2
                    elif operateur == "/":
                        if num2 == 0:
                            print("Erreur: Division par zéro!")
                            continue
                        result = num1 / num2

                    calcul = f"{num1} {operateur} {num2} = {result}"
                    historique.append(calcul)
                    print(f"Résultat: {result}")

                except ValueError:
                    print("Erreur: Nombres invalides!")
            else:
                print("Opérateur invalide!")

        elif choix == '2':
            if historique:
                print("\n--- HISTORIQUE ---")
                for i, calc in enumerate(historique, 1):
                    print(f"{i}. {calc}")
            else:
                print("Aucun calcul dans l'historique!")

        elif choix == '3':
            historique.clear()
            print("Historique effacé!")

        elif choix == '4':
            print("Au revoir!")
            break

        else:
            print("Choix invalide!")


# Lancer la calculatrice
if __name__ == "__main__":
    # Choisissez quelle version utiliser:
    calculatrice()  # Version avancée
    calculatrice_avec_historique()  # Version avec historique

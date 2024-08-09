import random


def jeu_multiplication():
    points = 0

    while points < 100:
        num1 = random.randint(2, 20)
        num2 = random.randint(2, 20)

        produit = num1 * num2

        try:
            reponse = int(input(f"Combien fait {num1} X {num2} ? "))

            if reponse == produit:
                points += 1
                print(
                    f"Bonne réponse ! Votre score est maintenant de {points}/100")
            else:
                print(f"Mauvaise réponse")

        except ValueError:
            print("Veuillez entrer un nombre valide.")

    print("Félicitations ! Vous avez atteint 100 points.")


# Démarrer le jeu
jeu_multiplication()

import random
from time import sleep
from rich.console import Console
import subprocess

console = Console()


def jeu_maths():
    try:
        objectif = int(input("Entrez l'objectif de points à atteindre : "))
    except ValueError:
        console.print("Veuillez entrer un nombre valide pour l'objectif.",
                      style="bold yellow")
        return

    points = 0

    while points < objectif:
        # Générer les nombres jusqu'à ce qu'aucun ne soit un multiple de 10
        while True:
            num1 = random.randint(2, 100)
            num2 = random.randint(2, 100)
            if num1 % 10 != 0 and num2 % 10 != 0:
                break

        operation = random.choice(['+', '-', 'x'])

        if operation == '+':
            resultat = num1 + num2
        elif operation == '-':
            resultat = num1 - num2
        else:  # operation == 'x'
            resultat = num1 * num2

        try:
            reponse = int(input(f"Combien font {num1} {operation} {num2} ? "))

            if reponse == resultat:
                points += 1
                console.print(
                    f"Bonne réponse ! Votre score est maintenant de {points}/{objectif}", style="bold green")
                sleep(1)
                subprocess.run(["powershell", "-Command", "Clear-Host"])
            else:
                console.print(
                    f"Mauvaise réponse, la réponse correcte était {resultat}", style="bold red")
                sleep(1)
                subprocess.run(["powershell", "-Command", "Clear-Host"])

        except ValueError:
            console.print("Veuillez entrer un nombre valide.",
                          style="bold yellow")
            sleep(1)
            subprocess.run(["powershell", "-Command", "Clear-Host"])

    console.print(f"Félicitations ! Vous avez atteint {objectif} points.",
                  style="bold purple")


# Démarrer le jeu
jeu_maths()

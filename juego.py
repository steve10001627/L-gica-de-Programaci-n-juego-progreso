
import random

# En esta parte se detalla el inicio del juego 
def jugar_ahorcado():
    palabras = ["python", "programa", "ahorcado", "juego", "computadora"]
    palabra_secreta = random.choice(palabras)
    letras_adivinadas = ["_"] * len(palabra_secreta)
    intentos = 6

    print("\n¡Bienvenido al juego del Ahorcado!")
    print("Tienes", intentos, "intentos para adivinar la palabra secreta.")
    print(" ".join(letras_adivinadas))

    # Bucle del juego
    while intentos > 0 and "_" in letras_adivinadas:
        letra = input("Adivina una letra: ").lower()

        if letra in palabra_secreta:
            print("¡Bien! La letra está en la palabra.")
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    letras_adivinadas[i] = letra
        else:
            print("Esa letra no está en la palabra.")
            intentos -= 1

        print(" ".join(letras_adivinadas))
        print("Te quedan", intentos, "intentos.")

    # Termina el juego
    if "_" not in letras_adivinadas:
        print("¡Felicidades! Adivinaste la palabra:", palabra_secreta)
    else:
        print("Perdiste. La palabra era:", palabra_secreta)



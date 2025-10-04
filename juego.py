import random

# En esta parte se detalla el inicio del juego 
def jugar_ahorcado():
    palabras = ["naruto", "futurama", "heroes", "juego", "academia" , "messi"]
    palabra_secreta = random.choice(palabras)
    letras_adivinadas = ["_"] * len(palabra_secreta)
    intentos = 3

    print("Bienvenido al juego del Ahorcado")
    print("Tienes", intentos, "intentos para adivinar la palabra secreta.")
    print(" ".join(letras_adivinadas))

    # Bucle del juego
    while intentos > 0 and "_" in letras_adivinadas:
        letra = input("Adivina una letra: ").lower()

        if letra in palabra_secreta:
            print("Correcto la letra está en la palabra.")
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    letras_adivinadas[i] = letra
        else:
            print("No esa letra no está en la palabra.")
            intentos -= 1

        print(" ".join(letras_adivinadas))
        print("Te quedan", intentos, "intentos.")

    # Termina el juego
    if "_" not in letras_adivinadas:
        print("Muy bien hecho adivinaste la palabra:", palabra_secreta)
    else:
        print("Lo siento perdiste mas suerte la próxima. La palabra era:", palabra_secreta)



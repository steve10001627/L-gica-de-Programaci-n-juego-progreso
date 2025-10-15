# Juego del Ahorcado en Python

¡Bienvenido a este simple y divertido juego del Ahorcado desarrollado en Python!  
Este proyecto está pensado para ser fácil de entender, ideal para quienes están aprendiendo programación y quieren explorar cómo funcionan los bucles, condicionales y listas en Python.

---

##  ¿Cómo funciona?

Este juego selecciona una palabra al azar de una lista de palabras relacionadas con el entretenimiento y el deporte. El jugador tiene **3 intentos** para adivinar la palabra, ingresando una letra en cada turno. Si adivinas todas las letras, ganas. Si se te acaban los intentos, pierdes.

---

##  Explicación del Código

## Definicion de funciones y mensajes de salida para el usuario

import random

Importa el módulo random que nos permite elegir palabras al azar.

def jugar_ahorcado():

Define la función principal que contiene la lógica del juego.

    palabras = ["naruto", "futurama", "heroes", "juego", "academia", "messi"]

Lista de palabras posibles para adivinar.

     palabra_secreta = random.choice(palabras)

Se elige una palabra secreta al azar de la lista.

    letras_adivinadas = ["_"] * len(palabra_secreta)

Se crea una lista de guiones bajos para mostrar el progreso del jugador.

    intentos = 3

El jugador comienza con 3 intentos.

    print("Bienvenido al juego del Ahorcado")
    print("Tienes", intentos, "intentos para adivinar la palabra secreta.")
    print(" ".join(letras_adivinadas))

    Muestra un mensaje de bienvenida, cuántos intentos tienes y el estado inicial de la palabra.


## Bucle del juego

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

Mientras tengas intentos y queden letras por adivinar:

Pide una letra.

Si está en la palabra, se revela en su posición.

Si no está, pierdes un intento.

Se muestra el estado actual de la palabra y los intentos restantes.

## Parte final del juego

    if "_" not in letras_adivinadas:
        print("Muy bien hecho adivinaste la palabra:", palabra_secreta)
    else:
        print("Lo siento perdiste mas suerte la próxima. La palabra era:", palabra_secreta)

Si completaste la palabra, ganas. Si no, pierdes y se muestra la palabra correcta.

## Bucle que repite o termina el juego

def main():
    while True:
        jugar_ahorcado()
        jugar_nuevamente = input("¿Quieres jugar otra vez? (sí/no): ").lower()
        if jugar_nuevamente != "sí":
            print("Gracias por jugar. ¡Hasta luego!")
            break

main()

Permite al usuario volver a jugar si lo desea. Si responde "no", el programa finaliza con un mensaje de despedida.


## Cómo ejecutarlo

1. Asegúrate de tener Python instalado en tu sistema.
2. Descarga este repositorio o clónalo con:

git clone https://github.com/steve10001627/L-gica-de-Programaci-n-juego-progreso.git

3. Ve al directorio del proyecto:

cd L-gica-de-Programaci-n-juego-progreso

4. Ejecuta el archivo juego.py:

python juego.py


## Quieres mejorarlo

Las contribuciones son bienvenidas. Siéntete libre de modificar con tus mejoras o nuevas funcionalidades.
Este proyecto es ideal para aprender colaborativamente y experimentar con Python. Se puede usar, modificar y distribuir libremente.


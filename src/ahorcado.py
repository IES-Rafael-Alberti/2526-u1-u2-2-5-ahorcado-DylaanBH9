"""
Juego del Ahorcado
==================

Práctica de programación que evalúa:
- Variables y tipos de datos primitivos
- Sentencias condicionales
- Sentencias iterativas
- Manipulación de strings

Autor: Dylan Bauti Huelva
Fecha: 6/11/25
"""
from wordfreq import top_n_list
import random


def solicitar_palabra():
    # "en" o "es" según idioma; 5000 -> tamaño de la lista de las más frecuentes
    words = top_n_list("es", 5000)  # cambia a "en" si quieres inglés
    candidates = [w for w in words if w.isalpha() and 4 <= len(w) <= 8]
    word = random.choice(candidates)
    return word

def quitar_tildes(palabra: str) -> str:
    palabra_lista = list(palabra)
    for posicion, caracter in enumerate(palabra):
        if caracter == 'Á':
            palabra_lista[posicion] = 'A'
        elif caracter == 'É':
            palabra_lista[posicion] = 'E'
        elif caracter == 'Í':
            palabra_lista[posicion] = 'I'
        elif caracter == 'Ó':
            palabra_lista[posicion] = 'O'
        elif caracter == 'Ú':
            palabra_lista[posicion] = 'U'

    palabra_sin_tildes = "".join(palabra_lista)
    return palabra_sin_tildes


def solicitar_letra(letras_usadas: list[str]) -> str:
    """
    Solicita una letra al jugador 2
    La letra debe ser válida (solo una letra) y no estar ya usada
    
    Args:
        letras_usadas (list): Lista de letras ya introducidas
        
    Returns:
        str: La letra introducida en mayúsculas
    """

    letra_usuario= ""
    while not letra_usuario.isalpha():
        letra_usuario = input(">> Introduce una letra: ").upper()
        if len(letra_usuario) != 1:
            print("Solo debes introducir una letra")
            letra_usuario = ""
        elif not letra_usuario.isalpha():
            print("Debes introducir una letra")
        elif letra_usuario in letras_usadas:
            print("Debes introducir una nueva letra")
            letra_usuario = ""
    return letra_usuario

def mostrar_estado(palabra_oculta, intentos, letras_usadas):
    """
    Muestra el estado actual del juego
    
    Args:
        palabra_oculta (str): La palabra con _ y letras adivinadas
        intentos (int): Número de intentos restantes
        letras_usadas (list): Lista de letras ya usadas
    """

    print(f"Intentos restantes: {5 - intentos}")
    print(f"Palabra: {palabra_oculta}")
    print(f"Letras usadas: {letras_usadas}\n")


def actualizar_palabra_oculta(palabra, palabra_oculta, letra):
    """
    Actualiza la palabra oculta revelando las apariciones de la letra
    
    Args:
        palabra (str): La palabra completa a adivinar
        palabra_oculta (str): La palabra actual con _ y letras adivinadas
        letra (str): La letra que se ha adivinado
        
    Returns:
        str: La palabra oculta actualizada
    """

    palabra_oculta_lista= list(palabra_oculta)
    for posicion, caracter in enumerate(palabra):
        if caracter == letra:
            palabra_oculta_lista[posicion] = letra

    palabra_oculta_actualizada = "".join(palabra_oculta_lista)
    return palabra_oculta_actualizada

def jugar():
    """
    Función principal que ejecuta el juego del ahorcado
    """
    print("=== JUEGO DEL AHORCADO ===\n")
    
    # Configuración inicial
    INTENTOS_MAXIMOS = 5
    
    palabra = solicitar_palabra().upper()

    palabra = quitar_tildes(palabra)

    palabra_oculta = "".join(["_" for _ in palabra])
    intentos = 0
    letras_usadas= []
    juego_terminado = False
    
    print("¡Adivina la palabra!\n")

    while intentos != INTENTOS_MAXIMOS and juego_terminado != True:
        mostrar_estado(palabra_oculta, intentos, letras_usadas)
        letra = solicitar_letra(letras_usadas)
        letras_usadas.append(letra)
        if letra in palabra:
            palabra_oculta = actualizar_palabra_oculta(palabra, palabra_oculta, letra)
            print(f"¡Bien! La letra {letra} está en la palabra.\n")
            if not "_" in palabra_oculta:
                juego_terminado = True
        else:
            intentos += 1
            print(f"¡Letra incorrecta!\n")

    if juego_terminado == True:
        mostrar_estado(palabra_oculta, intentos, letras_usadas)
        print(f"¡FELICIDADES! Has adivinado la palabra: {palabra}")
    else:
        mostrar_estado(palabra_oculta, intentos, letras_usadas)
        print("¡GAME OVER! Te has quedado sin intentos.")
        print(f"La palabra era: {palabra}")


def main():
    """
    Punto de entrada del programa
    """
    jugar()

    jugar_otra_vez = input("\n¿Quieres jugar otra vez? (s/n): ")
    if jugar_otra_vez.lower() == 's':
        main()


if __name__ == "__main__":
    main()

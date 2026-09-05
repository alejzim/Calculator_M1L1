import random
import time

def tarea_vocabulario():
    print("\n--- TAREA: JUEGO DE VOCABULARIO (INGLÉS - ESPAÑOL) ---")
    eng_words = ['Hi', 'Bye', 'Task', 'Programm']
    sp_words = ['Hola', 'Adiós', 'Tarea', 'Programa']
    score = 0

    mode = input("Elige un modo: 0 - añadir nuevas palabras, 1 - entrenamiento: \n")
    while ((mode != '0') and (mode != '1')):
        mode = input("Símbolo no válido. Elija 0 o 1. (0 añade nuevas palabras, mientras que 1 permite el entrenamiento) \n")

    if mode == "1":
        print("¡Traduce tantas palabras como puedas! ¡Tienes 10 intentos!")
        for i in range(10):
            number = random.randint(0, len(eng_words)-1)
            print("Cómo deberíamos traducirlo " + eng_words[number])
            if input() == sp_words[number]:
                print("¡¡¡Genial!!!")
                score += 1
            else:
                print("No, no del todo... La palabra correcta es - " + sp_words[number])
        print(f"\n¡Entrenamiento finalizado! Tu puntuación final es: {score}/10")
    else:
        word = input("Escribe una palabra en español: ")
        translate = input("Escriba la traducción de esta palabra en inglés: ")
        if len(word) > 0 and len(translate) > 0:
            sp_words.append(word)
            eng_words.append(translate)
            print("¡La palabra se ha añadido correctamente!")

def tarea_diccionario():
    print("\n--- TAREA 0: DICCIONARIO PARA MAYORES ---")
    meme_dict = {
        "LOL": "Una respuesta común a algo gracioso (Laughing Out Loud).",
        "CRINGE": "Algo excepcionalmente raro, incómodo o embarazoso.",
        "ROFL": "Una respuesta a una broma muy graciosa (Rolling On the Floor Laughing).",
        "SHEESH": "Expresión de sorpresa, asombro o ligera desaprobación.",
        "CREEPY": "Algo aterrador, siniestro o que da mala espina.",
        "AGGRO": "Ponerse agresivo, enojado o buscar pelea."
    }

    print("INSTRUCCIONES: Escribe palabras en mayúsculas o minúsculas.")
    for i in range(1, 6):
        print(f"\nConsulta {i} de 5")
        word = input("Escribe una palabra que no entiendas: ").strip().upper()

        if word in meme_dict:
            print(f"--> Significado de '{word}': {meme_dict[word]}")
        else:
            print(f"--> Lo sentimos, '{word}' no se encuentra en el diccionario.")
        time.sleep(0.5)

def tarea_edad():
    print("\n--- TAREA 1: CÁLCULO DE EDAD FUTURA ---")
    nombre = input("¿Cuál es tu nombre? ")
    
    # Manejo de error por si ingresan texto en lugar de un número
    while True:
        try:
            edad = int(input("¿Cuántos años tienes? "))
            break
        except ValueError:
            print("Por favor, ingresa un número entero válido para la edad.")

    edad_el_proximo_ano = edad + 1
    print(f"\nHola, {nombre}, ¡en un año tendrás {edad_el_proximo_ano} años!")

def tarea_vocales():
    print("\n--- TAREA 2: CONTADOR DE VOCALES ---")
    palabra = input("Ingresa una palabra: ")
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    contador = 0

    for letra in palabra:
        if letra in vocales:
            contador += 1

    print(f"Número de vocales: {contador}")

def tarea_calculo_x():
    print("\n--- TAREA 3: SEGUIMIENTO DE VARIABLE X ---")
    print("Ejecutando el código paso a paso:")
    print("x = 5")
    x = 5
    print(f"x = x + 2  -> x vale: {x + 2}")
    x = x + 2
    print(f"x *= 3     -> x vale: {x * 3}")
    x *= 3
    print(f"\nResultado impreso por el programa: {x}")

def menu_principal():
    while True:
        print("\n" + "=" * 45)
        print("         MENÚ DE TAREAS EN PYTHON         ")
        print("=" * 45)
        print("1. Diccionario de Jerga Moderna (5 consultas)")
        print("2. Corregir código de Edad Futura")
        print("3. Contador de Vocales")
        print("4. Análisis de la Variable X (Cálculo)")
        print("5. Juego de Vocabulario (Inglés/Español)")
        print("6. Salir")
        print("=" * 45)

        opcion = input("¿Qué tarea quieres ver? (1-6): ").strip()

        if opcion == "1":
            tarea_diccionario()
        elif opcion == "2":
            tarea_edad()
        elif opcion == "3":
            tarea_vocales()
        elif opcion == "4":
            tarea_calculo_x()
        elif opcion == "5":
            tarea_vocabulario()
        elif opcion == "6":
            print("\n¡Gracias por usar el programa! Hasta luego.")
            break
        else:
            print("\nOpción no válida. Por favor, ingresa un número entre 1 y 6.")
        
        input("\n[Presiona ENTER para volver al menú principal]")

# Inicio del programa
if __name__ == "__main__":
    menu_principal()

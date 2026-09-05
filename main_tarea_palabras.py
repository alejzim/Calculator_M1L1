import time

# 1. Almacenamiento de palabras y significados
# Usamos un DICCIONARIO (dict) porque permite asociar claves únicas (palabras) 
# con sus valores correspondientes (significados) de forma rápida.
meme_dict = {
    "LOL": "Una respuesta común a algo gracioso (Laughing Out Loud).",
    "CRINGE": "Algo excepcionalmente raro, incómodo o embarazoso.",
    "ROFL": "Una respuesta a una broma muy graciosa (Rolling On the Floor Laughing).",
    "SHEESH": "Expresión de sorpresa, asombro o ligera desaprobación.",
    "CREEPY": "Algo aterrador, siniestro o que da mala espina.",
    "AGGRO": "Ponerse agresivo, enojado o buscar pelea.",
    "GHOSTING": "Terminar una relación o contacto cortando toda comunicación sin explicación.",
    "NPC": "Alguien que parece no tener criterio propio o actúa de forma programada."
}

# Saludo inicial e instrucciones para los adultos mayores
print("=" * 55)
print(" ¡BIENVENIDO AL DICCIONARIO DE JERGA MODERNA PARA MAYORES! ")
print("=" * 55)
print("Esta aplicación le ayudará a entender las palabras que usan los jóvenes.\n")
print("INSTRUCCIONES:")
print("- Puede escribir las palabras en MAYÚSCULAS o minúsculas (nosotros nos encargamos).")
print("- En cada sesión podrá consultar hasta 5 palabras.")
print("-" * 55)

# Bucle del programa para preguntar 5 palabras en una sola ejecución
for i in range(1, 6):
    print(f"\n--- Consulta {i} de 5 ---")
    
    # 2. Recepción de la solicitud
    # Usamos .upper() para convertir la entrada a mayúsculas automáticamente,
    # así el usuario no tiene que preocuparse por cómo lo escribe.
    word = input("Escribe una palabra que no entiendas: ").strip().upper()

    # 3. Procesamiento de la solicitud
    if word in meme_dict:
        # Qué hacer si la palabra existe: mostrar el significado
        print(f"\n Visualizando significado para '{word}':")
        print(f"--> {meme_dict[word]}")
    else:
        # Qué hacer si la palabra no se encuentra
        print(f"\n Lo sentimos, la palabra '{word}' aún no está en nuestro diccionario.")
        print("Sugerencia: Revisa si está bien escrita o intenta con otra palabra.")
    
    # Pequeña pausa visual antes de la siguiente pregunta
    time.sleep(1)

print("\n" + "=" * 55)
print(" ¡Gracias por usar el Diccionario Moderno! Vuelve pronto.")
print("=" * 55)

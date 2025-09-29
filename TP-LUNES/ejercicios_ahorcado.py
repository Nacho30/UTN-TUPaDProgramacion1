#Crea un juego interactivo del ahorcado en Python. El juego debe seleccionar una palabra al 
#azar de una lista de palabras predefinidas y permitir que el jugador adivine la palabra letra por 
#letra. El jugador tiene un número limitado de intentos antes de perder el juego. 
#Requisitos: 
# Define una lista de palabras que el programa pueda elegir al azar para que el jugador 
#adivine. Puedes usar palabras relacionadas con la programación, tecnología o cualquier tema que te guste. 
# El programa debe seleccionar una palabra al azar de la lista para cada partida. 
# El juego debe mostrar el estado actual de la palabra oculta con guiones bajos (_) que 
#representan las letras no adivinadas y las letras adivinadas deben mostrarse en su 
#lugar correspondiente. 
# El jugador debe poder ingresar una letra adivinada en cada turno. 
# El programa debe verificar si la letra adivinada está en la palabra secreta y actualizar el 
#tablero en consecuencia. 
# El jugador tiene un número limitado de intentos (por ejemplo, 6) antes de perder el juego. 
# Muestra mensajes informativos al jugador, como "Adivinaste una letra correctamente" 
#o "Letra incorrecta, te quedan X intentos". 
# El juego debe terminar cuando el jugador adivina todas las letras o se quedan sin 
#intentos. 
# Proporciona un mensaje de victoria si el jugador adivina la palabra y un mensaje de 
#derrota si se quedan sin intentos. 
#Consideraciones adicionales: 
# Puedes utilizar funciones para organizar tu código de manera efectiva. 
# Agrega comentarios para explicar el funcionamiento de tu código. 

import random

def seleccionar_palabra():
    """
    Selecciona una palabra al azar de la lista predefinida
    """
    palabras = ["DEMBELE", "MBAPPE", "ORTIGOZA", "VILLA", "JANSON", 
                "MESSI", "NEYMAR", "SUAREZ", "FATI", "PEDRI",
                "KUN", "AGUERO", "ZIDANE", "RONALDO", "PELE", "MARADONA",
                "HAALAND", "KANE", "SALAH", "MODRIC", "KROOS"]
    return random.choice(palabras)
 
def mostrar_palabra(palabra, letras_adivinadas):
    """
    Muestra la palabra con letras adivinadas y guiones para las no adivinadas
    """
    resultado = []
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado.append(letra)
        else:
            resultado.append("_")
    return " ".join(resultado)

def jugar_ahorcado():
    """
    Función principal que ejecuta el juego del ahorcado
    """
    # Inicialización del juego
    bienvenida = "¡Bienvenido al juego del Ahorcado con nombres de jugadores de futbol!"
    print(bienvenida)
    
    palabra = seleccionar_palabra()
    letras_adivinadas = []
    intentos = 6
    letras_intentadas = []
    
    print(f"La palabra tiene {len(palabra)} letras. ¡Buena suerte!")
    
    # Bucle principal del juego
    while intentos > 0:
        # Mostrar estado actual
        print("\n" + "="*30)
        print(f"Palabra: {mostrar_palabra(palabra, letras_adivinadas)}")
        print(f"Intentos restantes: {intentos}")
        if letras_intentadas:
            print(f"Letras intentadas: {', '.join(letras_intentadas)}")
        
        # Solicitar letra al jugador
        letra = input("Adivina una letra: ").upper()
        
        # Validar entrada
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa solo una letra válida.")
            continue
            
        if letra in letras_intentadas:
            print("Ya intentaste con esa letra. Prueba con otra.")
            continue
            
        letras_intentadas.append(letra)
        
        # Verificar si la letra está en la palabra
        if letra in palabra:
            letras_adivinadas.append(letra)
            print("¡Adivinaste una letra correctamente!")
            
            # Verificar si ganó
            if all(letra in letras_adivinadas for letra in palabra):
                print("\n" + "🎉" * 10)
                print(f"¡BUENA CHINCHULIN! Adivinaste la palabra: {palabra}")
                print("🎉" * 10)
                return True  # Retorna True si ganó
        else:
            intentos -= 1
            print(f"MAAAAL CHINCHULIN. Te quedan {intentos} intentos.")
    
    # Mensaje final si perdió
    print("\n" + "💀" * 10)
    print(f"¡JSAJSAJSJA PERDISTE! La palabra era: {palabra}")
    print("💀" * 10)
    return False  # Retorna False si perdió

# Bucle principal para jugar múltiples veces
def main():
    """
    Función principal que permite jugar múltiples partidas
    """
    jugar_otra_vez = True
    victorias = 0
    derrotas = 0
    
    while jugar_otra_vez:
        resultado = jugar_ahorcado()
        
        if resultado:
            victorias += 1
        else:
            derrotas += 1
        
        # Mostrar estadísticas
        print(f"\n--- ESTADÍSTICAS ---")
        print(f"Victorias: {victorias}")
        print(f"Derrotas: {derrotas}")
        
        # Preguntar si quiere jugar otra vez
        while True:
            respuesta = input("\n¿Quieres jugar otra vez? (S/N): ").upper()
            if respuesta in ['S', 'SI', 'SÍ', 'Y', 'YES']:
                print("\n" + "✨" * 20)
                print("¡Nueva partida!")
                print("✨" * 20)
                break
            elif respuesta in ['N', 'NO']:
                jugar_otra_vez = False
                print("\n¡Gracias por jugar! ¡Hasta la próxima! 👋")
                break
            else:
                print("Por favor, responde con 'S' o 'N'")

# Ejecutar el juego
if __name__ == "__main__":
    main()
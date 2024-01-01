from random import choice

# Lista
palabras = ['perro', 'gato', 'mama']
letras_correctoas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False


# Elegir y mezclar lista
def elegir_palabra(palabras):
    palabras_elegida = choice(palabras)
    letras_unicas = len(set(palabras_elegida))

    return palabras_elegida, letras_unicas

# pedir letra
def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input("Por favor elige una letra: ").lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("No haz elegido una letra correcta")
    return letra_elegida


# Corroborar letra
def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    fin = False

    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctoas:
        letras_correctoas.append(letra_elegida)
        coincidencias += 1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctoas:
        print("Ya haz encontrado esa letra. Intenta con otra letra")

    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()

    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)

    return vidas, fin, coincidencias

# Cambiar guion por letra
def mostrar_tablero(palabra_elegida):
    lista_oculta = []

    for letra in palabra_elegida:
        if letra in letras_correctoas:
            lista_oculta.append(letra)
        else:
            lista_oculta.append('-')

    print(' '.join(lista_oculta))

def perder():
    print("Te haz quedado sin vidas")
    print("La palabra oculta era: " + palabra)

    return True


def ganar(palabra_descubierta):
    mostrar_tablero(palabra_descubierta)
    print("Felicitaciones, haz encontrado la palabra!")

    return True


palabra, letras_unicas = elegir_palabra(palabras)

while not juego_terminado:
    print('\n' + '*' * 20 + '\n')
    print('Letras incorrectas: ' + '-'.join(letras_incorrectas))
    print(f"Te quedan: {intentos} vidas")
    mostrar_tablero(palabra)
    print('*' * 20 + '\n')
    letra = pedir_letra()
    
    intentos, terminado, aciertos = chequear_letra(letra, palabra, intentos, aciertos)

    juego_terminado = terminado

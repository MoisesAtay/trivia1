import random
import time


BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

iniciarTrivia = True
print('CULTURA GENERAL')
print("Bienvenido a mi trivia sobre cultura general")
print("Pondremos a prueba tus conocimientos")

nombre = input("Ingresa tu nombre: ")

print(
    "\nHola ", nombre,
    "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"
)
time.sleep(1)
print(YELLOW, "si presionas x, tendrás un mensaje oculto, puede que sea la respuesta pero tendras un puntaje mínimo")
while iniciarTrivia == True:
    puntaje = random.randint(0, 10)
    time.sleep(1)
    print(RED, "Tienes ", puntaje, " puntos, cortesía de Trivia:)", RESET)
    time.sleep(1)

    print("La trivia empieza en: ")
    for numeroCarga in range(5, 0, -1):
        print("...", numeroCarga, "...")
        time.sleep(1)

    #pregunta 1**********************************
    #time.sleep(3)
    print(BLUE, '\n1) ¿Cuál es el lugar mas frio de la tierra? ', CYAN)
    print('\t a) la Antártida')
    print('\t b) el Polo Norte')
    print('\t c) Asia')
    print('\t d) Oceania', GREEN)
    resp = input('respuesta: ')
    print(YELLOW)

    while resp not in ("a", "b", "c", "d", "x"):
        resp = input(
            'debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ')

    if resp == 'a':
        puntaje += random.randint(10, 20)
        print('muy bien')
    elif resp == 'b':
        puntaje -= random.randint(5, 10)
        print('el Polo Norte puede ser, pero no lo es tanto')
    elif resp == 'c':
        puntaje -= random.randint(5, 10)
        print("frio tu respuesta")
    elif resp == 'd':
        puntaje -= random.randint(5, 10)
        print("Oceania noo!!")
    else:
        puntaje += 2
        print("la respuesta es tan fria como la Antartida")
    time.sleep(1)
    print(RED, "puntaje: ", puntaje, RESET)

    #pregunta 2*****************************
    time.sleep(3)
    print(BLUE, '\n2) ¿Quien escribió la Odisea? ', CYAN)
    print('\t a) Shakespeare')
    print('\t b) Mario Vargas Llosa')
    print('\t c) Homero')
    print('\t d) Hercules', GREEN)

    resp = input('respuesta: ')
    print(YELLOW)
    while resp not in ("a", "b", "c", "d", "x"):
        resp = input(
            'debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ')

    if resp == 'c':
        puntaje += 10
        print('muy bien')
    elif resp in ("a", "b", "d"):
        puntaje -= random.randint(5, 10)
        print('respuesta incorrecta')
    else:
        puntaje += 2
        print("shhh!... Homero")
    time.sleep(1)
    print(RED, "puntaje: ", puntaje, RESET)

    #pregunta 3***************************
    time.sleep(3)
    print(BLUE, '\n3) ¿Cuál es el rio mas grande del mundo? ', CYAN)
    print('\t a) Marte')
    print('\t b) Nilo')
    print('\t c) Rimac')
    print('\t d) Amazonas', GREEN)

    resp = input('respuesta: ')
    print(YELLOW)
    while resp not in ("a", "b", "c", "d", "x"):
        resp = input(
            'debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ')

    if resp == 'a':
        if puntaje > 0:
            puntaje /= 2
        else:
            puntaje *= 2
        print('Marte no es río')
    elif resp == 'b':
        puntaje += 5
        print("Algunos creen que es el Nilo pero no lo es")
    elif resp == 'c':
        puntaje -= 5
        print("no, para nada")
    elif resp == 'd':
        if puntaje > 0:
            puntaje *= 2
        else:
            puntaje *= -1

        print('muy bien ', nombre)
    else:
        puntaje += 2
        print("es el rio Amazonas")
    time.sleep(1)
    print(RED, "puntaje: ", puntaje)

    #pregunta 4 ***********************
    time.sleep(3)
    print(BLUE, '\n4) ¿Donde se ecuentra la torre Eiffel? ', CYAN)
    print('\t a) Paris')
    print('\t b) Francia')
    print('\t c) Italia')
    print('\t d) España', GREEN)

    resp = input('respuesta: ')
    print(YELLOW)

    while resp not in ("a", "b", "c", "d", "x"):
        resp = input(
            'debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ')

    if resp == 'b':
        puntaje += 10
        print('muy bien')
    elif resp in ("a", "c", "d"):
        puntaje -= random.randint(5, 10)
        print('respuesta incorrecta')
    else:
        puntaje += 2
        print("Esa torre es tan famosa como Francia")
    time.sleep(1)
    print(RED, "puntaje: ", puntaje, RESET)

    aleat = random.randint(3, 8)
    for puntFin in range(aleat, 0, -1):
        print("...", puntFin)
        time.sleep(0.5)
    print(MAGENTA, "TU PUNTAJE FINAL ES: ", puntaje, RESET)

    time.sleep(2)
    print("\n\nQuiere continuar jugando?: ")
    repetirJuego = input(
        "Ingresa \"si\" para repetir o cualquier tecla para finalizar: ").lower()
    if repetirJuego != "si":
        iniciarTrivia = False
        print(f"\nEspero {nombre} hayas pasado muy bien. Hasta pronto!!")
      

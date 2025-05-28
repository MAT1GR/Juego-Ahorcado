negro = '\033[30m'
rojo = '\033[31m'
verde = '\033[32m'
amarillo = '\033[33m'
azul = '\033[34m'
rosa = '\033[35m'
celeste = '\033[36m'
blanco = '\033[37m'
RESET = '\033[39m'


import os

historico = [0, 0, 0, 0, 0]


def main():
  opcion = 0
  while (opcion != 3):
    mostrarMenu()
    opcion = int(input(azul+"\nSeleccione la opcion deseada: "+rosa))
    if (opcion == 1):
      jugar()
    if (opcion == 2):
      registro()


def limpiarPantalla():
  os.system("clear")


def mostrarMenu():
  limpiarPantalla()
  print(azul+"*--------------------------------------------------*")
  print("*       Bienvenido a Juego de Ahorcado v0.1        *")
  print("*--------------------------------------------------*\n")
  print("Menú principal:\n\n")
  print(verde+"1-Comenzar la partida\n")
  print(amarillo+"2-Ultimas partidas\n")
  print(rojo+"3-Salir\n")


def jugar():
  letrasIngresadas = set()
  letrasAcertadas = set()
  limpiarPantalla()
  print(rosa+"🎮 ¡Vamos a jugar! 🎮")
  print("   ***************")
  secret = input("Ingrese la palabra oculta: ")
  secret = secret.lower()
  limpiarPantalla()
  jugador = input(verde+"Ingrese su nombre: ")
  vidas = 5
  while (vidas > 0):
    for revelar in secret:
      if (revelar in letrasAcertadas):
        print(revelar, end=" ")
      else:
        print("_ ", end=" ")
    print("\n_____________________________________")
    letra = input("\nIngrese una letra que quiera revelar: ")
    if letra in secret:
      letrasAcertadas.add(letra)
      limpiarPantalla()
    else:
      vidas = vidas - 1
      limpiarPantalla()
      print("Uy! La letra no se encuentra en la palabra")
      print("-----------------------------")
      print("      Te quedan", vidas, "vidas    ")
      print("-----------------------------")

    if letrasAcertadas == set(secret):
      print("¡Felicitaciones, ganaste!")
      print("> Presiona enter para volver al menú principal.")
      desplazar_registro()
      historico[0] = (jugador, secret, "Ganó")

  if (vidas == 0):
    print(jugador, "lamentablemente perdiste 😭")
    print("La palabra oculta era:", secret)
    input("> Presiona enter para volver al menú principal.")
    desplazar_registro()
    historico[0] = (jugador, secret, "Perdió")


def desplazar_registro():
  for i in range(3, -1, -1):
    historico[i + 1] = historico[i]


def registro():
  print(amarillo+"\nJugador - Resultado - Palabra oculta")
  print("--------------------------------------")
  print(historico[0])
  print(historico[1])
  print(historico[2])
  print(historico[3])
  print(historico[4])
  a = input("")




"""
El primer paso es llamar a la libreria "random" y determinar la variable historico_global,
esto permitira almacenar los datos de las partidas en ella e imprimirla más adelante.
"""

import random

historico_global = []

"""
Luego declaramos funciones, para poder hacer un menú interactivo, para el usuario o jugador.
las funciones a hacer son: Obtener_limite, jugar_partida, mostrar_estadiscticas, ver ultimas
estadisticas y por ultimo la función donde estaran todas las funciones, que es la de menú
principal. 
"""

def obtener_limite():
    while True:
        try:
            limite_inferior = int(input("Jugador, ingrese por favor un límite inferior: "))
            limite_superior = int(input("Jugador, ingrese por favor un límite superior: "))
            if limite_superior - limite_inferior + 1 == 100:
                return limite_inferior, limite_superior
            else:
                print("El rango debe contener exactamente 100 números. Inténtelo de nuevo.")
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos.")

def jugar_partida():
    nombre = input("Ingrese su nombre: ")
    while True:
        try:
            n_partidas = int(input("Ingrese el número de partidas a jugar: "))
            if n_partidas > 0:
                break
            else:
                print("Debe ingresar un número positivo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    historico = []

    for partida in range(n_partidas):
        print(f"\nPartida {partida + 1} de {n_partidas}")
        limite_inferior, limite_superior = obtener_limite()
        numero_secreto = random.randint(limite_inferior, limite_superior)
        intentos = 3
        rango_actual = (limite_inferior, limite_superior)
        aciertos = 0
        errores = 0

        while intentos > 0 and rango_actual[0] != rango_actual[1]:
            print(f"\nIntentos restantes: {intentos}")
            mitad = (rango_actual[0] + rango_actual[1]) // 2
            print(f"1. Si cree que el número está entre {rango_actual[0]} y {mitad}, presione 1")
            print(f"2. Si cree que el número está entre {mitad + 1} y {rango_actual[1]}, presione 2")
            print("3. Si ya sabe el número, escríbalo directamente:")

            opcion = input("Ingrese su opción (1, 2 o un número directamente): ")

            try:
                opcion = int(opcion)
            except ValueError:
                print("Entrada inválida. Ingrese 1, 2 o un número dentro del rango.")
                continue

            if opcion == 1:
                nuevo_rango = (rango_actual[0], mitad)
            elif opcion == 2:
                nuevo_rango = (mitad + 1, rango_actual[1])
            elif rango_actual[0] <= opcion <= rango_actual[1]:  # Intento de adivinanza
                if opcion == numero_secreto:
                    print("¡Felicidades! Has adivinado el número.")
                    resultado = "Adivinó"
                    break
                else:
                    print("Incorrecto. Ese no es el número.")
                    intentos -= 1
                    errores += 1
                    continue
            else:
                print("Opción inválida, intente nuevamente.")
                continue

            # Si el número está en el nuevo rango, se mantiene
            if nuevo_rango[0] <= numero_secreto <= nuevo_rango[1]:
                print("¡Vas por buen camino!")
                aciertos += 1
                rango_actual = nuevo_rango  # ✅ Se actualiza el rango correctamente
            else:
                print("Ese rango no contiene el número. Intento perdido.")
                errores += 1
                intentos -= 1  # ❌ Se pierde un intento si el usuario elige mal

        if intentos == 0:
            print(f"Te has quedado sin intentos. El número secreto era {numero_secreto}.")
            resultado = "No adivinó"
        elif rango_actual[0] == rango_actual[1]:  
            print(f"¡El número es {rango_actual[0]}!")
            resultado = "Adivinó"
        else:
            while True:
                try:
                    intento_final = int(input("Última oportunidad, ingrese su suposición final: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido.")

            if intento_final == numero_secreto:
                print("¡Felicidades! Has adivinado el número.")
                resultado = "Adivinó"
            else:
                print(f"Incorrecto. El número secreto era {numero_secreto}.")
                resultado = "No adivinó"

        historico.append({
            "jugador": nombre,
            "partida": partida + 1,
            "aciertos": aciertos,
            "errores": errores,
            "resultado": resultado,
            "numero_secreto": numero_secreto
        })
        historico_global.append(historico[-1])

    mostrar_estadisticas(historico)

def mostrar_estadisticas(historico):
    if not historico:
        print("\nNo hay estadísticas registradas aún.")
        return

    total_adivinados = sum(1 for partida in historico if partida["resultado"] == "Adivinó")
    total_no_adivinados = len(historico) - total_adivinados

    print("\nResumen del último juego:")
    print("{:<15} {:<10} {:<10} {:<10} {:<20}".format("Jugador", "Partida", "Aciertos", "Errores", "Número Secreto"))
    print("-" * 65)
    for partida in historico:
        print("{:<15} {:<10} {:<10} {:<10} {:<20}".format(
            partida['jugador'], partida['partida'], partida['aciertos'], partida['errores'], partida['numero_secreto']))
    
    print("\nEstadísticas generales:")
    print(f"Total de veces que adivinó el número: {total_adivinados}")
    print(f"Total de veces que no adivinó el número: {total_no_adivinados}")
    print(f"Porcentaje de aciertos: {total_adivinados / len(historico) * 100:.2f}%")

def ver_ultimas_estadisticas():
    mostrar_estadisticas(historico_global)

def menu_principal():
    while True:
        print("\nMenú Principal:")
        print("1. Jugar")
        print("2. Reglas del juego")
        print("3. Ver estadísticas de la última partida")
        print("4. Salir del juego")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            jugar_partida()
        elif opcion == '2':
            print("\nReglas del juego:")
            print("- Se selecciona un número aleatorio en el rango de 100 números.")
            print("- Se ofrecen pistas reduciendo el rango de búsqueda.")
            print("- Puedes elegir un rango o ingresar un número si crees saberlo.")
            print("- Perderás intentos si eliges un rango incorrecto o fallas al adivinar.")
        elif opcion == '3':
            ver_ultimas_estadisticas()
        elif opcion == '4':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
        else:
            print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    menu_principal()

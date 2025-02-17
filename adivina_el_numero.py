


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
            if limite_superior - limite_inferior == 100:
                return limite_inferior, limite_superior
            else:
                print("El rango debe contener exactamente 100 números. Inténtelo de nuevo.")
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos.")

def jugar_partida():
    nombre = input("Ingrese su nombre: ")
    n_partidas = int(input("Ingrese el número de partidas a jugar: "))
    historico = []
    
    for partida in range(n_partidas):
        print(f"\nPartida {partida + 1} de {n_partidas}")
        limite_inferior, limite_superior = obtener_limite()
        numero_secreto = random.randint(limite_inferior, limite_superior)
        intentos = 3
        rango_actual = (limite_inferior, limite_superior)
        aciertos = 0
        errores = 0
        
        while intentos > 0:
            print(f"Intentos restantes: {intentos}")
            mitad = (rango_actual[0] + rango_actual[1]) // 2
            print(f"Si cree que el número está entre {rango_actual[0]} y {mitad}, presione 1")
            print(f"Si cree que el número está entre {mitad + 1} y {rango_actual[1]}, presione 2")
            
            opcion = input("Ingrese su opción (1 o 2): ")
            if opcion == '1':
                nuevo_rango = (rango_actual[0], mitad)
            elif opcion == '2':
                nuevo_rango = (mitad + 1, rango_actual[1])
            else:
                print("Opción inválida, intente nuevamente.")
                continue
            
            if numero_secreto in range(nuevo_rango[0], nuevo_rango[1] + 1):
                print("¡Vas por buen camino!")
                aciertos += 1
                rango_actual = nuevo_rango
            else:
                print(f"Incorrecto. El número está en el rango {rango_actual[0]} a {rango_actual[1]}")
                errores += 1
                intentos -= 1
        
        print(f"Intentos restantes: {intentos}")
        print("Última oportunidad, ingrese su suposición final:")
        intento_final = int(input("Después de todas las pistas, ¿cuál crees que es el número?: "))
        acerto = intento_final == numero_secreto
        resultado = "Adivinó" if acerto else "No adivinó"
        print(f"Resultado de la partida: {resultado}")
        
        partida_info = {
            "jugador": nombre,
            "partida": partida + 1,
            "aciertos": aciertos,
            "errores": errores,
            "resultado": resultado,
            "numero_secreto": numero_secreto
        }
        historico.append(partida_info)
        historico_global.append(partida_info)
    
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
            print("- La máquina escogerá un número entre el rango inferior y superior que determina el jugador (tiene que tener 100 números de diferencia).")
            print("- Se te dará un rango de opciones para elegir.")
            print("- Si aciertas el rango, avanzas sin perder vidas.")
            print("- Si fallas, pierdes intentos (tienes 3 en total).")
            print("- El rango se irá reduciendo acercándose al número secreto hasta que aciertes o pierdas.")
            print("- Las últimas estadísticas solo estarán hasta que el juego sea cerrado a través de salir del juego.")
        
        elif opcion == '3':
            ver_ultimas_estadisticas()
        elif opcion == '4':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
        else:
            print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    menu_principal()

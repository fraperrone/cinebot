## AUTORES:
# Franco Perrone Rey
# Maximiliano Ezequiel Funes


# Descripción general sintesis: CineBot es un asistente virtual diseñado para ayudar a los usuarios a reservar entradas, consultar la cartelera y dejar reseñas en el cine MovieTime. El bot ofrece una experiencia interactiva y amigable, guiando al usuario a través de cada proceso de manera clara y eficiente. Con funciones específicas para cada opción del menú, CineBot facilita la gestión de reservas, proporciona información actualizada sobre las películas disponibles y permite a los usuarios compartir sus opiniones sobre las películas que han visto.


nombre_bot = "CineBot"
nombre_cine = "MovieTime"

# descripcion variables globales: se definen las variables globales que contienen la información de la cartelera, los horarios, los precios y los tipos de entradas disponibles en el cine. Estas variables se utilizan en las funciones para mostrar la información al usuario y realizar los cálculos necesarios para la reserva de entradas.
cartelera = {
    1: "Mortal Kombat 2",
    2: "Stars Wars: The Mandalorian and Grogu",
    3: "The Devil Wears Prada 2"
}

horarios = {
    1: "17:30 hs",
    2: "20:30 hs",
    3: "23:30 hs"
}

precios = {
    "2D": 3500,
    "3D": 5000,
    "VIP": 7000
}

tipos_entrada = {
    1: "2D",
    2: "3D",
    3: "VIP"
}

def validar_opcion(opcion, opciones_validas):
    ## validar opcion ingresada por el usuario hasta que sea correcta
    while opcion not in opciones_validas:
        print("\nOpción no válida. Por favor, elija una opción válida.")
        opcion = int(input("\nIngrese la opción: "))
    return opcion


def menu():

    # descripcion: mostrar el menú principal con las opciones disponibles para el usuario

    print(f"\nHola, soy {nombre_bot}, el asistente virtual del cine {nombre_cine}")     #   Bienvenida
    print(f"\nIndíqueme cómo le puedo ayudar:")
    print("1. Reservar entradas.")
    print("2. Consultar cartelera.")
    print("3. Dejar una reseña.")

def reservar_entradas():
    
    #   OPCIÓN 1: RESERVAR ENTRADAS

    # descripcion: mostrar las películas disponibles, solicitar al usuario que elija una película, luego mostrar los tipos de entradas disponibles y sus precios, solicitar el tipo de entrada y la cantidad, solicitar el nombre de cada asistente, calcular el total a pagar, mostrar un resumen de la compra y agradecer al usuario por su reserva

    print("\nTenemos las siguientes películas disponibles:")
    for num, peli in cartelera.items():
        print(f"{num}. {peli}")

    opcion_pelicula = int(input("\n¿Qué película quiere ver? "))    
    opcion_pelicula = validar_opcion(opcion_pelicula, cartelera.keys())
    pelicula_elegida = cartelera[opcion_pelicula]

    print("\n¿Qué tipo de entrada desea?")
    for num, tipo in tipos_entrada.items():
        print(f"{num}. {tipo} - ${precios[tipo]:,}")

    opcion_tipo = int(input("\nIngrese el tipo de entrada: "))
    opcion_tipo = validar_opcion(opcion_tipo, tipos_entrada.keys())
    tipo_elegido = tipos_entrada[opcion_tipo]
    precio_unitario = precios[tipo_elegido]

    cantidad = int(input("\n¿Cuántas entradas quiere comprar? "))

    nombres_asistentes = []                                         #   Nombre de cada asistente
    for i in range(1, cantidad + 1):
        nombre = input(f"Ingrese el nombre de la persona {i}: ")
        nombres_asistentes.append(nombre)

    total = precio_unitario * cantidad                              #   Calcular total

    print(f"\nResumen de su compra:")
    print(f"    Película:               {pelicula_elegida}")
    print(f"    Tipo:                   {tipo_elegido}")
    print(f"    Asistente/es:           {', '.join(nombres_asistentes)}")
    print(f"\nEl total a pagar es:      ${total:,}")

    nombre_reserva = input("\n¿Con qué nombre se registra la reserva? ")
    print(f"\nGracias por elegir {nombre_cine}, {nombre_reserva.upper()}.")
    print("Su reserva fue realizada con éxito. ¡Esperamos su visita!")
    pass

def consultar_cartelera():
    #   OPCIÓN 2: CONSULTAR CARTELERA

    # descripcion: mostrar la cartelera disponible hoy, incluyendo el nombre de cada película y su horario, y agradecer al usuario por consultar la cartelera

    print("\nCartelera disponible hoy:")
    for num, peli in cartelera.items():
        print(f"  - {peli}: {horarios[num]}")

    print(f"\nGracias por consultar la cartelera de {nombre_cine}.")

def dejar_reseña():

    #   OPCIÓN 3: DEJAR UNA RESEÑA

    # descripcion: mostrar las películas disponibles y solicitar al usuario que elija una película para dejar su reseña, luego solicitar la reseña y la puntuación, y finalmente agradecer al usuario por su comentario

    print("\n¿Qué película vió?")                                   
    for num, peli in cartelera.items():
        print(f"{num}. {peli}")

    opcion_pelicula = int(input("\nIngrese el número de la película: "))
    pelicula_vista = cartelera[opcion_pelicula]

    resenia = input(f"\nEscriba su reseña sobre '{pelicula_vista}':\n> ")

    puntuacion = int(input("\nDel 1 al 5, ¿qué puntuación le da? "))    #
    puntuacion = validar_opcion(puntuacion, [1, 2, 3, 4, 5])

    if puntuacion == 5:
        print("\n¡Nos alegra que haya disfrutado la película!")
    elif puntuacion in [3, 4]:
        print("\nGracias por su comentario. Seguiremos mejorando.")
    elif puntuacion in [1, 2]:
        print("\nLamentamos que su experiencia no haya sido la mejor.")

    print(f"\nGracias por dejar su reseña en {nombre_cine}. ¡Hasta la próxima!")
    pass


if __name__ == "__main__":
    while True:

        ## descripcion: mostrar el menú principal y solicitar al usuario que elija una opción hasta que ingrese una opción válida

        menu()
        opcion = int(input("\nIngrese la opción: "))
        opcion = validar_opcion(opcion, [1, 2, 3])

        if opcion == 1:                                                      
            reservar_entradas()
            break

        elif opcion == 2:                                                   
            consultar_cartelera()
            break

        elif opcion == 3:
            dejar_reseña()                                                   
            break

nombre_bot = "CineBot"
nombre_cine = "MovieTime"

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

def menu():
    print(f"\nHola, soy {nombre_bot}, el asistente virtual del cine {nombre_cine}")     #   Bienvenida
    print(f"\nIndíqueme cómo le puedo ayudar:")
    print("1. Reservar entradas.")
    print("2. Consultar cartelera.")
    print("3. Dejar una reseña.")

def reservar_entradas():
    
    #   OPCIÓN 1: RESERVAR ENTRADAS

    print("\nTenemos las siguientes películas disponibles:")
    for num, peli in cartelera.items():
        print(f"{num}. {peli}")

    opcion_pelicula = int(input("\n¿Qué película quiere ver? "))    #   CON OTROS NÚMEROS SE ROMPE
    pelicula_elegida = cartelera[opcion_pelicula]

    print("\n¿Qué tipo de entrada desea?")
    for num, tipo in tipos_entrada.items():
        print(f"{num}. {tipo} - ${precios[tipo]:,}")

    opcion_tipo = int(input("\nIngrese el tipo de entrada: "))
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
    print("\nCartelera disponible hoy:")
    for num, peli in cartelera.items():
        print(f"  - {peli}: {horarios[num]}")

    print(f"\nGracias por consultar la cartelera de {nombre_cine}.")

def dejar_reseña():

    #   OPCIÓN 3: DEJAR UNA RESEÑA

    print("\n¿Qué película vió?")                                   #   CON OTROS NÚMEROS SE ROMPE
    for num, peli in cartelera.items():
        print(f"{num}. {peli}")

    opcion_pelicula = int(input("\nIngrese el número de la película: "))
    pelicula_vista = cartelera[opcion_pelicula]

    resenia = input(f"\nEscriba su reseña sobre '{pelicula_vista}':\n> ")

    puntuacion = int(input("\nDel 1 al 5, ¿qué puntuación le da? "))    #   DEJA PONER OTROS VALORES

    if puntuacion == 5:
        print("\n¡Nos alegra que haya disfrutado la película!")
    elif puntuacion in [3, 4]:
        print("\nGracias por su comentario.")
    elif puntuacion in [1, 2]:
        print("\nLamentamos que su experiencia no haya sido la mejor.")

    print(f"\nGracias por dejar su reseña en {nombre_cine}. ¡Hasta la próxima!")
    pass

while True:

    menu()
    opcion = int(input("\nIngrese la opción: "))

    if opcion == 1:                                                      
        reservar_entradas()
        break

    elif opcion == 2:                                                   
        consultar_cartelera()
        break

    elif opcion == 3:
        dejar_reseña()                                                   
        break

    else:                                                               #   OPCIÓN INVÁLIDA
        print("\nOpción no válida. Por favor, elija 1, 2 o 3.")
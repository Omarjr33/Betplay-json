import mensajes
import json

def cargar_datos():
    try:
        with open('datos.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"equipos": {}, "jugadores": []}

def guardar_datos(datos):
    with open('datos.json', 'w') as f:
        json.dump(datos, f, indent=4)

def mostrar_menu_principal():
    print(mensajes.MENU_PRINCIPAL)
    return input("Seleccione una opción: ")

def mostrar_menu_registro_integrante():
    print(mensajes.TIPO_INTEGRANTE)
    return input("Seleccione el tipo de integrante: ")

def mostrar_menu_estadisticas_equipos():
    print("""
    Estadísticas de equipos:
    1. Equipo con más goles marcados
    2. Equipo con más goles en contra
    3. Equipo en último puesto
    4. Mostrar todos los equipos
    5. Volver al menú principal
    """)
    return input("Seleccione una opción: ")

def mostrar_menu_estadisticas_jugadores():
    print("""
    Estadísticas de jugadores:
    1. Jugador con más faltas cometidas
    2. Jugador con más tarjetas amarillas
    3. Mostrar todos los jugadores
    4. Volver al menú principal
    """)
    return input("Seleccione una opción: ")

def mostrar_todos_los_equipos(datos):
    if not datos['equipos']:
        print("No hay equipos registrados.")
    else:
        for nombre, equipo in datos['equipos'].items():
            print(f"\nEquipo: {nombre}")
            print(f"Jugadores: {', '.join([j['nombre'] for j in equipo['jugadores']])}")
            print(f"Cuerpo técnico: {', '.join([ct['nombre'] for ct in equipo['cuerpo_tecnico']])}")
            print(f"Goles a favor: {equipo['goles_favor']}")
            print(f"Goles en contra: {equipo['goles_contra']}")
            print(f"Puntos: {equipo['puntos']}")

def mostrar_todos_los_jugadores(datos):
    if not datos['jugadores']:
        print("No hay jugadores registrados.")
    else:
        for jugador in datos['jugadores']:
            print(f"\nNombre: {jugador['nombre']}")
            print(f"Equipo: {jugador['equipo']}")
            print(f"Goles: {jugador['goles']}")
            print(f"Tarjetas amarillas: {jugador['tarjetas_amarillas']}")
            print(f"Tarjetas rojas: {jugador['tarjetas_rojas']}")
            print(f"Faltas: {jugador['faltas']}")
import mensajes

def registrar_equipo(datos):
    print(mensajes.REGISTRO_EQUIPO)
    nombre = input(mensajes.NOMBRE_EQUIPO)
    datos['equipos'][nombre] = {
        'jugadores': [],
        'cuerpo_tecnico': [],
        'goles_favor': 0,
        'goles_contra': 0,
        'puntos': 0
    }
    print(mensajes.EQUIPO_REGISTRADO)

def obtener_equipo_mas_goles(datos):
    if not datos['equipos']:
        return "No hay equipos registrados."
    return max(datos['equipos'], key=lambda x: datos['equipos'][x]['goles_favor'])

def obtener_equipo_mas_goles_contra(datos):
    if not datos['equipos']:
        return "No hay equipos registrados."
    return max(datos['equipos'], key=lambda x: datos['equipos'][x]['goles_contra'])

def obtener_ultimo_equipo(datos):
    if not datos['equipos']:
        return "No hay equipos registrados."
    return min(datos['equipos'], key=lambda x: datos['equipos'][x]['puntos'])
import mensajes

def registrar_integrante(tipo, datos):
    print(mensajes.REGISTRO_INTEGRANTE)
    nombre = input(mensajes.NOMBRE_INTEGRANTE)
    equipo = input("Ingrese el nombre del equipo al que pertenece: ")
    
    if equipo not in datos['equipos']:
        return "El equipo no existe."
    
    if tipo == '1':  # Jugador
        nuevo_jugador = {
            'nombre': nombre,
            'equipo': equipo,
            'goles': 0,
            'tarjetas_amarillas': 0,
            'tarjetas_rojas': 0,
            'faltas': 0
        }
        datos['equipos'][equipo]['jugadores'].append(nuevo_jugador)
        datos['jugadores'].append(nuevo_jugador)
    else:
        datos['equipos'][equipo]['cuerpo_tecnico'].append({
            'nombre': nombre,
            'tipo': tipo
        })
    
    print(mensajes.INTEGRANTE_REGISTRADO)
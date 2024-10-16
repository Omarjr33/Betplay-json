def jugador_mas_faltas(datos):
    if not datos['jugadores']:
        return "No hay jugadores registrados."
    
    return max(datos['jugadores'], key=lambda x: x['faltas'])['nombre']

def jugador_mas_tarjetas_amarillas(datos):
    if not datos['jugadores']:
        return "No hay jugadores registrados."
    
    return max(datos['jugadores'], key=lambda x: x['tarjetas_amarillas'])['nombre']
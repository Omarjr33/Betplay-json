import mensajes
import menus
import equipos
import plantilla
import estadisticas

if __name__ == "__main__":
    print(mensajes.BIENVENIDA)
    datos = menus.cargar_datos()
    
    while True:
        opcion = menus.mostrar_menu_principal()
        
        if opcion == '1':
            equipos.registrar_equipo(datos)
            menus.guardar_datos(datos)
        elif opcion == '2':
            tipo = menus.mostrar_menu_registro_integrante()
            plantilla.registrar_integrante(tipo, datos)
            menus.guardar_datos(datos)
        elif opcion == '3':
            while True:
                opcion_estadisticas = menus.mostrar_menu_estadisticas_equipos()
                if opcion_estadisticas == '1':
                    print(f"Equipo con más goles: {equipos.obtener_equipo_mas_goles(datos)}")
                elif opcion_estadisticas == '2':
                    print(f"Equipo con más goles en contra: {equipos.obtener_equipo_mas_goles_contra(datos)}")
                elif opcion_estadisticas == '3':
                    print(f"Equipo en último puesto: {equipos.obtener_ultimo_equipo(datos)}")
                elif opcion_estadisticas == '4':
                    menus.mostrar_todos_los_equipos(datos)
                elif opcion_estadisticas == '5':
                    break
                else:
                    print(mensajes.OPCION_INVALIDA)
        elif opcion == '4':
            while True:
                opcion_estadisticas = menus.mostrar_menu_estadisticas_jugadores()
                if opcion_estadisticas == '1':
                    print(f"Jugador con más faltas: {estadisticas.jugador_mas_faltas(datos)}")
                elif opcion_estadisticas == '2':
                    print(f"Jugador con más tarjetas amarillas: {estadisticas.jugador_mas_tarjetas_amarillas(datos)}")
                elif opcion_estadisticas == '3':
                    menus.mostrar_todos_los_jugadores(datos)
                elif opcion_estadisticas == '4':
                    break
                else:
                    print(mensajes.OPCION_INVALIDA)
        elif opcion == '5':
            print(mensajes.SALIDA)
            break
        else:
            print(mensajes.OPCION_INVALIDA)
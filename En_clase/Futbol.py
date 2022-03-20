def equipo(ganados,empatados,perdidos):
    puntaje_final=(ganados*3)+(empatados*1)
    print(puntaje_final)
ganados=int(input("digite los partidos ganados: "))        
empatados=int(input("digite los partidos empatados: "))
perdidos=int(input("digite los partidos perdios: "))
equipo(ganados,empatados,perdidos)
total=(ganados+empatados+perdidos)
print(f'Partidos Jugados: {total}')
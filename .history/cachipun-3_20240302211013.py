# PREPARACION Y LIMPIEZA DE LA CONSOLA

import os
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')
limpiar_consola()

# USO DE CODIGOS DE FORMATO PARA TEXTO ANSI PARA TEXTO EN LA TERMINAL
#--------------------------------------------------------------------

def game_over():
    print("\033[41m*********************************\033[0m")
    print("\033[41m \033[0m")
    print("\033[41m******* g a m e    o v e r  ******\033[0m")
    print("")
    print("\033[41m*********************************\033[0m")



# Importar librería randomica

import random

# **** Solicitar una opcion al usuario ********
mi_jugada = input('Elige "\033[42m\033[1mpiedra", "papel" o "tijera\033[0m": ')

if mi_jugada != 'piedra' and mi_jugada != 'papel' and mi_jugada != 'tijera':
    print("Error... Debes escribir una opcion válida")
    game_over()
    #print("")
    #print("******* g a m e    o v e r  ***")

       
else:
# Ejecucion del codigo por opcion correcta, con la indentación correcta del IF
#-----------------------------------------------------------------------------
    
    # Generar la jugada de la máquina
    # --------------------------------

    opciones = ['piedra', 'papel', 'tijera']
    jugada_maquina = random.choice(opciones)  # Eleccion de la PC según azar




    # DEBIDO A QUE LA LINEA DE COMPARACIONES ES MUY EXTENSA
    # PUSE EL SIGNO DE CONTINUADOR DE LINEA (backslah , similar al sub-guion como VBA)
    # PARA EFECTOS DE IMPRIMIR/REVISAR/ANALIZAR EL CODIGO

    if mi_jugada == jugada_maquina:

        print(f'Plop ... Empatamos. Ambos tenemos \033[41m{mi_jugada}\033[0m.')
        game_over()

    elif (mi_jugada == 'piedra' and jugada_maquina == 'tijera')  or \
        (mi_jugada == 'tijera' and jugada_maquina == 'papel')  or \
            (mi_jugada == 'papel' and jugada_maquina == 'piedra'): 


        print(f'¡Ganééééééééé Yo con \033[31m{mi_jugada}\033[0m y tu tienes {jugada_maquina}.')

        # G A M E   O V E R
    # --------------------------------    
        game_over()
    else: 

        print(f'Guaaaaa... Perdíííííí, tengo \033[31m{mi_jugada}\033[0m y tu elegiste {jugada_maquina}.')

    # G A M E   O V E R
    # --------------------------------    
        game_over()

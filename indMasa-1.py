# Limpieza de consola y aparicion del cursor activo

import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

# Llamar a la función para limpiar la consola
limpiar_consola()

# Solicitar al usuario que ingrese su peso y altura



peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

# Calcular el IMC
imc = peso / (altura ** 2)
imc_fmto ="{:,.2f}".format(imc)
print("")

# Mostrar el resultado
print("Su Índice de Masa Corporal (IMC) es:", imc_fmto, 
      "\ny según la tabla de la NASA/UNESCO/PIPIRIPI \nse le clasifica con salud de: ")
print("")
print("**********************")

# CLASIFICAR SEGUN TABLA

if imc < 18.5 :
    print("** bajo peso **")
elif imc >= 18.5 and imc < 25:
    print("** Adecuado **")
elif imc >=25 and imc < 30:
    print("** Sobrepeso **")
elif imc >= 30 and imc < 35:
    print("** Obesidad Grado 1 **")
elif imc >= 35 and imc < 40:
    print("** Obesidad Grado 2 **")
elif imc >= 40:
    print("** Obesidad Grado 3 **")
print("**********************")








    # sad esa un comentario

#-------- Mensajes ----------#
MENSAJE_BIENVENIDA = "Bienvenid@!!!!! te apoyaré ahorrando"
PREGUNTA_VALOR_PC = "Cuanto vale el pc que deseas?: "
PREGUNTA_CUANDO_TIENES = "Cuanto llevas ahorrado?: "
MENSAJE_AHORRO = "LLEVAS AHORRADO: "

#------ Entrada --------#
print("---------------- Bienvenida -----------------")
print(MENSAJE_BIENVENIDA)
valor = float(input(PREGUNTA_VALOR_PC))
ahorrado = float(input(PREGUNTA_CUANDO_TIENES))

while(valor > ahorrado):
    print(MENSAJE_AHORRO, ahorrado, "Te falta", valor - ahorrado)
    ahorrado = +1000
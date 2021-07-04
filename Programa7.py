'''
UNAM FI
Inteligencia Artificial

Intregrantes:
-Aguilar Plascencia Laura Fabiola
-Flores Gómez Jessica Victoria
-Martínez Martínez Yanni
'''
operandos = {"^": "and" ,
               "v": "or", 
               "¬": "not" ,
               "=>": "" , 
               "<=>": ""}
               
operador = {"V" :"true",
            "F" :"false"}

#****************************************************
def prepo(listaExp, listaOperadores, listaOperando):
	""" 
	TODO: El funcionamiento de esta función es separar operandos y operadores en diferentes pilas, una vez
	que encuentra un ")" comenzará la recursividad y evaluará los casos base. En esta versión no está
	permitido el valor ¬ aún.

	----------------------------------------------------------------------------------------------
	Parametros:
	@param listaExp Hace referencia a la lista con la expresión completa hasta ese momento.
	@param listaOperadores Hace referencia a la pila de operadores al momento.
	@param listaOperando Hace referencia a la pila de operandos al momento.

	----------------------------------------------------------------------------------------------
	Retorno:
	@return Retorna una cadena donde indica si la expresión es invalida o retorna el valor del resultado de la 
	expresion.
	 """
	resultado = "X Su expresión no está bien formada" #Significa que hubo un error
	if(len(listaOperadores) > 0 and len(listaOperando)>0):
		#Hace la operación.
		op2 = listaOperadores.pop()
		operando = listaOperando.pop()
		op1 = listaOperadores.pop()
		
		#Casos particulares:
		if(operando == "v"):
			if(op1 == "F" and op2 == "F"):
				return "F"
			else:
				return "V"
		#
		if(operando == "^"):
			if(op1 == "V" and op2 == "V"):
				return "V"
			else:
				return "F"

		if(operando == "=>"):
			if(op1 == "V" and op2 == "F"):
				return "F"
			else: 
				return "V"

		if(operando == "<=>"):
			if(op1 == op2):
				return "V"
			else:
				return "F"
	
		#Dejar al final el negado
		#este return va a la lista de operadores

	for elemento in listaExp: #Recorre toda la lista
		if elemento == ")":
			#Recursividad
			resultado = prepo(listaExp, listaOperadores, listaOperando)
			listaOperadores.append(resultado) #Agregando a operadores
		
			
		elif elemento in operador:
			print("Soy un operador "+elemento)
			listaOperadores.append(elemento)

		elif elemento in operandos:
			print("Soy un operando "+elemento)
			listaOperando.append(elemento)

		elif elemento == "(":
			#Simplemente deja pasar el simbolo (
			pass
		else: #Error si encuentra un simbolo incorrecto
			print("Su expresión no está bien estructurada, el programa finalizará ... ")
			break
	return resultado

#**************************************
def main():
	listaOperadores = []
	listaOperando = []
	expresion = input("Ingrese su expresión: ") #Será un string donde está la expresión prepo
	listaExp = expresion.split(" ")
	
	resultado = prepo(listaExp, listaOperadores, listaOperando)
	print(resultado)
	

main()

""" 
Expresiones Testeadas

( V v V ) = V
( V v F ) = V
( F v V ) = V
( F v F ) = F

( V ^ V ) = V
( V ^ F ) = F
( F ^ V ) = F
( F ^ F ) = F

( V => V ) = V
( V => F ) = F
( F => V ) = V
( F => F ) = V

( V <=> V ) = V
( V <=> F ) = F
( F <=> V ) = F
( F <=> F ) = V

( V v ( V ^ F ) )  = V

( V v ( V ^ F ) => ( F ^ V ) ) = V
  V        F     V      F     = V

( V <=> ( V v F ) => ( F v V ) ) = V
  V  |V|    V     |V|     V      = V

( V <=> ( V v F ) => ( F v V ) v F ) = V

( V <=> ( V v F ) => ( F v V ) ^ F <=> V ) = F

F <=> V ^ ( F v F ) => ( V ^ V ) <=> ( F <=> F ) = V

( F v F
"""
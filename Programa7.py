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
	
	@param
	
	 """
	resultado = "X Su expresión no está bien formada" #Significa que hubo un error
	if(len(listaOperadores) > 0 and len(listaOperando)>0):
		#Hace la operación.
		print("Entre por recursividad")

		op2 = listaOperadores.pop()
		operando = listaOperando.pop()
		op1 = listaOperadores.pop()
		
		#Casos particulares:
		if(operando == "v"):
			print("Entre a -v- ")
			if(op1 == "F" and op2 == "F"):
				print("Sor retorno recursivo")
				return "F"
			else:
				print("Sor retorno recursivo")
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
			print("Soy un ) ="+elemento)
			resultado = prepo(listaExp, listaOperadores, listaOperando)
			print(resultado)
			listaOperadores.append(resultado) #Agregando a operadores
		
			
		elif elemento in operador:
			print("Soy un operador "+elemento)
			listaOperadores.append(elemento)

		elif elemento in operandos:
			print("Soy un operando "+elemento)
			listaOperando.append(elemento)

		elif elemento == "(":
			#print("Soy un parentesis ( = "+elemento)
			#listaOperando.append(elemento)
			pass
		else:
			print("Su expresión no está bien estructurada, el programa finalizará ... ")
			break
	return resultado
	#print(listaOperando)
	#print(listaOperadores)

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
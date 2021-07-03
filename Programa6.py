""" PROGRAMA 6: Cálculo preposicional

Aguilar Plascencia Laura Fabiola
Flores Gomez Jessica Victoria
Martínez Martínez Yanni

Programa:
♦Desarrollar un programa que evalúe expresiones de lógica proposicional usando el
algoritmorecursivopresentado en clase.
♦Nota: No es válido utilizar alguna librería  o programa hecho por terceros.
 """

operandos = {"^": "and" ,
               "v": "or", 
               "¬": "not" ,
               "=>": "" , 
               "<=>": ""}
               
operador = {"V" :"true",
            "F" :"false"}

print(operadorBin.keys())

def preposicional(expresion):
    pilaOperadores = []
    pilaOperandos = []


from cmath import sqrt
from random import randint
def suma(a=0,b=0):
    a= float(input("Ingrese un numero: "))
    b= float(input("Ingrese un numero: "))
    return a + b
def resta(a=0,b=0):
    a= float(input("Ingrese un numero: "))
    b= float(input("Ingrese un numero: "))
    return a - b
def multiplicacion(a=0,b=0):
    a= float(input("Ingrese un numero: "))
    b= float(input("Ingrese un numero: "))
    return a * b
def division(a=0,b=0):
    a= float(input("Ingrese un numero: "))
    b= float(input("Ingrese un numero: "))
    return a / b
def cuadrado(a=0):
    a= float(input("Ingrese un numero: "))
    return a**2
def raiz(a=0):
    a= int(input("Ingrese un numero: "))
    return sqrt(a)
def conversion(a=0):
    a= float(input("Ingrese un numero: "))
    return (a*5)/100
def cuadraticaPositiva(a=0,b=0,c=0):
    return (-b+sqrt(b**2-(4*a*c)))/(2*a) 
def cuadraticaNegativa(a=0,b=0,c=0):
    return (-b-sqrt(b**2-(4*a*c)))/(2*a) 

continuar = True
while continuar:
    opcion= input("Suma, Resta, Multiplicacion, Division, Cuadrado, Raiz, Conversion(Notas), Cuadratica: ")

    if opcion == "Suma":
        print(suma())
    elif opcion == "Resta":
        print(resta())
    elif  opcion == "Multiplicacion":
        print(multiplicacion())
    elif opcion == "Division":
        print(division())
    elif opcion == "Cuadrado":
        print(cuadrado())
    elif opcion == "Raiz":
        print(raiz())
    elif opcion == "Conversion":
        print(conversion())
    elif opcion == "Cuadratica":
        a= float(input("Ingrese un numero: "))
        b= float(input("Ingrese un numero: "))
        c= float(input("Ingrese un numero: "))
        print(cuadraticaPositiva(a,b,c), cuadraticaNegativa(a,b,c))
        

        






print("Hola! Este programa convierte los numeros en base 10 a base 2")
Numero = int(input("Ingresa un numero en base 10: "))

modulos = [] 

while Numero != 0: 
    modulo = Numero % 2
    cociente = Numero // 2
    modulos.append(modulo) 
    Numero = cociente 
print(modulos)  
#Ingresar un valor por teclado y determinar si es menor que 10 si está comprendido
#entre 10 y 100 o si es mayor a 100, imprimir una leyenda, repetir el proceso 10 veces.

for valor in range(10):
    num = float(input("Ingrese un número: "))
    if num < 10:
        print("El número es menor que 10.")
    elif 10 <= num <= 100:
        print("El número está entre 10 y 100.")
    else:
        print("El número es mayor que 100.")

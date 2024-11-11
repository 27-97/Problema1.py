#Ingresar un valor por teclado y determinar si es positivo, negativo o igual a cero,
#imprimir una leyenda en cada caso

num = float(input("Ingrese un número: "))

if num > 0:
    print("El número es positivo.")
elif num < 0:
    print("El número es negativo.")
else:
    print("El número es igual a cero.")

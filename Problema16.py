#Ingresar 10 valores numéricos y obtener el promedio de los que estén
#comprendidos entre 5 y 2500 ambos inclusive, imprimir el resultado.

suma = 0
contador = 0

for y in range(10):
    valor = float(input("Ingrese un valor: "))

    if 5 <= valor <= 2500:
        suma += valor
        contador += 1

if contador > 0:
    promedio = suma / contador
    print(f"El promedio es: {promedio}")
else:
    print("No se ingresaron valores en el rango especificado.")

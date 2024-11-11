#Ingresar 10 valores numéricos por teclado y calcular la suma, el promedio e
#imprimir la suma, el promedio agregando una leyenda en cada caso.

suma = 0

for num in range(10):
    valor = float(input("Ingrese un valor: "))
    suma += valor

promedio = suma / 10

print(f"La suma es: {suma}")
print(f"El promedio es: {promedio}")


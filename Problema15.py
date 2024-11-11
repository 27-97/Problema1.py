#Ingresar 100 valores por teclado y determinar cuántas veces el valor ingresado
#es: a) Mayor a 0 y menor a 10
#b) Esta comprendido entre 10 y 100 ambos inclusive.
#c) Es mayor a 100
#d) Es negativo
#e) Es igual a 0Imprimir los resultados.

mayor_0_menor_10 = 0
entre_10_y_100 = 0
mayor_100 = 0
negativos = 0
igual_0 = 0

for i in range(100):
    valor = float(input("Ingrese un valor: "))

    if valor > 0 and valor < 10:
        mayor_0_menor_10 += 1
    elif 10 <= valor <= 100:
        entre_10_y_100 += 1
    elif valor > 100:
        mayor_100 += 1
    elif valor < 0:
        negativos += 1
    elif valor == 0:
        igual_0 += 1

print(f"Mayor a 0 y menor a 10: {mayor_0_menor_10}")
print(f"Entre 10 y 100: {entre_10_y_100}")
print(f"Mayor a 100: {mayor_100}")
print(f"Negativos: {negativos}")
print(f"Igual a 0: {igual_0}")


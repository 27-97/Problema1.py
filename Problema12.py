#Ingresar valores por teclado y acumularlos en una variable detener el proceso
#cuando la suma supere los 78500, al final imprimir el resultado

suma = 0

while suma <= 78500:
    valor = float(input("Ingrese un valor: "))
    suma += valor

print(f"La suma total es: {suma}")


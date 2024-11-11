#En un curso de computación, que consta de 24 alumnos, deberán armar un
#algoritmo que informe por pantalla el apellido y nombre junto a la nota de examen de
#cada alumno.

for alumno in range(1, 25):
    nombre = input(f"Ingrese el nombre del alumno {alumno}: ")
    apellido = input(f"Ingrese el apellido del alumno {alumno}: ")
    nota = float(input(f"Ingrese la nota del examen del alumno {alumno}: "))
    print(f"Alumno: {apellido}, {nombre} - Nota: {nota}")

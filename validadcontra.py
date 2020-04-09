"""
	Autor: Edgard Díaz
	Date: 09 - 04 - 2020
	Este código valida el formato de una contraseña.

"""
import re # libreria para la crecion de expresiones regulares.


print("\t\t --crear contraseña--")
note = "La contraseña no debe contener espacios en blanco y debe ser mayor a ocho caracteres."
password = input(f"{note}\nIngrese la contraseña: \n")


contador = 0

while len(password) < 8:
	print("la  contraseña no cumple con los requerimientos.")
	password = input("ingrese una nueva contraseña:\n")

	contador = contador + 1;

	if contador == 2:
		print("Intentos agotados.")
		exit()


match = re.search(r" ",password);

if not (match):
	print('La contraseña creada con exito')
else:
	while True:
		print("la  contraseña no cumple con los requerimientos.")
		password = input("ingrese una nueva contraseña:\n")
		
		match = re.search(r" ",password);
		if not (match):
			print('La contraseña creada con exito')
			exit()
		contador = contador + 1;
		if contador == 2:
			print("Intentos agotados.")
			exit()

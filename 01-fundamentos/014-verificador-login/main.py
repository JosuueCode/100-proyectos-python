"""Proyecto 014: Verificador de login.

Pide un usuario y una contraseña, y revisa si coinciden con los datos
guardados.
"""

# Datos de acceso de ejemplo. Un sistema real nunca guarda contraseñas así en
# el código; aquí se hace solo para practicar comparaciones.
USUARIO_CORRECTO = "admin"
CONTRASENA_CORRECTA = "python123"

usuario = input("Usuario: ")
contrasena = input("Contraseña: ")

print()

# == compara cadenas letra por letra y distingue mayúsculas de minúsculas:
# "Admin" no es igual a "admin".
# Con and, el acceso se permite solo si las dos comparaciones son True.
if usuario == USUARIO_CORRECTO and contrasena == CONTRASENA_CORRECTA:
    print("Acceso permitido. Te damos la bienvenida,", usuario)
else:
    # No se dice cuál de los dos datos falló, para no darle pistas a alguien
    # que intente adivinar el acceso.
    print("Usuario o contraseña incorrectos.")

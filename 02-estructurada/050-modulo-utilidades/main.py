"""Proyecto 050: Módulo de utilidades.

Divide la cuenta de una comida entre varias personas, con propina opcional,
usando las funciones del módulo propio utilidades.py.
"""

# Un módulo propio se importa igual que uno de la biblioteca estándar: con
# el nombre del archivo sin el .py. Python lo busca primero en la carpeta
# del programa, por eso utilidades.py tiene que estar junto a este archivo.
import utilidades


def calcular_propina(total, porcentaje):
    """Devuelve la propina para un total y un porcentaje dados."""
    return total * porcentaje / 100


def main():
    """Pide los datos de la cuenta y muestra cuánto paga cada persona."""
    print("=== Dividir la cuenta ===")
    lugar = utilidades.pedir_texto("¿Dónde comieron? ")
    total = utilidades.pedir_decimal("Total de la cuenta: ", 1)
    personas = utilidades.pedir_entero("¿Cuántas personas? ", 1, 50)

    propina = 0
    if utilidades.confirmar("¿Quieren dejar propina?"):
        porcentaje = utilidades.pedir_entero("Porcentaje de propina: ", 0, 30)
        propina = calcular_propina(total, porcentaje)

    total_con_propina = total + propina
    por_persona = total_con_propina / personas

    print()
    print(f"Cuenta en {lugar}")
    print(f"  Consumo:   {utilidades.formatear_dinero(total)}")
    print(f"  Propina:   {utilidades.formatear_dinero(propina)}")
    print(f"  Total:     {utilidades.formatear_dinero(total_con_propina)}")
    print(f"  Cada uno:  {utilidades.formatear_dinero(por_persona)}")


# Al ejecutar python main.py, __name__ vale "__main__" y se llama a main().
# Si algún día otro programa importa este archivo para usar
# calcular_propina(), la cuenta no se va a pedir sola.
if __name__ == "__main__":
    main()

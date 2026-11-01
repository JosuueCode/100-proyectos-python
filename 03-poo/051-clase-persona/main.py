"""Proyecto 051: Clase Persona.

Define una clase Persona con nombre, edad y ciudad, crea varias personas y
hace que cada una se presente.
"""

EDAD_ADULTA = 18


# class define una clase: un molde que describe qué datos guarda y qué
# puede hacer un tipo de cosa. La clase no es una persona concreta, es la
# descripción de cómo son todas. Por convención, el nombre de una clase
# empieza con mayúscula.
class Persona:
    """Representa a una persona con nombre, edad y ciudad."""

    # __init__ es un método especial que Python llama solo cada vez que se
    # crea un objeto nuevo. Sirve para darle sus datos iniciales.
    # self es el objeto que se está creando o usando. Python lo pasa
    # automáticamente como primer parámetro de cada método, por eso al
    # crear una persona solo se escriben nombre, edad y ciudad.
    def __init__(self, nombre, edad, ciudad):
        # self.nombre es un atributo: una variable que pertenece al objeto.
        # Cada persona guarda sus propios valores, sin mezclarse con otras.
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    # Un método es una función definida dentro de la clase. Recibe self
    # para poder usar los atributos del objeto que lo llama.
    def presentarse(self):
        """Muestra un saludo con los datos de la persona."""
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")
        print(f"  Vivo en {self.ciudad}.")

    def cumplir_anios(self):
        """Suma un año a la edad de la persona."""
        self.edad = self.edad + 1
        print(f"{self.nombre} cumplió años. Ahora tiene {self.edad}.")

    def es_mayor_de_edad(self):
        """Devuelve True si la persona tiene la edad adulta o más."""
        return self.edad >= EDAD_ADULTA


def main():
    """Crea varias personas y usa sus métodos."""
    # Crear un objeto es llamar a la clase como si fuera una función. Cada
    # objeto es una instancia de la clase: una persona concreta hecha con
    # el mismo molde. Aquí hay tres objetos distintos de la clase Persona.
    ana = Persona("Ana", 28, "Guadalajara")
    luis = Persona("Luis", 16, "Monterrey")
    sofia = Persona("Sofía", 35, "Puebla")

    # Los métodos se llaman con un punto, igual que los de str o list.
    # Python convierte ana.presentarse() en Persona.presentarse(ana), y así
    # self vale ana dentro del método.
    ana.presentarse()
    luis.presentarse()
    sofia.presentarse()
    print()

    # Cambiar el atributo de un objeto no afecta a los demás
    luis.cumplir_anios()
    print()

    personas = [ana, luis, sofia]
    for persona in personas:
        if persona.es_mayor_de_edad():
            print(f"{persona.nombre} es mayor de edad.")
        else:
            print(f"{persona.nombre} todavía no es mayor de edad.")


if __name__ == "__main__":
    main()

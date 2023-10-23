# Concepto 1: Variables
# Definimos variables para representar objetos en el dominio.
x = "Perro"
y = "Gato"

# Concepto 2: Predicados
# Definimos predicados para representar propiedades y relaciones.
def EsAnimal(objeto):
    animales = ["Perro", "Gato"]
    return objeto in animales

def EsDuenio(persona, animal):
    duenios = {"Juan": "Perro", "Maria": "Gato"}
    return persona in duenios and duenios[persona] == animal

# Concepto 3: Cuantificadores
# Usamos cuantificadores para expresar afirmaciones.
def TodosSonAnimales():
    return all(EsAnimal(obj) for obj in [x, y])

def AlgunoEsDuenio():
    return any(EsDuenio(persona, x) for persona in ["Juan", "Maria"])

# Concepto 4: Funciones
# Definimos funciones para representar operaciones en el dominio.
def Edad(animal):
    edades = {"Perro": 5, "Gato": 3}
    return edades.get(animal, 0)

# Concepto 5: Sentencias Compuestas
# Construimos sentencias compuestas para expresar relaciones y propiedades más complejas.
def MayorQue3Anios(animal):
    return Edad(animal) > 3

# Concepto 6: Validez y Modelos (no se implementa aquí)
# Concepto 7: Complejidad y Potencia Expresiva (no se implementa aquí)
# Concepto 8: Aplicaciones (no se implementan aquí)

# Verificamos las afirmaciones
print("1. Todos son animales:", TodosSonAnimales())
print("2. Juan es dueño de un perro:", AlgunoEsDuenio())
print("3. Edad del gato:", Edad("Gato"))
print("4. El perro tiene más de 3 años:", MayorQue3Anios("Perro"))

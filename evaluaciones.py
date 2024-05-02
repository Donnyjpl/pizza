# Importar la clase creada en el requerimiento 1
from pizza import Pizza


# a. Mostrar los valores de los atributos de clase de la clase importada sin crear una instancia de ella
print("Valores de los atributos de clase de la clase Pizza:")
print("Ingredientes Vegetales:", Pizza.ingredientes_vegetales)
print("Ingredientes Proteicos:", Pizza.ingredientes_proteicos)
print("Tipos de Masa:", Pizza.tipo_de_masa)
print("Tipos de salsa:", Pizza.tipo_salsa)
print()

# b. Verificar si "salsa de tomate" está presente en la lista ["salsa de tomate", "salsa bbq"] utilizando el método del requerimiento 2
print("¿La salsa de tomate está presente en la lista?")
if Pizza.verificar_ingrediente("salsa de tomate", ["salsa de tomate", "salsa bbq"]):
    print("Sí, está presente.")
else:
    print("No, no está presente.")
print()

# c. Crear una instancia de la clase importada y solicitar ingredientes y tipo de masa al usuario
mi_pizza = Pizza()
mi_pizza.realizar_pedido()
print()

# d. Mostrar en pantalla los ingredientes vegetales, proteicos, tipo de masa y si la instancia es una pizza válida o no
print("Ingredientes Vegetales:", mi_pizza.ingredientes_vegetales)
print("Ingredientes Proteicos:", mi_pizza.ingredientes_proteicos)
print("Tipo de Masa:", mi_pizza.tipo_de_masa)
if mi_pizza.es_pizza_valida():
    print("Esta es una pizza válida.")
else:
    print("Esta no es una pizza válida.")
print()

try:
    print("¿La clase Pizza es una pizza válida?", mi_pizza.pizza_valida)
except AttributeError as e:
    print("Error: todos los pasos anteriores se deben haber ejecutado correctamente", e)

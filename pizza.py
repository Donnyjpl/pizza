class Pizza:
    costo = 10000
    tamaño = "familiar"
    ingredientes_vegetales = ["tomate", "aceitunas", "champiñones"]
    ingredientes_proteicos = ["pollo", "vacuno", "carne vegetal"]
    tipo_de_masa = ["tradicional", "delgada"]
    tipo_salsa = ["salsa de tomate", "salsa bbq"]
    pizza_valida = False

    @staticmethod
    def validate(opciones, eleccion: str):
        # Definir validación de eleccion
        if eleccion in opciones:
            return True
        else:
            print(f"{eleccion} no está en {opciones}. Por favor realizar nuevamente el pedido")
            return False
    @staticmethod
    def verificar_ingrediente(ingrediente:str, opciones):
        return ingrediente in opciones
    
    def realizar_pedido(self):
        self.proteico = input("Ingrese el ingrediente proteico (pollo, vacuno, carne vegetal): ")
        self.vegetal1 = input("Ingrese el primer ingrediente vegetal (tomate, aceitunas, champiñones): ")
        self.vegetal2 = input("Ingrese el segundo ingrediente vegetal (tomate, aceitunas, champiñones): ")
        self.masa = input("Ingrese el tipo de masa (tradicional, delgada): ")
        self.salsa = input("Ingrese el tipo de salsa (salsa de tomate, salsa bbq): ")

        self.valido = (
            self.validate(self.ingredientes_proteicos, self.proteico) and
            self.validate(self.ingredientes_vegetales, self.vegetal1) and
            self.validate(self.ingredientes_vegetales, self.vegetal2) and
            self.validate(self.tipo_de_masa, self.masa) and 
            self.validate(self.salsa, self.salsa)
        )
        if self.valido:
            self.ingredientes_proteicos = [self.proteico]
            self.ingredientes_vegetales = [self.vegetal1, self.vegetal2]
            self.tipo_de_masa = [self.masa]
            self.salsa = [self.salsa]
            self.pizza_valida = True

    def es_pizza_valida(self):
        return self.pizza_valida

if __name__ == "__main__":
    mi_pizza=Pizza()
    mi_pizza.realizar_pedido()
  # Intentamos imprimir el valor del atributo pizza_valida de la clase Pizza
    try:
     print("¿La clase Pizza es una pizza válida?", mi_pizza.pizza_valida)
    except AttributeError as e:
     print("Error:", e)
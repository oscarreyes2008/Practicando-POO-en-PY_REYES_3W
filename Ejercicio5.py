class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio

class Moto(Fabrica):
    def cantidad(self):
        print(f"La cantidad de llantas: {self._llantas}\nEl color es: {self._color}\nEl precio es: {self._precio}")

class Carro(Fabrica):
    def cantidad(self):
        print(f"La cantidad de llantas: {self._llantas}\nEl color es: {self._color}\nEl precio es: {self._precio}")
        print("OBJETO=carro")

# Crear un objeto de la clase Moto
moto = Moto(2, "Gris", "$200")
moto.cantidad()

# Crear un objeto de la clase Carro
print("OBJETO=carro")
carro = Carro(4, "Negro", "$600")
carro.cantidad()

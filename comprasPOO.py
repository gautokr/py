class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre.lower()
        self.precio = precio
        self._cantidad = cantidad
    def mostrar_info(self):
        print(f'Nombre:{self.nombre.capitalize()}, Precio:${self.precio}, Stock:{self._cantidad}')
    def comprar(self, cantidad):
        if cantidad <= self._cantidad:
            self._cantidad -= cantidad
            return self.precio * cantidad
        else:
            print(f'No hay suficiente stock de {self.nombre}')
            return 0
        
class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla
    def mostrar_info(self):
        super().mostrar_info()
        print(f'Talla:{self.talla}')
        
class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla
    def mostrar_info(self):
        super().mostrar_info()
        print(f'Talla:{self.talla}')

class Inventario:
    def __init__(self):
        self.prendas = []
    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)
    def mostrar_inventario(self):
        for prenda in self.prendas:
            prenda.mostrar_info()
    def procesar_compra(self, nombre_ropa, cantidad):
        nombre_ropa = nombre_ropa.lower()
        for prenda in self.prendas:
            if prenda.nombre == nombre_ropa:
                total = prenda.comprar(cantidad)
                if total>0:
                    print(f'Su compra de {nombre_ropa} ha sido realizada. El costo es ${total}')
                return
        print('La prenda no existe.')
            
camisa = RopaHombre("Camisa de Hombre", 25.00, 50, "M")
pantalon = RopaHombre("Pantalón de Hombre", 30.00, 30, "M")
chaqueta = RopaHombre("Chaqueta de Hombre", 55.00, 20, "G")
falda = RopaMujer("Falda de Mujer", 28.00, 15, "S")
blusa = RopaMujer("Blusa de Mujer", 22.00, 40, "M")
vestido = RopaMujer("Vestido de Mujer", 45.00, 10, "S")
zapatos = RopaHombre("Zapatos de Hombre", 60.00, 25, 40)
zapatosfem = RopaMujer("Zapatos de Mujer", 50.00, 20, 38)

inventario = Inventario()
inventario.agregar_prenda(camisa)
inventario.agregar_prenda(pantalon)
inventario.agregar_prenda(chaqueta)
inventario.agregar_prenda(falda)
inventario.agregar_prenda(blusa)
inventario.agregar_prenda(vestido)
inventario.agregar_prenda(zapatos)
inventario.agregar_prenda(zapatosfem)

print('Bienvenido. Este es nuestro inventario.')
inventario.mostrar_inventario()

while True:
    nombre = input('¿Qué prenda desea adquirir? Escriba "salir" si ya no quiere adquirir prendas.')
    if nombre.lower() == "salir":
        break
    cantidad = int(input('Ingrese la cantidad'))
    inventario.procesar_compra(nombre, cantidad)

print('\nInventario luego de la compra ')
inventario.mostrar_inventario()
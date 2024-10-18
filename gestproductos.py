productos = []

def añadir_producto():
    print('Ingrese el nombre del producto, su costo y la cantidad disponible.')
    nombre = input('Producto: ')
    
    while True:
        try:
            costo = float(input('Precio: '))
            if costo < 0:
                print('El número debe ser positivo.')
                continue 
                
            cantidad = int(input('Cantidad: '))
            if cantidad < 0:
                print('El número debe ser positivo.')
                continue
            
            producto_dict = {
                'nombre': nombre,
                'costo': costo,
                'cantidad': cantidad,
            }
            productos.append(producto_dict)
            print(f'Su producto {nombre} ha sido añadido a la lista.')
            break
    
        except ValueError:
            print('Este campo solo acepta valores numéricos')
        

def ver_productos():
    if not productos:
        print('No hay productos disponibles.')
        return
    
    for items in productos:
        print(f'Nombre: {items["nombre"]}, Costo: {items["costo"]}, Cantidad: {items["cantidad"]}')
    
def actualizar_producto():
    nombre = input('¿Qué producto desea actualizar? ').strip().lower()
    for items in productos:
        if items['nombre'].lower() == nombre:
            updated_name = input('Introduzca el nuevo nombre: ')
            if updated_name:
                items['nombre'] = updated_name
            updated_cost = input('Introduzca el nuevo costo: ')
            if updated_cost:
                items['costo'] = float(updated_cost)
            updated_quantity = input('Introduzca la nueva cantidad: ')
            if updated_quantity:
                items['cantidad'] = int(updated_quantity)
            print('Su producto ha sido actualizado.')
            break
    else:
        print('Lo siento, el producto no ha sido encontrado.')
            

def eliminar_producto():
    nombre = input('¿Qué producto desea eliminar? ').strip().lower()
    for items in productos:
        if items['nombre'].lower() == nombre:
            productos.remove(items)
            print('El producto ha sido eliminado')
            break
    else:
        print('Lo siento, el producto no ha sido encontrado.')

def guardar_datos(): 
    with open('productos.txt', 'w') as txt_file:
        for items in productos:
            txt_file.write(f"{items['nombre']}, {items['costo']}, {items['cantidad']}\n")
            print('Sus datos han sido guardados correctamente.')
    
def cargar_datos(): 
        try:
            with open('productos.txt', 'r') as txt_file:
                for item in txt_file:
                    if not item:
                        continue
                    try:
                        nombre, costo, cantidad = item.split(',')
                        producto_dict = {
                            'nombre': nombre.strip(),
                            'costo': float(costo.strip()),
                            'cantidad': int(cantidad.strip())
                        }
                        productos.append(producto_dict)
                    except ValueError:
                        print('El formato es incorrecto.')
            print('Los datos han sido cargados correctamente.')
        except FileNotFoundError:
            print('No existen datos para cargar.')

def menu():
    cargar_datos()
    while True:
        print("1. Añadir producto")
        print("2. Ver productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Guardar datos")
        print("6. Salir")
        
        opcion = input('Bienvenido. Seleccione una opción: ')
        
        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
        elif opcion == '6':
            print('Hasta la próxima.')
            break
        else:
            print('Por favor, selecciona una opción válida')
            
menu()
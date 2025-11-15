#TRABAJO PRÁCTICO N°8 - MANEJO DE ARCHIVOS

# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

# Crear archivo productos.txt con 3 productos iniciales
with open('productos.txt', 'w') as archivo:
    archivo.write("Manzanas,1500,50\n")
    archivo.write("Bananas,1200,30\n")
    archivo.write("Naranjas,1800,40\n")

print("Archivo productos.txt creado exitosamente")


#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea, 
#la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:
#Producto: Lapicera | Precio: $120.5 | Cantidad: 30

with open('productos.txt', 'r') as archivo:
    print("=== LISTA DE PRODUCTOS ===\n")
    for linea in archivo:
        linea = linea.strip()  # Elimina espacios y saltos de línea
        datos = linea.split(",")  
    
        nombre = datos[0]
        precio = datos[1]
        cantidad = datos[2]
        
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar los productos,
# le pida al usuario que ingrese un nuevo producto (nombre, precio, cantidad) y lo agregue al 
# archivo sin borrar el contenido existente.

#productos existentes
with open('productos.txt', 'r') as archivo:
    print("=== LISTA DE PRODUCTOS ===\n")
    for linea in archivo:
        datos = linea.strip().split(",")
        print(f"Producto: {datos[0]} | Precio: ${datos[1]} | Cantidad: {datos[2]}")

#nuevo producto 
print("\n=== AGREGAR NUEVO PRODUCTO ===")
nombre = input("Ingrese el nombre del producto: ")
precio = input("Ingrese el precio: ")
cantidad = input("Ingrese la cantidad: ")

#agrega al archivo (sin borrar lo que ya existe)
with open('productos.txt', 'a') as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")

print(f"\n✓ Producto '{nombre}' agregado exitosamente")

#lista actualizada
print("\n=== LISTA ACTUALIZADA ===\n")
with open('productos.txt', 'r') as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        print(f"Producto: {datos[0]} | Precio: ${datos[1]} | Cantidad: {datos[2]}")

#4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en una 
#lista llamada productos, donde cada elemento sea un diccionario con claves: 
#nombre, precio, cantidad.

productos = []

with open('productos.txt', 'r') as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        
        #diccionario para cada producto
        producto = {
            'nombre': datos[0],
            'precio': float(datos[1]),
            'cantidad': int(datos[2])
        }
        
        #agregar a la lista
        productos.append(producto)

#productos cargados
print("=== PRODUCTOS CARGADOS ===\n")
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

print(f"\nTotal de productos: {len(productos)}")

# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto. 
# Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si no existe, 
# mostrar un mensaje de error.

productos = []

with open('productos.txt', 'r') as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        producto = {
            'nombre': datos[0],
            'precio': float(datos[1]),
            'cantidad': int(datos[2])
        }
        productos.append(producto)

#producto por nombre
print("=== BUSCAR PRODUCTO ===")
nombre_buscar = input("Ingrese el nombre del producto a buscar: ")

#variable para saber si lo encontramos
encontrado = False

for p in productos:
    if p['nombre'].lower() == nombre_buscar.lower():
        print("\n✓ Producto encontrado:")
        print(f"Nombre: {p['nombre']}")
        print(f"Precio: ${p['precio']}")
        print(f"Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print(f"\n✗ Error: El producto '{nombre_buscar}' no existe")

#6. Guardar los productos actualizados: Después de haber leído, buscado o agregado productos, 
#sobrescribir el archivo productos.txt escribiendo nuevamente todos los productos actualizados 
#desde la lista.

productos = []

with open('productos.txt', 'r') as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        producto = {
            'nombre': datos[0],
            'precio': float(datos[1]),
            'cantidad': int(datos[2])
        }
        productos.append(producto)

print("=== PRODUCTOS ACTUALES ===")
for p in productos:
    print(f"{p['nombre']} - ${p['precio']} - {p['cantidad']} unidades")

#agregar producto
print("\n=== AGREGAR PRODUCTO ===")
nombre = input("Nombre: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))

#agregar a la lista
nuevo_producto = {
    'nombre': nombre,
    'precio': precio,
    'cantidad': cantidad
}
productos.append(nuevo_producto)

#guardar lista actualizada en el archivo
with open('productos.txt', 'w') as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("\n✓ Archivo actualizado correctamente")

print("\n=== PRODUCTOS ACTUALIZADOS ===")
for p in productos:
    print(f"{p['nombre']} - ${p['precio']} - {p['cantidad']} unidades")
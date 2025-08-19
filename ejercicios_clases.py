#Ejercicio: Crea una clase ListaDeTareas que permita agregar tareas y listar todas las tareas pendientes. Debe comenzar con una lista 
#vacía.
class ListaDeTareas:
    def __init__(self, tareas):
        self.tareas = tareas

    def agregar_tareas(self, tarea):
        self.tareas.append(tarea)

    def tarea_realizada(self, tarea):
        for t in self.tareas:
            if tarea == t:
                self.tareas.remove(tarea)
                return 'Tarea completada y removida de la lista'
        return 'Tarea no encontrada'

    def listar_pendientes(self):
        for i in self.tareas:
            print(i)

lista = ListaDeTareas([]) #el atributo tareas debe ser una lista, en este caso, vacia
lista.agregar_tareas('Cortar el Pasto')
lista.agregar_tareas('Podar los arboles')
lista.agregar_tareas('Limpiar el parrillero')
lista.agregar_tareas('limpiar el auto')
lista.listar_pendientes()
print(lista.tarea_realizada('Cortar el Pasto'))
lista.listar_pendientes()

#Ejercicio: crea una clase CarritoDeCompra que cuente con un metodo para agregar productos con su respectivo precio y otro metodo que
#devuelva el valor total de la compra.
class CarritoDeCompra:
    def __init__(self, productos, precios):
        self.productos = productos
        self.precios = precios

    def agregar_productos(self, producto, precio):
        self.productos.append(producto)
        self.precios.append(precio)
    
    def total_compra(self):
        return (f'El total de su compra es: {sum(self.precios)}$')
    
compra = CarritoDeCompra([], [])
compra.agregar_productos('huevos', 265)
compra.agregar_productos('carne', 455)
compra.agregar_productos('refresco', 72)
compra.agregar_productos('leche', 96)
compra.agregar_productos('shampoo', 1237)

#Ejercicio: crea una clase CuentaBancaria que permita depositar y retirar saldo, impidiendole al usuario retirar mas dinero del que
#tiene en su cuenta.
class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        while cantidad > self.saldo:
            print('La cantidad a retirar es superior a su saldo.')
            cantidad = float(input('Ingrese la cantidad a retirar: '))
        self.saldo -= cantidad
        print('Dinero retirado exitosamente')

miCuenta = CuentaBancaria(2534)

#Ejercicio: crea una clase Empresa con un atributo empleados que sera un diccionario. La misma debe contener metodos para agregar
#empleados, obtener el nombre de un empleado, eliminar un empleado y listar todos los empleados. Cada empleado debe ser identificado
#con un id.
class Empresa:
    def __init__(self, empleados): #el atributo empleados debe ser un diccionario
        self.empleados = empleados

    def agregar_empleados(self, id, nombre): #el metodo recibe un id y un nombre
        self.empleados[id] = nombre #se agrega al diccionario el id como clave y el nombre como valor

    def obtener_nombre(self, id):
        for i in self.empleados.keys(): #se itera en las claves del diccionario (id)
            if i == id: #si una clave coincide con el valor introducido
                print(f'Nombre del empleado: {self.empleados[i]}') #se muestra el valor asociado a la clave

    def eliminar_empleados(self, id):
        self.empleados.pop(id) #se elimina la clave si existe en el diccionario
        print('Empleado eliminado correctamente')

    def listar_empleados(self):
        for i, n in self.empleados.items(): #dos variables de iteracion, una para las claves y otra para los valores
            print(f'Identificador del empleado: {i}, Nombre del empleado: {n}')

fabrica = Empresa({})
fabrica.agregar_empleados(205, 'Julian')
fabrica.agregar_empleados(207, 'Damian')
fabrica.agregar_empleados(209, 'Jhonathan')
fabrica.agregar_empleados(211, 'Esteban')
fabrica.listar_empleados()
fabrica.obtener_nombre(205)
fabrica.eliminar_empleados(205)
fabrica.obtener_nombre(205) #no devuelve nada, el empleado fue eliminado
fabrica.listar_empleados()

#Ejercicio Parte 1: crea una clase Juguete con los atributos nombre, precio y partes (estos ultimos almacenados en un set). Debe incluir
#un metodo que devuelva un booleano determinando si el juguete es costoso, es decir, si su precio es mayor a 1000. Y un metodo que
#devuelva otro booleano determinando si el juguete es electronico o no; un objeto es electronico si su set de partes incluye 'bateria'.
class Juguete:
    def __init__(self, nombre, precio, partes): #las partes deben almacenarse en un set
        self.nombre = nombre
        self.precio = precio
        self.partes = partes

    def es_costoso(self):
        return self.precio > 1000
    
    def es_electronico(self):
        return 'bateria' in list(self.partes)

#Parte 2: crea la clase Tienda que almacene una lista o diccionario de objetos juguetes y cuente con un metodo para agregar un juguete
#al inventario y otro metodo que devuelva una lista con los nombres de los juguetes que no sean costosos.
#Forma 1:
class TiendaDeJuguetes:
    def __init__(self):
        self.inventario = {} #el inventario sera un diccionario, donde el nombre del juguete es la clave y su precio como valor.

    def agregar_juguete(self, juguete): #el objeto juguete
        self.inventario[juguete.nombre] = juguete.precio
#se toma el nombre del objeto juguete para asignarlo como clave y su precio como valor
    def catalogo_oferta(self):
        baratos = [] #lista que almacenara los juguetes que son baratos
        for n, p in self.inventario.items():
            if p < 1000: #si el precio de un producto es menor a 1000
                baratos.append(n) #se agrega su nombre a la lista baratos
        return baratos

mi_tienda = TiendaDeJuguetes()
auto = Juguete('Cars', 850, {'bateria', 'ruedas', 'control'})
arma = Juguete('arma_Nerf', 2600, {'proyectiles', 'objetivos', 'repuestos'})
muñeco = Juguete('soldado', 487, {'bateria', 'auto', 'repuestos'})
mi_tienda.agregar_juguete(auto)
mi_tienda.agregar_juguete(arma)
mi_tienda.agregar_juguete(muñeco)
print(mi_tienda.inventario)
print(mi_tienda.catalogo_oferta())

#Forma 2
class Tienda:
    def __init__(self):
        self.inventario = []

    def agregar_juguete(self, juguete): #el objeto juguete
        self.inventario.append(juguete) #se agregan las instancias de juguete a la lista

    def catalogo_oferta(self):
        juguetes_oferta = []
        for j in self.inventario:
            if not j.es_costoso(): #a cada objeto de la lista se le envia el mensaje es_costoso(); si un objeto no es costoso el mensaje
                #devolvera False, por eso se antepone not al mensaje para que el booleano pase a True y lo agregue a la lista.
                juguetes_oferta.append(j.nombre)
        return juguetes_oferta #se devuelve una lista con el nombre de los juguetes menos costosos

jugueteria = Tienda()
jugueteria.agregar_juguete(auto)
jugueteria.agregar_juguete(arma)
jugueteria.agregar_juguete(muñeco)
print(jugueteria.catalogo_oferta())

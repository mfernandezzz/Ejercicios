#crea una funcion para contar cuantos numeros de una lista son positivos y mostrar en pantalla la cantidad.
lista = [3.2, -4, 5, -8, 9, 16, -2, -79]
def contar_Positivos(lista):
    return len([e for e in lista if e > 0])
print(contar_Positivos(lista))

#crea una funcion que cuente cuantos elementos de una lista son pares
numeros = [3, 4, 7, 8, 15, 90, 43, 80, 33, 32]
def contar_Pares(lista):
    return len([i for i in lista if i % 2 == 0])
print(contar_Pares(numeros))

#crea una funcion que sume los numeros pares de una lista y devuelva su suma
numeros2 = [6, 9, 14, 16, 30, 45, 86, 40, 17, 19]
def suma_Pares(lista):
    return sum([i for i in lista if i % 2 == 0])
print(suma_Pares(numeros2))

#crea una funcion que reciba dos listas y que sume solamente los valores de la lista elementos cuya posicion este en la lista 
#posiciones.
elementos, posiciones = [10, 22, 34, 46, 58], [1, 3, 4]
def sumar_elementos(elementos, posiciones):
    suma_total = 0
    for e in posiciones:
        suma_total += elementos[e]
    return suma_total
print(sumar_elementos(elementos, posiciones))

#crear una funcion que reciba una lista y que sume solamente los valores de la lista que se encuentren en posiciones pares y que 
#devuelva su suma.
valores = [14, 22, 38, 46, 51, 60, 79, 88, 92, 101]
def suma_pos_pares(valores):
    return sum([valores[i] for i in range(0, len(valores), 2)])
print(suma_pos_pares(valores))
#solucion 2
def pos_pares(valores):
    suma_de_pares = 0
    for i in range(0, len(valores), 2):
        suma_de_pares += valores[i]
    return suma_de_pares
print(pos_pares(valores))

#crea una funcion que reciba dos numeros enteros como parametros para despues devolver una lista con el conteo de los numeros 
#introducidos, sin contar el ultimo. Se deben contemplar los conteos regresivos.
primero, segundo = int(input('Ingrese un numero: ')), int(input('Ingrese otro numero: '))
def conteo(primero, segundo):
    while primero < segundo:
        conteo = list(range(primero, segundo))
        return conteo
    conteo = list(range(primero - 1, segundo - 1, -1))
    return conteo
print(conteo(primero, segundo))

#crea una funcion que reciba tres listas como parametros y que devuelva la lista con la mayor cantidad de elementos.
lista, lista2, lista3 = [1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17, 18, 19, 20]
def largo_maximo(lista, lista2, lista3):
    return max(lista, lista2, lista3) #devuelve la lista con mas elementos
print(largo_maximo(lista, lista2, lista3))
def largo_maximo2(lista, lista2, lista3):
    maximo = max(len(lista), len(lista2), len(lista3))
    return maximo #devuelve la cantidad de elementos que tiene la lista mas grande
print(largo_maximo2(lista, lista2, lista3))

#crea una funcion que reciba como parametro una lista y que decuelva una lista con los primeros tres elementos de la misma.
decimales = [2.2, 3.5, 6.7, 9.1, 7.3, 4.2, 5.8, 8.6]
def primeros_tres(decimales):
    return decimales[:3]
print(primeros_tres(decimales))
#crea una funcion que reciba como parametro una lista y que devuelva la misma pero con los dos ultimos elementos.
def ultimosDos(decimales):
    return decimales[-2:]
print(ultimosDos(decimales))

#crea una funcion que reciba como parametro una lista y que devuelva una lista con los valores invertidos y un diez al final.
lista = [11, 12, 13, 14, 15]
def invertir_lista(lista):
    lista_inv = lista[ : : -1]
    lista_inv.append(10)
    return lista_inv
print(invertir_lista(lista))

#crea una funcion que reciba una lista como parametro y que devuelva la cantidad de ceros de dicha lista.
lista_ceros = [2, 0, 4, 0, 6, 0, 8, 0, 10, 0, 12, 0, 14, 16, 0, 18, 0, 20]
def contar_ceros(lista):
    return lista.count(0)
print(contar_ceros(lista_ceros))

#crea una funcion que reciba como parametro una lista y que devuelva una lista cuyos valores sean iguales al valor de sus 
#elementos mas el indice de los mismos. Ejemplo lista_entrada = [7, 8, 2, 5, 3]  lista_salida = [7, 9, 4, 8, 7]
#solucion 1
numericos = [3, 8, 6, 1, 7, 4] #[3, 9, 8, 4, 11, 9]
def valor_mas_indice(numericos):
    num_mas_index = [] #creamos la nueva lista donde se almacenaran los nuevos valores
    for i in range(len(numericos)): 
        num_mas_index.append(numericos[i] + i)#a la nueva lista le agregamos los valores de la lista anterior mas el valor de su posicion(indice)
    return num_mas_index 
print(valor_mas_indice(numericos))
#solucion 2
numericos2 = [5, 2, 7, 11, 3, 14]
def valor_mas_indice2(numericos2):
    for i in range(len(numericos2)):
        numericos2[i] = numericos2[i] + i 
#modificamos la lista original, para que almacene la suma de los valores originales mas su valor posicional(index)
    return numericos2
print(valor_mas_indice2(numericos2))

#crea una funcion que reciba como parametro una lista y que devuelva la suma de los indices cuyos valores son iguales a 0. 
numericos = [4, 0, 5, 11, 0, 7, 31, 64, 0] #13
def suma_indices0(numericos):
    suma = 0 # variable suma donde se almacenara la suma de los indices
    for i in range(len(numericos)):
        if numericos[i] == 0: # la condicion para que se sumen los indices de los valores 0 de la lista.
            suma += i #se suman los valores de indices obtenidos
    return suma
print(suma_indices0(numericos))

#crea una funcion que reciba como parametro una lista y devuelva la suma de los valores mayores a 10 y cuyos indices sean impares.
numeros = [6, 12, 2, 14, 8, 52, 22, 9, 16, 1]
def suma_rara(lista):
    return sum([lista[i] for i in range(1, len(lista), 2) if lista[i] > 10])
print(suma_rara(numeros))

#crea una funcion que reciba como parametro un string y que si el largo del mismo es menor a diez, le agregue el caracter x al 
#final tantas veces como sea necesario hasta que el largo del string sea diez.
string = (input('Escriba una palabra menor a diez letras: '))
def padding_derecha(string):
    return string.ljust(10,"X") #la funcion ljust recibe una cantidad y el string con el que se va a rellenar la cantidad previamente dada.
print(padding_derecha(string))
#Solucion 2
def padding_derecha2(string):
    while len(string) < 10:
        string += 'X'
    return string
#crea una funcion padding izquierda que haga lo mismo que el ejercicio anterior, pero con las x al principio.
def pad_izq(string):
    return string.rjust(10, 'X') #funcion rjust (justificado a la derecha) igual a ljust pero al reves.
print(pad_izq(string))
#Solucion2
def padding_izquierda(string):
    while len(string) < 10:
        string = 'X' + string
    return string

#crea una funcion que se llame pad_and_invert que reciba como parametro una lista y si el largo de la misma es menor a
#10, le agregue los ceros necesarios y despues la invierta. Si el largo de la lista es mayor a diez, "truncarla" para que
#solo tenga diez elementos y los invierta.
lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
def pad_and_invert(lista_num):
    while len(lista_num) < 10:
        lista_num.append(0)
    lista_num = lista_num[ :10] #se trunca la lista a maximo 10 elementos
    lista_num = lista_num[ : :-1] #invertir la lista
    return lista_num
print(pad_and_invert(lista_num))

#crea una funcion que reciba un parametro tipo lista y devuelva el menor valor de la lista sin tener en cuenta el primer y ultimo 
#valor.
numeros = [-40, 3, 2, 18, 1]
def menor_sin_extremos(numeros):
    return min(numeros[1:-1])
print(menor_sin_extremos(numeros))

#crear una funcion que reciba como parametro una lista con solo dos elementos y los intercambie de posicion.
dos_elementos = [2, 4]
def intercambiar(dos_elementos):
    return dos_elementos[: :-1] #cuando el tercer valor del rango esta en -1, se cuenta a partir del ultimo elemento.
print(intercambiar(dos_elementos))

#crea una funcion que reciba como parametro una lista y devuelva una lista igual a la recibida pero con el primer valor 
#intercambiado por el ultimo.
inter = [1, 2, 3, 4, 5]
def intercambiar_primero_ultimo(inter):
    p, u = inter[0], inter[-1]
    inter[0] = u
    inter[-1] = p
    return inter
print(intercambiar_primero_ultimo(inter))

#crea una funcion que reciba tres parametros, una lista y dos indices. Debe devolver una lista igual a la recibida pero con 
#el valor de los indices intercambiados. Ejemplo input lista = [40, 2, 3, 4, 5, 1], a=1 b=4 [40, 5, 3, 4, 2, 1]
lista_num = [65, 77, 84, 23, 91, 47, 22]
def intercambiar(lista_num, a, b):
    c, d = lista_num[a], lista_num[b]#se almacena en variables los elementos en base a los indices
    lista_num[a], lista_num[b] = d, c#intercambio los valores en la lista
    return lista_num
print(intercambiar(lista_num, 1, 5))

#crear una funcion que reciba como parametros dos listas donde una de ellas seran los indices. Despues devolver la suma 
#de los elementos de la lista indicados por su indice. 
listaCinco, indices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [4, 6, 9]
def suma_rara2(lista, indices):
    return sum([lista[i] for i in indices])
print(suma_rara2(listaCinco, indices))

#crea una funcion que reciba como parametro una lista y que devuelva la misma lista pero que cada elemento a partir del indice 
#dos sea igual a la suma de los dos anteriores.
serie = [2, 5, 6, 19, 10, 22]
def suma_dos_anteriores(serie):
    for i in range(2, len(serie)): #se itera en la lista serie a partir de la posicion 2 hasta el ultimo elemnto de la lista.
        serie[i] = serie[i-2] + serie[i-1] #a partir de la posicion dos, se asigna un nuevo valor(sustituye al almacenado)que sera la suma de los dos anteriores.
    return serie 
print(suma_dos_anteriores(serie))

#crea una funcion que reciba dos parametros de tipo lista y devuelva una lista de igual tamaño donde cada elemento sea igual 
#a la suma de los elementos de las dos listas que estan en la misma posicion.
lista_par, lista_impar = [2, 4, 5, 8, 10, 12], [1, 3, 5, 7, 9, 11] #[3, 7, 10, 15, 19, 23]
def sumar_listas(lista_par, lista_impar):
    lista_suma = [0] * len(lista_par) #se crea la lista y se le asigna la cantidad de elementos a almacenar.
    for i in range(len(lista_par)):
        lista_suma[i] = lista_par[i] + lista_impar[i]#la nueva lista almacena la suma de los elementos de lista_par y lista_impar cuya posicion sea la misma.
    return lista_suma
print(sumar_listas(lista_par, lista_impar))
#solucion 2
def sumarListas(par, impar):
    sumada = []
    for i in range(len(par)):
        for j in range(len(impar)):
            if i == j:
                sumada.append(par[i] + impar[j])
    return sumada
print(sumarListas(lista_par, lista_impar))

#crea una funcion que reciba tres parametros, lista, indices y lista2. Dicha funcion debe devolver una lista de igual tamaño 
#donde cada elemento sea igual a la suma de los valores de la primera lista mas los de la segunda lista dados por las posiciones 
#indicadas en el parametro indices. 
lista, indices, lista2 = [5, 6, 9, 1], [3, 1, 2, 0], [8, 4, 7, 2] #[7, 10, 16, 9]
def sumar_listas_dos(lista, indices, lista2):
    s = []
    for i in range(len(indices)):
        s.append(lista[i] + lista2[indices[i]])#se toma el elemento de lista2 en base a su valor posicional determinado por la lista indices
    return s
print(sumar_listas_dos(lista, indices, lista2))

#crea una funcion que reciba una lista como parametro y devuelva una lista que contenga solo los elementos pares de dicha lista.
par_impar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 22, 15]
def dev_pares(lista):
    return [p for p in lista if p % 2 == 0]
print(dev_pares(par_impar))

#crear una funcion que reciba un parametro de tipo lista y devuelva la suma de las diferencias entre los numeros contiguos de la lista.
numeros = [2, 5, 7, 12, 10, 15, 25, 17]
def suma_diferencias(numeros):
    sum_diferencia = 0#variable que almacenara la suma de las diferencias entre numeros contiguos.
    for i in range(1, len(numeros)):
        sum_diferencia += numeros[i] - numeros[i-1]#el elemento almacenado por la variable de iteracion menos el elemento almacenado en el valor posicional anterior.
    return sum_diferencia
#las diferencias entre los elementos pueden ser numeros negativos o positivos.
print(suma_diferencias(numeros))
#solucion 2
def sumaDiferencias(numeros):
    diferencias = []
    for i in range(1, len(numeros)):
        diferencias.append(numeros[i] - numeros[i - 1])
    return sum(diferencias)
print(sumaDiferencias(numeros))

#crea una funcion que reciba un parametro tipo lista y devuelva una lista que contenga los indices de los valores 
#que sean menores a 0.
lista_num = [-2, 5, 11, -4, -8, 55, -77, 32, -57, -63] #[0, 3, 4, 6, 8, 9]
def obtener_indices(lista):
    return [i for i in range(len(lista)) if lista[i] < 0]
print(obtener_indices(lista_num))

#crea una funcion que reciba dos parametros de tipo lista y devuelva una lista solo con los valores de la lista original sin los que 
#se encuentren en la lista errores.
lista, errores = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [2, 6, 10, 14, 18]
def eliminar_errores(lista, errores):
    return [i for i in lista if i not in errores]
print(eliminar_errores(lista, errores))
#solucion 2
def eliminarErrores3(lista, errores):
    listaC, erroresC = set(lista), set(errores)
    return list(listaC.difference(erroresC))
print(eliminarErrores3(lista, errores))

#crea una funcion que reciba dos listas con la misma cantidad de elementos como parametros y devuelva una nueva lista con los 
#elementos de las dos listas intercalados.
letras = ['a', 'b', 'c', 'd', 'e']
numeros = [1, 2, 3, 4, 5]
def intercalada(letras, numeros):
    inter = []
    for i in range(len(letras)):
        inter.append(letras[i])
        inter.append(numeros[i])
    return inter
print(intercalada(letras, numeros))

#crea una funcion que reciba dos listas como parametros y devuelva la concatenacion de las mismas.
comidas = ['Hamburguesa', 'Pizza', 'Chivito', 'Milanesa', 'Sandwich']
bebidas = ['Vino', 'Cerveza', 'Licor', 'Refresco', 'Agua']
def concatenar_listas(comidas, bebidas):
    menu = []
    menu.extend(comidas)#con extend se une el contenido de una lista a otra lista.
    menu.extend(bebidas)
    return menu
print(concatenar_listas(comidas, bebidas))
#solucion 2
def concatenar_listas2(comidas, bebidas):
    alimentos = []
    for i in range(len(comidas)):
        alimentos.append(comidas[i])
        alimentos.append(bebidas[i])
    return alimentos#se devuelve una lista con los elementos de las dos listas anteriores intercalados. 
#Solo funciona si ambas listas tienen igual cantidad de elementos.
print(concatenar_listas2(comidas, bebidas))
#solucion 3
def conc_listas(comidas, bebidas):
    return comidas + bebidas
print(conc_listas(comidas, bebidas))

#crea una funcion que reciba como parametro dos listas y devuelva un booleano dependiendo de si la primer lista contiene 
#al menos un valor de la lista dos.
lista1, lista2 = ['a', 'k', 'b'], ['o', 'q']
def esta_en_lista(lista1, lista2):
    for i in range(len(lista1)):
        if lista1[i] in lista2:
            return True
    return False
print(esta_en_lista(lista1, lista2))

#Diseñar un programa que muestre el producto de los 10 primeros numeros impares.
secuencia = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
def obtenerImpares(lista):
    impares = [i for i in lista if i % 2 != 0]
    return impares[:10]
print(obtenerImpares(secuencia)) #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
def obtenerProducto(lista):
    producto = 1
    for i in lista:
        producto *= i
    return producto
print(obtenerProducto(obtenerImpares(secuencia))) #654.729.075

#Pedir 10 numeros. Mostrar la media de los numeros positivos, la media de los numeros negativos y la cantidad de ceros.
def pedirNumeros(): #[0, 2, -8, 0, 7, -5, 0, 12, -15, 4] media positivos: 6 media negativos: -9 cant ceros: 3
    numeros = []
    while len(numeros) < 10:
        numero = int(input('Ingrese un numero entero, puede ser positivo. negativo o cero: '))
        numeros.append(numero)
    return numeros
def obtenerDatos(lista):
    postivos = [i for i in lista if i > 0]
    negativos = [i for i in lista if i < 0]
    ceros = [i for i in lista if i == 0]
    return (f'Promedio de positivos: {sum(postivos)/len(postivos)} Promedio negativos: {sum(negativos)/len(negativos)} Ceros: {len(ceros)}')
print(obtenerDatos(pedirNumeros()))
#Para que el codigo funcione, se debe incluir al menos un numero de cada uno (positivo, negativo y cero).

#Crear una funcion que determine si un puntaje de la lista es mayor al record
ranking1 = [30, 25, 34, 32, 28]
ranking2 = [25, 33, 60]
def esRecord(ranking):
    record, supero = 35, False
    for i in ranking:
        if i > record:
            supero = True
    return supero
print(esRecord(ranking2))

#Contar cuántas veces aparece un número específico en una lista
#Crear una función que reciba una lista de números y un número específico. La función debe contar cuántas veces aparece ese número 
#en la lista.
numerosEnteros, num = [32, 55, 21, 32, 88, 164, 32, 49, 190, 32], 32
def contarAparicion(lista, numero):
    conteo = 0
    for i in lista:
        if i == numero:
            conteo += 1
    return (f'El numero {numero} aparece {conteo} veces')
print(contarAparicion(numerosEnteros, num))

def contarAparicion2(lista, numero):
    return (f'El numero {numero} aparece {lista.count(numero)} veces.')
print(contarAparicion2(numerosEnteros, num))

#Escribe una función que cuente cuántos números pares hay en un rango dado por el usuario
numRango = int(input('Indique un rango: '))
def contarPares(rango):
    return (f'La cantidad de numeros pares en el rango dado es de: {len([i for i in range(2, rango + 1) if i % 2 == 0])}')
print(contarPares(numRango))

#Crea una funcion que le pida al usuario un numero y muestre el conteo hasta dicho numero dentro de una lista.
numero = int(input('Ingrese la cantidad de numeros para generar un conteo: '))
def imprimirConteo(numero):
    return [i for i in range(1, numero + 1)]
print(imprimirConteo(numero))

#Ejercicio: crear lista de colores. Crear una lista de colores para agregar elementos a una lista vacia.
colores = []
def agregar_colores(lista):
    agregar = True
    while agregar:
        color = str.lower(input('Color a agregar a la lista: '))
        lista.append(color)
        opcion = str.lower(input('¿Deseas seguir agregando colores a la lista? si/no: '))
        if opcion == 'si':
            agregar = True
        else:
            agregar = False
    return lista
#print(agregar_colores(colores))

#Ejercicio: crear una lista de juguetes y una funcion que agregue elementos a la misma.
juguetes = []
def agregar_juguetes(lista):
    cantidad = int(input('Ingrese la cantidad de juguetes que quiere añadir a la lista: '))
    while len(lista) < cantidad:
        juguete = str.lower(input('Nombre del juguete a ingresar a la lista: '))
        lista.append(juguete)
    return lista
#print(agregar_juguetes(juguetes))

#Ejercicio: crear una funcion que agregue numeros a una lista hasta que el usuario escriba fin. Mostrar el mayor numero ingresado.
numeros = [] #99 124 5 44 36.7 75
def agregar_numeros(lista):
    agregar = True
    while agregar:
        num = float(input('Ingrese un numero a agregar a la lista: '))
        lista.append(num)
        opcion = str.lower(input('Desea seguir agregando numeros a la lista: si/fin '))
        if opcion == 'fin':
            agregar = False
    return (f'El numero mas alto ingresado es: {max(lista)}')
#print(agregar_numeros(numeros))

#Ejercicio: crear un programa que le permita a un docente ingresar todas las calificaciones de un grupo de estudiantes, una por una.
#Cuando termine de ingresar las calificaciones, el programa debe mostrar: cantidad de calificaciones ingresadas, promedio general del
#grupo, nota maxima y minima ingresada. El ingreso termina cuando se ingresa la palabra fin.
calificaciones = [] #12 10 8 13 8 7 4
def gestionar_notas(lista):
    agregar = True
    while agregar:
        nota = int(input('Ingrese una nota: '))
        if nota > 0 and nota <= 12:
            lista.append(nota)
        else:
            print('La nota ingresada es incorrecta.')
        opcion = str.lower(input('¿Seguir agregando notas a la lista? si/fin '))
        if opcion == 'fin':
            agregar = False
    return (f'Cantidad de calificaciones ingresadas: {len(lista)}. Promedio del grupo: {round(sum(lista) / len(lista), 2)}. Nota minima ingresada: {min(lista)}. Nota maxima ingresada: {max(lista)}')
#print(gestionar_notas(calificaciones))

#Ejercicio: crear un programa que le permita a una persona gestionar una lista de peliculas favoritas. El programa debe crear una lista
#llamada peliculas, agregar titulos de peliculas hasta que el usuario ingrese 'fin', mostrar cuantas peliculas existen, consultar al
#usuario si desea eliminar una pelicula y mostrar un mensaje indicando si la pelicula fue eliminada o no fue encontrada.
def agregar_pelicula(lista, pelicula):
    lista.append(pelicula)
    print(f'La pelicula {pelicula} ha sido añadida a la lista.')

def cantidad_peliculas(lista):
    print(f'Cantidad de peliculas en la lista: {len(lista)}')

def eliminar_pelicula(lista, pelicula):
    if pelicula in lista:
        lista.remove(pelicula)
        print(f'La pelicula {pelicula} ha sido removida de la lista')
    else:
        print(f'La pelicula {pelicula} no fue encontrada en la lista.')

def main():
    peliculas = []
    while True:
        print('Gestionador basico de peliculas')
        print('Opciones:')
        print('1. Agregar una pelicula a la lista')
        print('2. Mostrar la cantidad de peliculas guardadas')
        print('3. Eliminar una pelicula de la lista')
        print('Ingrese la palabra fin para cerrar el Gestionador basico de peliculas')
        opcion = input('Ingrese la opcion: ')
        if opcion == '1':
            pelicula = str.lower(input('Ingrese el titulo de la pelicula: '))
            agregar_pelicula(peliculas, pelicula)
        elif opcion == '2':
            cantidad_peliculas(peliculas)
        elif opcion == '3':
            pelicula = str.lower(input('Ingrese el titulo de una pelicula a eliminar: '))
            eliminar_pelicula(peliculas, pelicula)
        elif opcion == 'fin':
            break
        else:
            print('Opcion no encontrada.')
    return 'Saliendo del Gestor'

#print(main())

#Ejercicio: Crea un programa que cree una lista llamada deportes, imprmir el primer y ultimo deporte de la lista usando indices.
#Pedir al usuario que escriba el nombre de un deporte, si ya esta en la lista, mostrar su posicion; si no esta dicho
#deporte, agregarlo a la lista y mostrar la misma actualizada.
deportes = ['tenis', 'futbol', 'basquetbol', 'voleybol', 'handball']
def variada(lista):
    print(f'Primer elemento de la lista: {lista[0]}')
    print(f'Ultimo elemento de la lista: {lista[-1]}')
    consulta = str.lower(input('Ingrese el nombre de un deporte para verificar si esta en la lista: '))
    if consulta in lista:
        print(f'El deporte {consulta} se encuentra en la lista y su posicion es: {lista.index(consulta)}')
    else:
        print(f'El deporte {consulta} no se encuentra en la lista, por lo que sera agregado.')
        lista.append(consulta)
    return (f'La lista de deportes actualizada es: {lista}') 
print(variada(deportes))

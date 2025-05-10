#crea una funcion para contar cuantos numeros de una lista son positivos y mostrar en pantalla la cantidad.
def contar_positivos(lista):
    contador = 0
    for e in lista: 
        if e > 0: #lista[e]
            contador += 1
    return contador
lista = [3.2, -4, 5, -8, 9, 16, -2, -79]
print(contar_positivos(lista))

#crea una funcion que cuente cuantos elementos de una lista son pares
numeros = [3, 4, 7, 8, 15, 90, 43, 80, 33, 32]
def contar_pares(numeros):
    contador = 0
    for i in numeros:
        if i % 2 == 0: #numeros[i]
            contador += 1
    return contador
print(contar_pares(numeros))

#crea una funcion que sume los numeros pares de una lista y devuelva su suma
numeros = [3, 4, 7, 8, 15, 90, 43, 80, 33, 32]
def sumaPares(numeros):
    s = 0
    for i in numeros:
        if i % 2 == 0:
            s += i
    return s
print(sumaPares(numeros))

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
def pos_pares(valores):
    suma_de_pares = 0
    for i in range(0, len(valores), 2):
        suma_de_pares += valores[i]
    return suma_de_pares
print(pos_pares(valores))
#solucion 2
def posPares(valores):
    pares = []
    for i in range(0, len(valores), 2):
        pares.append(valores[i])
    return sum(pares)
print(posPares(valores))

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

#crea una funcion valor mas indice que reciba como parametro una lista y que devuelva una lista cuyos valores sean
#iguales al valor de sus elementos mas el indice de los mismos.
#ejemplo lista_entrada = [7, 8, 2, 5, 3]  lista_salida = [7, 9, 4, 8, 7]
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
def sumaRara(numeros):
    rara = 0
    for i in range(1, len(numeros), 2):#aqui se determina que se iterara solo en las posiciones impares
        if numeros[i] > 10:
            rara += numeros[i]
    return rara
print(sumaRara(numeros))

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
def sumaSeleccionados(listaCinco, indices):
    s = 0
    for i in indices:
        s += listaCinco[i]
    return s
print(sumaSeleccionados(listaCinco, indices))
#solucion 2
def sumaXindices2(listaCinco, indices):
    suma = [listaCinco[i] for i in indices]
    return sum(suma)

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
def pares(par_impar):
    p = []
    for i in par_impar:
        if i % 2 == 0:
            p.append(i)
    return p
print(pares(par_impar))

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
def obtener_indices(lista_num):
    indices = []
    for i in range(len(lista_num)):#se itera entre todos los elementos de la lista
        if lista_num[i] < 0:#si el elemento almacenado por la variable de iteracion es menor a 0
            indices.append(i)#se le agrega a la lista indices el valor posicional(indice) de dicho elemento
    return indices
print(obtener_indices(lista_num))

#crea una funcion llamada eliminar_errores que reciba dos parametros de tipo lista y devuelva una
#lista solo con los valores de la lista original sin los que se encuentren en la lista errores.
lista, errores = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [2, 6, 10, 14, 18]
def eliminarErrores(lista, errores):
    for i in lista:
        for j in errores:
            if j == i:
                lista.remove(j)
    return lista
print(eliminarErrores(lista, errores))
#solucion 2
def eliminarErrores2(lista, errores):
    salida = []
    for i in lista:
        if i not in errores:
            salida.append(i)
    return salida
print(eliminarErrores2(lista, errores))
#solucion 3
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
def concatenar_listas(comidas, bebidas):
    alimentos = []
    for i in range(len(comidas)):
        alimentos.append(comidas[i])
        alimentos.append(bebidas[i])
    return alimentos#se devuelve una lista con los elementos de las dos listas anteriores intercalados. 
#Solo funciona si ambas listas tienen igual cantidad de elementos.
print(concatenar_listas(comidas, bebidas))

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
#[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
def obtenerImpares(secuencia):
    impares = []
    for i in secuencia:
        if i % 2 != 0:
            impares.append(i)
    return impares[0:10]
print(obtenerImpares(secuencia))
def multiplicarImpares(impares): #654.729.075
    producto = 1
    for i in impares:
        producto *= i
    return producto
print(multiplicarImpares(obtenerImpares(secuencia)))

#Pedir 10 numeros. Mostrar la media de los numeros positivos, la media de los numeros negativos y la cantidad de ceros.
def pedirNumeros(): #[0, 2, -8, 0, 7, -5, 0, 12, -15, 4] media positivos: 6 media negativos: -9 cant ceros: 3
    numeros = []
    while len(numeros) < 10:
        numero = int(input('Ingrese un numero entero. El numero puede ser positivo, negativo o cero. '))
        numeros.append(numero)
    return numeros
def obtenerMedia(numeros):
    positivos, negativos = [], []
    ceros = 0
    for i in numeros:
        if i > 0:
            positivos.append(i)
        elif i < 0:
            negativos.append(i)
        else:
            ceros += 1
    return (f'Media de positivos: {sum(positivos)/len(positivos)}, Media negativos: {sum(negativos)/len(negativos)}, Ceros: {ceros}')
print(obtenerMedia(pedirNumeros()))
#Para que el codigo funcione, se debe incluir al menos un numero de cada uno (positivo, negativo y/o cero).

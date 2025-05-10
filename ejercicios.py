import random, string
#crea una funcion que realice una division, mostrando un mensaje de error si el divisor es cero
def division(dividendo, divisor):
    while divisor == 0:
        print('No se puede dividir entre 0')
        divisor = float(input('Ingrese el divisor: '))
    return (dividendo / divisor)
dividendo, divisor = float(input('Ingrese el dividendo: ')), float(input('Ingrese el divisor: '))
print(division(dividendo, divisor))

#crea una funcion que calcule el area de un triangulo
def area_triangulo(base, altura):
    return (base * altura) / 2
base, altura = float(input('la base del triangulo: ')), float(input('la altura del triangulo: '))
print(area_triangulo(base, altura))

#crea una funcion que realice la conversion de km a millas
def kilometros_millas(kilometros):
    return (f'El equivalente en millas es: {(kilometros / 1.609)}')
kilometros = float(input('Cantidad de kilometros a convertir: '))
print(kilometros_millas(kilometros))

#crea una funcion que realice la conversion de grados celsius a farenheit
def celsius_farenheit(celsius):
    return (f'El equivalente en farenheit es: {(celsius * 9/5) + 32}')
celsius = float(input('Cantidad de grados a convertir: '))
print(celsius_farenheit(celsius))

#crea una funcion que indique si un numero es par o impar
def par_impar(entero):
    while entero > 0:
        if ((entero % 2) == 0):
            return 'El numero es par'
        else:
            return 'El numero es impar'
    return 'El numero es 0'
entero = int(input('Digite un numero entero: '))
print(par_impar(entero))

#escribe una funcion que reciba dos palabras o frases y retorne verdadero o falso segun sean o no anagramas. Un anagrama es una palabra
#o frase que se puede utilizar para crear otra, utilizando exactamente las mismas letras.
primera, segunda = str.lower(input('Escriba una palabra: ')), str.lower(input('Escriba otra palabra: '))
def esAnagrama(primera, segunda):
    primera, segunda = primera.replace(' ', ''), segunda.replace(' ', '')#se eliminan los espacios de los strings
    primeraL, segundaL = list(primera), list(segunda)#se pasan los strings a lista
    return (sorted(primeraL) == sorted(segundaL))#se compara si ambas listas ordenadas son iguales
print(esAnagrama(primera, segunda))

#crea una funcion que reciba una frase y devuelva un booleano determinando si la frase es un palindromo o no. Un palindromo es una 
#frase que se lee al derecho y al reves de la misma manera. Se debe contemplar que la frase puede contener signos ortograficos, como 
#exclamaciones, signos de interrogacion, puntos, etc.
#Opcion 1:
frase = str.lower(input('Escriba una frase para verificar si es un palindromo o no: '))
abecedario = list(string.ascii_lowercase)#lista que almacena todas las letras del abecedario
def es_palindromo(frase, abecedario):
    frase_l = list(frase)#se pasa la frase a lista
    for e in frase_l:#se itera en busca de espacios
        if e == ' ':
            frase_l.remove(e)#se eliminan los espacios en blanco
    for s in frase_l:#se itera en busca de signos ortograficos
        if s not in abecedario:
            frase_l.remove(s)#se eliminan los signos ortograficos
    return frase_l[::1] == frase_l[::-1]
#Opcion 2:
def es_palindromo2(frase, abecedario):
    frase = frase.replace(' ', '')#se eliminan los espacios
    frase_l = list(frase)#se pasa la frase a lista
    for i in frase_l:
        if i not in abecedario:#se verifica si la frase contiene signos ortograficos
            frase_l.remove(i)#se eliminan los signos ortograficos
    return frase_l[::1] == frase_l[::-1]
if es_palindromo2(frase, abecedario):
    print('La frase introducida es un palindromo')
else:
    print('La frase introducida no es un palindromo')

#crea un programa que le pida al usuario(alumno) sus notas, las agregue a una lista y le devuelva su promedio. La cantidad maxima de
#notas ingresadas debe ser 5.
def agregarNotas():
    notas = []
    while len(notas) < 5:#se establece que el maximo de notas sera cinco
        nota = int(input('Ingrese su nota: '))
        if nota >= 1 and nota <= 12:#la nota debe tener el valor correcto
            notas.append(nota)
        else:
            print('Nota incorrecta')
    return notas
def calcularPromedio(calificaciones):
    return (f'Su nota promedio del curso es: {round(sum(calificaciones) / len(calificaciones))}')
print(calcularPromedio(agregarNotas()))

#Crea un diccionario que contenga los nombre de 5 frutas con sus respectivos precios. Escribe la funcion que pida al usuario el 
#nombre de una fruta y luego imprima su precio.
frutas = [{
    'fruta': 'manzana',
    'precio': 48,
},{
    'fruta': 'durazno',
    'precio': 50,
},{
    'fruta': 'kiwi',
    'precio': 28,
},{
    'fruta': 'naranja',
    'precio': 70,
},{
    'fruta': 'pera',
    'precio': 78,
}]
consulta = str.lower(input('Nombre de fruta para consultar su precio: '))
def consultar_precio(frutas):
    for i in frutas:
        if i['fruta'] == consulta:
            return i['precio']
    return 'Sin datos'
print(consultar_precio(frutas))

#Crear un juego donde el usuario debe adivinar un numero entre 1 y 100. Con cada interaccion, se le debe decir al usuario
#si el numero ingresado es mayo o menor al generado. El juego debe terminar cuando el usuario adivine el numero.
import random
numeroIngresado = int(input('Ingrese un numero entre 1 y 100: '))
def adivinar_numero(numero):
    aleatorio = random.randint(1, 100)
    #print(aleatorio)
    while numero != aleatorio:
        if numero > aleatorio:
            print('El numero ingresado es mayor')
        else:
            print('El numero ingresado es menor')
        numero = int(input('Ingrese un numero entre 1 y 100: '))
    return 'Adivinaste el numero!!!'
print(adivinar_numero(numeroIngresado))

#crea una funcion que reciba una lista y devuelva la suma de los elementos de la misma
numeros = [5, 10, 15, 20, 25] #75
def suma(numeros):
    suma_n = 0
    for i in numeros:
        suma_n += i
    return suma_n
print(suma(numeros))
#opcion 2:
def suma2(numeros):
    return sum(numeros)
print(suma2(numeros))

#crea una funcion que reciba una cadena de texto y luego la imprima al reves
texto = str(input('Escriba una cadena de texto: '))
def invertir(texto):
    texti_inv = list(texto[::-1])#se pasa a lista el string ingresado y se invierte el orden de sus caracteres
    r = ''.join(texti_inv)#el metodo join ingresa el string invertido en la nueva variable
    return r
print(invertir(texto))

#crea una funcion que le pida al usuario cuantos numeros quiere agregar a una lista y los devuelva en orden descendente
agregar = int(input('¿Cuantos numeros desea agregar a la lista?'))
def ordenar(agregar):
    lista = []
    while len(lista) < agregar:
        numero = int(input('Ingrese un numero: '))
        lista.append(numero)
    return sorted(lista, reverse=True)
print(ordenar(agregar))

#crear una funcion que reciba una fecha y calcule la edad de una persona
fecha = str(input('Ingrese una fecha en formato dd/mm/aa: '))
def calcularEdad(fecha):
    año = int(fecha[-4::])#se toma los ultimos cuatro digitos de la fecha, correspondientes al año
    return (f'Tu edad es: {2025 - año} años.')
print(calcularEdad(fecha))

#crea una funcion que sume todos los numeros pares del 1 al 100
def suma_pares():
    suma = 0
    for i in range(0, 101, 2):
        suma += i
    return suma
print(suma_pares())

#crea una funcion que busque un elemento en una lista y devuelva su valor posicional
lista, elemento = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 14
def buscarPosicion(lista, elemento):
    for i in lista:
        if lista[i] == elemento:
            return i
print(buscarPosicion(lista, elemento))
#crea una funcion que reciba un valor posicional y devuelve el elemento correspondiente en una lista
posicion = 3
def buscarElemento(lista, posicion):
    for i in lista:
        if i == lista[posicion]:
            return i
print(buscarElemento(lista, posicion))

#crea una funcion que cuente la cantidad de vocales en una cadena de texto
frase, vocales = str.lower(input('Escriba una frase para contar sus vocales: ')), ['a', 'e', 'i', 'o', 'u']
def contador_vocales(frase, vocales):
    sum = 0
    for i in frase:
        if i in vocales:
            sum += 1
    return sum
print(contador_vocales(frase, vocales))

#crea una funcion que reciba un numero y calcule la suma de sus digitos
numero = str(input('Ingrese un numero entero: '))
def sumar_digitos(numero):
    digitos = [int(i) for i in str(numero)]#se itera y asigna los valores dentro de la lista
    return sum(digitos)
print(sumar_digitos(numero))

#crea una funcion que calcule el numero de palabras en una cadena de texto
cadena = str(input('Ingrese una cadena de texto: '))
def contar_palabras(cadena):
    palabras = cadena.rsplit()#este metodo transforma un string a lista, donde cada elemento de la misma es una palabra.
    return len(palabras)
print(contar_palabras(cadena))

#crea una funcion que solicite un email y verifique si el mismo es valido o no
email = str.lower(input('Ingresar email: '))
term, arroba = str.endswith(email, '.com'), '@' in email#se comprueba la existencia de @ y terminacion .com
x = term and arroba
def es_mail(email, term, arroba, x): #la funcion puede no tener parametros; las cuatro variables pueden ir dentro de la funcion.
    while x == False:
        print('Correo incorrecto')
        email = str.lower(input('Ingresar email: '))
        term, arroba = str.endswith(email, '.com'), '@' in email
        x = term and arroba
    return 'Correo correcto'
print(es_mail(email, term, arroba, x))
#solucion 2
def esEmail(email):
    x = ('@' in email) and (str.endswith(email, '.com'))#se comprueba la existencia de @ y terminacion .com
    while x == False:#si no hay @ o terminacion .com, se le pide al usuario que ingrese nuevamente
        print('E-mail incorrecto. Ingrese nuevamente')
        email = str.lower(input('Ingrese su correo electronico: '))
        x = ('@' in email) and (str.endswith(email, '.com'))
    return (f'El E-mail {email} ha sido ingresado correctamente.')
print(esEmail(email))

#crea una funcion que solicite una lista con numeros y los ordene en orden ascendente [28, 12, 32, 21, 77, 75, 99, 2]
numeros = int(input('¿Cuantos numeros desea ingresar?'))
def ascendente(numeros):
    lista = []
    while len(lista) < numeros:
        agregar = int(input('Numero a ingresar: '))
        lista.append(agregar)
    return sorted(lista)
print(ascendente(numeros))

#crea una funcion que reciba un numero y devuelva un booleano que determine si el numero es divisible entre 3 y 5
def divisible_entre_3_y_5(numero):
    return (numero % 3 == 0) and (numero % 5 == 0)
print(divisible_entre_3_y_5(-30))

#crea una funcion que devuelva una cantidad de estrellas en base a determinado porcentaje
porcentaje = int(input('Ingrese un valor porcentual para obtener su equivalente en estrellas: '))
def calcular_estrellas(porcentaje):
    while porcentaje < 0 or porcentaje > 100:
        print('Fuera de Rango')
        porcentaje = int(input('Ingrese un valor porcentual para obtener su equivalente en estrellas: '))
    if porcentaje > 90 and porcentaje <= 100:
        print('5 estrellas')
    elif porcentaje > 80:
        print('4 estrellas')
    elif porcentaje > 50:
        print('3 estrellas')
    elif porcentaje > 20:
        print('2 estrellas')
    else:
        print('1 estrella')
    return 'Fin'
print(calcular_estrellas(porcentaje))

#crea una funcion que reciba una cantidad de unidades y devuelva el costo total dependiendo de la cantidad de unidades y su valor
#por unidad. La cantidad maxima de unidades debe ser 200.
unidades = int(input('Ingrese la cantidad de unidades: '))
def calcular_costo(unidades):
    while unidades > 200 or unidades < 1:
        print('Cantidad erronea. Vuelva a ingresar la cantidad de unidades.')
        unidades = int(input('Ingrese la cantidad de unidades: '))
    if unidades >= 1 and unidades <= 50:
        costo = unidades * 0.60
    elif unidades > 50 and unidades <= 100:
        costo = unidades * 1.10
    else:
        costo = unidades * 1.70
    return f'El costo total es: {round(costo)} dolares'
print(calcular_costo(unidades))

#Dado un diccionario donde las claves son nombres de personas y los valores son sus edades, crea un nuevo diccionario
#que invierta las claves y los valores, de modo que las edades sean las claves y los nombres sean los valores.
personas = {
    'Pedro': 35,
    'Alberto': 27,
    'Josue': 52,
    'Kevin': 22,
    'Jonathan': 43
}
nombres, edades = personas.keys(), personas.values()
def crearDiccionario(edades, nombres):
    return dict(zip(edades, nombres))
print(crearDiccionario(edades, nombres)) 

#Crea un diccionario con nombres de estudiantes y sus calificaciones. Escribe una funcion que filtre y devuelva un nuevo
#diccionario solo con los estudiantes que tienen una calificacion mayor a cierto umbral.
alumnos = {
    'Roberto': 9,
    'Alfonso': 5,
    'Julian': 7,
    'Agustin': 4,
    'Jose': 8,
    'David': 3,
    'Alan': 11,
    'Lautaro': 5,
    'Cristian': 4,
    'Ismael': 11
}
notas, altas = alumnos.values(), [] #se extraen las notas y se crea la lista que almacenara las notas altas
for i in notas:
    if i > 6:
        altas.append(i) #si las notas son superiores a seis, se añaden a la lista
def alAprobados(alumnos, altas):
    aprobados = {} #nuevo diccionario solo con los alumnos aprobados
    for n in alumnos:
        for c in altas:
            if alumnos[n] == c: #si un alumno del diccionario tiene una nota comprendida dentro de la lista
                aprobados[n] = c #se lo agrega al diccionario aprobados
    return aprobados
print(alAprobados(alumnos, altas))

#Escribe un programa que pida al usuario una clave y verifique si existe en un diccionario. Si existe, imprimir su valor.
#De lo contrario, imprimir un mensaje que diga que la clave no se encontro.
pares = {
    2: 'Computadoras',
    4: 'Smartwatch',
    6: 'Smartphone',
    8: 'Smart TV',
    10: 'Tarjeta de video'
}
def comprobarClave(pares):
    x = int(input('Ingrese una clave para verificar su existencia: '))
    if x in pares.keys():
        return pares[x]
    else:
        return 'No se encontro la clave.'
print(comprobarClave(pares))

#Crea un diccionario que contenga palabras y sus sinónimos. Escribe una función que, dado una palabra, devuelva su
#sinónimo.
palabras = {
    'anteojos': 'gafas',
    'cabello': 'pelo',
    'camino': 'sendero',
    'elegir': 'escoger',
    'fragmento': 'pedazo'
}
p = str(input('Escriba una palabra para ver su sinonimo: '))
def sinonimo(palabras, p):
    if p in palabras.keys(): #si la palabra introducida se encuentra en el diccionario como clave
        return palabras[p] #se muestra el sinonimo de esa palabra (su valor)
    else:
        return 'No se encontro la palabra'
print(sinonimo(palabras, p))

#Escribe un programa que tome una lista de números y devuelva un diccionario que contenga cada número como clave y su
#frecuencia como valor.
lista = [0, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5]
def frecuencia(lista):
    f = {} #diccionario nuevo
    e = 0 #variable que obtendra la cantidad de veces que se repite un numero
    for i in lista:
        e = lista.count(i) #se cuenta la cantidad de veces que se repite un numero
        f[i]=e #el diccionario de salida almacena cada numero como clave y la cantidad de veces que se repite como valor
    return f
print(frecuencia(lista))

#Escribe un programa que tome una cadena de texto y cuente cuantas veces aparece cada palabra. Almacena los resultados
#en un diccionario.
cadena = 'contorsion brazo brazo espalda espalda espalda pierna pierna pierna pierna cuello cuello cuello cuello cuello'
cadenaL = cadena.split() #se transforma el string a lista, donde cada elemento de la lista es una palabra
def palabrasCount(cadenaL):
    d = {} #diccionario de salida
    p = 0 #variable que almacena la cantidad de veces que se repite cada palabra
    for i in cadenaL:
        p = cadenaL.count(i) #se cuenta la cantidad de veces que se repite cada palabra
        d[i]=p #se guarda en el diccionario cada palabra como clave y la cantidad de veces que se repite como valor
    return d
print(palabrasCount(cadenaL))

#Escribe un programa que tome una cadena de texto y cuente cuántas veces aparece cada letra (ignorando espacios y
#mayúsculas). Almacena los resultados en un diccionario.
import string
texto = 'No me gusta Literatura y tampoco Filosofia'
texto = texto.replace(' ', '') #elimino los espacios
textoL = list(texto) #el texto se pasa a lista, donde cada elemento de la misma es una letra
for i in textoL: #itero en la lista en busca de mayusculas
    if i in list(string.ascii_uppercase): #si la variable de iteracion encuentra una mayuscula
        textoL.remove(i) #se elimina la mayuscula
textoN = ''.join(textoL) #se forma un nuevo string sin mayusculas ni espacios
def letrasCount(textoN):
    f = {}
    e = 0
    for i in textoN:
        e = textoN.count(i)
        f[i]=e #el diccionario de salida tendra cada letra como clave y su frecuencia como valor
    return f
print(letrasCount(textoN))

#Dado un diccionario con nombres de estudiantes y una lista de sus calificaciones, calcula el promedio de calificaciones
#de cada estudiante y almacena los resultados en un nuevo diccionario.
estudiantesC = {
    'Mateo': [4, 8, 6, 7, 9],
    'Fernando': [5, 9, 10, 11, 4],
    'Sebastian': [7, 12, 8, 11, 9],
    'Adrian': [10, 8, 7, 9, 11],
    'Kevin': [5, 2, 9, 4, 5]
}
calificaciones = estudiantesC.values() #variable que almacenara las listas con las notas de los estudiantes
def promedios(calificaciones):
    c = [] #lista que almacenara los promedios de cada alumno
    x = 0 #variable que obtendra cada promedio
    for i in calificaciones: #la variable de iteracion itera sobre cada lista con notas
        x = sum(i) / len(i) #obtiene la suma de los elementos dividido la cantidad de elementos (promedio)
        c.append(x) 
    return dict(zip(estudiantesC.keys(), c)) #se crea el diccionario
print(promedios(calificaciones))

#Crea un diccionario con nombres de países y sus poblaciones. Escribe un programa que ordene el diccionario por poblacion
#y lo imprima.
paises = {
    'Uruguay': 3500000,
    'Argentina': 41000000,
    'Brasil': 210000000,
    'Rusia': 150000000,
    'España': 40000000
}
poblaciones = sorted(paises.values()) #variable que almacena una lista con las poblaciones
def ordenar(paises, poblaciones):
    o = {}
    for i in poblaciones:
        for j in paises: #se itera dentro de las claves del diccionario paises
            if i == paises[j]: #si la cifra de poblacion se encuentra asignada a un pais
                o[i] = j #al diccionario nuevo se le asigna la poblacion como clave y el pais como valor
    return o
print(ordenar(paises, poblaciones))

#Dado dos diccionarios, escribe una funcion que los combine. Si hay claves duplicadas, suma los valores de esas claves.
vehiculos = {
    'autos': 4,
    'camiones': 8,
    'camionetas': 5,
    'motos': 6,
    'retroexcavadoras': 3
}
maquinaria = {
    'retroexcavadoras': 6,
    'grua': 7,
    'aplanadora': 5,
    'cortacesped': 6,
    'perforadora': 2
}
def combinar(vehiculos, maquinaria):
    salida = vehiculos.copy() #variable que almacena la copia del primer diccionario
    for c, v in maquinaria.items(): #se itera en las claves y los valores del segundo diccionario
        if c in salida: #se comprueba si una clave se encuentra en ambos diccionarios
            salida[c] += v #si una clave esta repetida, se suma su valor
        else:
            salida[c]=v #si la clave no esta repetida, se agrega al diccionario de salida
    return salida
print(combinar(vehiculos, maquinaria))

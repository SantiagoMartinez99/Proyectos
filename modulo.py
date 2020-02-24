import math as mt
import random as rd
import time as t
#EJEMPLOS SIMPLES
#5.) Area de un triangulo
def area_triangulo(b,h):
    area=b*h/2
    return print('El area del triángulo es: ', area)
#6.) Longitud y area de una circunferencia
def area_circunferencia(r):
    area1=mt.pi*r**2
    perimetro=2*mt.pi*r
    return area1, perimetro
"""--------------------------------------------------------------------------"""
#EJEMPLOS CON CONDICIONALES
#18.) Detectar si un numero leído es par o impar
def par_o_impar(n):
    numero=n%2
    if numero==0:
        return "par"
    else:
        return "impar"
"""23.) Programa que detecte dos números del teclado y si el primero es mayor que
el segundo intercambie sus valores"""
def mayor_menor(a,b):
    if a>b:
        print(b,a)
    else:
        print(a,b)
"""--------------------------------------------------------------------------"""
#EJERCICIOS CON CICLOS
"""29.) Programa que visualice en pantalla los números múltiplos de 5
comprendidos entre 1 y 100"""
def multiplos():
    cont=0
    i=1
    while cont<100:
        cont=5*i
        i+=1
        print(cont)
#33.) Calcule la suma de los números hasta un número dado por el usuario
def la_sumatoria(n):
    cont=0
    for i in range(n+1):
        cont+=i
    return cont
"""--------------------------------------------------------------------------"""
#EJERCICIOS CON COLECCIONES
#44.Solicite cinco numeros y calcular la media aritmetica)
def media_aritmetica():
    lista=[]
    for i in range(5):
        lista.append(int(input("Ingrese un numero: ")))
    cont=0
    for valor in lista:
        cont+=valor
    return cont/len(lista)
#45.
def matriz(ancho, largo):
    lista=[]
    matriz=[]
    for i in range(ancho):
        for i in range(largo):
            lista.append(rd.randint(0,100))
        matriz.append(lista)
        lista=[]
    maximo=matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]>maximo:
                maximo=matriz[i][j]
    print(matriz)
    return maximo
"""--------------------------------------------------------------------------"""
#CADENAS DE CARACTERES
#56.) Programa que elimine espacios en blanco de caracteres
def eliminador_espacios(palabra):
    return palabra.replace(" ", "")
#57.)
def palindromo(palabra):
    lista=[]
    palabra.strip(" ")
    if palabra[:]==palabra[::-1]:
        return True
    else:
        return False
"""--------------------------------------------------------------------------"""
#FUNCIONES Y PROCEDIMIENTOS
#66.) Calcular factorial usando funciones
def factorial(numero):
    i=0
    for i in range(numero):
        i+=i*i
    return i
#
def primo(numero):
    if numero<1:
        return "no es primo"
    elif numero==2:
        return "es primo"
    else:
        for i in range (2,numero):
            if numero % i == 0:
                return "no es primo"
            else:
                return "es primo"


"""--------------------------------------------------------------------------"""
#RECURSIVIDAD
#75.) Calcular la potencia de un numero usando recursividad
def potencia_recursivo(a,b):
    if b==0:
        return 1
    else:
        return a*potencia_recursivo(a,b-1)
#76.) Calcular factorial usando recursividad
def factorial_recursivo(numero):
    if(numero==0):
        return 1
    else:
        return numero*factorial_recursivo(numero-1)
"""--------------------------------------------------------------------------"""
#MODULOS
"""81.) Crear funciones artiméticas que realicen las operaciones de suma, resta,
multiplicación, división y potencia de enteros"""
def operaciones_modulo(a,b):
    suma=a+b
    resta=a-b
    multiplicacion=a*b
    division=a/b
    potencia=a**b
    return suma,resta,multiplicacion,division,potencia

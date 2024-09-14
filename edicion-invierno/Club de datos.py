# Dado una lista llamada numeros, 
# eliminar todos los mayores a 10

lista = [1,20,31,4,3,64] # [1,4,3]
lista_resultado = []
longitud_lista = len(lista)
for i in range(longitud_lista):
    elem_actual = lista[i]
    if elem_actual <= 10:
        lista_resultado.append(elem_actual)
print(lista_resultado)
    
#Dado un número X, 
#generar una lista con los pares menores a ese número
def pares_menoresque(x):
    lista = [] # [2,4,6,8,10]
    for i in range(x):
        resto = i % 2
        es_par = resto == 0 
        if es_par:
            lista.append(i)
    return lista

lista1 = pares_menoresque(3)
lista2 = pares_menoresque(20)
lista3 = pares_menoresque(5)
lista4 = pares_menoresque(24)
lista5 = pares_menoresque(100)
print(lista1,lista2,lista3,lista4,lista5)

def minimo(lista):
    minimo_elemento = lista[0]
    for i in lista:
        if i < minimo_elemento:
            minimo_elemento = i
    return minimo_elemento

def selection_sort(lista):
    lista_ordenada = []
    longitud_lista = len(lista)
    for i in range(longitud_lista):
        min_actual = minimo(lista)
        lista_ordenada.append(min_actual)
        lista.remove(min_actual)
    return lista_ordenada

lista1 = [5,2,37,1]
lista1_ordenada = selection_sort(lista1)
print("RESULTADO DEL SORTING: ", lista1_ordenada)
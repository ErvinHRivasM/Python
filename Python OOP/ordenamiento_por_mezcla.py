import random
import sys
#sys.setrecursionlimit(11000000)
#Inventado por Jhon Bon Newman.

def ordenamiento_por_Mezclas(lista):

    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(izquierda, '*' * 5, derecha)

        #llamada de recursividad en cada mitad
        ordenamiento_por_Mezclas(izquierda)
        ordenamiento_por_Mezclas(derecha)

        #Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        #Iterador para la lista ppal
        k=0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] =  derecha[j]
                j += 1 
            k += 1
        
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('-' * 50)

    return lista

        

if __name__ == '__main__':
    list_size = int(input('De que tamano sera la lista? '))
    lista = [random.randint(0, 100) for i in range(list_size)]
    print(lista)
    print('-' * 20)
    lista_ordenada = ordenamiento_por_Mezclas(lista)
    print(lista_ordenada)

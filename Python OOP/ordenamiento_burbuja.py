import random
import sys
#print(sys.getrecursionlimit())
sys.setrecursionlimit(11000000)
#print(sys.getrecursionlimit())

def ordenamiento_de_burbuja(lista):
    n = len(lista)
        
    for i in range(n):
        for j in range(0, n-i-1): # O(n) * O(n) = O(n*n) =O(n)**2
            if lista[j] > lista[j + 1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    
    return lista

        

if __name__ == '__main__':
    list_size = int(input('De que tamano sera la lista? '))
    lista = [random.randint(0, 100) for i in range(list_size)]
    print(lista)
    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(lista_ordenada)

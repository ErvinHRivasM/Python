import random
import sys
#print(sys.getrecursionlimit())
sys.setrecursionlimit(11000000)
#print(sys.getrecursionlimit())

def busqueda_binaria(lista, comienzo, final, objetivo):
        
    if comienzo > final:
        return False

    medio = ((comienzo + final) // 2)

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio+1, final, objetivo)
        
    else:
        return busqueda_binaria(lista, medio-1, final, objetivo)
        

if __name__ == '__main__':
    list_size = int(input('De que tamano sera la lista? '))
    objetivo = int(input("Que numero quieres encontra? "))
    lista = sorted([random.randint(0, 100) for i in range(list_size)])
    print(lista)
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    print(f'El elemento  {objetivo} {"esta" if encontrado else "no esta"} en la lista')

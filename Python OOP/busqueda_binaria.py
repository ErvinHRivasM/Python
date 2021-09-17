import random

class BusquedaBinaria:

    def __init__(self, lista, comienzo, final, objetivo):
        self.lista = lista
        self.comienzo = comienzo
        self.final = final
        self.objetivo = objetivo

    def busqueda_binaria(self):
        
        if self.comienzo > self.final:
            return False

        medio = (self.comienzo +self.final) // 2

        if lista[medio] == self.objetivo:
            return True
        elif lista[medio] < self.objetivo:
            temp1 = BusquedaBinaria(lista, medio + 1 ,self.final, self.objetivo)
            return temp1.busqueda_binaria()
        else:
            temp2 = BusquedaBinaria(lista, medio - 1 ,self.final, self.objetivo)
            return temp2.busqueda_binaria()

    if __name__ == '__main__':
        pass

list_size = int(input('De que tamano sera la lista? '))
objetivo = int(input("Que numero quieres encontra? "))
lista = sorted([random.randint(0, 100) for i in range(list_size)])
busqueda = BusquedaBinaria(lista, 0, len(lista), objetivo)
encontrado = busqueda.busqueda_binaria()
print(f'El elemento  {objetivo} {"esta" if encontrado else "no esta"} en la lista')

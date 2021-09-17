import random

class Busqueda:

    listado = ""

    def __init__(self, lista, objetivo):
        self.lista = lista
        self.objetivo = objetivo

    def busqueda_lineal(self):
        match = False
        print("List..."+str(self.lista))

        for element in self.lista:
            if element == self.objetivo:
                match = True
                break
        return match

    if __name__ == '__main__':
        pass

list_size = int(input('De que tamano sera la lista? '))
objetivo = int(input("Que numero quieres encontra? "))
lista = [random.randint(0, 100) for i in range(list_size)]
encontrado = Busqueda(lista, objetivo)
encontrado.busqueda_lineal()
print(f'El elemento  {objetivo} {"esta" if encontrado else "no esta"} en la lista')

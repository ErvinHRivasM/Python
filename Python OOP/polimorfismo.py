
#Polimorfismo  Habilidad de tomar varias formas.
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print(" Anda caminando")

#Herencia === extends in java
class Ciclista(Persona):
    
    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print(" Anda pedaliando la bicicleta")


if __name__ == '__main__':
    persona = Persona("Ervin Rivas")
    print(persona.avanza())

    ciclista = Ciclista("Mayra Aleja")
    print(ciclista.avanza())

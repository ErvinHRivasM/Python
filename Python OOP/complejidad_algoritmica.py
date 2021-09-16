import time

class Factorial:

    def __init__(self, n):
        self.n = n

    def factorial(self):
        respuesta = 1
       
        while self.n > 1:
            respuesta *= self.n
            self.n -= 1
        return respuesta

    def factorial_r(self):
        if self.n == 1:
            return 1
        return self.n * factorial_r(self.n - 1)


if __name__ == '__main__':
    n = 1000
    comienzo = time.time()
    #print("Comienzo.."+str(comienzo))
    factorial = Factorial(n)
    #print("Factorial(n):: "+str(factorial.factorial()))
    final = time.time()
    #print("final.."+str(final))
    
    comienzo2 = time.time()
    factorial = Factorial(n)
    #print("Factorial(n):: "+str(factorial.factorial_r()))
    final2 = time.time()
    
    print ("tiempo 1: "+str(final - comienzo))
    print ("tiempo 2: "+str(final2 - comienzo2))


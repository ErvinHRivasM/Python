class Coordenadas:
    
    def __init__(self, x , y):
        self.x = x
        self.y = y
    
    def distancia(x, otra_coordenada):
        dif_x = (self.x - otra_coordenada.x)**2
        dif_y = (self.y - otra_coordenada.y)**2
        
        return (dif_x + dif_y)**0.5 


if __name__ == '__main__' :
    coord_1 = Coordenadas(7, 25)
    coord_2 = Coordenadas(7, 25)

    #print(coord_1.distancia(coord_1))
    print(isinstance(coord_2))


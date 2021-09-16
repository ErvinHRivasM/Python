class CasillaDeVotaciones:

	def __init__(self, identificador, pais):
		self.__identificador = identificador
        self.__pais = pais
        self.__region = None


	@property
	def region(self):
		return self.__region


	@region.setter
	def region(self, region):
		if region in self.__pais:
            self.__region = region
        else:
			raise ValueError("la regioón {region} no es valida en {self.__pais}")



casilla = CasillaDeVotaciones(123,['Colombia','Valle del cauca'])
casilla.region


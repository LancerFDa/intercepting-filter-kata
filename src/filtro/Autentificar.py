from Filtro import Filtro

class Autentificacion(Filtro):

    def __init__(self, usuario):
        self.usuairo = usuario

    def autentificacion(self):
        print("Autenticacion OK para " + self.usuario)
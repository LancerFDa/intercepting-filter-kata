from Filtro import Filtro

class Autentificacion(Filtro):

    def autentificacion(self, usuario):
        print("Autenticacion OK para " + usuario)
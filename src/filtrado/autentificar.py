from filtro import Filtro

class Autentificacion(Filtro):

    def autentificacion(self, usuario):
        print("Autenticacion OK para " + usuario)


if __name__=="__main__":
    autentificacion = Autentificacion()
    autentificacion.autentificacion("jonh")
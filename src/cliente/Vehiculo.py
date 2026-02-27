from cliente import Target

class Vehiculo(Target):   

    def __init__(self, usuario):
        self.usuario = usuario

    def ejecucion(self):
        print("Puerta abierta " + self.usuario + "!")
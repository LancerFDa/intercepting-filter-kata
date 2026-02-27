from Target import Target

class Vehiculo(Target):
    
    def __init__(self, usuario):
        self.usuario = usuario

    def Vehiculo(self):
        Target.ejecucion(self.usuario)
        print("Puerta abierta " + self.usuario + "!")
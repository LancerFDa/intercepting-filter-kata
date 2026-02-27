from target import Target

class Vehiculo(Target):   

    def __init__(self, usuario):
        self.usuario = usuario

    def ejecucion(self):
        print("Puerta abierta " + self.usuario + "!")

if __name__=="__main__":
    vehiculo = Vehiculo()
    vehiculo.ejecucion("jonh persona")
    
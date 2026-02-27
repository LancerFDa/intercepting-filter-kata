from target import Target

class Vehiculo(Target):   

    def ejecucion(self, usuario):
        print("Puerta abierta " + usuario + "!")

if __name__=="__main__":
    vehiculo = Vehiculo()
    vehiculo.ejecucion("jonh")
    
print("Act 9 clase humano")
print("Diana E. Leyva Solis Mat:22308051281071")

## zona de clases
class Humano1071:
    ## zona de atributos
    edad = 0
    genero = ""
    estatura = 0
    ojos = ""
    colordepelo = ""

    ## zona de funciones dentro de la clase
    def caracteristicas(self, nombre):
        print("")
        print(f"Nombre: {nombre}")
        print(f"Edad: {self.edad}")
        print(f"Género: {self.genero}")
        print(f"Estatura: {self.estatura}")
        print(f"Ojos: {self.ojos}")
        print(f"Color de pelo: {self.colordepelo}")
        print("")

    def correr1071(self, nombre):
        print(f"{nombre} corre")

    def caminar1071(self, nombre):
        print(f"{nombre} camina")

    def escribir1071(self, nombre):
        print(f"{nombre} escribe")

    def comer1071(self, nombre):
        print(f"{nombre} come")

    def estudiar1071(self, nombre):
        print(f"{nombre} estudia")

## zona de creación de objetos
diana = Humano1071()
hector = Humano1071()

## zona de asignación de atributos
diana.edad = 16
diana.genero = "Femenino"
diana.estatura = 1.57
diana.ojos = "café"
diana.colordepelo = "castaño"

hector.edad = 20
hector.genero = "Masculino"
hector.estatura = 1.78
hector.ojos = "café"
hector.colordepelo = "negro"

## zona de usando objetos
diana.caracteristicas("Diana")
diana.correr1071("Diana")
diana.caminar1071("Diana")
diana.escribir1071("Diana")
diana.comer1071("Diana")
diana.estudiar1071("Diana")

hector.caracteristicas("Héctor")
hector.correr1071("Héctor")
hector.caminar1071("Héctor")
hector.escribir1071("Héctor")
hector.comer1071("Héctor")
hector.estudiar1071("Héctor")

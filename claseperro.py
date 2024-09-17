print("Clases version 2 el constructor")
class perro:
    # Funcion constructor
    def __init__(self,color,edad):
        self.color=color
        self.edad=edad

    # Funciones creadas por el usuario
    def muerde(self):
        print("Chale, el perro me mordio")

    def chatperro(self, mensaje):
        print(f"Chat perro: {mensaje}")
    
    def chatperra(self, mensajep):
        print(f"Chat perra: {mensajep}") 

    def datos(self):
        print(f"Color: {self.color} Edad: {self.edad}")

# Crear el objeto

chihuas=perro("Negro",2)

# Llamadas a funciones

chihuas.datos()
chihuas.muerde()
chihuas.chatperro("Hola canina")
chihuas.chatperra("Hola boby")
chihuas.chatperro("Quieres ser mi gugguu?")
chihuas.chatperra("Grrru....")
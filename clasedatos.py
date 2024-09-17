class informacion:

    def mi_lista(self):
        lista_Nomperros=["Boby", "Dollar", "Fany"]
        for x in lista_Nomperros:
            print(x)

    def mi_tupla(self):
        tupla_razaperros=("Chihuahua", "Pastor Aleman", "Pitbull")
        for x in tupla_razaperros:
            print(x)

    def mi_conjunto(self):
        conjunto_edadperros={2, 8 , 3 }
        for x in conjunto_edadperros:
            print(x)

    def mi_diccionario(self):
        diccionario_Nomperros= {
            "Nombre: ": "Boby",
            "Edad: ": 3,
            "Raza: ": "Chihuahua"
        }
        for x, y in diccionario_Nomperros.items():
            print(x, y)


# Creadndo el objeto

datos=informacion()
print("Listado de nombres de perros")
datos.mi_lista()

print("------------------------------")

print("Tupla de raza de perros")
datos.mi_tupla()

print("------------------------------")

print("Conjunto de edades de perros")
datos.mi_conjunto()

print("------------------------------")

print("Diccionario de perros")
datos.mi_diccionario()

print("------------------------------")
class Costumers:
    def __init__(self,name,password):
        self.name = name
        self.password = password
    def mostrar(self):
        print(f"Bienvenido {self.name}")
class Discs:
    def __init__(self,id,title,artist,year,cost,price):
        self.id = id
        self.title = title
        self.artist = artist
        self.year = year
        self.cost = cost
        self.price = price

    def mostrar(self):
        print(f"Informacion del disco--------- \nID: {self.id} \nTitulo: {self.title} \nArtista: {self.artist} \nAño: {self.year} \nCosto: {self.cost} \nPrecio: {self.price}")    
    def database(self):
        data = open("Database.txt", "a")
        data.write(f"{self.id},{self.title},{self.artist},{self.year},{self.cost},{self.price}\n")
        data.close()
        print("Disco agregado a la base de datos")

        


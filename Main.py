#Aqui hago los imports---------------
import random
from Usuario import Usuario
from Costumers import Costumers
from Discs import Discs
#------------------------------------

#----------------------Este es el modulo administrativo------------------------------------------------------------
def management(discs):
    while True:
        option = input("Elija una opcion a realizar: \n1.Agregar \n2.Eliminar \n> ")
        while not option.isnumeric() or int(option) not in range(1,3):
            print("Por favor introduzca una opcion valida")
            option = input("Elija una opcion a realizar: \n1.Agregar \n2.Eliminar \n> ")
        contador = 0
        if contador != 0:
                data = open("Database.txt", "r")
                for x in data:
                    i = 0
                    disc = Discs(x.split(",")[i],x.split(",")[i+1],x.split(",")[i+2],x.split(",")[i+3],x.split(",")[i+4],x.split(",")[i+5])
                    discs.append(disc.id)
                data.close()
        #-----------------------------Aqui agrego un nuevo disco------------------------------------------
        if option == "1":
            id = str(random.randrange(0,9)) + str(random.randrange(0,9)) + str(random.randrange(0,9)) + str(random.randrange(0,9))
            while id in discs:
                print("Ya ese ID existe")
                id = str(random.randrange(0,9)) + str(random.randrange(0,9)) + str(random.randrange(0,9)) + str(random.randrange(0,9))

            title = input("Titulo de la cancion: ").title()

            artist = input("Artista: ").title()

            year = input("Año: ")
            while not year.isnumeric() or int(year) not in range(1700,2023):
                print("Introduzca un año valido")
                year = input("Año: ")

            cost = input("Costo: ")
            while not cost.isnumeric() or int(cost) < 0:
                print("Introduza un costo valido")
                cost = input("Costo: ")

            price = input("Precio: ")
            while not price.isnumeric() or int(price) < 0:
                print("Introduzca un precio valido")
                price = input("Precio: ")
                      
            disc = Discs(id, title, artist, year, cost, price)
            disc.mostrar()
            disc.database()
            contador +=1
        #--------------------------Aqui elimino un disco ------------------------------
        else:
            discs = []
            ids = []
            data = open("Database.txt", "r")
            content = data.read()
            data.close()
            if content == "":
                print("Lo siento en estos momentos no hay nada en la base de datos")     
            else:
                data = open("Database.txt", "r")
                for x in data:
                    i = 0
                    disc = Discs(x.split(",")[i],x.split(",")[i+1],x.split(",")[i+2],x.split(",")[i+3],x.split(",")[i+4],x.split(",")[i+5])
                    new_disc = {}
                    new_disc["id"] = disc.id
                    new_disc["title"] = disc.title
                    new_disc["artist"] = disc.artist
                    new_disc["year"] = disc.year
                    new_disc["cost"] = disc.cost
                    new_disc["price"] = disc.price
                    ids.append(disc.id)
                    discs.append(new_disc)
                print(discs)
                data.close()

                id = input("Introduzca id a eliminar: ")
                while not id.isnumeric() or len(id) != 4 or id not in ids:
                    print("Introduzca un ID valido a eliminar")
                    id = input("Introduzca id a eliminar: ")

                for x in discs:
                    if discs[i]["id"] == id:
                        discs.pop(i)
                        print("Eliminado")
                    else:
                        i += 1
                #----------------Aqui vuelvo a agregar los discos a la base de datos, excepto el elminado----------
                data = open("Database.txt", "w")
                for i in range(0,len(discs)):
                    discs[i]["price"] = discs[i]["price"].replace("\n","")
                    disc = Discs(discs[i]["id"],discs[i]["title"],discs[i]["artist"],discs[i]["year"],discs[i]["cost"],discs[i]["price"])
                    disc.database()       
                data.close()
        option = input("Desea: \n1.Continuar \n2.Salir \n> ")
        while not option.isnumeric() or int(option) not in range(1,3):
            print("Introduzca una opcion valida")
            option = input("1.Continuar \n2.Salir \n> ")
        if option != "1":
            break
#------------Este es el modulo de ventas-----------------------
def sales():
    discs = []
    option = input("Elija una opcion: \n1.Crear una cuenta \n2.Iniciar sesion \n3.Salir \n> ")
    while not option.isnumeric() or int(option) not in range(1,4):
        print("Error, elija una opcion valida")
        option = input("Elija una opcion: \n1.Crear una cuenta \n2.Iniciar sesion \n3.Salir \n> ")
    #-------------------Aqui creo la cuenta de un cliente nuevo-------------------------------------
    if option == "1":
        name = input("Introduzca su nombre: ").title()
        while not name.isalpha():
            print("Introduzca un nombre valido")
            name = input("Introduzca su nombre: ")
        
        password = input("Contraseña: ")
        while password.isspace():
            print("Introduzca una contraseña valida")
            password = input("Contraseña: ")

        costumer = Costumers(name,password)
        costumer.mostrar()
        
        data = open("Costumers.txt", "a")
        data.write(f"{costumer.name},{costumer.password}")
        data.close()
    #--------------------Aqui inicio sesión si el cliente esta en la base de datos----------------
    elif option == "2":
        data = open("Costumers.txt", "r")
        content = data.read()
        data.close()
        if content == "":
            print("Lo siento no hay ningun cliente en la base de datos")
        else:
            while True:
                name = input("Introduzca su nombre: ").title()
                while not name.isalpha():
                    print("Introduzca un nombre valido")
                    name = input("Introduzca su nombre: ")
                
                password = input("Contraseña: ")
                while password.isspace():
                    print("Introduzca una contraseña valida")
                    password = input("Contraseña: ")
                new_costumers = []
                data = open("Costumers.txt", "r")
                for x in data:
                    i = 0
                    costumer = Costumers(x.split(",")[i],x.split(",")[i+1])
                    new_costumer = {}
                    new_costumer["name"] = costumer.name
                    new_costumer["password"] = costumer.password
                    new_costumers.append(new_costumer)
                data.close()
                find = 0
                for i in range(0,len(new_costumers)):
                    if new_costumers[i]["name"] == name and new_costumers[i]["password"] == password:
                        costumer.mostrar()
                        find = 1
                        break
                if find == 0:
                    print("Lo siento, el usuario no esta registrado en la base de datos")
                    True
                else:
                    break
            print(f"Bienvenid@ de nuevo {name}")
            data = open("Database.txt", "r")
            for x in data:
                i = 0
                disc = Discs(x.split(",")[i],x.split(",")[i+1],x.split(",")[i+2],x.split(",")[i+3],x.split(",")[i+4],x.split(",")[i+5])
                new_disc = {}
                new_disc["id"] = disc.id
                new_disc["title"] = disc.title
                new_disc["artist"] = disc.artist
                new_disc["year"] = disc.year
                new_disc["cost"] = disc.cost
                new_disc["price"] = disc.price
                discs.append(new_disc)
            print("Esto son los discos en la base de datos")
            i = 1

            for x in discs:
                print(f"-----------{i}----------------")
                print(x)
                i += 1

            sorted_by = input("Ordenar por: \n1.Orden alfabético \n2.Año de lanzamiento \n3.Precio \n> ")
            while not sorted_by.isnumeric() or int(sorted_by) not in range(1,4):
                print("Elija un orden válido")
                sorted_by = input("Ordenar por: \n1.Orden alfabético \n2.Año de lanzamiento \n3.Precio \n> ")

            #-----------------Aqui ordeno el catalogo usando funciones lambda---------------------------
            if sorted_by == "1":
                print("------------------Catálogo en orden alfabético-----------------")
                print()
                sorted_alpha = sorted(discs, key = lambda i: i["title"])
                i = 1
                for x in sorted_alpha:
                    print(f"----------{i}----------")
                    print(x)
                    i +=1
            elif sorted_by == "2":
                print("------------------Catálogo en orden de año de lanzamiento-----------------")
                print()
                sorted_year = sorted(discs, key = lambda i: i["year"])
                i = 1
                for x in sorted_year:
                    print(f"----------{i}----------")
                    print(x)
                    i +=1
            else:
                print("------------------Catálogo en orden de precio-----------------")
                print()
                sorted_title = sorted(discs, key = lambda i: i["price"])
                i = 1
                for x in sorted_title:
                    print(f"----------{i}----------")
                    print(x)
                    i += 1
                    

discs = []

def main():
    #-----------------Aqui tengo el menu principal con todos los modulos---------------------
    while True:
        option = input("Bienvenido al sistema de discos reciclados, por favor elija una opcion a realizar: \n1.Administracion \n2.Ventas \n3.Estadisticas \n4.Salir \n> ")
        while not option.isnumeric() or int(option) not in range(1,5):
            print("Por favor introduzca una opcion valida")
            option = input("Bienvenido al sistema de discos reciclados, por favor elija una opcion a realizar: \n1.Administracion \n2.Ventas \n3.Estadisticas \n4.Salir \n> ")
        if option == "1":
            name = input("Nombre: ").title()
            while not name.isalpha():
                print("Por favor introduzca un nombre válido")
                name = input("Nombre: ").title()
            find = 0
            with open("Usuarios.txt", "r") as archivo:
                for x in archivo:
                    i = 0
                    usuario = Usuario(x.split(",")[i],x.split(",")[i+1])
                    if usuario.name == name:
                        management(discs)
                        find = 1
                if find == 0:
                    print("Lo siento no es jefe/a o empleado/a")
        elif option == "2":
            sales()
        elif option == "3":
            pass
        else:
            print("Gracias por usar el sistema vuelva pronto")
            break
main()
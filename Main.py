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
                    disc = Discs(x.split(",")[i],x.split(",")[i+1],x.split(",")[i+2],x.split(",")[i+3],x.split(",")[i+4],x.split(",")[i+5],x.split(",")[i+6],x.split(",")[i+7])
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

            gender = input("Indique el tipo de género: \n1.Merengue \n2.Rap \n3.Hip Hop \n4.Reggaeton \n5.Trap \n> ")
            while not gender.isnumeric() or int(gender) not in range(1,6):
                print("Elija un género válido")
                gender = input("Indique el tipo de género: \n1.Merengue \n2.Rap \n3.Hip Hop \n4.Reggaeton \n5.Trap \n> ")

            if gender == "1":
                gender = "Merengue"
            elif gender == "2":
                gender = "Rap"
            elif gender == "3":
                gender = "Hip Hop"
            elif gender == "4":
                gender = "Reggaeton"
            else:
                gender = "Trap"
            
            amount = input("Introduzca la cantidad: ")
            while not amount.isnumeric() or int(amount) <= 0:
                print("Error, elija una cantidad válida")
                amount = input("Introduzca la cantidad: ")
      
            disc = Discs(id, title, artist, year, cost, price, gender, amount)
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
                    disc = Discs(x.split(",")[i],x.split(",")[i+1],x.split(",")[i+2],x.split(",")[i+3],x.split(",")[i+4],x.split(",")[i+5],x.split(",")[i+6],x.split(",")[i+7])
                    new_disc = {}
                    new_disc["id"] = disc.id
                    new_disc["title"] = disc.title
                    new_disc["artist"] = disc.artist
                    new_disc["year"] = disc.year
                    new_disc["cost"] = disc.cost
                    new_disc["price"] = disc.price
                    new_disc["gender"] = disc.gender
                    new_disc["amount"] = disc.amount

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
                    disc = Discs(discs[i]["id"],discs[i]["title"],discs[i]["artist"],discs[i]["year"],discs[i]["cost"],discs[i]["price"],discs[i]["gender"],discs[i]["amount"])
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
        total_1 = 0
        buy_list = []
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
            content = data.read()
            data.close()
            if content == "":
                print("Lo siento en estos momentos no hay nada en la base de datos")  
            else:
                data = open("Database.txt", "r")
                for x in data:
                    i = 0
                    disc = Discs(x.split(",")[i],x.split(",")[i+1],x.split(",")[i+2],x.split(",")[i+3],x.split(",")[i+4],x.split(",")[i+5],x.split(",")[i+6],x.split(",")[i+7])
                    new_disc = {}
                    new_disc["id"] = disc.id
                    new_disc["title"] = disc.title
                    new_disc["artist"] = disc.artist
                    new_disc["year"] = disc.year
                    new_disc["cost"] = disc.cost
                    new_disc["price"] = disc.price
                    new_disc["gender"] = disc.gender
                    new_disc["amount"] = disc.amount

                    discs.append(new_disc)
                print("Esto son los discos en la base de datos")
                i = 1

                for x in discs:
                    print(f"-----------{i}----------------")
                    print(x)
                    i += 1
            while True:
                sorted_by = input("Ordenar por: \n1.Orden alfabético \n2.Año de lanzamiento \n3.Precio \n4.Género \n> ")
                while not sorted_by.isnumeric() or int(sorted_by) not in range(1,5):
                    print("Elija un orden válido")
                    sorted_by = input("Ordenar por: \n1.Orden alfabético \n2.Año de lanzamiento \n3.Precio \n4.Género \n> ")


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

                    buy = input("Indique el número de disco que desea comprar: ")
                    while not buy.isnumeric() or int(buy) < 0 or int(buy) -1 not in range(0,len(sorted_alpha)):
                        print("Ingresa un número de disco válido")
                        buy = input("Indique el número de disco que desea comprar: ")

                    
                    amount_1 = input("Cantidad que desea comprar: ")
                    while not amount_1.isnumeric() or int(amount_1) <= 0 or int(amount_1) > int(sorted_alpha[int(buy)-1]["amount"]):
                        print("Elija una cantidad válida")
                        amount_1 = input("Cantidad que desea comprar: ")
                    
                    total_1 += int(amount_1) * int(sorted_alpha[int(buy)-1]["price"])
                    print(total_1)
                    buy_list.append(sorted_alpha[int(buy)-1])
                    sorted_alpha[int(buy)-1]["amount"] = int(sorted_alpha[int(buy)-1]["amount"].replace("\n","")) - int(amount_1)
                    buy_list[int(buy)-1]["amount"] = amount_1

                elif sorted_by == "2":
                    print("------------------Catálogo en orden de año de lanzamiento-----------------")
                    print()
                    sorted_year = sorted(discs, key = lambda i: i["year"])
                    i = 1
                    for x in sorted_year:
                        print(f"----------{i}----------")
                        print(x)
                        i +=1

                    
                elif sorted_by == "3":
                    print("------------------Catálogo en orden de precio-----------------")
                    print()
                    sorted_title = sorted(discs, key = lambda i: i["price"])
                    i = 1
                    for x in sorted_title:
                        print(f"----------{i}----------")
                        print(x)
                        i += 1
                else:
                    genders = []
                    for x in discs:
                        if x["gender"] not in genders:
                            genders.append(x["gender"])
                    
                    i = 1
                    for x in genders:
                        print(f"{i}.{x}")
                    

                    sort_gender = input("Escriba el género a ordenar: ").title()
                    while not sort_gender.isalpha() or sort_gender not in genders:
                        print("Error, escriba un genero válido")
                        sort_gender = input("Escriba el género a ordenar: ").title()
          
                option = input("Desea realizar otra compra: \n1.Sí \n2.No \n> ")
                while not option.isnumeric() or int(option) not in range(1,3):
                    print("Introduzca una opción valida")
                    option = input("Desea realizar otra compra: \n1.Sí \n2.No \n> ")
                if option == "1":
                    True
                else:
                    break

        while True:
            print(buy_list)
            check = input("Selecciones: \n1.Finalizar compra \n2.Eliminar disco \n3.> ")
            while not check.isnumeric() or int(check) not in range(1,3):
                print("Elija una opción válida")
                check = input("Selecciones: \n1.Finalizar compra \n2.Eliminar disco \n> ")

            if check == "1":
                i = 0
                for x in buy_list:
                    print(f"-----{i}-----")
                    buy_disc = Discs(x["id"],x["title"],x["artist"],x["year"],x["cost"],x["price"],x["gender"],amount_1)
                    buy_disc.mostrar()
                    total_d = int(amount_1) * int(x["price"])
                    print(f"Monto: {total_d}")
                    i+=1
                print(f"Monto total a pagar: {total_1}$")
            else:
                i = 1
                for x in buy_list:
                    print(f"-----{i}-----")
                    print(x)
                    i += 1

                delete = input("Ingrese el numero del articulo a elminar: ")
                while not delete.isnumeric() or int(delete) - 1 not in range(0,len(buy_list)):
                    print("Ingrese un número de artículo válido")
                    delete = input("Ingrese el numero del articulo a elminar: ")

                buy_list.pop(int(delete)-1)
                total -= buy_list[int(delete)-1]["price"]
                print(f"Articulo eliminado número {delete}")
                print()
                i = 1
                for x in buy_list:
                    print(f"-----{i}-----")
                    print(x)
                    i += 1
            break



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
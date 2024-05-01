from dataclasses import dataclass, field


@dataclass
class Autores:
    nombre: str
    nacionalidad: str


@dataclass
class Obras:
    id: int
    nombre: str
    paginas: int
    autor: Autores
    genero: str
    precio: int
    cant_libros: int
    calificacion: str = field(init=False)
    obras: list = field(init=False, default_factory=list)



    def administar_obra(self):
        opcion = 1
        while opcion != 0:
            print("\nEn el servicio de Administrar Obra tenemos las siguientes opciones")
            print("1. Agregar Obra")
            print("2. Eliminar Obra")
            print("3. Modificar Obra")
            print("4. Ver Obras Agregadas")
            print("0. Regresar")
            opcion = int(input())
            print("\n")

            if opcion == 1:
                print("INGRESE LA SIGUIENTE INFORMACION")
                id = int(input("ID de la obra: "))
                nombre = input("El nombre de la obra: ")
                paginas = int(input("El numero de paginas: "))
                autor = Autores(input("Nombre del autor: "), input("Nacionalidad del autor: "))
                genero = input("El genero: ")
                precio = int(input("Precio: "))
                cant_libros = int(input("Cuantos libros hay de esta obra: "))
                self.agregar_obra(id, nombre, paginas, autor, genero, precio, cant_libros)

            elif opcion == 2:
                id = int(input("Ingrese el ID de la obra que desea eliminar: "))
                self.eliminar_obra(id)

            elif opcion == 3:
                self.modificar_obra()

            elif opcion == 4:
                self.ver_obras_agregadas()

            else:
                print("-Ingrese una opcion correcta-")

    def agregar_obra(self, id: int, nombre: str, paginas: int, autor: Autores, genero: str, precio: int, cant_libros: int):
        obra = Obras(id, nombre, paginas, autor, genero, precio, cant_libros)
        self.obras.append(obra)


    def eliminar_obra(self, id: int):
        for obra in self.obras:
            if obra.id == id:
                self.obras.remove(obra)
                print("-La Obra se eliminó correctamente-\n")
                return
        print("No se encontró la obra con ese ID.")

    def modificar_obra(self):
        opcion = 1
        while opcion != 0:
            id = int(input("Ingrese el ID del obra que desea modificar: "))
            print("Seleccione qué desea modificar")
            print("1. Precio")
            print("2. Cantidad de libros")
            print("0. Regresar")
            opcion = int(input())
            print("\n")
            if opcion == 1:
                nv_precio = int(input("Ingrese el nuevo precio que va a tener la obra: "))
                self.m_precio(id, nv_precio)
            elif opcion == 2:
                nv_cantidad = int(input("Ingrese la nueva cantidad de libros que hay de esa obra: "))
                self.m_cantidad_libros(id, nv_cantidad)
            else:
                print("-Ingrese una opcion correcta-")

    def m_precio(self, id: int, nv_precio: int):
        for obra in self.obras:
            if obra.id == id:
                obra.precio = nv_precio
                print("-El Precio se ha modificado correctamente-\n")
                return
        print("No se encontró la obra con ese ID.")

    def m_cantidad_libros(self, id: int, nv_cantidad: int):
        for obra in self.obras:
            if obra.id == id:
                obra.cant_libros = nv_cantidad
                print("-La Cantidad de Libros se ha modificado correctamente-\n")
                return
        print("No se encontró la obra con ese ID.")

    def ver_obras_agregadas(self):
        if self.obras:
            print("Obras en Catálogo:")
            for obra in self.obras:
                print(f"ID: {obra.id}, Nombre: {obra.nombre}, Autor: {obra.autor.nombre}")
        else:
            print("No hay obras agregadas.")


@dataclass
class Usuarios:
    documento: str
    nombre: str
    telefono: str
    correo: str
    libro_prestado: bool = field(init=False, default=False)
    usuarios: list = field(init=False, default_factory=list)

    def administrar_usuario(self):
        opcion = 1
        while opcion != 0:
            print("SELECCIONE LA OPCION QUE DESEA REALIZAR")
            print("1. Agregar Usuario")
            print("2. Eliminar Usuario")
            print("3. Ver Correos Registrados")
            print("0. Salir")
            opcion = int(input())
            print("\n")
            if opcion == 1:
                print("Ingrese la siguiente informacion")
                documento = input("Documento: ")
                nombre = input("Nombre: ")
                telefono = input("Teléfono: ")
                correo = input("COrreo: ")
                self.agregar_usuario(documento, nombre, telefono, correo)

            if opcion == 2:
                documento = input("Ingrese el documento del usuario que desea eliminar: ")
                self.eliminar_usuario(documento)

            if opcion == 3:
                self.ver_correos_agregados()

            else:
                print("-Ingrese una opcion correcta")

    def agregar_usuario(self, documento: str, nombre: str, telefono: str, correo: str):
        usuario = Usuarios(documento, nombre, telefono, correo)
        self.usuarios.append(usuario)
        print("El Usuario ha sido agregado correctamente\n")

    def eliminar_usuario(self, documento: str):
        for usuario in self.usuarios:
            if usuario.documento == documento:
                self.usuarios.remove(usuario)
                print("El Usuario ha sido eliminado correctamente\n")
                return
        print("No se encontró el usuario con ese documento.")

    def ver_correos_agregados(self):
        print("Correos Agregados:")
        for usuario in self.usuarios:
            print(usuario.correo)




obras_iniciales = [
    Obras(1, "Principito", 200, Autores("Antoine de Saint", "Francia"), "Infantil", 120000, 5),
    Obras(2, "Harry Potter y la piedra filosofal", 300, Autores("J.K. Rowling", "Reino Unido"), "Fantasía", 150000, 8),
    Obras(3, "Cien años de soledad", 432, Autores("Gabriel García Márquez", "Colombia"), "Realismo mágico", 180000, 6),
    Obras(4, "Don Quijote de la Mancha", 863, Autores("Miguel de Cervantes", "España"), "Novela de caballería", 200000, 7),
    Obras(5, "1984", 328, Autores("George Orwell", "Reino Unido"), "Ciencia ficción", 140000, 5),
    Obras(6, "El señor de los anillos: La comunidad del anillo", 576, Autores("J.R.R. Tolkien", "Reino Unido"), "Fantasía", 170000, 9),
    Obras(7, "El amor en los tiempos del cólera", 368, Autores("Gabriel García Márquez", "Colombia"), "Romance", 150000, 4),
    Obras(8, "Moby Dick", 544, Autores("Herman Melville", "Estados Unidos"), "Novela de aventuras", 160000, 6),
    Obras(9, "Orgullo y prejuicio", 432, Autores("Jane Austen", "Reino Unido"), "Novela romántica", 140000, 8),
    Obras(10, "El retrato de Dorian Gray", 254, Autores("Oscar Wilde", "Irlanda"), "Novela gótica", 130000, 7)
]

biblioteca = Obras(0, "", 0, Autores("", ""), "", 0, 0)

biblioteca.obras.extend(obras_iniciales)

usuario = Usuarios("documento", "nombre", "telefono", "correo")
obra = Obras(1, "Principito", 200, Autores("Antoine de Saint", "Francia"), "Infantil", 120000, 5)
usuario = Usuarios("documento", "nombre", "telefono", "correo")


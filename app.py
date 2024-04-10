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
        print("Seleccione la opcion que desea realizar")
        print("1. Agregar Obra")
        print("2. Eliminar Obra")
        print("3. Modificar Obra")
        print("0. Salir")
        opcion = 1
        while opcion != 0:
            opcion = int(input())
            if opcion == 1:
                print("Ingrese la siguiente informacion")
                id: int = int(input("ID de la obra: "))
                nombre: str = input("El nombre de la obra: ")
                paginas: int = int(input("El numero de paginas: "))
                autor: Autores = Autores(input("Nombre del autor: "), input("Nacionalidad del autor: "))
                genero: str = input("El genero: ")
                precio: int = int(input("Precio: "))
                cant_libros: int = int(input("Cuantos libros hay de esta obra"))
                self.agregar_obra(id, nombre, paginas, autor, genero, precio, cant_libros)

            elif opcion == 2:
                id: int = int(input("Ingrese el ID de la obra que desea eliminar: "))
                self.eliminar_obra(id)

            elif opcion == 3:
                self.modificar_obra()

            else:
                print("-Ingrese una opcion correcta-")

    def agregar_obra(self, id: int, nombre: str, paginas: int, autor: Autores, genero: str, precio: int,
                     cant_libros: int):
        obra = Obras(id, nombre, paginas, autor, genero, precio, cant_libros)
        self.obras.append(obra)
        return "-La Obra ha sido agregada correctamente-"

    def eliminar_obra(self, id: int):
        for obra in self.obras:
            if obra.id == id:
                del obra
            else:
                print("Ingrese el ID de una obra existente")
        return "-La Obra se elimino correctamente-"

    def modificar_obra(self):
        id = int(input("Ingrese el ID del obra que desea modificar: "))
        print("Seleccione que desea modificar")
        print("1. Precio")
        print("2. Cantidad de libros")
        print("0.Regresar")
        opcion = 1
        while opcion != 0:
            opcion = int(input())
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
        return "-El Precio se ha modificado correctamente-"

    def m_cantidad_libros(self, id: int, nv_cantidad: int):
        for obra in self.obras:
            if obra.id == id:
                obra.cantidad_libros = nv_cantidad
        return "-La Cantidad de Libros se ha modificado correctamente-"


@dataclass
class Usuarios:
    documento: str
    nombre: str
    telefono: str
    correo: str
    libro_prestado: bool = field(init=False, default=False)
    usuarios: list = field(init=False, default_factory=list)

    def administrar_usuario(self):
        print("Seleccione la opcion que desea realizar")
        print("1. Agrgar Usuario")
        print("2. Eliminar Usuario")
        print("0. Salir")
        opcion = 1
        while opcion != 0:
            if opcion == 1:
                print("Ingrese la siguiente informacion")
                documento: str = input("El documento: ")
                nombre: str = input("El nombre: ")
                telefono: str = input("El telefono: ")
                correo: str = input("El correo")
                self.agregar_usuario(documento, nombre, telefono, correo)

            if opcion == 2:
                documento: str = input("Ingrese el documento del usuario que desea eliminar: ")
                self.eliminar_usuario(documento)

            else:
                print("-Ingrese una opcion correcta")

    def agregar_usuario(self, documento: str, nombre: str, telefono: str, correo: str):
        usuario = Usuarios(documento, nombre, telefono, correo)
        self.usuarios.append(usuario)
        return "El Usuario ha sido agregado correctamente"

    def eliminar_usuario(self, documento: str):
        for usuario in self.usuarios:
            if usuario.documento == documento:
                del usuario
            else:
                print("-Ingrese el documento de un usuario existente")
        return "El Usuario ha sido eliminado correctamente"

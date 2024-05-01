from dataclasses import dataclass, field

from app import biblioteca


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

    def __eq__(self, other):
        if isinstance(other, Obras):
            return self.id == other.id
        return False

    def agregar_obra(self, id: int, nombre: str, paginas: int, autor: Autores, genero: str, precio: int, cant_libros: int):
        obra = Obras(id, nombre, paginas, autor, genero, precio, cant_libros)
        self.obras.append(obra)

    def eliminar_obra(self, id: int):
        for obra in self.obras:
            if obra.id == id:
                self.obras.remove(obra)

    def m_precio(self, id: int, nv_precio: int):
        for obra in self.obras:
            if obra.id == id:
                obra.precio = nv_precio

    def m_cantidad_libros(self, id: int, nv_cantidad: int):
        for obra in self.obras:
            if obra.id == id:
                obra.cant_libros = nv_cantidad

    def ver_obras_agregadas(self) -> str:
        str = ""
        if self.obras:
            for obra in self.obras:
                str += f"ID: {obra.id}, Nombre: {obra.nombre}, Autor: {obra.autor.nombre}\n"
        return str


@dataclass
class Usuarios:
    documento: str
    nombre: str
    telefono: str
    correo: str
    libro_prestado: bool = field(init=False, default=False)
    usuarios: list = field(init=False, default_factory=list)

    def agregar_usuario(self, documento: str, nombre: str, telefono: str, correo: str):
        usuario = Usuarios(documento, nombre, telefono, correo)
        self.usuarios.append(usuario)

    def eliminar_usuario(self, documento: str):
        for usuario in self.usuarios:
            if usuario.documento == documento:
                self.usuarios.remove(usuario)

    def ver_correos_agregados(self):
        str = ""
        for usuario in self.usuarios:
            str += f"El correo de {usuario.nombre} es {usuario.correo}\n"
        return str


def prestar_libro(documento: str, id_libro: int):
    usuario_encontrado = None
    for usuario in Usuarios.usuarios:
        if usuario.documento == documento:
            usuario_encontrado = usuario

    obra_encontrada = None
    for libro in biblioteca.obras:
        if libro.id == id_libro:
            obra_encontrada = libro

    if usuario_encontrado is not None and obra_encontrada is not None:
        obra_encontrada.cant_libros -= 1
        usuario_encontrado.libro_prestado = True

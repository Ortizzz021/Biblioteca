from typing import List
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

    def _eq_(self, other):
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

def prestar_libro(documento: str, id_libro: int, obras: List[Obras], usuarios: List[Usuarios]):
    usuario_encontrado = next((usuario for usuario in usuarios if usuario.documento == documento), None)
    obra_encontrada = next((obra for obra in obras if obra.id == id_libro), None)

    if usuario_encontrado is not None and obra_encontrada is not None:
        obra_encontrada.cant_libros -= 1
        usuario_encontrado.libro_prestado = True

# Ejemplo de uso:
if _name_ == "_main_":
    obra1 = Obras(id=1, nombre="El principito", paginas=100, autor=Autores(nombre="Antoine de Saint-Exupéry", nacionalidad="Francés"), genero="Infantil", precio=10, cant_libros=5)
    obra2 = Obras(id=2, nombre="Don Quijote de la Mancha", paginas=500, autor=Autores(nombre="Miguel de Cervantes", nacionalidad="Español"), genero="Clásico", precio=15, cant_libros=8)
    obras_disponibles = [obra1, obra2]

    usuario1 = Usuarios(documento="123456789", nombre="Juan", telefono="123456789", correo="juan@example.com")
    usuario2 = Usuarios(documento="987654321", nombre="María", telefono="987654321", correo="maria@example.com")
    usuarios_registrados = [usuario1, usuario2]

    prestar_libro(documento="123456789", id_libro=1, obras=obras_disponibles, usuarios=usuarios_registrados)

    for obra in obras_disponibles:
        print(f"ID: {obra.id}, Nombre: {obra.nombre}, Cantidad de libros disponibles: {obra.cant_libros}")

    for usuario in usuarios_registrados:
        print(f"Usuario: {usuario.nombre}, Libro prestado: {usuario.libro_prestado}")
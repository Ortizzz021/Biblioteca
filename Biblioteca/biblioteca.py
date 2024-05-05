from dataclasses import dataclass, field
from typing import List, Any

from Biblioteca.autores import Autores
from Biblioteca.obras import Obras
from Biblioteca.usuarios import Usuarios


@dataclass
class Biblioteca:
    obras: list = field(init=False, default_factory=list)
    usuarios: list = field(init=False, default_factory=list)

    def agregar_obra(self, id: int, nombre: str, paginas: int, autor: Autores, genero: str, precio: int,
                     cant_libros: int):
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

def buscar_obras(works: List[Obras], criterio: str, valor: Any) -> List[Obras]:
    """Busca obras por diferentes criterios."""
    result = []
    for obra in works:
        if criterio == "precio" and obra.precio == valor:
            result.append(obra)
        elif criterio == "genero" and obra.genero.lower() == valor.lower():
            result.append(obra)
        elif criterio == "autor" and obra.autor.nombre.lower() == valor.lower():
            result.append(obra)
        elif criterio == "paginas" and obra.paginas == valor:
            result.append(obra)
        elif criterio == "nombre" and obra.nombre.lower() == valor.lower():
            result.append(obra)
    return result

def prestar_libro(self, documento: str, id_libro: int):
    usuario_encontrado = None
    for usuario in self.usuarios:
        if usuario.documento == documento:
            usuario_encontrado = usuario

        obra_encontrada = None
        for obra in self.obras:
            if obra.id == id_libro:
                obra_encontrada = obra

        if usuario_encontrado is not None and obra_encontrada is not None:
            obra_encontrada.cant_libros -= 1
            obra_encontrada.disponible = False
            usuario_encontrado.libros_prestados += 1
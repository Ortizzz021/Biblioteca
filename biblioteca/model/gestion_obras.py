from dataclasses import dataclass, field

from biblioteca.model import Autor
from biblioteca.model.gestion_humana import GestionHumana
from biblioteca.model.obra import Obra


@dataclass
class GestionObras:
    obras: list = field(init=False, default_factory=list)

    def agregar_obra(self, id: int, nombre: str, paginas: int, autor: Autor, genero: str, precio: int,
                     cant_libros: int):
        obra = Obra(id, nombre, paginas, autor, genero, precio, cant_libros)
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
        result = ""
        if self.obras:
            for obra in self.obras:
                prestado = "Sí" if not obra.disponible else "No"
                if not obra.disponible:
                    usuario_prestamo = next(
                        (usuario for usuario in GestionHumana.usuarios if usuario.documento == obra.usuario_prestamo),
                        None)
                    correo_prestamo = f" ({usuario_prestamo.correo})" if usuario_prestamo else ""
                else:
                    correo_prestamo = ""
                result += f"ID: {obra.id}, Nombre: {obra.nombre}, Autor: {obra.autor.nombre}, Prestado: {prestado}{correo_prestamo}\n"
        else:
            result += "No hay obras agregadas"
        return result

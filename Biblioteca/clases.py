# clases.py

from typing import List, Any
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
    calificacion_total: float = field(default=0.0)
    calificaciones_count: int = field(default=0)
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
        str_result = ""
        if self.obras:
            for obra in self.obras:
                str_result += f"ID: {obra.id}, Nombre: {obra.nombre}, Autor: {obra.autor.nombre}\n"
        return str_result

    def calificar_obra(self, calificacion: float):
        """Califica una obra."""
        if 0 <= calificacion <= 10:  # Asumiendo que las calificaciones están en un rango de 0 a 10
            self.calificacion_total += calificacion
            self.calificaciones_count += 1

    def calcular_promedio_calificacion(self) -> float:
        """Calcula el promedio de calificación de la obra."""
        if self.calificaciones_count > 0:
            return self.calificacion_total / self.calificaciones_count
        else:
            return 0.0

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


@dataclass
class Usuarios:
    documento: str = ""
    nombre: str = ""
    telefono: str = ""
    correo: str = ""
    libro_prestado: bool = False

    def agregar_usuario(self, documento: str, nombre: str, telefono: str, correo: str):
        self.documento = documento
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def eliminar_usuario(self):
        self.documento = ""
        self.nombre = ""
        self.telefono = ""
        self.correo = ""

    def ver_correos_agregados(self):
        if self.correo:
            return f"El correo de {self.nombre} es {self.correo}\n"
        else:
            return ""


def prestar_libro(documento: str, id_libro: int, obras: List[Obras], usuarios: List[Usuarios]):
    usuario_encontrado = next((usuario for usuario in usuarios if usuario.documento == documento), None)
    obra_encontrada = next((obra for obra in obras if obra.id == id_libro), None)

    if usuario_encontrado is not None and obra_encontrada is not None:
        obra_encontrada.cant_libros -= 1
        usuario_encontrado.libro_prestado = True

        print("Obras Disponibles:")
        for obra in obras:  # Iteramos sobre todas las obras disponibles
            print(f"ID: {obra.id}, Nombre: {obra.nombre}, Cantidad de libros disponibles: {obra.cant_libros}")

        for usuario in usuarios:  # Iteramos sobre todos los usuarios registrados
            print(f"Usuario: {usuario.nombre}, Libro prestado: {usuario.libro_prestado}")
    else:
        print("El usuario o la obra no fueron encontrados.")


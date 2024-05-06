from dataclasses import dataclass, field

from Biblioteca.autores import Autores


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
    disponible: bool = field(init=False, default=True)
    calificacion_total: float = field(default=0.0)
    calificaciones_count: int = field(default=0)


    def __eq__(self, other):
        if isinstance(other, Obras):
            return self.id == other.id
        return False
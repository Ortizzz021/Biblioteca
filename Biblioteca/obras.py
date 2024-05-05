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


    def __eq__(self, other):
        if isinstance(other, Obras):
            return self.id == other.id
        return False
from dataclasses import dataclass, field

@dataclass
class Usuarios:
        documento: str
        nombre: str
        telefono: str
        correo: str
        libros_prestados: int = field(init=False, default=False)
from dataclasses import dataclass, field

from biblioteca.model.usuario import Usuario


@dataclass
class GestionHumana:
    usuarios: list = field(init=False, default_factory=list)

    def agregar_usuario(self, documento: str, nombre: str, telefono: str, correo: str):
        usuario = Usuario(documento, nombre, telefono, correo)
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

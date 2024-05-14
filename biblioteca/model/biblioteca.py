import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dataclasses import dataclass, field
from typing import Any

from biblioteca.model.autor import Autor
from biblioteca.model.obra import Obra
from biblioteca.model.usuario import Usuario

@dataclass
class Biblioteca:
    obras: list = field(init=False, default_factory=list)
    usuarios: list = field(init=False, default_factory=list)

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
                        (usuario for usuario in self.usuarios if usuario.documento == obra.usuario_prestamo), None)
                    correo_prestamo = f" ({usuario_prestamo.correo})" if usuario_prestamo else ""
                else:
                    correo_prestamo = ""
                result += f"ID: {obra.id}, Nombre: {obra.nombre}, Autor: {obra.autor.nombre}, Prestado: {prestado}{correo_prestamo}\n"
        else:
            result += "No hay obras agregadas"
        return result

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

    def buscar_obras(self, criterio: str, valor: Any) -> list[Obra]:
        """Busca obras por diferentes criterios."""
        result = []
        if criterio == "precio":
            if valor == "Menos de 100.000":
                result = [obra for obra in self.obras if obra.precio < 100000]
            elif valor == "100.000 - 200.000":
                result = [obra for obra in self.obras if 100000 <= obra.precio < 200000]
            elif valor == "200.000 - 300.000":
                result = [obra for obra in self.obras if 200000 <= obra.precio < 300000]
            elif valor == "Más de 300.000":
                result = [obra for obra in self.obras if obra.precio >= 300000]
        elif criterio == "genero":
            result = [obra for obra in self.obras if obra.genero.lower() == valor.lower()]
        elif criterio == "autor":
            result = [obra for obra in self.obras if obra.autor.nombre.lower() == valor.lower()]
        elif criterio == "paginas":
            if valor == "Menos de 50":
                result = [obra for obra in self.obras if obra.paginas < 50]
            elif valor == "50 - 100":
                result = [obra for obra in self.obras if 50 <= obra.paginas < 100]
            elif valor == "100 - 150":
                result = [obra for obra in self.obras if 100 <= obra.paginas < 150]
            elif valor == "Más de 150":
                result = [obra for obra in self.obras if obra.paginas >= 150]
        elif criterio == "nombre":
            result = [obra for obra in self.obras if obra.nombre.lower() == valor.lower()]
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

    def calificar_obra(self, calificacion: float):
        if 0 <= calificacion <= 10:
            Obra.calificacion_total += calificacion
            Obra.calificaciones_count += 1

    def calcular_promedio_calificacion(self) -> float:
        if Obra.calificaciones_count > 0:
            return Obra.calificacion_total / Obra.calificaciones_count
        else:
            return 0.0

    def notificaiones(self, destinatario: str, asunto: str, mensaje: str):
        message = Mail(
            from_email='bibliotecajdpython@gmail.com',
            to_emails=destinatario,
            subject=asunto,
            plain_text_content=mensaje)

        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(str(e))


    def agregar_obras_predeterminadas(self):

        obra1 = (Biblioteca, 1, "El principito", 120, "Saint_Exupery", "Ficción", 120000, 3)
        obra2 = (Biblioteca, 2, "El priipito", 120, "Saint_Exupery", "Ficción", 120000, 3)

        self.obras.append(obra1)
        self.obras.append(obra2)
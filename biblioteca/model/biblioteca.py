import smtplib
import ssl
from email.message import EmailMessage

from biblioteca.model import Autor
from biblioteca.model.gestion_humana import GestionHumana
from biblioteca.model.gestion_obras import GestionObras
from biblioteca.model.obra import Obra


class Biblioteca:
    def __init__(self):
        self.gestion_obras: GestionObras = GestionObras()
        self.gestion_humana: GestionHumana = GestionHumana()
        self.obra: Obra = Obra(0, "", 0, Autor("", ""), "", 0, 0)

    def buscar_obras(self, criterio, valor):

        if criterio == "precio":
            result = [obra for obra in self.gestion_obras.obras if 100000 <= obra.precio < 200000]
        elif criterio == "genero":
            result = [obra for obra in self.gestion_obras.obras if obra.genero.lower() == valor.lower()]
        elif criterio == "autor":
            result = [obra for obra in self.gestion_obras.obras if obra.autor.nombre.lower() == valor.lower()]
        elif criterio == "paginas":
            result = [obra for obra in self.gestion_obras.obras if obra.paginas < 50]
        elif criterio == "nombre":
            result = [obra for obra in self.gestion_obras.obras if obra.nombre.lower() == valor.lower()]
        else:
            result = []

        return result

    def prestar_libro(self, documento: str, id_libro: int):
        destinatario = ""
        mensaje = ""
        usuario_encontrado = None
        for usuario in self.gestion_humana.usuarios:
            if usuario.documento == documento:
                usuario_encontrado = usuario
                destinatario = usuario.correo
                break

        obra_encontrada = None
        for obra in self.gestion_obras.obras:
            if obra.id == id_libro:
                obra_encontrada = obra
                mensaje = obra.nombre
                break

        if usuario_encontrado is not None and obra_encontrada is not None:
            obra_encontrada.cant_libros -= 1
            obra_encontrada.disponible = False
            obra_encontrada.usuario_prestamo = usuario_encontrado.documento
            usuario_encontrado.libros_prestados += 1

        self.notificaciones(destinatario, "Prestamo Libro", f"El libro {mensaje} fue prestado con exito, que lo disfrutes.")

    def calificar_obra(self, id_obra: int, calificacion: float):
        if 0 <= calificacion <= 10:
            for obra in self.gestion_obras.obras:
                if obra.id == id_obra:
                    obra.calificacion_total += calificacion
                    obra.calificaciones_count += 1

    def calcular_promedio_calificacion(self) -> float:
        if self.obra.calificaciones_count > 0:
            return self.obra.calificacion_total / self.obra.calificaciones_count
        else:
            return 0.0

    def notificaciones(self, destinatario: str, asunto: str, mensaje: str):
        emisor = "bibliotecajdpython@gmail.com"
        contrasena = "wiew xwwr drpg udfc"
        destinatario = destinatario
        asunto_correo = asunto
        mensaje_correo = mensaje

        em = EmailMessage()
        em["From"] = emisor
        em["To"] = destinatario
        em["Subject"] = asunto_correo
        em.set_content(mensaje_correo)

        contexto = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=contexto) as smtp:
                smtp.login(emisor, contrasena)
                smtp.sendmail(emisor, destinatario, em.as_string())
        except smtplib.SMTPRecipientsRefused as e:
            print(f"Error al enviar correo: {e}")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

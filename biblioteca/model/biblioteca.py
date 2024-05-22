from dataclasses import dataclass
from typing import Any

from biblioteca.model.gestion_humana import GestionHumana
from biblioteca.model.gestion_obras import GestionObras
from biblioteca.model.obra import Obra


@dataclass
class Biblioteca:
    def __init__(self):
        self.gestion_obras = GestionObras()

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
        usuario_encontrado = None
        for usuario in GestionHumana().usuarios:
            if usuario.documento == documento:
                usuario_encontrado = usuario
                break

        obra_encontrada = None
        for obra in GestionObras().obras:
            if obra.id == id_libro:
                obra_encontrada = obra
                break

        if usuario_encontrado is not None and obra_encontrada is not None:
            obra_encontrada.cant_libros -= 1
            obra_encontrada.disponible = False
            obra_encontrada.usuario_prestamo = usuario_encontrado.documento
            usuario_encontrado.libros_prestados += 1

    def calificar_obra(self, id_obra: int, calificacion: float):
        if 0 <= calificacion <= 10:
            for obra in GestionObras().obras:
                if obra.id == id_obra:
                    obra.calificacion_total += calificacion
                    obra.calificaciones_count += 1

    def calcular_promedio_calificacion(self) -> float:
        if Obra.calificaciones_count > 0:
            return Obra.calificacion_total / Obra.calificaciones_count
        else:
            return 0.0

    def notificaciones(self, destinatario: str, asunto: str, mensaje: str):
        pass
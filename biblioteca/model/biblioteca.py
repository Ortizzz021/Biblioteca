from dataclasses import dataclass
from typing import Any

from biblioteca.model.gestion_humana import GestionHumana
from biblioteca.model.gestion_obras import GestionObras
from biblioteca.model.obra import Obra


@dataclass
class Biblioteca:
    def buscar_obras(self, criterio: str, valor: Any) -> list[Obra]:
        result = []
        if criterio == "precio":
            if valor == "Menos de 100.000":
                result = [obra for obra in GestionObras.obras if obra.precio < 100000]
            elif valor == "100.000 - 200.000":
                result = [obra for obra in GestionObras.obras if 100000 <= obra.precio < 200000]
            elif valor == "200.000 - 300.000":
                result = [obra for obra in GestionObras.obras if 200000 <= obra.precio < 300000]
            elif valor == "Más de 300.000":
                result = [obra for obra in GestionObras.obras if obra.precio >= 300000]
        elif criterio == "genero":
            result = [obra for obra in GestionObras.obras if obra.genero.lower() == valor.lower()]
        elif criterio == "autor":
            result = [obra for obra in GestionObras.obras if obra.autor.nombre.lower() == valor.lower()]
        elif criterio == "paginas":
            if valor == "Menos de 50":
                result = [obra for obra in GestionObras.obras if obra.paginas < 50]
            elif valor == "50 - 100":
                result = [obra for obra in GestionObras.obras if 50 <= obra.paginas < 100]
            elif valor == "100 - 150":
                result = [obra for obra in GestionObras.obras if 100 <= obra.paginas < 150]
            elif valor == "Más de 150":
                result = [obra for obra in GestionObras.obras if obra.paginas >= 150]
        elif criterio == "nombre":
            result = [obra for obra in GestionObras.obras if obra.nombre.lower() == valor.lower()]
        return result

    def prestar_libro(self, documento: str, id_libro: int):
        usuario_encontrado = None
        for usuario in GestionHumana.usuarios:
            if usuario.documento == documento:
                usuario_encontrado = usuario

            obra_encontrada = None
            for obra in GestionObras.obras:
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
        pass

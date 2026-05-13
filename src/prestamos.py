"""Módulo de gestión de préstamos."""
from datetime import datetime, timedelta

class Prestamo:
    DIAS_PRESTAMO = 14  # versión A: 14 días

    def __init__(self, isbn, usuario):
        self.isbn = isbn
        self.usuario = usuario
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=self.DIAS_PRESTAMO)
    
    def esta_vencido(self):
        return datetime.now() > self.fecha_devolucion
    
    def __str__(self):
        return f"Préstamo: {self.isbn} → {self.usuario} | Vence: {self.fecha_devolucion.date()}"
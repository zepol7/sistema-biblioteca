"""Módulo de gestión de préstamos."""
from datetime import datetime, timedelta

class Prestamo:
    DIAS_PRESTAMO = 7   # Política institucional: 7 días (aprobado por CCB-2024-05)

    def __init__(self, isbn, usuario):
        self.isbn = isbn
        self.usuario = usuario
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=self.DIAS_PRESTAMO)
    
    def esta_vencido(self):
        return datetime.now() > self.fecha_devolucion

    def dias_restantes(self):
        delta = self.fecha_devolucion - datetime.now()
        return max(0, delta.days)
    
    def __str__(self):
        return f"Préstamo: {self.isbn} → {self.usuario} | Vence: {self.fecha_devolucion.date()} | Días restantes: {self.dias_restantes()}"
from abc import ABC
from abc import abstractmethod


class Servicio(ABC):

    def __init__(
        self,
        codigo,
        nombre,
        precio_base
    ):
        self.codigo = codigo
        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(
        self,
        descuento=0,
        impuesto=0
    ):
        pass

    @abstractmethod
    def mostrar_detalle(self):
        pass
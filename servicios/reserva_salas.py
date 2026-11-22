from modelos.servicio import Servicio


class ReservaSalas(Servicio):

    def __init__(
        self,
        codigo,
        nombre,
        precio_base,
        capacidad
    ):
        super().__init__(
            codigo,
            nombre,
            precio_base
        )
        self.capacidad = capacidad

    def calcular_costo(
        self,
        descuento=0,
        impuesto=0
    ):

        costo = self.precio_base

        costo -= costo * descuento

        costo += costo * impuesto

        return costo

    def mostrar_detalle(self):

        print(
            f"Servicio: {self.nombre}"
        )

        print(
            f"Capacidad: {self.capacidad}"
        )
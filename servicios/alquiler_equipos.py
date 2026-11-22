from modelos.servicio import Servicio


class AlquilerEquipos(Servicio):

    def __init__(
        self,
        codigo,
        nombre,
        precio_base,
        tipo_equipo
    ):
        super().__init__(
            codigo,
            nombre,
            precio_base
        )

        self.tipo_equipo = tipo_equipo

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
            f"Equipo: {self.tipo_equipo}"
        )

from modelos.servicio import Servicio


class Asesoria(Servicio):

    def __init__(
        self,
        codigo,
        nombre,
        precio_base,
        especialista
    ):
        super().__init__(
            codigo,
            nombre,
            precio_base
        )

        self.especialista = especialista

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
            f"Especialista: {self.especialista}"
        )
        

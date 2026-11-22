from excepcioness.excepcioness_personalizadas import ReservaError


class Reserva:

    def __init__(
        self,
        cliente,
        servicio,
        fecha,
        duracion,
        costo_total,
        descuento,
        impuesto
    ):

        self.cliente = cliente
        self.servicio = servicio
        self.fecha = fecha
        self.duracion = duracion

        self.descuento = descuento
        self.impuesto = impuesto

        self.costo_total = costo_total

        self.estado = "Pendiente"

    def confirmar(self):

        if self.estado == "Cancelada":
            raise ReservaError(
                "No se puede confirmar una reserva cancelada."
            )

        self.estado = "Confirmada"

    def cancelar(self):

        if self.estado == "Procesada":
            raise ReservaError(
                "No se puede cancelar una reserva procesada."
            )

        self.estado = "Cancelada"

    def procesar(self):

        if self.estado == "Cancelada":
            raise ReservaError(
                "No se puede procesar una reserva cancelada."
            )

        if self.estado != "Confirmada":
            raise ReservaError(
                "Solo se pueden procesar reservas confirmadas."
            )

        self.estado = "Procesada"

    def mostrar_reserva(self):

        print("\n===== RESERVA =====")

        print(
            f"Cliente: {self.cliente.nombre}"
        )

        print(
            f"Fecha: {self.fecha}"
        )

        print(
            f"Duración: {self.duracion} horas"
        )

        print(
            f"Estado: {self.estado}"
        )

        print(
            f"Descuento: {self.descuento * 100:.0f}%"
        )

        print(
            f"Impuesto: {self.impuesto * 100:.0f}%"
        )

        print(
            f"Costo Total: ${self.costo_total:,.0f}"
        )

        self.servicio.mostrar_detalle()

        print(
            f"Precio Base por Hora: ${self.servicio.precio_base:,.0f}"
        )

        print(
            f"Descuento: {self.descuento * 100:.0f}%"
        )

        print(
            f"Impuesto: {self.impuesto * 100:.0f}%"
        )

        print(
            f"Costo Total: ${self.costo_total:,.0f}"
        )
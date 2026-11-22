class Cliente:

    def __init__(
        self,
        identificacion,
        nombre,
        correo,
        telefono
    ):
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    @property
    def nombre(self):
        return self.__nombre

    @property
    def identificacion(self):
        return self.__identificacion

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def mostrar_datos(self):

        print(
            f"Cliente: {self.__nombre}"
        )

        print(
            f"Correo: {self.__correo}"
        )

        print(
            f"Teléfono: {self.__telefono}"
        )
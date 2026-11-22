class Cliente:
    def __init__(self, identificacion, nombre, correo, telefono):
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    def mostrar_datos(self):
        print("Identificación:", self.identificacion)
        print("Nombre:", self.nombre)
        print("Correo:", self.correo)
        print("Teléfono:", self.telefono)

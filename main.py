from modelos.cliente import Cliente
from modelos.reserva import Reserva

from servicios.reserva_salas import ReservaSalas
from servicios.alquiler_equipos import AlquilerEquipos
from servicios.asesorias import Asesoria

from utilidades.logger import registrar_log

from excepcioness.excepcioness_personalizadas import *

from datetime import datetime
import re

clientes = []
reservas = []
servicios = []


def validar_fecha(fecha):

    try:

        datetime.strptime(
            fecha,
            "%d/%m/%Y"
        )

        return fecha

    except ValueError as e:

        raise FechaNoValidaError(
            "La fecha debe estar en formato dd/mm/aaaa."
        ) from e


def registrar_cliente():

    try:

        identificacion = input(
            "Identificación: "
        )

        if identificacion.strip() == "":
            raise ClienteNoValidoError(
                "La identificación es obligatoria."
            )

        nombre = input(
            "Nombre: "
        )

        if nombre.strip() == "":
            raise ClienteNoValidoError(
                "El nombre es obligatorio."
            )

        correo = input(
            "Correo: "
        )

        patron = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

        if not re.match(
            patron,
            correo,
            re.IGNORECASE
        ):
            raise CorreoNoValidoError(
                "Correo inválido."
            )

        telefono = input(
            "Teléfono: "
        )

        if not telefono.isdigit():

            raise TelefonoNoValidoError(
                "El teléfono debe ser numérico."
            )

        cliente = Cliente(
            identificacion,
            nombre,
            correo,
            telefono
        )

        clientes.append(cliente)

    except Exception as e:

        registrar_log(
            f"ERROR CLIENTE: {e}"
        )

        print(
            "\nERROR:",
            e
        )

    else:

        registrar_log(
            f"CLIENTE REGISTRADO: {nombre}"
        )

        print(
            "\nCliente registrado correctamente."
        )

    finally:

        registrar_log(
            "Finalizó proceso de registro de cliente."
        )


def crear_reserva():

    try:

        if len(clientes) == 0:

            raise ReservaError(
                "No existen clientes registrados."
            )

        cliente = clientes[-1]

        print(
            "\n1. Reserva de Salas"
        )

        print(
            "2. Alquiler de Equipos"
        )

        print(
            "3. Asesoría"
        )

        opcion = input(
            "Seleccione servicio: "
        )

        if opcion == "1":

            servicio = ReservaSalas(
                "S01",
                "Sala Premium",
                100000,
                20
            )

        elif opcion == "2":

            servicio = AlquilerEquipos(
                "E01",
                "Video Beam",
                50000,
                "Proyector"
            )

        elif opcion == "3":

            servicio = Asesoria(
                "A01",
                "Asesoría Técnica",
                150000,
                "Ingeniero Senior"
            )

        else:

            raise ServicioNoDisponibleError(
                "Servicio no disponible."
            )

        fecha = input(
            "Fecha (dd/mm/aaaa): "
        )

        validar_fecha(
            fecha
        )

        duracion = int(
            input(
                "Duración en horas: "
            )
        )

        descuento =  0.10

        impuesto = 0.19
                
        
        
        costo_base = (
            servicio.precio_base
            * duracion
        )

        costo_total = costo_base

        costo_total -= (
            costo_total
            * descuento
        )

        costo_total += (
            costo_total
            * impuesto
        )
        
        print(
            "\n===== DETALLE DEL COSTO ====="
        )

        print(
            f"Servicio seleccionado: {servicio.nombre}"
        )

        print(
            f"\nCosto por Hora: ${servicio.precio_base:,.0f}"
        )

        print(
            f"Duración: {duracion} horas"
        )

        print(
            f"Subtotal: ${costo_base:,.0f}"
        )

        print(
            f"Descuento Institucional: {descuento * 100:.0f}%"
        )

        print(
            f"IVA: {impuesto * 100:.0f}%"
        )

        print(
            f"Costo Total: ${costo_total:,.0f}"
        )

        servicios.append(
            servicio
        )

        reserva = Reserva(
            cliente,
            servicio,
            fecha,
            duracion,
            costo_total,
            descuento,
            impuesto
        )

        reservas.append(
            reserva
        )

        registrar_log(
            "Reserva creada."
        )

        print(
            "\nReserva registrada."
        )

    except Exception as e:

        registrar_log(
            f"ERROR RESERVA: {e}"
        )

        print(
            "\nERROR:",
            e
        )


def mostrar_reservas():

    if len(reservas) == 0:

        print(
            "\nNo existen reservas."
        )

        return

    for i, reserva in enumerate(reservas):

        print(
            f"\nReserva #{i+1}"
        )

        reserva.mostrar_reserva()


def mostrar_clientes():

    if len(clientes) == 0:

        print(
            "\nNo existen clientes registrados."
        )

        return

    for i, cliente in enumerate(clientes):

        print(
            f"\n===== CLIENTE #{i+1} ====="
        )

        print(
            f"Identificación: {cliente.identificacion}"
        )

        print(
            f"Nombre: {cliente.nombre}"
        )

        print(
            f"Correo: {cliente.correo}"
        )

        print(
            f"Teléfono: {cliente.telefono}"
        )        


def confirmar_reserva():

    try:

        indice = int(
            input(
                "Número de reserva: "
            )
        )

        reservas[indice - 1].confirmar()

        registrar_log(
            "Reserva confirmada"
        )

        print(
            "Reserva confirmada."
        )

    except Exception as e:

        print(
            "ERROR:",
            e
        )


def cancelar_reserva():

    try:

        indice = int(
            input(
                "Número de reserva: "
            )
        )

        reservas[indice - 1].cancelar()

        registrar_log(
            "Reserva cancelada"
        )

        print(
            "Reserva cancelada."
        )

    except Exception as e:

        print(
            "ERROR:",
            e
        )

def procesar_reserva():

    try:

        if len(reservas) == 0:

            raise ReservaError(
                "No existen reservas registradas."
            )

        indice = int(
            input(
                "Número de reserva: "
            )
        )

        reservas[indice - 1].procesar()

        registrar_log(
            "Reserva procesada."
        )

        print(
            "\nReserva procesada correctamente."
        )

    except Exception as e:

        registrar_log(
            f"ERROR PROCESAR RESERVA: {e}"
        )

        print(
            "\nERROR:",
            e
        )

def simular_operaciones():

    print(
        "\n===== INICIO SIMULACIÓN ====="
    )

    registrar_log(
        "Inicio simulación automática."
    )

    try:

        # Operación 1
        print(
            "\n1. Cliente válido"
        )

        cliente_prueba = Cliente(
            "999999",
            "Cliente Prueba",
            "cliente@prueba.com",
            "3001234567"
        )

        clientes.append(
            cliente_prueba
        )

        registrar_log(
            "Cliente válido creado."
        )

        # Operación 2
        print(
            "\n2. Correo inválido"
        )

        try:

            raise CorreoNoValidoError(
                "Correo inválido."
            )

        except CorreoNoValidoError as e:

            registrar_log(
                f"ERROR: {e}"
            )

        # Operación 3
        print(
            "\n3. Teléfono inválido"
        )

        try:

            raise TelefonoNoValidoError(
                "Teléfono inválido."
            )

        except TelefonoNoValidoError as e:

            registrar_log(
                f"ERROR: {e}"
            )

        # Operación 4
        print(
            "\n4. Fecha inválida"
        )

        try:

            validar_fecha(
                "99/99/9999"
            )

        except Exception as e:

            registrar_log(
                f"ERROR FECHA: {e}"
            )

        # Operación 5
        print(
            "\n5. Reserva válida"
        )

        servicio = ReservaSalas(
            "S99",
            "Sala Simulación",
            100000,
            30
        )

        costo_base = (
            servicio.precio_base
            * 2
        )

        descuento = 0.10

        impuesto = 0.19

        costo_total = costo_base

        costo_total -= (
            costo_total
            * descuento
        )

        costo_total += (
            costo_total
            * impuesto
        )

        reserva = Reserva(
            cliente_prueba,
            servicio,
            "30/10/2026",
            2,
            costo_total,
            descuento,
            impuesto
        )

        reservas.append(
            reserva
        )

        registrar_log(
            "Reserva válida creada."
        )

        # Operación 6
        print(
            "\n6. Confirmar reserva"
        )

        reserva.confirmar()

        registrar_log(
            "Reserva confirmada."
        )

        # Operación 7
        print(
            "\n7. Procesar reserva"
        )

        reserva.procesar()

        registrar_log(
            "Reserva procesada."
        )

        # Operación 8
        print(
            "\n8. Intentar cancelar procesada"
        )

        try:

            reserva.cancelar()

        except Exception as e:

            registrar_log(
                f"ERROR: {e}"
            )

        # Operación 9
        print(
            "\n9. Servicio inexistente"
        )

        try:

            raise ServicioNoDisponibleError(
                "Servicio inexistente."
            )

        except Exception as e:

            registrar_log(
                f"ERROR: {e}"
            )

        # Operación 10
        print(
            "\n10. Confirmar reserva cancelada"
        )

        try:

            reserva.estado = "Cancelada"

            reserva.confirmar()

        except Exception as e:

            registrar_log(
                f"ERROR: {e}"
            )

    finally:

        registrar_log(
            "Fin simulación automática."
        )

        print(
            "\n===== FIN SIMULACIÓN ====="
        )

def menu():

    while True:

        print("\n===== SOFTWARE FJ =====")

        print("1. Registrar Cliente")
        print("2. Crear Reserva")
        print("3. Confirmar Reserva")
        print("4. Cancelar Reserva")
        print("5. Procesar Reserva")
        print("6. Mostrar Reservas")
        print("7. Mostrar Clientes")
        print("8. Simular Operaciones")
        print("9. Salir")

        opcion = input(
            "\nSeleccione una opción: "
        )

        if opcion == "1":

            registrar_cliente()

        elif opcion == "2":

            crear_reserva()

        elif opcion == "3":

            confirmar_reserva()

        elif opcion == "4":

            cancelar_reserva()

        elif opcion == "5":

            procesar_reserva()

        elif opcion == "6":

            mostrar_reservas()

        elif opcion == "7":

            mostrar_clientes()

        elif opcion == "8":

            simular_operaciones()

        elif opcion == "9":    

            registrar_log(
                "Aplicación finalizada."
            )

            print(
                "\nVuelve pronto, feliz día."
            )

            break

        else:

            print(
                "\nOpción inválida."
            )

if __name__ == "__main__":

    menu()
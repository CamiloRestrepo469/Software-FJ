

from abc import ABC, abstractmethod
import logging
import os

# =====================================================
# CONFIGURACION LOGS
# =====================================================

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# =====================================================
# EXCEPCIONES PERSONALIZADAS
# =====================================================

class ClienteInvalidoError(Exception):
    pass

class ServicioInvalidoError(Exception):
    pass

class ReservaError(Exception):
    pass

class ServicioNoDisponibleError(Exception):
    pass


# =====================================================
# CLASE ABSTRACTA
# =====================================================

class Entidad(ABC):

    @abstractmethod
    def mostrar_info(self):
        pass


# =====================================================
# CLIENTE
# =====================================================

class Cliente(Entidad):

    def __init__(self, nombre, correo, telefono):

        self.set_nombre(nombre)
        self.set_correo(correo)
        self.set_telefono(telefono)

    # Encapsulación

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):

        if not nombre.strip():
            raise ClienteInvalidoError(
                "El nombre no puede estar vacío"
            )

        self.__nombre = nombre

    def get_correo(self):
        return self.__correo

    def set_correo(self, correo):

        if "@" not in correo:
            raise ClienteInvalidoError(
                "Correo inválido"
            )

        self.__correo = correo

    def get_telefono(self):
        return self.__telefono

    def set_telefono(self, telefono):

        if not str(telefono).isdigit():
            raise ClienteInvalidoError(
                "Teléfono inválido"
            )

        self.__telefono = telefono

    def mostrar_info(self):

        return (
            f"Cliente: {self.__nombre} | "
            f"{self.__correo} | "
            f"{self.__telefono}"
        )

# =====================================================
# LUIS FELIPE GONZALEZ CLAVIJO
# =====================================================

class Servicio(ABC):

    def __init__(self, nombre, costo_base):

        if costo_base <= 0:
            raise ServicioInvalidoError(
                "Costo base inválido"
            )

        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(
        self,
        impuesto=0,
        descuento=0
    ):
        pass

    @abstractmethod
    def describir(self):
        pass

    @abstractmethod
    def validar_parametros(self):
        pass
# =====================================================
# BRAYAN DANIEL MENA MEDRANO
# =====================================================

class Reserva:

    def __init__(self,
                 cliente,
                 servicio,
                 duracion):

        if cliente is None:
            raise ReservaError(
                "Cliente no válido"
            )

        if servicio is None:
            raise ReservaError(
                "Servicio no válido"
            )

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):

        if self.estado == "Cancelada":
            raise ReservaError(
                "No puede confirmarse"
            )

        self.estado = "Confirmada"

    def cancelar(self):

        self.estado = "Cancelada"

    def procesar(self):

        try:

            costo = self.servicio.calcular_costo()

            logging.info(
                f"Reserva procesada: {costo}"
            )

            return costo

        except Exception as e:

            logging.error(str(e))

            raise ReservaError(
                "Error al procesar reserva"
            ) from e

    def mostrar_info(self):

        return (
            f"{self.cliente.get_nombre()} - "
            f"{self.servicio.nombre} - "
            f"{self.estado}"
        )


# =====================================================
# PRUEBAS
# =====================================================

def ejecutar_pruebas():

    print("\n========== SOFTWARE FJ ==========\n")

    # OPERACION 1

    try:

        cliente1 = Cliente(
            "Juan Perez",
            "juan@gmail.com",
            "3001234567"
        )

        print(cliente1.mostrar_info())

    except Exception as e:

        logging.error(e)

    # OPERACION 2

    try:

        cliente2 = Cliente(
            "Ana Gomez",
            "ana@gmail.com",
            "3111111111"
        )

        print(cliente2.mostrar_info())

    except Exception as e:

        logging.error(e)

    # OPERACION 3

    try:

        Cliente(
            "",
            "correo@gmail.com",
            "123456"
        )

    except ClienteInvalidoError as e:

        print("ERROR:", e)
        logging.error(e)

    # OPERACION 4

    try:

        Cliente(
            "Pedro",
            "correo_malo",
            "123456"
        )

    except ClienteInvalidoError as e:

        print("ERROR:", e)
        logging.error(e)

    # OPERACION 5

    try:

        sala = ReservaSala(
            "Sala Principal",
            4,
            50000
        )

        print(sala.describir())

    except Exception as e:

        logging.error(e)

    # OPERACION 6

    try:

        equipo = AlquilerEquipo(
            "Portátil",
            3,
            40000
        )

        print(equipo.describir())

    except Exception as e:

        logging.error(e)

    # OPERACION 7

    try:

        asesoria = AsesoriaEspecializada(
            "Ingeniero Senior",
            5,
            80000
        )

        print(asesoria.describir())

    except Exception as e:

        logging.error(e)

    # OPERACION 8

    try:

        servicio_malo = ReservaSala(
            "Sala Error",
            5,
            -1000
        )

    except ServicioInvalidoError as e:

        print("ERROR:", e)
        logging.error(e)

    # OPERACION 9

    try:

        reserva = Reserva(
            cliente1,
            sala,
            4
        )

        reserva.confirmar()

    except ReservaError as e:

        print(e)

    else:

        print(
            "Reserva confirmada correctamente"
        )

    # OPERACION 10

    try:

        costo = reserva.procesar()

        print(
            f"Costo reserva: ${costo:,.0f}"
        )

    except Exception as e:

        print(e)

    finally:

        print(
            "Proceso de reserva finalizado"
        )

    # OPERACION 11
    # Encadenamiento de excepciones

    try:

        try:

            valor = int("abc")

        except ValueError as e:

            raise ReservaError(
                "Conversión inválida"
            ) from e

    except ReservaError as e:

        print("ERROR:", e)

    print("\nSistema funcionando correctamente.")




# =====================================================
# CARLOS HERNAN GALEANO HERRERA
# CLASE RESERVA
# =====================================================
class Reserva:

    def __init__(self, cliente, servicio, duracion):
        if cliente is None:
            raise ReservaError("La reserva necesita un cliente válido")

        if servicio is None:
            raise ReservaError("La reserva necesita un servicio válido")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        if self.estado == "Cancelada":
            raise ReservaError("No se puede confirmar una reserva cancelada")
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar(self):
# Calcula el costo final de la reserva.
               
        try:
            self.servicio.verificar_disponibilidad()
            costo = self.servicio.calcular_costo()
            logging.info(f"Reserva procesada correctamente. Costo: {costo}")
            return costo

        except ServicioNoDisponibleError as e:
            logging.error(str(e))
            raise ReservaError("No se pudo procesar la reserva") from e

        except Exception as e:
            logging.error(str(e))
            raise ReservaError("Error inesperado al procesar la reserva") from e

    def mostrar_info(self):
        return f"{self.cliente.get_nombre()} - {self.servicio.nombre} - {self.estado}"



# =====================================================
# MAIN NO BORAR NADA
# =====================================================

if __name__ == "__main__":

    ejecutar_pruebas()

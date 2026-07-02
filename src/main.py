

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





# =====================================================
# BRAYAN DANIEL MENA MEDRANO
# =====================================================




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
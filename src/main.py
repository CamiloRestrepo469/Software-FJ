

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




# =====================================================
# CARLOS HERNAN GALEANO HERRERA
# =====================================================



# =====================================================
# MAIN NO BORAR NADA
# =====================================================

if __name__ == "__main__":

    ejecutar_pruebas()
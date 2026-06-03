# Clase base para cualquier servicio del homelab
class Servicio:
    def __init__(self, nombre, puerto):
        self.nombre = nombre
        self.puerto = puerto

    def info(self):
        print(f"Servicio: {self.nombre} | Puerto: {self.puerto}")

    def estado(self):
        print(f"Comprobando {self.nombre}...")

# Servicios específicos heredan de Servicio
class ServidorWeb(Servicio):
    def __init__(self, nombre, puerto, dominio):
        super().__init__(nombre, puerto)
        self.dominio = dominio

    def info(self):
        super().info()
        print(f"Dominio: {self.dominio}")

class BaseDatos(Servicio):
    def __init__(self, nombre, puerto, base):
        super().__init__(nombre, puerto)
        self.base = base

    def info(self):
        super().info()
        print(f"Base de datos: {self.base}")

# Usar las clases
nginx = ServidorWeb("Nginx", 80, "ivanlabnexus.duckdns.org")
mariadb = BaseDatos("MariaDB", 3306, "homelab_db")

nginx.info()
print("---")
mariadb.info()
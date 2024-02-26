class Marca:
    def __init__(self,nombre,estado):
        self._nombre = nombre
        self._estado = estado
    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre
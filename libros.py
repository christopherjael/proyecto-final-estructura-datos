class Libro:

    def __init__(self, codigo: int, titulo: str, apellido_autor: str, nombre_autor: str, area_conocimiento: str, publicador: str, tramo_asignado: str, estado: str = "en sala"):
        self.codigo = codigo
        self.titulo = titulo
        self.apellido_autor = apellido_autor
        self.nombre_autor = nombre_autor
        self.area_conocimiento = area_conocimiento
        self.publicador = publicador
        self.tramo_asignado = tramo_asignado
        self.estado = estado

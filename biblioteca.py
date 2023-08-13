from prettytable import PrettyTable
import csv
from os import path
from libros import Libro

pt = PrettyTable()

pt.field_names = ["codigo", "titulo", "apellido_autor", "nombre_autor",
                  "area_conocimiento", "publicador", "tramo_asignado", "estado"]


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.archivo_csv = './data/libros.csv'

    # cargar libros desde un archivo csv
    def cargar_csv_libros(self):
        with open(self.archivo_csv, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for fila in reader:
                self.libros.append(Libro(int(fila['codigo']), fila['titulo'], fila['apellido_autor'], fila['nombre_autor'],
                                         fila['area_conocimiento'], fila['publicador'], fila['tramo_asignado'], fila['estado']))
        file.close()

    # guardar los libros en un archivo csv
    def guardar_csv_libros(self):
        if (not path.exists(self.archivo_csv)):
            open(self.archivo_csv, 'a').close()

        with open(self.archivo_csv, mode='w', newline='', encoding='utf-8') as file:
            # limiar el archivo antes de guardar la nueva data
            file.write("")
            fieldnames = ['codigo', 'titulo', 'apellido_autor', 'nombre_autor',
                          'area_conocimiento', 'publicador', 'tramo_asignado', 'estado']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            data = []
            for libro in self.libros:
                data.append({'codigo': libro.codigo, 'titulo': libro.titulo, 'apellido_autor': libro.apellido_autor, 'nombre_autor': libro.nombre_autor,
                             'area_conocimiento': libro.area_conocimiento, 'publicador': libro.publicador, 'tramo_asignado': libro.tramo_asignado, 'estado': libro.estado})
            writer.writerows(data)
            file.close()

    # guardar un nuevo libro
    def guardar_libro(self, libro):
        pt.clear_rows()
        libro.codigo = (self.libros[-1].codigo +
                        1) if len(self.libros) > 0 else 1
        self.libros.append(libro)
        pt.add_row([libro.codigo, libro.titulo, libro.apellido_autor, libro.nombre_autor,
                    libro.area_conocimiento, libro.publicador, libro.tramo_asignado, libro.estado])
        print("Nuevo libro agregado")
        print(pt.get_string())
        self.guardar_csv_libros()

    # modificar un libro
    def modificar_libro(self, codigo: int):
        for libro in self.libros:
            if libro.codigo == codigo:
                # pidindo los nuevos valores al usuario
                print("Info: Si no quieres modificar el campo solo preciona (Enter)")
                n_titulo = input(
                    f"Valor:({libro.titulo}) , Inserte el nuevo titulo: ")
                n_apellido_autor = input(
                    f"Valor:({libro.apellido_autor}) , Inserte el nuevo apellido del autor: ")
                n_nombre_autor = input(
                    f"Valor:({libro.nombre_autor}), Inserte el nuevo nombre del autor: ")
                n_area_conocimiento = input(
                    f"Valor:({libro.area_conocimiento}), Inserte la nueva area de conocimiento del libro: ")
                n_publicador = input(
                    f"Valor:({libro.publicador}), Inserte el nuevo publicador: ")
                n_tramo = input(
                    f"Valor:({libro.tramo_asignado}), Inserte el nuevo tramo asiganado: ")
                estado = int(input(
                    f"Valor:({libro.estado}), Inserte el nuevo estado 1 = en sala | 2 = prestado): "))
                n_estado = ''
                if estado == 1 and estado != '':
                    n_estado = 'en sala'
                elif estado == 2 and estado != '':
                    n_estado = "prestado"
                else:
                    n_estado == ''
                # modificarndo el libro
                libro.titulo = n_titulo if n_titulo != "" else libro.titulo
                libro.apellido_autor = n_apellido_autor if n_apellido_autor != "" else libro.apellido_autor
                libro.nombre_autor = n_nombre_autor if n_nombre_autor != "" else libro.nombre_autor
                libro.area_conocimiento = n_area_conocimiento if n_area_conocimiento != "" else libro.area_conocimiento
                libro.publicador = n_publicador if n_publicador != "" else libro.publicador
                libro.tramo_asignado = n_titulo if n_tramo != "" else libro.tramo_asignado
                libro.estado = n_estado if n_estado != "" else libro.estado
                self.guardar_csv_libros()
                break

    def consultar_libros(self):
        pt.clear_rows()
        for libro in self.libros:
            pt.add_row([libro.codigo, libro.titulo, libro.apellido_autor, libro.nombre_autor,
                       libro.area_conocimiento, libro.publicador, libro.tramo_asignado, libro.estado])
        print(pt.get_string())

    def buscar_libro(self, codigo: int):
        pt.clear_rows()
        for libro in self.libros:
            if libro.codigo == codigo:
                pt.add_row([libro.codigo, libro.titulo, libro.apellido_autor, libro.nombre_autor,
                            libro.area_conocimiento, libro.publicador, libro.tramo_asignado, libro.estado])
                print(pt.get_string())
                return libro
        print('No se encontro un libro con este codigo\n')
        return None

    def eliminar_libro(self, codigo):
        libro = self.buscar_libro(codigo)
        if libro:
            self.libros.remove(libro)
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")
        self.guardar_csv_libros()

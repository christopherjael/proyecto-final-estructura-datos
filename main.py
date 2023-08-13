from biblioteca import Biblioteca
from libros import Libro


def mostrar_opciones():
    print("Lista de opciones")
    print("------------------")
    print("1. Mostrar todos los libros")
    print("2. Buscar un libro")
    print("3. Agregar un libro")
    print("4. Modificar un libro")
    print("5. Eliminar un libro")
    print("0. Salir el programa")


if __name__ == "__main__":
    biblioteca = Biblioteca()
    biblioteca.cargar_csv_libros()

    while True:
        try:
            mostrar_opciones()
            opcion = int(input('Inserte una opcion: '))
            if opcion == 1:
                biblioteca.consultar_libros()
            elif opcion == 2:
                biblioteca.buscar_libro(
                    int(input('Inserte el codigo del libro que quiere buscar: ')))
            elif opcion == 3:
                titulo = input("Inserte el titulo: ")
                apellido_autor = input("Inserte el apellido del autor: ")
                nombre_autor = input("Inserte el nombre del autor: ")
                area_conocimiento = input(
                    "Inserte la area de conocimiento del libro: ")
                publicador = input("Inserte el publicador: ")
                tramo = input("Inserte el tramo asiganado: ")
                libro = Libro(0, titulo, apellido_autor,
                              nombre_autor, area_conocimiento, publicador, tramo)
                biblioteca.guardar_libro(libro)
                print("Libro agregado")
            elif opcion == 4:
                biblioteca.modificar_libro(
                    int(input("Inserte el codigo del libro que quiere modificar: ")))
                print("Libro modificado")
            elif opcion == 5:
                codigo = int(
                    input('Inserte el codigo del libro que quiere borrar: '))
                biblioteca.eliminar_libro(codigo)
            elif opcion == 0:
                print("Saliendo del programa")
                exit()
        except Exception as e:
            print(e)
            print("Saliendo del programa")
            exit()

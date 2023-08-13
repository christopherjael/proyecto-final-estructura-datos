# Sistema de biblioteca

<p>En la última reunión con el encargado de la biblioteca pública Nacional este se aquejo sobre lo tedioso que se hace el trabajo de préstamos de libros y control de inventario en la biblioteca. El lead del equipo de desarrollo ha propuesto desarrollar un software que les permita simplificar este proceso.</p>

<p>Para su demostración primero se desarrollara una app en consola en Python utilizando estructura de datos como lista para manejar la entrada y salida de los libros. Del libro se desea tener guardado código del libro, título del libro, apellido del autor, nombre del autor, Área de Conocimiento y publicador, tramo asignado.</p>

Por ahora el lead desea presentar esta opción básica luego se trabajaran los módulos:
<br>
<br>
<strong>Préstamo de libros</strong>

1. El encargado de biblioteca cambia el estado de los libros de “en sala” a “prestado”, mediante un lector.
   <br>
   <br>
   <strong>Autoservicio</strong>
2. El estudiante puede realizar operaciones de préstamo, renovación y devolución sin la intervención del encargado de biblioteca con la ayuda de un lector rfid y un equipo tipo kiosko.
   <br>
   <br>
   <strong>Salida de libros de biblioteca</strong>
3. Si un libro sale de la biblioteca con el estado “En sala”, el controlador conjuntamente con la antena dan aviso de la salida irregular.
   <br>
   <br>
   <strong>Criterios que se evaluaran:</strong>

- Si se puede guardar el libro
- Si se puede modificar un libro ya guardo con su código.
- Si se puede realizar consulta o mostrar un listado de los libros guardados.
- Si se puede realizar búsqueda en base a su código.
- Si se puede eliminar un libro en base a su código.

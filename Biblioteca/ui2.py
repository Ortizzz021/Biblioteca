from biblioteca import Autores, Obras, Usuarios, prestar_libro, buscar_obras

print("------------")
print("-BIENVENIDO-")
print("------------")
print("Esta es una aplicación de una biblioteca en la cual podrás hacer uso de nuestros servicios.\nLos servicios con los que contamos en estos momentos son: Administración de las Obras, Administración de los Usuarios y Prestar libros.")
print("Mas adelante agregaremos nuevos servicios.")
print("------------------------------------------\n")

opcion = 1
biblioteca = Obras(0, "", 0, Autores("", ""), "", 0, 0)
while opcion != 0:
    print("=INGRESE EL SERVICIO QUE DESEA UTILIZAR=\n")
    print("1. Administrar Obra")
    print("2. Administrar Usuario")
    print("3. Prestar Libro")
    print("4. Buscar Obras")
    print("0. Salir")
    opcion = int(input())
    print("\n")

    if opcion == 1:
        opcion_ao = 1
        while opcion_ao != 0:
            print("En el servicio de Administrar Obra tenemos las siguientes opciones")
            print("1. Agregar Obra")
            print("2. Eliminar Obra")
            print("3. Modificar Obra")
            print("4. Ver Obras Agregadas")
            print("0. Regresar")
            opcion_ao = int(input())
            print("\n")

            if opcion_ao == 1:
                print("INGRESE LA SIGUIENTE INFORMACION")
                id = int(input("ID de la obra: "))
                nombre = input("El nombre de la obra: ")
                paginas = int(input("El numero de paginas: "))
                autor = Autores(input("Nombre del autor: "), input("Nacionalidad del autor: "))
                genero = input("El genero: ")
                precio = int(input("Precio: "))
                cant_libros = int(input("Cuantos libros hay de esta obra: "))
                biblioteca.agregar_obra(id, nombre, paginas, autor, genero, precio, cant_libros)
                print("-La Obra ha sido agregada correctamente-\n")

            elif opcion_ao == 2:
                id = int(input("Ingrese el ID de la obra que desea eliminar: "))
                biblioteca.eliminar_obra(id)
                print("-La Obra se eliminó correctamente-\n")

            elif opcion_ao == 3:
                opcion_mo = 1
                while opcion_mo != 0:
                    id = int(input("Ingrese el ID del obra que desea modificar: "))
                    print("Seleccione qué desea modificar")
                    print("1. Precio")
                    print("2. Cantidad de libros")
                    print("0. Regresar")
                    opcion_mo = int(input())
                    print("\n")
                    if opcion_mo == 1:
                        nv_precio = int(input("Ingrese el nuevo precio que va a tener la obra: "))
                        biblioteca.m_precio(id, nv_precio)
                        print("-El Precio se ha modificado correctamente-\n")
                    elif opcion_mo == 2:
                        nv_cantidad = int(input("Ingrese la nueva cantidad de libros que hay de esa obra: "))
                        biblioteca.m_cantidad_libros(id, nv_cantidad)
                        print("-La Cantidad de Libros se ha modificado correctamente-\n")
                    elif opcion_mo != 0:
                        print("-Ingrese una opcion correcta-")

            elif opcion_ao == 4:
                print("Obras en Catálogo:")
                print(biblioteca.ver_obras_agregadas())  # Llamar a ver_obras_agregadas en la instancia de Obras

            elif opcion_ao != 0:
                print("-Ingrese una opcion correcta-")

    elif opcion == 2:
        opcion_au = 1
        while opcion_au != 0:
            print("En el servicio de Administrar Usuario tenemos las siguientes opciones")
            print("1. Agregar Usuario")
            print("2. Eliminar Usuario")
            print("3. Ver Correos Registrados")
            print("0. Salir")
            opcion_au = int(input())
            print("\n")

            if opcion_au == 1:
                print("INGRESE LA SIGUIENTE INFORMACION")
                documento = input("Documento: ")
                nombre = input("Nombre: ")
                telefono = input("Teléfono: ")
                correo = input("Correo: ")
                # Usuarios.agregar_usuario(documento, nombre, telefono, correo)
                print("-El Usuario ha sido agregado correctamente-\n")

            if opcion_au == 2:
                documento = input("Ingrese el documento del usuario que desea eliminar: ")
                # Usuarios.eliminar_usuario(documento)
                print("-El Usuario ha sido eliminado correctamente-\n")

            if opcion_au == 3:
                usuarios = Usuarios()
                correos_registrados = usuarios.ver_correos_agregados()
                if correos_registrados:
                    print("Correos Agregados:")
                    print(correos_registrados)
                else:
                    print("No se han agregado correos anteriormente.")
            else:
                print("-Ingrese una opcion correcta")

    elif opcion == 3:
        print("Para prestar un libro necesitamos saber la siguiente informacion")
        documento = input("Su documento: ")
        id_libro = int(input("El ID del libro que quiere prestar: "))
        prestar_libro(documento, id_libro, biblioteca.obras,[])  # Pasar la lista de obras como argumento a prestar_libro
        print("-El libro ha sido prestado correctamente-")

    elif opcion == 4:
        print("Buscar Obras")
        print("1. Por Precio")
        print("2. Por Género")
        print("3. Por Autor")
        print("4. Por Rango de Páginas")
        print("5. Por Nombre")
        print("0. Regresar")
        criterio = int(input("Seleccione el criterio de búsqueda: "))
        if criterio == 1:
            valor = int(input("Ingrese el precio a buscar: "))
        elif criterio == 2 or criterio == 3 or criterio == 5:
            valor = input("Ingrese el valor a buscar: ")
        elif criterio == 4:
            valor = int(input("Ingrese el rango de páginas a buscar: "))
        else:
            print("Opción no válida")
            continue

        if criterio == 4:
            valor_max = int(input("Ingrese el valor máximo del rango de páginas: "))
            obras_encontradas = buscar_obras(biblioteca.obras, "paginas", (valor, valor_max))
        else:
            criterios = ["", "precio", "genero", "autor", "nombre"]
            obras_encontradas = buscar_obras(biblioteca.obras, criterios[criterio], valor)

        if obras_encontradas:
            print("Obras Encontradas:")
            for obra in obras_encontradas:
                print(f"ID: {obra.id}, Nombre: {obra.nombre}, Autor: {obra.autor.nombre}")
        else:
            print("No se encontraron obras que coincidan con la búsqueda.")

    else:
        print("-Ingrese una opción correcta-")

print("-Gracias por utilizar nuestros servicios-\n-Que tenga buen día-")
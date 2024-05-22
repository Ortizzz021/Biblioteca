import tkinter as tk
from tkinter import messagebox

import pywhatkit

from biblioteca.model.autor import Autor
from biblioteca.model.biblioteca import Biblioteca
from biblioteca.model.gestion_humana import GestionHumana
from biblioteca.model.gestion_obras import GestionObras

biblioteca1 = Biblioteca()
gestion_humana = GestionHumana()
gestion_obras = GestionObras()


class BibliotecaApp(tk.Tk):
    title_font = ("Arial", 18)
    label_font = ("Arial", 12)
    button_bg = "#3B496F"
    button_fg = "#FFFFFF"

    def __init__(self):
        super().__init__()
        self.title("Aplicación de Biblioteca")
        self.geometry("600x500")
        self.resizable(width=False, height=False)
        self.configure(bg="#FFFFFF")
        self.menu_principal()

    def menu_principal(self):
        self.clear_window()

        tk.Label(self, text="BIENVENIDO", font=self.title_font, bg="#FFFFFF").pack(pady=20)

        tk.Button(self, text="Administrar Obra", command=self.administrar_obras,
                  font=self.label_font, bg=self.button_bg, fg=self.button_fg).pack(pady=10)
        tk.Button(self, text="Administrar Usuario", command=self.administrar_usuarios,
                  font=self.label_font, bg=self.button_bg, fg=self.button_fg).pack(pady=10)
        tk.Button(self, text="Prestar Libro", command=self.prestar_libro,
                  font=self.label_font, bg=self.button_bg, fg=self.button_fg).pack(pady=10)
        tk.Button(self, text="Buscar Obras", command=self.buscar_obras,
                  font=self.label_font, bg=self.button_bg, fg=self.button_fg).pack(pady=10)
        tk.Button(self, text="Calificar Obra", command=self.calificar_obra,
                  font=self.label_font, bg=self.button_bg, fg=self.button_fg).pack(pady=10)
        tk.Button(self, text="Salir", command=self.destroy,
                  font=self.label_font, bg=self.button_bg, fg=self.button_fg).pack(pady=10)

    def administrar_obras(self):
        self.clear_window()

        tk.Label(self, text="Administrar Obra", font=("Arial", 16)).pack(pady=10)

        tk.Button(self, text="Agregar Obra", command=self.agregar_obra).pack(pady=5)
        tk.Button(self, text="Eliminar Obra", command=self.eliminar_obra).pack(pady=5)
        tk.Button(self, text="Modificar Obra", command=self.modificar_obra).pack(pady=5)
        tk.Button(self, text="Ver Obras Agregadas", command=self.ver_obras_agregadas).pack(pady=5)
        tk.Button(self, text="Regresar", command=self.menu_principal).pack(pady=10)

    def administrar_usuarios(self):
        self.clear_window()

        tk.Label(self, text="Administrar Usuario", font=("Arial", 16)).pack(pady=10)

        tk.Button(self, text="Agregar Usuario", command=self.agregar_usuario).pack(pady=5)
        tk.Button(self, text="Eliminar Usuario", command=self.eliminar_usuario).pack(pady=5)
        tk.Button(self, text="Ver Correos Registrados", command=self.ver_correos_registrados).pack(pady=5)
        tk.Button(self, text="Regresar", command=self.menu_principal).pack(pady=10)

    def prestar_libro(self):
        self.clear_window()

        tk.Label(self, text="Prestar Libro", font=("Arial", 16)).pack(pady=10)

        tk.Label(self, text="Seleccione el usuario: ").pack()
        usuario_var = tk.StringVar(self)
        usuarios_registrados = [usuario.nombre for usuario in gestion_humana.usuarios]
        usuario_menu = tk.OptionMenu(self, usuario_var, *usuarios_registrados)
        usuario_menu.pack()

        tk.Label(self, text="Seleccione la obra disponible: ").pack()
        obra_var = tk.StringVar(self)
        obras_disponibles = [obra.nombre for obra in gestion_obras.obras if obra.disponible]
        obra_menu = tk.OptionMenu(self, obra_var, *obras_disponibles)
        obra_menu.pack()

        def prestar(usuario_var=usuario_var, obra_var=obra_var):
            usuario_seleccionado = usuario_var.get()
            obra_seleccionada = obra_var.get()

            usuario = next((usuario for usuario in gestion_humana.usuarios if usuario.nombre == usuario_seleccionado),
                           None)
            obra = next((obra for obra in gestion_obras.obras if obra.nombre == obra_seleccionada), None)

            if usuario is not None and obra is not None:
                biblioteca1.prestar_libro(usuario.documento, obra.id)
                messagebox.showinfo("Éxito", "El libro ha sido prestado correctamente.")
                pywhatkit.send_mail("bibliotecajdpython@gmail.com", "pqtu yadm anpv iiqf", "¡Felicitaciones!",f"Libro {obra.nombre} prestado correctamente, que lo disfrutes", usuario.correo)
                self.menu_principal()
            else:
                messagebox.showerror("Error", "Por favor, selecciona un usuario y una obra válidos.")

        tk.Button(self, text="Prestar", command=prestar).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.menu_principal).pack(pady=10)

    def buscar_obras(self):
        self.clear_window()

        tk.Label(self, text="Buscar Obras", font=("Arial", 16)).pack(pady=10)

        criterio_var = tk.StringVar(self)
        criterio_var.set("precio")
        criterio_menu = tk.OptionMenu(self, criterio_var, "precio", "género", "autor", "paginas", "nombre")
        criterio_menu.pack()

        self.dropdown_frame = tk.Frame(self)

        precio_var = tk.StringVar(self)
        genero_var = tk.StringVar(self)
        autor_var = tk.StringVar(self)
        paginas_var = tk.StringVar(self)
        nombre_var = tk.StringVar(self)
        def update_dropdowns(criterio):
            for widget in self.dropdown_frame.winfo_children():
                widget.destroy()

            if criterio == "precio":
                precios = ["Menos de 100.000", "100.000 - 200.000", "200.000 - 300.000", "Más de 300.000"]
                precio_var.set(precios[0])
                precio_menu = tk.OptionMenu(self.dropdown_frame, precio_var, *precios)
                precio_menu.pack()
            elif criterio == "genero":
                genero_options = ["Ficción", "Acción", "Misterio", "Romance", "Ciencia ficción", "Fantasía", "Aventura",
                                  "Comedia", "Terror", "Drama", "Suspenso"]
                genero_var.set(genero_options[0])
                genero_menu = tk.OptionMenu(self.dropdown_frame, genero_var, *genero_options)
                genero_menu.pack()
            elif criterio == "autor":
                autores = list(set([obra.autor.nombre for obra in gestion_obras.obras]))
                autor_var.set(autores[0])
                autor_menu = tk.OptionMenu(self.dropdown_frame, autor_var, *autores)
                autor_menu.pack()
            elif criterio == "paginas":
                rangos_paginas = ["Menos de 50", "50 - 100", "100 - 150", "Más de 150"]
                paginas_var.set(rangos_paginas[0])
                paginas_menu = tk.OptionMenu(self.dropdown_frame, paginas_var, *rangos_paginas)
                paginas_menu.pack()
            elif criterio == "nombre":
                nombres_obras = [obra.nombre for obra in gestion_obras.obras]
                nombre_var.set(nombres_obras[0])
                nombre_menu = tk.OptionMenu(self.dropdown_frame, nombre_var, *nombres_obras)
                nombre_menu.pack()

            self.dropdown_frame.pack(pady=10)

        update_dropdowns("precio")

        def criterio_changed(*args):
            criterio = criterio_var.get()
            update_dropdowns(criterio)

        criterio_var.trace("w", criterio_changed)

        def buscar():
            criterio = criterio_var.get()
            valor = None
            if criterio == "precio":
                valor = precio_var.get()
            elif criterio == "genero":
                valor = genero_var.get()
            elif criterio == "autor":
                valor = autor_var.get()
            elif criterio == "paginas":
                valor = paginas_var.get()
            elif criterio == "nombre":
                valor = nombre_var.get()

            obras_encontradas = biblioteca1.buscar_obras(criterio, valor)

            if obras_encontradas:
                messagebox.showinfo("Obras Encontradas", "\n".join([str(obra) for obra in obras_encontradas]))
            else:
                messagebox.showinfo("Obras Encontradas", "No se encontraron obras que coincidan con la búsqueda.")

        tk.Button(self, text="Buscar", command=buscar).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.menu_principal).pack(pady=10)

    def calificar_obra(self):
        self.clear_window()

        tk.Label(self, text="Calificar Obra", font=("Arial", 16)).pack(pady=10)

        obra_var = tk.StringVar(self)
        obras_agregadas = [obra.nombre for obra in gestion_obras.obras]
        obra_menu = tk.OptionMenu(self, obra_var, *obras_agregadas)
        obra_menu.pack(pady=5)

        tk.Label(self, text="Puntaje (1-10): ").pack()
        puntaje_entry = tk.Entry(self)
        puntaje_entry.pack()

        def calificar(obra_var=obra_var, puntaje_entry=puntaje_entry):
            obra_seleccionada = obra_var.get()
            puntaje = float(puntaje_entry.get())

            obra = next((obra for obra in gestion_obras.obras if obra.nombre == obra_seleccionada), None)

            if obra:
                biblioteca1.calificar_obra(obra.id, puntaje)
                messagebox.showinfo("Éxito", "La obra ha sido calificada correctamente.")
                self.menu_principal()
            else:
                messagebox.showerror("Error", "No se encontró la obra seleccionada.")

        tk.Button(self, text="Calificar", command=calificar).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.menu_principal).pack(pady=10)

        promedio_calificacion = biblioteca1.calcular_promedio_calificacion()
        tk.Label(self, text=f"Promedio de Calificación: {promedio_calificacion:.2f}").pack()

    def agregar_obra(self):
        self.clear_window()

        tk.Label(self, text="Agregar Obra", font=("Arial", 16)).pack(pady=10)

        tk.Label(self, text="ID de la obra: ").pack()
        id_entry = tk.Entry(self)
        id_entry.pack()

        tk.Label(self, text="Nombre de la obra: ").pack()
        nombre_entry = tk.Entry(self)
        nombre_entry.pack()

        tk.Label(self, text="Número de páginas: ").pack()
        paginas_entry = tk.Entry(self)
        paginas_entry.pack()

        tk.Label(self, text="Nombre del autor: ").pack()
        autor_nombre_entry = tk.Entry(self)
        autor_nombre_entry.pack()

        tk.Label(self, text="Nacionalidad del autor: ").pack()
        autor_nacionalidad_entry = tk.Entry(self)
        autor_nacionalidad_entry.pack()

        tk.Label(self, text="Género: ").pack()
        genero_var = tk.StringVar(self)
        genero_var.set("Ficción")
        genero_options = ["Ficción", "Acción", "Misterio", "Romance", "Ciencia ficción", "Fantasía", "Aventura",
                          "Comedia", "Terror", "Drama", "Suspenso"]
        genero_menu = tk.OptionMenu(self, genero_var, *genero_options)
        genero_menu.pack()

        tk.Label(self, text="Precio: ").pack()
        precio_entry = tk.Entry(self)
        precio_entry.pack()

        tk.Label(self, text="Cantidad de libros: ").pack()
        cant_libros_entry = tk.Entry(self)
        cant_libros_entry.pack()

        def agregar():
            try:
                id = int(id_entry.get())
                nombre = nombre_entry.get()
                paginas = int(paginas_entry.get())
                autor = Autor(autor_nombre_entry.get(), autor_nacionalidad_entry.get())
                genero = genero_var.get()
                precio = int(precio_entry.get())
                cant_libros = int(cant_libros_entry.get())
                gestion_obras.agregar_obra(id, nombre, paginas, autor, genero, precio, cant_libros)
                messagebox.showinfo("Éxito", "La obra ha sido agregada correctamente.")
                self.menu_principal()
            except ValueError:
                messagebox.showerror("Error",
                                     "Por favor, asegúrate de ingresar números enteros en los campos correspondientes.")

        tk.Button(self, text="Agregar", command=agregar).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.menu_principal).pack(pady=10)

    def eliminar_obra(self):
        self.clear_window()

        tk.Label(self, text="Eliminar Obra", font=("Arial", 16)).pack(pady=10)

        tk.Label(self, text="ID de la obra a eliminar: ").pack()
        id_entry = tk.Entry(self)
        id_entry.pack()

        def eliminar():
            id = int(id_entry.get())
            gestion_obras.eliminar_obra(id)
            messagebox.showinfo("Éxito", "La obra ha sido eliminada correctamente.")
            self.menu_principal()

        tk.Button(self, text="Eliminar", command=eliminar).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.menu_principal).pack(pady=10)

    def modificar_obra(self):
        self.clear_window()

        tk.Label(self, text="Modificar Obra", font=("Arial", 16)).pack(pady=10)

        obra_var = tk.StringVar(self)
        obras_agregadas = [obra.nombre for obra in gestion_obras.obras]
        obra_var.set(obras_agregadas[0])
        obra_menu = tk.OptionMenu(self, obra_var, *obras_agregadas)
        obra_menu.pack(pady=5)

        tk.Label(self, text="Selecciona qué deseas modificar: ").pack()

        mod_options = tk.StringVar(self)
        mod_options.set("Precio")
        mod_menu = tk.OptionMenu(self, mod_options, "Precio", "Cantidad de libros")
        mod_menu.pack()
        specific_frame = tk.Frame(self)

        def update_specific_frame(option):
            nonlocal specific_frame
            specific_frame.destroy()
            specific_frame = tk.Frame(self)
            if option == "Precio":
                tk.Label(specific_frame, text="Nuevo precio: ").pack()
                specific_frame.new_value_entry = tk.Entry(specific_frame)
                specific_frame.new_value_entry.pack()
            elif option == "Cantidad de libros":
                tk.Label(specific_frame, text="Nueva cantidad de libros: ").pack()
                specific_frame.new_value_entry = tk.Entry(specific_frame)
                specific_frame.new_value_entry.pack()
            specific_frame.pack()

        def on_option_change(*args):
            update_specific_frame(mod_options.get())

        mod_options.trace("w", on_option_change)

        update_specific_frame("Precio")

        def modificar():
            obra_seleccionada = obra_var.get()
            obra = next((obra for obra in gestion_obras.obras if obra.nombre == obra_seleccionada), None)
            if obra:
                option = mod_options.get()
                new_value = specific_frame.new_value_entry.get()
                if option == "Precio":
                    new_value = int(new_value)
                    gestion_obras.m_precio(obra.id, new_value)
                elif option == "Cantidad de libros":
                    new_value = int(new_value)
                    gestion_obras.m_cantidad_libros(obra.id, new_value)
                messagebox.showinfo("Éxito", "La obra ha sido modificada correctamente.")
                self.menu_principal()
            else:
                messagebox.showerror("Error", "No se encontró la obra seleccionada.")

        tk.Button(self, text="Modificar", command=modificar).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.menu_principal).pack(pady=10)

    def ver_obras_agregadas(self):
        self.clear_window()

        tk.Label(self, text="Obras Agregadas", font=("Arial", 16)).pack(pady=10)

        obras = gestion_obras.obras
        for obra in obras:
            tk.Label(self,
                     text=f"ID: {obra.id}, Nombre: {obra.nombre}, Autor: {obra.autor.nombre}, Precio: {obra.precio}, Cantidad: {obra.cant_libros}").pack()

        tk.Button(self, text="Regresar", command=self.menu_principal).pack(pady=10)

    def agregar_usuario(self):
        self.clear_window()

        tk.Label(self, text="Agregar Usuario", font=("Arial", 16)).pack(pady=10)

        tk.Label(self, text="Documento: ").pack()
        documento_entry = tk.Entry(self)
        documento_entry.pack()

        tk.Label(self, text="Nombre: ").pack()
        nombre_entry = tk.Entry(self)
        nombre_entry.pack()

        tk.Label(self, text="Teléfono: ").pack()
        telefono_entry = tk.Entry(self)
        telefono_entry.pack()

        tk.Label(self, text="Correo: ").pack()
        correo_entry = tk.Entry(self)
        correo_entry.pack()

        def agregar():
            documento = documento_entry.get()
            nombre = nombre_entry.get()
            telefono = telefono_entry.get()
            correo = correo_entry.get()
            pywhatkit.send_mail("bibliotecajdpython@gmail.com", "pqtu yadm anpv iiqf", "¡BIENVENIDO!", "Su registro ha sido exitoso", correo)
            gestion_humana.agregar_usuario(documento, nombre, telefono, correo)
            messagebox.showinfo("Éxito", "El usuario ha sido agregado correctamente.")
            self.menu_principal()

        tk.Button(self, text="Agregar", command=agregar).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.menu_principal).pack(pady=10)

    def eliminar_usuario(self):
        self.clear_window()

        tk.Label(self, text="Eliminar Usuario", font=("Arial", 16)).pack(pady=10)

        tk.Label(self, text="Documento del usuario a eliminar: ").pack()
        documento_entry = tk.Entry(self)
        documento_entry.pack()

        def eliminar():
            documento = documento_entry.get()
            gestion_humana.eliminar_usuario(documento)
            messagebox.showinfo("Éxito", "El usuario ha sido eliminado correctamente.")
            self.menu_principal()

        tk.Button(self, text="Eliminar", command=eliminar).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.menu_principal).pack(pady=10)

    def ver_correos_registrados(self):
        self.clear_window()

        tk.Label(self, text="Correos Registrados", font=("Arial", 16)).pack(pady=10)

        usuarios = gestion_humana.usuarios
        for usuario in usuarios:
            tk.Label(self, text=f"Nombre: {usuario.nombre}, Correo: {usuario.correo}").pack()

        tk.Button(self, text="Regresar", command=self.menu_principal).pack(pady=10)

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

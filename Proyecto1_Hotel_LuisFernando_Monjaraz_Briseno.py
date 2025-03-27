import tkinter as tk
from tkinter import messagebox, ttk
import re
from datetime import datetime, timedelta

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("300x150")
        self.root.configure(bg='black')

        tk.Label(root, text="Nombre de Usuario:", bg='black', fg='gold').place(x=10, y=30)
        self.username_entry = tk.Entry(root)
        self.username_entry.place(x=150, y=30)

        tk.Label(root, text="Contraseña:", bg='black', fg='gold').place(x=10, y=60)
        self.password_entry = tk.Entry(root, show='*')
        self.password_entry.place(x=150, y=60)

        btn_login = tk.Button(root, text="Iniciar Sesión", command=self.login, bg='gold')
        btn_login.place(x=150, y=90)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Verificar las credenciales
        if username == "LFMB" and password == "UDG":
            self.root.destroy()
            root = tk.Tk()
            app = Hotel(root)
            root.mainloop()
        else:
            messagebox.showerror("Error de inicio de sesión", "Credenciales incorrectas")


class Clientes:
    def __init__(self, id, nombre, direccion, telefono, email):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

class Reservaciones:
    def __init__(self, reservacionID, clienteNombre, habitacionID, fecha_Reservacion, hora_reservacion, fecha_salida, costo, fecha_salida2):
        self.reservacionID = reservacionID
        self.clienteNombre = clienteNombre
        self.habitacionID = habitacionID
        self.fecha_Reservacion = fecha_Reservacion
        self.hora_reservacion = hora_reservacion
        self.fecha_salida = fecha_salida
        self.costo = costo
        self.fecha_salida2 = fecha_salida2

class Habitacion:
    def __init__(self, habitacionID, numero_habitacion, estado):
        self.habitacionID = habitacionID
        self.numero_habitacion = numero_habitacion
        self.estado = estado  # Libre/Reservada/Cancelado

class Hotel:
    def __init__(self, root):
        self.clientes = []
        self.reservaciones = []
        self.habitaciones = []

        self.style = ttk.Style()
        self.style.configure("TNotebook", background='black')  # Color de fondo del notebook
        self.style.configure("TNotebook.Tab", background='black', foreground='gold')  # Color de fondo y texto de las pestañas
        root.title("Hotel")

        root.config(width=500, height=400)
        root.title("Hotel")
        root.configure(bg='black')

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both')

        # Pestaña original "Clientes"
        clientes_tab = ttk.Frame(self.notebook)
        self.notebook.add(clientes_tab, text="Clientes")
        self.style.configure("TFrame", background='black')  
        self.style.configure("TLabel", background='black', foreground='gold')

        tk.Label(clientes_tab, text="Buscar ID:", bg='black', fg='gold').place(x=250, y=10)
        self.txBuscarCliente = tk.Entry(clientes_tab)
        self.txBuscarCliente.place(x=360, y=10)

        btnBuscarCliente = tk.Button(clientes_tab, text="Buscar", command=self.buscarCliente, bg='gold')
        btnBuscarCliente.place(x=310, y=10)

        tk.Label(clientes_tab, text="ID:", bg='black', fg='gold').place(x=10, y=10)
        self.txId = tk.Entry(clientes_tab, state='disabled')
        self.txId.place(x=10, y=30)

        tk.Label(clientes_tab, text="Nombre", bg='black', fg='gold').place(x=10, y=50)
        self.txNombre = tk.Entry(clientes_tab, width=30, state='disabled')
        self.txNombre.place(x=10, y=70)

        tk.Label(clientes_tab, text="Dirección", bg='black', fg='gold').place(x=10, y=90)
        self.txDireccion = tk.Entry(clientes_tab, width=30, state='disabled')
        self.txDireccion.place(x=10, y=110)

        tk.Label(clientes_tab, text="Teléfono", bg='black', fg='gold').place(x=10, y=130)
        self.txTelefono = tk.Entry(clientes_tab, width=30, state='disabled')
        self.txTelefono.place(x=10, y=150)

        tk.Label(clientes_tab, text="Email:", bg='black', fg='gold').place(x=10, y=170)
        self.txEmail = tk.Entry(clientes_tab, width=30, state='disabled')
        self.txEmail.place(x=10, y=190)

        self.btnNuevoCliente = tk.Button(clientes_tab, text="Nuevo", command=self.nuevoCliente, bg='gold')
        self.btnNuevoCliente.place(x=150 + 10, y=220)

        self.btnGuardarCliente = tk.Button(clientes_tab, text="Guardar", state='disabled', command=self.guardarCliente, bg='gold')
        self.btnGuardarCliente.place(x=200 + 10, y=220)

        self.btnCancelarCliente = tk.Button(clientes_tab, text="Cancelar", state='disabled', command=self.cancelar, bg='gold')
        self.btnCancelarCliente.place(x=257 + 10, y=220)

        self.btnEditarCliente = tk.Button(clientes_tab, text="Editar", state='disabled', command=self.editarCliente, bg='gold')
        self.btnEditarCliente.place(x=317 + 10, y=220)

        self.btnEliminarCliente = tk.Button(clientes_tab, text="Eliminar", state='disabled', command=self.eliminarCliente, bg='gold')
        self.btnEliminarCliente.place(x=360 + 10, y=220)

        # Nueva pestaña en "reservaciones"
        reservaciones_tab = ttk.Frame(self.notebook)
        self.notebook.add(reservaciones_tab, text="Reservaciones")

        tk.Label(reservaciones_tab, text="Buscar Reservacion:", bg='black', fg='gold').place(x=200, y=10)
        self.txBuscarReservacion = tk.Entry(reservaciones_tab)
        self.txBuscarReservacion.place(x=360, y=10)
        btnBuscarReservacion = tk.Button(reservaciones_tab, text="Buscar", command=self.buscarReservacion, bg='gold')
        btnBuscarReservacion.place(x=310, y=10)

        tk.Label(reservaciones_tab, text="ID:", bg='black', fg='gold').place(x=10, y=10)
        self.txIdReservacion = tk.Entry(reservaciones_tab, state='disabled')
        self.txIdReservacion.place(x=10, y=30)

        tk.Label(reservaciones_tab, text="Cliente Nombre", bg='black', fg='gold').place(x=10, y=50)
        self.txClienteNombre = tk.Entry(reservaciones_tab, width=30, state='disabled')
        self.txClienteNombre.place(x=10, y=70)

        tk.Label(reservaciones_tab, text="Habitación ID", bg='black', fg='gold').place(x=10, y=90)
        self.txHabitacionID = tk.Entry(reservaciones_tab, width=30, state='disabled')
        self.txHabitacionID.place(x=10, y=110)

        tk.Label(reservaciones_tab, text="Costo", bg='black', fg='gold').place(x=10, y=130)
        self.txCosto = tk.Entry(reservaciones_tab, width=30, state='disabled')
        self.txCosto.place(x=10, y=150)

        tk.Label(reservaciones_tab, text="Fecha Reservación:", bg='black', fg='gold').place(x=10, y=170)
        self.txFechaReservacion = tk.Entry(reservaciones_tab, width=30, state='disabled')
        self.txFechaReservacion.place(x=10, y=190)

        tk.Label(reservaciones_tab, text="Días instancia:", bg='black', fg='gold').place(x=10, y=210)
        self.txFechaSalida = tk.Entry(reservaciones_tab, width=30, state='disabled')
        self.txFechaSalida.place(x=10, y=230)

        tk.Label(reservaciones_tab, text="Hora Reservacion:", bg='black', fg='gold').place(x=10, y=250)
        self.txHoraReservacion = tk.Entry(reservaciones_tab, width=30, state='disabled')
        self.txHoraReservacion.place(x=10, y=270)

        tk.Label(reservaciones_tab, text="Fecha Salida:", bg='black', fg='gold').place(x=10, y=290)
        self.txFechaSalida2 = tk.Entry(reservaciones_tab, width=30, state='disabled')
        self.txFechaSalida2.place(x=10, y=310)

        self.btnNuevoReservacion = tk.Button(reservaciones_tab, text="Nuevo", command=self.nuevoReservacion, bg='gold')
        self.btnNuevoReservacion.place(x=150 + 10, y=300+40)

        self.btnGuardarReservacion = tk.Button(reservaciones_tab, text="Guardar", state='disabled', command=self.guardarReservacion, bg='gold')
        self.btnGuardarReservacion.place(x=200 + 10, y=300+40)

        self.btnCancelarReservacion = tk.Button(reservaciones_tab, text="Cancelar", state='disabled', command=self.cancelar, bg='gold')
        self.btnCancelarReservacion.place(x=257 + 10, y=300+40)

        self.btnEditarReservacion = tk.Button(reservaciones_tab, text="Editar", state='disabled', command=self.editarReservacion, bg='gold')
        self.btnEditarReservacion.place(x=317 + 10, y=300+40)

        

        # Nueva pestaña en "habitacion"
        habitacion_tab = ttk.Frame(self.notebook)
        self.notebook.add(habitacion_tab, text="Habitacion")

        tk.Label(habitacion_tab, text="Buscar Habitacion:", bg='black', fg='gold').place(x=180, y=10)
        self.txBuscarHabitacion = tk.Entry(habitacion_tab)
        self.txBuscarHabitacion.place(x=360, y=10)
        btnBuscarHabitacion = tk.Button(habitacion_tab, text="Buscar", command=self.buscarHabitacion, bg='gold')
        btnBuscarHabitacion.place(x=310, y=10)

        tk.Label(habitacion_tab, text="ID:", bg='black', fg='gold').place(x=10, y=10)
        self.txIdHabitacion = tk.Entry(habitacion_tab, state='disabled')
        self.txIdHabitacion.place(x=10, y=30)

        tk.Label(habitacion_tab, text="Numero Habitacion", bg='black', fg='gold').place(x=10, y=50)
        self.txNumeroHabitacion = tk.Entry(habitacion_tab, width=30, state='disabled')
        self.txNumeroHabitacion.place(x=10, y=70)

        tk.Label(habitacion_tab, text="Estado", bg='black', fg='gold').place(x=10, y=90)
        opciones_estado = ["Libre", "Reservado", "Cancelado"]
        self.comboEstado = ttk.Combobox(habitacion_tab, values=opciones_estado, state='readonly')
        self.comboEstado.place(x=10, y=110)

        # Agregar txEstado
        tk.Label(habitacion_tab, text="Estado:", bg='black', fg='gold').place(x=10, y=130)
        self.txEstado = tk.Entry(habitacion_tab, width=30, state='disabled')
        self.txEstado.place(x=10, y=150)

        self.btnNuevoHabitacion = tk.Button(habitacion_tab, text="Nuevo", command=self.nuevaHabitacion, bg='gold')
        self.btnNuevoHabitacion.place(x=150 + 10, y=180)

        self.btnGuardarHabitacion = tk.Button(habitacion_tab, text="Guardar", state='disabled', command=self.guardarHabitacion, bg='gold')
        self.btnGuardarHabitacion.place(x=200 + 10, y=180)

        self.btnEditarHabitacion = tk.Button(habitacion_tab, text="Editar", state='normal', command=self.editarHabitacion, bg='gold')
        self.btnEditarHabitacion.place(x=260 + 10, y=180)


    def idEx(self, id):
        if not id.isdigit():
            messagebox.showerror("Error", "ID debe ser un número entero")
            return False
        for cliente in self.clientes:
            if cliente.id == id:
                return True
        return False

    def buscarCliente(self):
        idBuscar = self.txBuscarCliente.get()
        for cliente in self.clientes:
            if cliente.id == idBuscar:
                self.txId.config(state='normal')
                self.txNombre.config(state='normal')
                self.txDireccion.config(state='normal')
                self.txTelefono.config(state='normal')
                self.txEmail.config(state='normal')
                self.txId.delete(0, tk.END)
                self.txNombre.delete(0, tk.END)
                self.txDireccion.delete(0, tk.END)
                self.txTelefono.delete(0, tk.END)
                self.txEmail.delete(0, tk.END)
                self.txId.insert(tk.END, cliente.id)
                self.txNombre.insert(tk.END, cliente.nombre)
                self.txDireccion.insert(tk.END, cliente.direccion)
                self.txTelefono.insert(tk.END, cliente.telefono)
                self.txEmail.insert(tk.END, cliente.email)
                self.btnEditarCliente.config(state='normal')
                self.btnEliminarCliente.config(state='normal')
                self.txId.config(state='disabled')
                self.txId.delete(0, tk.END)
                break

    def buscarReservacion(self):
        idBuscar = self.txBuscarReservacion.get()
        for reservacion in self.reservaciones:
            if reservacion.reservacionID == idBuscar:
                self.txIdReservacion.config(state='normal')
                self.txClienteNombre.config(state='normal')
                self.txHabitacionID.config(state='normal')
                self.txCosto.config(state='normal')
                self.txFechaReservacion.config(state='normal')
                self.txFechaSalida.config(state='normal')
                self.txHoraReservacion.config(state='normal')
                self.txIdReservacion.delete(0, tk.END)
                self.txClienteNombre.delete(0, tk.END)
                self.txHabitacionID.delete(0, tk.END)
                self.txCosto.delete(0, tk.END)
                self.txFechaReservacion.delete(0, tk.END)
                self.txFechaSalida.delete(0, tk.END)
                self.txHoraReservacion.delete(0, tk.END)
                self.txIdReservacion.insert(tk.END, reservacion.reservacionID)
                self.txClienteNombre.insert(tk.END, reservacion.clienteNombre)
                self.txHabitacionID.insert(tk.END, reservacion.habitacionID)
                self.txCosto.insert(tk.END, reservacion.costo)
                self.txFechaReservacion.insert(tk.END, reservacion.fecha_Reservacion)
                self.txFechaSalida.insert(tk.END, reservacion.fecha_salida)
                self.txHoraReservacion.insert(tk.END, reservacion.hora_reservacion)
                self.txFechaSalida2.config(state='normal')
                self.txFechaSalida2.delete(0, tk.END)
                self.txFechaSalida2.insert(tk.END, reservacion.fecha_salida2)
                self.txFechaSalida2.config(state='disabled')
                self.btnEditarReservacion.config(state='normal')
                self.txIdReservacion.config(state='disabled')
                self.txIdReservacion.delete(0, tk.END)
                break

    def buscarHabitacion(self):
        idBuscar = self.txBuscarHabitacion.get()
        for habitacion in self.habitaciones:
            if habitacion.habitacionID == idBuscar:
                self.txIdHabitacion.config(state='normal')
                self.txNumeroHabitacion.config(state='normal')
                self.txEstado.config(state='normal')
                self.txIdHabitacion.delete(0, tk.END)
                self.txNumeroHabitacion.delete(0, tk.END)
                self.txEstado.delete(0, tk.END)
                self.txIdHabitacion.insert(tk.END, habitacion.habitacionID)
                self.txNumeroHabitacion.insert(tk.END, habitacion.numero_habitacion)
                self.txEstado.insert(tk.END, habitacion.estado)
                self.txIdHabitacion.config(state='disabled')
                self.txIdHabitacion.delete(0, tk.END)
                break

    def nuevoCliente(self):
        self.limpiar()
        self.txId.config(state='normal')
        self.txNombre.config(state='normal')
        self.txDireccion.config(state='normal')
        self.txTelefono.config(state='normal')
        self.txEmail.config(state='normal')
        self.txId.delete(0, tk.END)
        self.txNombre.delete(0, tk.END)
        self.txDireccion.delete(0, tk.END)
        self.txTelefono.delete(0, tk.END)
        self.txEmail.delete(0, tk.END)
        self.txId.insert(tk.END, len(self.clientes) + 1)
        self.txId.config(state='disabled')

        self.btnNuevoCliente.config(state='disabled')
        self.btnGuardarCliente.config(state='normal')
        self.btnCancelarCliente.config(state='normal')

    def nuevoReservacion(self):
        self.limpiar()
        self.txIdReservacion.config(state='normal')
        self.txClienteNombre.config(state='normal')
        self.txHabitacionID.config(state='normal')
        self.txCosto.config(state='normal')
        self.txFechaReservacion.config(state='normal')
        self.txFechaSalida.config(state='normal')
        self.txHoraReservacion.config(state='normal')
        self.txIdReservacion.delete(0, tk.END)
        self.txClienteNombre.delete(0, tk.END)
        self.txHabitacionID.delete(0, tk.END)
        self.txCosto.delete(0, tk.END)
        self.txFechaReservacion.delete(0, tk.END)
        self.txFechaSalida.delete(0, tk.END)
        self.txHoraReservacion.delete(0, tk.END)
        self.txIdReservacion.insert(tk.END, len(self.reservaciones) + 1)
        self.txIdReservacion.config(state='disabled')

        self.btnNuevoReservacion.config(state='disabled')
        self.btnGuardarReservacion.config(state='normal')
        self.btnCancelarReservacion.config(state='normal')

    def nuevaHabitacion(self):
        self.limpiar()
        self.txIdHabitacion.config(state='normal')
        self.txNumeroHabitacion.config(state='normal')
        self.txEstado.config(state='normal')
        self.txIdHabitacion.delete(0, tk.END)
        self.txNumeroHabitacion.delete(0, tk.END)
        self.txEstado.delete(0, tk.END)
        self.txIdHabitacion.insert(tk.END, len(self.habitaciones) + 1)
        self.txIdHabitacion.config(state='disabled')

        self.btnNuevoHabitacion.config(state='disabled')
        self.btnGuardarHabitacion.config(state='normal')
        self.limpiar()

    def guardarCliente(self):
        id = self.txId.get()
        nombre = self.txNombre.get()
        direccion = self.txDireccion.get()
        telefono = self.txTelefono.get()
        email = self.txEmail.get()

        patron = re.compile(r'^\d{10}$')

        if not id or not nombre or not direccion or not telefono or not email:
            messagebox.showerror("Error", "Deben estar todos los datos")
        elif not nombre.replace(' ', '').isalpha():
            messagebox.showerror("Error", "El nombre solo debe contener caracteres alfabéticos y espacios")
        elif not direccion.replace(' ', '').isalnum():
            messagebox.showerror("Error", "La dirección solo debe contener caracteres alfabéticos y números")
        elif not telefono.isdigit() and patron.match(telefono):
            messagebox.showerror("Error", "El teléfono debe ser un número entero de 10 dígitos y mayor a 0")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Error", "El email debe tener el formato")
        else:
            cliente = Clientes(id, nombre, direccion, telefono, email)
            self.clientes.append(cliente)
            self.limpiar()
            self.btnNuevoCliente.config(state='normal')
            self.btnGuardarCliente.config(state='disabled')
            self.btnCancelarCliente.config(state='disabled')
            self.txId.config(state='normal')
            self.txId.delete(0, tk.END)
            self.txId.config(state='disabled')

    def guardarReservacion(self):
        id = self.txIdReservacion.get()
        nombre = self.txClienteNombre.get()
        habitacion_id = self.txHabitacionID.get()
        costo = self.txCosto.get()
        fecha_reservacion = self.txFechaReservacion.get()
        fecha_salida = self.txFechaSalida.get()
        hora_reservacion = self.txHoraReservacion.get()

        if not id or not nombre or not habitacion_id or not costo or not fecha_reservacion or not fecha_salida or not hora_reservacion:
            messagebox.showerror("Error", "Deben estar todos los datos")
        elif nombre not in [cliente.nombre for cliente in self.clientes]:
            messagebox.showerror("Error", "El nombre no está en la lista de clientes")
        elif habitacion_id not in [habitacion.habitacionID for habitacion in self.habitaciones]:
            messagebox.showerror("Error", "El ID de la habitación no está en la lista de habitaciones")
        elif not costo.isdigit() or int(costo) <= 0:
            messagebox.showerror("Error", "El costo debe ser un número entero o mayor a 0")
        elif not re.match(r'\d{4}-\d{2}-\d{2}', fecha_reservacion):
            messagebox.showerror("Error", "La fecha de reservación debe tener el formato YYYY-MM-DD")
        elif not fecha_salida.isdigit() or int(fecha_salida) <= 0:
            messagebox.showerror("Error", "La cantidad de días de la fecha de salida debe ser un número entero o mayor a 0")
        elif not re.match(r'\d{2}:\d{2}', hora_reservacion):
            messagebox.showerror("Error", "La hora de reservación debe tener el formato HH:MM")
        else:
            # Verificar si la habitación ya está reservada
            habitacion_reservada = next((reservacion for reservacion in self.reservaciones if reservacion.habitacionID == habitacion_id), None)
            if habitacion_reservada:
                messagebox.showerror("Error", f"La habitación {habitacion_id} ya está reservada")
            else:
                # Verificar si el cliente existe
                cliente_existente = next((cliente for cliente in self.clientes if cliente.nombre == nombre), None)
                if cliente_existente:
                    fecha_reservacion_dt = datetime.strptime(fecha_reservacion, '%Y-%m-%d')
                    fecha_salida_dt = fecha_reservacion_dt + timedelta(days=int(fecha_salida))
                    fecha_salida2 = fecha_salida_dt.strftime('%Y-%m-%d %H:%M:%S')

                    reservacion = Reservaciones(id, nombre, habitacion_id, fecha_reservacion, hora_reservacion, fecha_salida, costo, fecha_salida2)
                    self.reservaciones.append(reservacion)
                    self.limpiar()
                    self.btnNuevoReservacion.config(state='normal')
                    self.btnGuardarReservacion.config(state='disabled')
                    self.btnCancelarReservacion.config(state='disabled')
                    self.txIdReservacion.config(state='normal')
                    self.txIdReservacion.delete(0, tk.END)
                    self.txIdReservacion.config(state='disabled')
                else:
                    messagebox.showerror("Error", f"No se encontró al cliente {nombre}")


    def guardarHabitacion(self):
        id = self.txIdHabitacion.get()
        numero_habitacion = self.txNumeroHabitacion.get()
        estado = self.comboEstado.get()

        if not id or not numero_habitacion or not estado:
            messagebox.showerror("Error", "Deben estar todos los datos")
        elif not numero_habitacion.isdigit() or int(numero_habitacion) <= 0 or numero_habitacion in [habitacion.numero_habitacion for habitacion in self.habitaciones]:
            messagebox.showerror("Error", "El número de habitación debe ser un número entero y mayor a 0")
        else:
            habitacion = Habitacion(id, numero_habitacion, estado)
            self.habitaciones.append(habitacion)
            self.limpiar()
            self.btnNuevoHabitacion.config(state='normal')
            self.btnGuardarHabitacion.config(state='disabled')
            self.txIdHabitacion.config(state='normal')
            self.txIdHabitacion.delete(0, tk.END)
            self.txIdHabitacion.config(state='disabled')
        self.limpiar()

    def cancelar(self):
        self.limpiar()
        self.btnNuevoCliente.config(state='normal')
        self.btnNuevoReservacion.config(state='normal')

    def editarCliente(self):
        idEditar = self.txId.get()
        nombre = self.txNombre.get()
        direccion = self.txDireccion.get()
        telefono = self.txTelefono.get()
        email = self.txEmail.get()
        patron = re.compile(r'^\d{10}$')
        if not id or not nombre or not direccion or not telefono or not email:
            messagebox.showerror("Error", "Deben estar todos los datos")
        elif not nombre.replace(' ', '').isalpha():
            messagebox.showerror("Error", "El nombre solo debe contener caracteres alfabéticos y espacios")
        elif not direccion.replace(' ', '').isalnum():
            messagebox.showerror("Error", "La dirección solo debe contener caracteres alfabéticos y números")
        elif not telefono.isdigit() and patron.match(telefono):
            messagebox.showerror("Error", "El teléfono debe ser un número entero de 10 dígitos y mayor a 0")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Error", "El email debe tener el formato")
        else:
            for cliente in self.clientes:
                if cliente.id == idEditar:
                    cliente.nombre = nombre
                    cliente.direccion = direccion
                    cliente.telefono = telefono
                    cliente.email = email
                    break
            self.limpiar()
            self.btnNuevoCliente.config(state='normal')
            self.txId.config(state='normal')
            self.txId.delete(0, tk.END)
            self.txId.config(state='disabled')

    def editarReservacion(self):
        idEditar = self.txIdReservacion.get()
        nombre = self.txClienteNombre.get()
        habitacion_id = self.txHabitacionID.get()
        costo = self.txCosto.get()
        fecha_reservacion = self.txFechaReservacion.get()
        fecha_salida = self.txFechaSalida.get()
        hora_reservacion = self.txHoraReservacion.get()

        if not id or not nombre or not habitacion_id or not costo or not fecha_reservacion or not fecha_salida or not hora_reservacion:
            messagebox.showerror("Error", "Deben estar todos los datos")
        elif nombre not in [cliente.nombre for cliente in self.clientes]:
            messagebox.showerror("Error", "El nombre no está en la lista de clientes")
        elif habitacion_id not in [habitacion.habitacionID for habitacion in self.habitaciones]:
            messagebox.showerror("Error", "El ID de la habitación no está en la lista de habitaciones")
        elif not costo.isdigit() or int(costo) <= 0:
            messagebox.showerror("Error", "El costo debe ser un número entero o mayor a 0")
        elif not re.match(r'\d{4}-\d{2}-\d{2}', fecha_reservacion):
            messagebox.showerror("Error", "La fecha de reservación debe tener el formato YYYY-MM-DD")
        elif not fecha_salida.isdigit() or int(fecha_salida) <= 0:
            messagebox.showerror("Error", "La cantidad de días de la fecha de salida debe ser un número entero o mayor a 0")
        elif not re.match(r'\d{2}:\d{2}', hora_reservacion):
            messagebox.showerror("Error", "La hora de reservación debe tener el formato HH:MM")
        else:
            for reservacion in self.reservaciones:
                if reservacion.reservacionID == idEditar:
                    reservacion.clienteNombre = nombre
                    reservacion.habitacionID = habitacion_id
                    reservacion.costo = costo
                    reservacion.fecha_Reservacion = fecha_reservacion
                    reservacion.fecha_salida = fecha_salida
                    reservacion.hora_reservacion = hora_reservacion
                    break
            self.limpiar()
            self.btnNuevoReservacion.config(state='normal')
            self.txIdReservacion.config(state='normal')
            self.txIdReservacion.delete(0, tk.END)
            self.txIdReservacion.config(state='disabled')

    def editarHabitacion(self):
        idEditar = self.txIdHabitacion.get()
        numero_habitacion = self.txNumeroHabitacion.get()
        estado = self.comboEstado.get()
        if not id or not numero_habitacion or not estado:
            messagebox.showerror("Error", "Deben estar todos los datos")
        elif not numero_habitacion.isdigit() or int(numero_habitacion) <= 0 or numero_habitacion in [habitacion.numero_habitacion for habitacion in self.habitaciones]:
            messagebox.showerror("Error", "El número de habitación debe ser un número entero y mayor a 0")
        else:
            for habitacion in self.habitaciones:
                if habitacion.habitacionID == idEditar:
                    habitacion.numero_habitacion = numero_habitacion
                    habitacion.estado = estado
                    break
            self.limpiar()
            self.btnNuevoHabitacion.config(state='normal')
            self.txIdHabitacion.config(state='normal')
            self.txIdHabitacion.delete(0, tk.END)
            self.txIdHabitacion.config(state='disabled')

    def eliminarCliente(self):
        id_eliminar = self.txId.get()
        for cliente in self.clientes:
            if cliente.id == id_eliminar:
                self.clientes.remove(cliente)
                break
        self.limpiar()
        self.btnNuevoCliente.config(state='normal')

    def eliminarReservacion(self):
        id_eliminar = self.txIdReservacion.get()
        for reservacion in self.reservaciones:
            if reservacion.reservacionID == id_eliminar:
                self.reservaciones.remove(reservacion)
                break
        self.limpiar()
        self.btnNuevoReservacion.config(state='normal')

    def limpiar(self):
        self.txId.delete(0, tk.END)
        self.txNombre.delete(0, tk.END)
        self.txDireccion.delete(0, tk.END)
        self.txTelefono.delete(0, tk.END)
        self.txEmail.delete(0, tk.END)
        self.txId.config(state='disabled')
        self.txNombre.config(state='disabled')
        self.txDireccion.config(state='disabled')
        self.txTelefono.config(state='disabled')
        self.txEmail.config(state='disabled')
        self.btnEditarCliente.config(state='disabled')
        self.btnEliminarCliente.config(state='disabled')

        self.txIdReservacion.delete(0, tk.END)
        self.txClienteNombre.delete(0, tk.END)
        self.txHabitacionID.delete(0, tk.END)
        self.txCosto.delete(0, tk.END)
        self.txFechaReservacion.delete(0, tk.END)
        self.txFechaSalida.delete(0, tk.END)
        self.txHoraReservacion.delete(0, tk.END)
        self.txIdReservacion.config(state='disabled')
        self.txClienteNombre.config(state='disabled')
        self.txHabitacionID.config(state='disabled')
        self.txCosto.config(state='disabled')
        self.txFechaReservacion.config(state='disabled')
        self.txFechaSalida.config(state='disabled')
        self.txHoraReservacion.config(state='disabled')
        self.btnEditarReservacion.config(state='disabled')
        #self.btnEliminarReservacion.config(state='disabled')
        self.txIdHabitacion.delete(0, tk.END)
        self.txNumeroHabitacion.delete(0, tk.END)
        self.comboEstado.set('')  # Limpiar el Combobox
        self.txEstado.delete(0, tk.END)
        self.txIdHabitacion.config(state='disabled')
        self.btnEditarHabitacion.config(state='disabled')


if __name__ == "__main__":
    login_root = tk.Tk()
    login_window = LoginWindow(login_root)
    login_root.mainloop()
    root = tk.Tk()
    app = Hotel(root)
    root.mainloop()

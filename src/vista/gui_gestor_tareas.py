import tkinter as tk
from tkinter import ttk, messagebox
from gestor_tareas import GestorTareas

class GestorTareasGUI:
    def __init__(self, root, gestor):
        self.gestor = gestor
        self.root = root
        self.root.title("Gestor de Tareas")

        # Campos de entrada
        self.titulo_entry = ttk.Entry(self.root, width=20)
        self.descripcion_entry = ttk.Entry(self.root, width=50)
        # Botones y lista de tareas
        self.agregar_btn = ttk.Button(self.root, text="Agregar Tarea", command=self.agregar_tarea)
        self.tareas_listbox = tk.Listbox(self.root, height=10, width=50)
        self.completar_btn = ttk.Button(self.root, text="Marcar como Completada", command=self.marcar_completada)
        self.eliminar_btn = ttk.Button(self.root, text="Eliminar Tarea", command=self.eliminar_tarea)

    # Lógica de interfaz (agregar tarea, actualizar lista, marcar completada, eliminar)
    ...

def run():
    root = tk.Tk()
    gestor = GestorTareas()
    app = GestorTareasGUI(root, gestor)
    root.mainloop()

if __name__ == "__main__":
    run()

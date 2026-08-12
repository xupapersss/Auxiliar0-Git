class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.tareas = []
    def listarTareas(self):
        for tarea in self.tareas:
            if tarea.estaLista():
<<<<<<< HEAD
                print(f"La tarea {tarea.obtenerNombre()} está lista")
                print(f"La tarea {tarea.obtenerNombre()} no está lista")
=======
                print(f"[X] {tarea.obtenerNombre()}" )

>>>>>>> 7a42b7e1e37515febe39a841c2af48c280b86732
    def agregarTarea(self, tarea):
        self.tareas.append(tarea)

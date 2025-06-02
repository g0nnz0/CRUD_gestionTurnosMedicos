class Menu:
    def __init__(self, opciones: list[str]):
        if not isinstance(opciones, list):
            raise ValueError("El parámetro opciones debe ser una lista de opciones")
        self.opciones_menu = opciones

    def mostrarMenu(self):
        print("\n---MENU PRINCIPAL---")
        #usé enumerate para poder obtener el indice y usarlo en print como numerador
        #por eso el for tiene dos variables, i(indice) y opcion
        for i, opcion in enumerate(self.opciones_menu, start=1):
            print(f"{i}- {opcion}")
        print("--------------------")    

    def pedirOpcionDeMenuValida(self) -> int:
        opcion_seleccionada = ""
        num_opciones = len(self.opciones_menu)

        #Este while combinado con iniciar opcion_seleccionada como un "" trabaja basicamente como un do while
        #Da las condiciones para que salte el primer print. y a partir de ahi pasa al if, que es la misma condicion pero con otro cartel.
        #si la condicion no se cumple, sigue loopeando el while
        while not opcion_seleccionada.isdigit() or int(opcion_seleccionada) not in range(1, num_opciones + 1):
            opcion_seleccionada = input(f"Por favor, seleccione una opcion entre 1 y {num_opciones}: ")
            if not opcion_seleccionada.isdigit() or int(opcion_seleccionada) not in range(1, num_opciones + 1):
                print(f"Opción no valida.")
        return int(opcion_seleccionada)
    
menu = Menu(["Gestion de Pacientes", "Gestión de Médicos", "Gestión de turnos", "Salir"])

menu.mostrarMenu()
    

# Importamos las librerías necesarias 
import numpy as np
import pandas as pd


# Creamos la clase simulador que contiene las funciones
class SimuladorF: 
    def __init__(self, capital_inicial):
        self.capital = capital_inicial
        self.historial = [capital_inicial]  # Guarda la evolución del capital
        self.desiciones = []  # Registro de decisiones tomadas

    #Se crea la funcion de invertir donde retorna un valor booleano dependiendo se vale la pena o no la inversión
    def invertir(self, montoInicial, retornoEsperado):
        if montoInicial > self.capital:
            print("No hay suficiente capital para invertir")
            return False
        
        if retornoEsperado <=0:
            print("La inversión no es recomendable ya que el retorno esperado es negativo o cero")
            return False
        
        ganancia = montoInicial * (retornoEsperado / 100)

        if ganancia < montoInicial * 0.05:  # Si el retorno es menor al 5% del monto, no vale la pena
            print("La inversión tiene un retorno muy bajo y podría no ser rentable.")
            return False
        
        self.capital += ganancia - montoInicial
        self.registrarDesicion(f"Inversión realizada: -${montoInicial} +${ganancia}")
        print("La inversión es recomendable, la puede realizar con éxito")
        return True
    #Se crea la funcion de contratar personal donde dependiendo el presupuesto indica la cantidad de empleados que se pueden contratar
    def contratarPersonal(self, presupuesto):
        if presupuesto > self.capital:
            print("No tienes suficiente capital para contratar personal con ese presupuesto")
            return
        
        empleadosMax = presupuesto // 1200000  # Suponiendo un salario base de $1,200,000 por empleado
        if empleadosMax < 1:
            print("Con el capital actual, no puedes contratar empleados.")
            return
        
        salarioPromedio = presupuesto / empleadosMax
        print(f"Con un presupuesto de ${presupuesto}, puedes contratar hasta {int(empleadosMax)} empleados con un salario promedio de ${salarioPromedio:.2f}.")

        #Se pregunta se desea contratar y realiza actualizacion del capital imaginando que se contrata el personal
        confirmacion = input("¿Deseas proceder con la contratación? (si/no): ").strip().lower()
        if confirmacion == "si":
            self.capital -= presupuesto
            self.registrarDesicion(f"Contratación de {int(empleadosMax)} empleados con salario promedio de ${salarioPromedio:.2f}: -${presupuesto}")
            print("Contratación de personal realizada con éxito.")
        else:
            print("Contratación cancelada.")

    #Se crea la funcion de expandir operaciones donde se realiza la actualizacion del capital imaginando que se expanden las operaciones
    def expandirOperaciones(self, costo, retornoEsperado):
        if costo > self.capital:
            print("No hay suficiente capital para expandir las operaciones")
            return     
        
        gananciaFutura = costo * (retornoEsperado / 100)
        self.capital += gananciaFutura - costo
        self.registrarDesicion(f"Expansión de operaciones: -${costo} +${gananciaFutura}")

    #Funcion que muestra el capital actual
    def mostrarCapital(self):
        print(f"Capital actual: ${self.capital:.2f}")

    #Funcion que registra las decisiones tomadas por el emprendedor 
    def registrarDesicion(self, desicion):
        self.desiciones.append(desicion)
        self.historial.append(self.capital)

    #Funcion que muestra el historial de decisiones tomadas por el emprendedor
    def mostrarHistorial(self):
        print("Historial de decisiones:")
        for i, decision in enumerate(self.desiciones, start=1):
            print(f"{i}. {decision}")
        
        self.mostrarCapital()


# Menu interactivo
def menu():
    print("Bienvenido al Simulador de Toma de Decisiones Financieras")
    capitalInicial = float(input("Ingrese el capital inicial: "))
    simulador = SimuladorF(capitalInicial)

    while True:
        print("\nMenú:")
        print("1. Invertir")
        print("2. Contratar Personal")
        print("3. Expandir Operaciones")
        print("4. Mostrar Capital Actual")
        print("5. Mostrar Historial de Decisiones")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            monto = float(input("Ingrese el monto de la inversión: "))
            retorno = float(input("Ingrese el porcentaje de retorno esperado (%): "))
            simulador.invertir(monto, retorno)
        
        elif opcion == "2":
            presupuesto = float(input("Ingrese el presupuesto total para contratar empleados: "))
            simulador.contratarPersonal(presupuesto)

        elif opcion == "3":
            costo = float(input("Ingrese el costo de la expansión de operaciones: "))
            retorno = float(input("Ingrese el porcentaje de retorno esperado (%): "))
            simulador.expandirOperaciones(costo, retorno)

        elif opcion == "4":
            simulador.mostrarCapital()

        elif opcion == "5":
            simulador.mostrarHistorial()

        elif opcion == "6":
            print("Saliendo... Gracias por usar el Simulador de Toma de Decisiones Financieras")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutamos el menú del simulador
if __name__ == "__main__":
    menu()

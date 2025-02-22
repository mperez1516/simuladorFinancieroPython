#Importamos las librerias necesarias 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Creamos la clase simulador que contiene las funciones

class simuladorF: 
    def __init__(self, capital_inicial):
        self.capital = capital_inicial
        #Se guarda la evolucion del capital
        self.historial = [capital_inicial]
        #Se guarda un registro de las desiciones tomadas
        self.desiciones = []

    def invertir(self, montoInicial, retornoEsperado):
        if montoInicial > self.capital:
            print("No hay suficiente capital para invertir")
            return False
        
        ganancia= montoInicial * (retornoEsperado/100)
        if ganancia <= montoInicial:
            print("La inversion no es recomendable ya que el retorno esperado es bajo o negativo")
            return False
        
        #En caso donde si valga la pena realizar la inversion 
        self.capital += ganancia - montoInicial
        self.registrarDesicion(f"Inversion en marketing: -${montoInicial} +${ganancia}")
        print("Si es recomendable la inversion, la puede realizar con exito")
        return True
    
    #Funcion para saber si es recomendable contratar personal y que tanto
    def contratarPersonal(self, presupuesto):
        if presupuesto > self.capital:
        print("No tienes suficiente capital para contratar personal con ese presupuesto.")
        return
    
    # Suponiendo un salario base de $1,200,000 por empleado
    empleadosMax = presupuesto // 1200000
    if empleadosMax < 1:
        print(" Con el capital actual, no puedes contratar empleados.")
        return
    
    salarioPromedio = presupuesto / empleados_max
    print(f"Con un presupuesto de ${presupuesto}, puedes contratar hasta {int(empleadosMax)} empleados con un salario promedio de ${salarioPromedio:.2f}.")

    # Confirmación del usuario para proceder
    confirmacion = input("¿Deseas proceder con la contratación? (si/no): ").strip().lower()
    if confirmacion == "si":
        self.capital -= presupuesto
        self.registrarDesicion(f"Contratación de {int(empleadosMax)} empleados con salario promedio de ${salarioPromedio:.2f}: -${presupuesto}")
        print("Contratación de personal realizada con éxito.")
    else:
        print("Contratación cancelada.")


    #Funcion para saber si es recomendable expandir las operaciones
    def expandirOperaciones(self, costo, retornoEsperado):
        if costo > self.capital:
            print("No hay suficiente capital para expandir las operaciones")
            return     
        
        gananciaFutura = costo * (retornoEsperado / 100)
        self.capital += gananciaFutura - costo
        self.registrarDesicion(f"Expansion de operaciones: -${costo} +${gananciaFutura}")

    #Funcion que muestra el capital
    def mostrarCapital(self):
        print(f"Capital actual: ${self.capital: .2f}")

    #Funcion que registra las desiciones tomadas
    def registrarDesicion(self, desicion):
        self.desiciones.append(desicion)
        self.historial.append(self.capital)

    #Funcion que muestra el historial de desiciones
    def mostrarHistorial(self):
        print("Historial de desiciones:")
        for i, decision in enumerate(self.desiciones, start=1 ):
            print(f"{i}. {decision}")
        
        self.mostrarCapital()

    #Funcion que muestra el grafica
    def mostrarGrafica(self):
        plt.figure(figsize=(8, 5))
        plt.plot(self.historial, marker= 'o', lineStyle= '-', color= 'b', label= "Capital Disponible" )
        plt.xlabel("Numero de Decision")
        plt.ylabel("Capital ($)")
        plt.title("Evolucion del Capital")
        plt.legend()
        plt.grid()
        plt.show()

    #Menu interactivo
    print("Bienvenido al simulador de Toma de Decisiones Financieras")
    capitalInicial = float(input("Ingrese el capital inicial: "))
    simulador = simuladorF(capitalInicial)

    while True:
        print("\nMenu:")
        print("1. Invertir")
        print("2. Contratar Personal")
        print("3. Expandir Operaciones")
        print("4. Mostrar Capital Actual")
        print("5. Mostrar Historial de Desiciones")
        print("6. Mostrar Grafica")
        print("7. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            monto = float(input("Ingrese el monto de la inversion: "))
            retorno = float(input("Ingrese el porcentaje de retorno esperado (%): "))
            simulador.invertir(monto, retorno)
        
        elif opcion == "2":
            presupuesto = float(input("Ingrese el presupuesto total para contratar empleados: "))
           simulador.contratarPersonal(presupuesto)

        elif opcion == "3":
            costo = float(input("Ingrese el costo de la expansion de operaciones: "))
            retorno = float(input("Ingrese el porcentaje de retorno esperado (%): "))
            simulador.expandirOperaciones(costo, retorno)

        elif opcion == "4":
            simulador.mostrarCapital()

        elif opcion == "5":
            simulador.mostrarHistorial()

        elif opcion == "6":
            simulador.mostrarGrafica()

        elif opcion == "7":
            print("Saliendo...Gracias por usar el simulador de Toma de Decisiones Financieras")
            break

        else:
            print("Opcion invalida. Intente de nuevo.")
        
    #Ejecutamos el menu del simulador
    if __name__ == "__main__":
        menu()


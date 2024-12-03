import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("proyectosFinalizados.csv", sep =";", decimal=",")

def menu():
    while True:
        print("Reportes sobre Proyectos financiados finalizados de PROINNOVATE")
        print("-------------------------------------------------------")
        print("1.Cantidad de concursos en realizados desde el 2007-2022")
        print("2.Proporción de moneda usada en el departamento de lima en el año" 
              "2017")
        print("3.¿En qué año los fondos FIDECOM invirtieron en la provincia" 
              "de Cajamarca?")
        print("4.¿Cuál es el monto no financiero en el cual el fondo FOMITEC participó"
              "en el concurso capital semilla para los emprendedores?")
        print("5.¿Qué tipo de fondos se usaron en el distrito de lima solamente "
              "en dólares?")
        print("6. Variación según los años del concurso de calidad - individual en" 
              "la provincia de arequipa")
        print("0.Salir")
        try:
            opcion = int(input("¿Que reporte se desea visualizar?: "))
            if opcion == 0:
                print("Programa finalizado")
                break
            elif opcion == 1:
                print(f"\n{reporte1()}\n\n")
            elif opcion == 2:
                print(f"\n{reporte2()}\n\n")
            elif opcion == 3:
                print(f"\n{reporte3()}\n\n")
            elif opcion == 4:
                print(f"\n{reporte4()}\n\n")
            elif opcion == 5:
                print(f"\n{reporte5()}\n\n")
            elif opcion == 6:
                print(f"\n{reporte6()}\n\n")
            else:
                print("ERROR ingrese una de las opciones")
        except ValueError:
            print("ERROR ingrese un número")


#REPORTE 1
años = df["ANIO"]

def ingresarAño():
    while True:
        try:
            año = int(input("\nIngrese el año: "))
            if año < 2007 or año > 2022:
                print("El año esta fuera del rango [2007 - 2022]")
            else:
                return año
        except ValueError:
            print("Debe ingresar un número entero")


def obtenerEjes():
    año = ingresarAño()
    concursos = []
    cantidadPorConcurso = {}
    for indice, año1 in enumerate(años):
        if año1 == año:
            concursos.append(df.loc[indice, "CONCURSO"])
    for concurso in concursos:
        cantidadPorConcurso[concurso] = concursos.count(concurso)
    return cantidadPorConcurso, año


def generarGrafico(cantidadPorConcurso, año):
    plt.barh(list(cantidadPorConcurso.keys()), list(cantidadPorConcurso.values()),
             color='#2F7814', label='Cantidad', linewidth=3)
    plt.title(f'Cantidad de concursos realizados en el año {año}')
    plt.ylabel('Concursos')
    plt.xlabel('Cantidad')
    plt.legend()
    plt.grid(True, color='#2F7814')
    plt.show()


def reporte1():
    cantidadPorConcurso, año = obtenerEjes()
    generarGrafico(cantidadPorConcurso, año)


#REPORTE 2
def obtenerMonedas():
    soles = 0
    dolares = 0
    monedas = np.array(df.loc[:, "ANIO"])
    for indice, año in enumerate(monedas):
        if año == 2017:
            moneda = df.loc[indice, "MONEDA"]
            if moneda == "SOLES":
                soles += 1
            else:
                dolares += 1
    return soles, dolares


def generarGraficoReporte2(soles, dolares):
    cantidades = [soles, dolares]
    etiquetas = ["Soles", "Dólares"]
    colores =  ["#2F7814", "#60D394"]
    desfase = (0, 0.1)
    plt.title("Proporción de moneda usada en el departamento de Lima en el año "
              "2017")
    plt.pie(cantidades, labels=etiquetas, autopct="%0.1f%%", colors=colores,
            explode=desfase)
    plt.show()


def reporte2():
    soles, dolares = obtenerMonedas()
    generarGraficoReporte2(soles, dolares)


#REPORTE3
def obtenerAños():
    fondos = np.array(df["FONDO"])
    años = []
    for indice, fondo in enumerate(fondos):
        if fondo == "FIDECOM":
            provincia = df.loc[indice, "PROVINCIA"]
            if provincia == "CAJAMARCA":
                año = df.loc[indice, "ANIO"]
                años.append(año)
    return años


def cantidadInversionesPorAño(años):
    cantidadPorAño = {}
    primerAño = min(años)
    ultimoAño = max(años)
    for i in range(primerAño, ultimoAño + 1):
        cantidadPorAño[i] = años.count(i)
    return cantidadPorAño


def generarGraficoReporte3(cantidadPorAño):
    plt.bar(cantidadPorAño.keys(), cantidadPorAño.values(), color='#2F7814',
            label='Cantidad', linewidth=3)
    plt.title('¿En qué años los fondos FIDECOM invirtieron en la provincia de'
              ' CAJAMARCA?')
    plt.ylabel('Cantidad')
    plt.xlabel('Años')
    plt.legend()
    plt.grid(True, color='#FF334E')
    plt.show()


def reporte3():
    años = obtenerAños()
    cantPorAño = cantidadInversionesPorAño(años)
    generarGraficoReporte3(cantPorAño)


#REPORTE 4 
fondos = np.array(df["FONDO"])
def obtenerMontosYCantidad():
    montos = []
    cantidad = []
    for indice, fondo in enumerate(fondos):
        if fondo == "FOMITEC":
            concurso = df.loc[indice, "CONCURSO"]
            if concurso == "CAPITAL SEMILLA PARA EMPRENDEDORES INNOVADORES":
                monto = df.loc[indice, "MONTO_NO_FINANCIERO"]
                montos.append(monto)
    for i in range(len(montos)):
        cantidad.append(i)
    return montos, cantidad


def generarGraficoReporte4(montos, cantidad):
    plt.plot(cantidad, montos, color='#2F7814', label='Monto no financiero',
             linewidth=1)
    plt.title('¿Cuál es el monto no financiero en el cuál el fondo FOMITEC participó'
              ' en el concurso capital semilla para lo emprendedores innovadores?')
    plt.xlabel('Número de concurso')
    plt.ylabel('Monto no financiero')
    plt.legend()
    plt.grid(True, color='#1CA5D9')
    plt.show()


def reporte4():
    montos, cantidad = obtenerMontosYCantidad()
    generarGraficoReporte4(montos, cantidad)


#REPORTE 5
def filtrarDatos():
    distritos = np.array(df['DISTRITO'])
    monedas = np.array(df['MONEDA'])
    indice = [i for i in range(len(df)) if distritos[i] == 'LIMA'
     and monedas[i] == 'DOLARES']
    datosFiltrados = df.loc[indice]
    return datosFiltrados


def contarFondos(df):
    fondos = {}
    for valor in df['FONDO']:
        if valor in fondos:
            fondos[valor] += 1
        else:
            fondos[valor] = 1
    nombreFondos = list(fondos.keys())
    cantidad = list(fondos.values())
    return nombreFondos, cantidad


def generarGraficoReporte5(nombreFondos, cantidad):
    plt.bar(nombreFondos, cantidad, color='#2F7814', width=.5)
    plt.xlabel('Fondo')
    plt.ylabel('Cantidad')
    plt.title('¿Qué tipo de fondos se usaron' 
              ' en el distrito de lima solamente en dólares?')
    plt.show()


def reporte5():
    datos = filtrarDatos()
    nombreFondos, cantidad = contarFondos(datos)
    generarGraficoReporte5(nombreFondos, cantidad)


#REPORTE 6
def obtenerAños():
    concursos = np.array(df["CONCURSO"])
    años = []
    for indice, concurso in enumerate(concursos):
        if concurso == "MEJORA DE LA CALIDAD - INDIVIDUAL":
            provincia = df.loc[indice, "PROVINCIA"]
            if provincia == "AREQUIPA":
                año = df.loc[indice, "ANIO"]
                años.append(año)
    return años


def cantidadPorAño(años):
    cantidadPorAño = {}
    primerAño = min(años)
    ultimoAño = max(años)
    for i in range(primerAño, ultimoAño + 1):
        cantidadPorAño[i] = años.count(i)
    return cantidadPorAño


def generarGraficoReporte6(cantidadPorAño):
    plt.plot(cantidadPorAño.keys(), cantidadPorAño.values(), color='#2F7814',
             label='Variación', linewidth=1)
    plt.title('Variación según los años del concurso de calidad - individual en la'
              ' provincia de Arequipa')
    plt.xlabel('Años')
    plt.ylabel('Cantidad')
    plt.legend()
    plt.grid(True, color='#1CA5D9')
    plt.show()


def reporte6():
    años = obtenerAños()
    cantidadAño = cantidadPorAño(años)
    generarGraficoReporte6(cantidadAño)


def main():
    menu()


main()

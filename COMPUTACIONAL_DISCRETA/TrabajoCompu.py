import tkinter as tk
from tkinter import messagebox, simpledialog
import numpy as np
from random import randint

arte_bicicleta = """
       *.      *Bike*
          d$$$$$$$P*                  $    J
              ^$.                     4r  *
              d*b                    .db
             P   $                  e* $
    ..ec.. .*"     *.              zP   $.zec..
.^        3*b.     *.           .P* .@"4F      *4
*          d*  ^b.    *c        .$*  d*   $         %
/          P      $.    *c      d*   @     3r         3
4        .eE........$r===e$$$$eeP    J       *..        b
$       $$$$$       $   4$$$$$$$     F       d$$$.      4
$       $$$$$       $   4$$$$$$$     L       *$$$"      4
4         *      ""3P ===$$$$$$"     3                  P
 *                 $       *""        b                J
  *.             .P                    %.             @
    %.         z*"                      ^%.        .r"
       "*==*"                             ^"*==*""  
"""



def mostrar_estudiantes():
    estudiantes = """
    Trabajo Parcial: Matemática Computacional
    -----------------------------------------
    Integrantes:
    - Giovanni Alexander Palomino Mathey (U202312001)
    - Paula Ariana Muñoz Guarnizo (U202312321)
    - Dayana Kety Gómez Rodríguez (U202311495)
    - Michelle Alessandra Aguilar Crispin (U202317258)
    - Maria Fernanda Mostajo Orosco (U202312874)
    """
    messagebox.showinfo("Integrantes", estudiantes)

def validar_tamano_matriz(tamano):
    if 8 <= tamano <= 16:
        return True
    else:
        messagebox.showwarning("Error", "El tamaño de la matriz debe estar entre 8 y 16.")
        return False

def generarMatriz(tamano):
    if validar_tamano_matriz(tamano):
        datos = []
        j = 0
        for i in range(tamano * tamano):
            if i == j * (tamano + 1):
                datos.append(0)
                j += 1
            else:
                datos.append(randint(1,99))
        matriz = np.array(datos).reshape(tamano, tamano)
        return matriz
    else:
        return None

def ingresarMatriz(tamano):
    if validar_tamano_matriz(tamano):
        datos = []
        for i in range(tamano * tamano):
            while True:
                valor = simpledialog.askinteger("Ingresar valor", f"Ingrese el valor para la posición {i // tamano}, {i % tamano} (0-99):", minvalue=0, maxvalue=99)
                if valor is not None and 0 <= valor <= 99:
                    datos.append(valor)
                    break
                else:
                    messagebox.showwarning("Error", "Error, pruebe con un número del 0 al 99.")
        matriz = np.array(datos).reshape(tamano, tamano)
        return matriz
    else:
        return None

def calcular_ciclo_hamiltoniano_minimo(matriz, text_widget):
    n = len(matriz)
    vertices = list(range(n))
    mejor_ciclo = None
    menor_distancia = float("inf")
    proceso_busqueda = []

    def calcular_ciclo_parcial(ciclo_actual, distancia_actual):
        nonlocal mejor_ciclo, menor_distancia
        if len(ciclo_actual) == n:
            distancia_total = distancia_actual + matriz[ciclo_actual[-1]][ciclo_actual[0]]
            proceso_busqueda.append(f"Evaluando ciclo: {ciclo_actual + [ciclo_actual[0]]} con distancia total {distancia_total}")
            if distancia_total < menor_distancia:
                menor_distancia = distancia_total
                mejor_ciclo = ciclo_actual[:]
        else:
            for v in vertices:
                if v not in ciclo_actual:
                    nueva_distancia = distancia_actual + matriz[ciclo_actual[-1]][v]
                    proceso_busqueda.append(f"Verificando vértice {v} desde {ciclo_actual[-1]} con distancia parcial {nueva_distancia}")
                    if nueva_distancia < menor_distancia:
                        calcular_ciclo_parcial(ciclo_actual + [v], nueva_distancia)

    calcular_ciclo_parcial([0], 0)

    ciclo_str = " ".join(map(str, mejor_ciclo)) + f" {mejor_ciclo[0]}"
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, f"(Ciclo Hamiltoniano mínimo):\n{ciclo_str}\n")
    text_widget.insert(tk.END, f"Distancia mínima: {menor_distancia}\n")
    return proceso_busqueda

def mostrar_proceso_busqueda(proceso_busqueda):
    ventana_proceso = tk.Toplevel()
    ventana_proceso.title("Proceso de Búsqueda del Ciclo Hamiltoniano")
    ventana_proceso.geometry("600x400")

    text_proceso = tk.Text(ventana_proceso, height=20, width=70)
    text_proceso.pack(pady=10)

    text_proceso.insert(tk.END, "Proceso de búsqueda del Ciclo Hamiltoniano:\n\n")
    for paso in proceso_busqueda:
        text_proceso.insert(tk.END, f"{paso}\n")

    boton_cerrar = tk.Button(ventana_proceso, text="Cerrar", command=ventana_proceso.destroy, bg="#D32F2F")
    boton_cerrar.pack(pady=5)

def mostrar_matriz(matriz, text_widget):
    if matriz is not None:
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END,"Matriz generada:\n")
        for fila in matriz:
            text_widget.insert(tk.END, f"{fila}\n")
    else:
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, "No se pudo generar la matriz.\n")

def solicitar_tamano():
    tamano = simpledialog.askinteger("Tamaño de la matriz", "Ingrese el tamaño de la matriz (entre 8 y 16):", minvalue=8, maxvalue=16)
    if tamano is None:
        return None
    if not validar_tamano_matriz(tamano):
        return None
    return tamano

def ajustar_text_widget(text_widget, tamano):
    caracteres_por_numero = 3
    ancho_necesario = tamano * caracteres_por_numero

    if tamano >= 12:
        text_widget.config(height=tamano + 2, width=ancho_necesario + 2)
    else:
        text_widget.config(height=18, width=34)

def iniciar_programa(ventana_inicio):
    ventana_inicio.destroy()
    main_program()

def main_program():
    ventana = tk.Tk()
    ventana.title("Matemática Computacional")
    ventana.geometry("800x600")
    ventana.configure(bg="#7788a4")  

    matriz = None
    proceso_busqueda = None

    label_titulo = tk.Label(ventana, text="Matemática Computacional", font=("Monserrat", 20, "bold"), fg="#881B37", bg="#7788a4")
    label_titulo.pack(pady=10)
    label_subtitulo = tk.Label(ventana, text="PROYECTO: CICLO HAMILTONIANO", font=("Times New Roman", 14), fg="black", bg="#7788a4")  
    label_subtitulo.pack()

    text_area = tk.Text(ventana, height=18, width=34)
    text_area.pack(pady=10)

    boton_estudiantes = tk.Button(ventana, text="Mostrar Estudiantes", command=mostrar_estudiantes, bg="#FCD128", width=20, height=2)
    boton_estudiantes.place(x=10, y=10)

    def calcular_exhaustivo():
        if matriz is not None:
            nonlocal proceso_busqueda
            proceso_busqueda = calcular_ciclo_hamiltoniano_minimo(matriz, text_area)
            boton_proceso.pack(pady=5, before=boton_salir)
        else:
            messagebox.showwarning("Error", "Primero genera o ingresa una matriz.")

    boton_exhaustivo = tk.Button(ventana, text="Aplicar \nCiclo Hamiltoniano", bg="#757575", fg="white", width=20, height=2, command=calcular_exhaustivo)

    def generar_matriz_aleatoria():
        nonlocal matriz
        tamano = solicitar_tamano()
        if tamano is not None:
            matriz = generarMatriz(tamano)
            ajustar_text_widget(text_area, tamano)
            mostrar_matriz(matriz, text_area)
            if matriz is not None:
                boton_exhaustivo.pack(pady=5, before=boton_salir)

    boton_matriz_aleatoria = tk.Button(ventana, text="Generar Matriz Aleatoria", bg="#66BB6A", width=20, height=2, command=generar_matriz_aleatoria)
    boton_matriz_aleatoria.pack(pady=5)

    def ingresar_matriz_manual():
        nonlocal matriz
        tamano = solicitar_tamano()
        if tamano is not None:
            matriz = ingresarMatriz(tamano)
            ajustar_text_widget(text_area, tamano)
            mostrar_matriz(matriz, text_area)
            if matriz is not None:
                boton_exhaustivo.pack(pady=5, before=boton_salir)

    boton_matriz_manual = tk.Button(ventana, text="Ingresar Matriz Manual", bg="#FF7043", width=20, height=2, command=ingresar_matriz_manual)
    boton_matriz_manual.pack(pady=5)

    def ver_proceso():
        if proceso_busqueda is not None:
            mostrar_proceso_busqueda(proceso_busqueda)
        else:
            messagebox.showwarning("Error", "Primero ejecuta la búsqueda del Ciclo Hamiltoniano.")

    boton_proceso = tk.Button(ventana, text="Mostrar \nProceso de Búsqueda", bg="#29B6F6", width=20, height=2, command=ver_proceso)

    boton_salir = tk.Button(ventana, text="Salir", command=ventana.destroy, bg="#D32F2F", width=20, height=2)
    boton_salir.pack(pady=5)

    ventana.mainloop()

def main():
    ventana_inicio = tk.Tk()
    ventana_inicio.title("Bienvenido")
    ventana_inicio.geometry("800x600")
    ventana_inicio.configure(bg="#1c2f4e")

    label_arte = tk.Label(ventana_inicio, text=arte_bicicleta, font=("Courier", 10), bg="#1c2f4e", fg="white", justify="left")
    label_arte.pack(pady=10)

    label_problema = tk.Label(ventana_inicio, text="PROBLEMA DEL AGENTE VIAJERO", font=("Monserrat", 16, "bold"), bg="#1c2f4e", fg="white")
    label_problema.pack(pady=10)

    boton_iniciar = tk.Button(ventana_inicio, text="INICIAR PROGRAMA", font=("Monserrat", 18, "bold"), bg="#881B37", fg="black", width=20, height=3, command=lambda: iniciar_programa(ventana_inicio))
    boton_iniciar.pack(expand=True, pady=50)

    ventana_inicio.mainloop()

if __name__ == "__main__":
    main()
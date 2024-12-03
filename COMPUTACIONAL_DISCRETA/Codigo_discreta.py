from random import randint
import networkx as nx
import matplotlib.pyplot as plt
import os


def mostrar_menu():
    print("Filogenia Dirigida")
    print("Menú:")
    print("-----")
    print("1. Ejercicios de árboles dirigidos")
    print("2. Ejercicios de árboles filogénicos")
    print("3. Salir")


def menu_ejercicios():
    print("Ejercicios de árboles dirigidos:")
    print("--------------------------------")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Regresar al menú principal")


def menu_filogenia():
    print("Ejercicios de árboles filogénicos:")
    print("--------------------------------")
    print("1. Descendientes del Archosauria")
    print("2. Descendientes del Bovidae")
    print("3. Descendientes del Chimaeriformes")
    print("4. Regresar al menú principal")


def mostrar_estudiantes():
    print("Segundo Avance TF - Semana 5")
    print("---------------------------")
    print("Integrantes:")
    print("- Lucia Ximena Flores Rivera (U202311345) ")
    print("- Giovanni Alexander Palomino Mathey (U202312001) ")
    print("- Paula Ariana Muñoz Guarnizo (U202312321) ")
    print("- Dayana Kety Gómez Rodríguez (U202311495) ")
    print("- Leonardo Sebastián Vásquez Montañe (U202312065) ")
    input("\nPresiona Enter para continuar...")


def generarDatos(n):
    conjunto = []
    for i in range(n):
        conjunto.append(chr(65 + i))
    return conjunto


def generarDR(n, conjunto):
    nodos = []
    for i in range(n):
        num = randint(0, len(conjunto) - 1)
        while conjunto[num] in nodos:
            num = randint(0, len(conjunto) - 1)
        nodos.append(conjunto[num])

    return nodos


def generarT(nodos):
    relacionT = [
        (nodos[0], nodos[1]),
        (nodos[0], nodos[2]),
        (nodos[1], nodos[3]),
        (nodos[2], nodos[4]),
    ]
    return relacionT


def digrafoT(nodos, relacionT):
    d = nx.DiGraph()
    d.add_nodes_from(nodos)
    d.add_edges_from(relacionT)
    pos = {
        nodos[0]: (0, 0),
        nodos[1]: (-1, -1),
        nodos[2]: (1, -1),
        nodos[3]: (-2, -2),
        nodos[4]: (2, -2),
    }
    plt.title("Dígrafo de T")
    nx.draw(d, pos, with_labels=True, node_color="pink", node_size=1500)
    plt.show()


def arbolbiT(nodos):
    relacionAB = [
        (nodos[0], nodos[1]),
        (nodos[1], nodos[2]),
        (nodos[1], nodos[3]),
        (nodos[2], nodos[4]),
    ]
    d = nx.DiGraph()
    d.add_nodes_from(nodos)
    d.add_edges_from(relacionAB)
    pos = {
        nodos[0]: (0, 0),
        nodos[1]: (-1, -1),
        nodos[2]: (0, -2),
        nodos[3]: (-2, -2),
        nodos[4]: (-1, -3),
    }
    plt.title("Árbol Binario B(T)")
    nx.draw(d, pos, with_labels=True, node_color="pink", node_size=1500)
    plt.show()


def generarR(nodos):
    relacionR = [
        (nodos[0], nodos[1]),
        (nodos[0], nodos[2]),
        (nodos[1], nodos[3]),
        (nodos[1], nodos[4]),
        (nodos[2], nodos[5]),
        (nodos[2], nodos[6]),
        (nodos[3], nodos[7]),
        (nodos[3], nodos[8]),
        (nodos[4], nodos[9]),
        (nodos[4], nodos[10]),
        (nodos[5], nodos[11]),
        (nodos[5], nodos[12]),
    ]
    return relacionR


def digrafoR(nodos, relacionR):
    d = nx.DiGraph()
    d.add_nodes_from(nodos)
    d.add_edges_from(relacionR)
    pos = {
        nodos[0]: (0, 0),
        nodos[1]: (-7, -1),
        nodos[2]: (7, -1),
        nodos[3]: (-10, -2),
        nodos[4]: (-4, -2),
        nodos[5]: (4, -2),
        nodos[6]: (10, -2),
        nodos[7]: (-11.5, -3),
        nodos[8]: (-8.5, -3),
        nodos[9]: (-5.5, -3),
        nodos[10]: (-2.5, -3),
        nodos[11]: (2.5, -3),
        nodos[12]: (5.5, -3),
    }
    plt.title("Dígrafo de R")
    nx.draw(d, pos, with_labels=True, node_color="pink", node_size=1500)
    plt.show()


def arbolbiR(nodos):
    relacionAB = [
        (nodos[0], nodos[1]),
        (nodos[1], nodos[2]),
        (nodos[1], nodos[3]),
        (nodos[2], nodos[5]),
        (nodos[3], nodos[4]),
        (nodos[3], nodos[7]),
        (nodos[4], nodos[9]),
        (nodos[5], nodos[6]),
        (nodos[5], nodos[11]),
        (nodos[7], nodos[8]),
        (nodos[9], nodos[10]),
        (nodos[11], nodos[12]),
    ]
    d = nx.DiGraph()
    d.add_nodes_from(nodos)
    d.add_edges_from(relacionAB)
    pos = {
        nodos[0]: (0, 0),
        nodos[1]: (-5, -1),
        nodos[2]: (0, -2),
        nodos[3]: (-10, -2),
        nodos[4]: (-7, -3),
        nodos[5]: (-3, -3),
        nodos[6]: (-1, -4),
        nodos[7]: (-13, -3),
        nodos[8]: (-11, -4),
        nodos[9]: (-9, -4),
        nodos[10]: (-7, -5),
        nodos[11]: (-5, -4),
        nodos[12]: (-3, -5),
    }
    plt.title("Árbol Binario B(R)")
    nx.draw(d, pos, with_labels=True, node_color="pink", node_size=1500)
    plt.show()


def generarS(nodos):
    relacionS = [
        (nodos[0], nodos[1]),
        (nodos[0], nodos[2]),
        (nodos[0], nodos[3]),
        (nodos[1], nodos[4]),
        (nodos[1], nodos[5]),
        (nodos[2], nodos[6]),
        (nodos[2], nodos[7]),
        (nodos[2], nodos[8]),
        (nodos[3], nodos[9]),
        (nodos[3], nodos[10]),
        (nodos[5], nodos[11]),
        (nodos[5], nodos[12]),
        (nodos[8], nodos[13]),
        (nodos[10], nodos[14]),
    ]
    return relacionS


def digrafoS(nodos, relacionS):
    d = nx.DiGraph()
    d.add_nodes_from(nodos)
    d.add_edges_from(relacionS)
    pos = {
        nodos[0]: (0, 0),
        nodos[1]: (-10, -1),
        nodos[2]: (0, -1),
        nodos[3]: (10, -1),
        nodos[4]: (-12, -2),
        nodos[5]: (-8, -2),
        nodos[6]: (-4, -2),
        nodos[7]: (0, -2),
        nodos[8]: (4, -2),
        nodos[9]: (8, -2),
        nodos[10]: (12, -2),
        nodos[11]: (-10, -3),
        nodos[12]: (-6, -3),
        nodos[13]: (4, -3),
        nodos[14]: (12, -3),
    }
    plt.title("Dígrafo de S")
    nx.draw(d, pos, with_labels=True, node_color="pink", node_size=1500)
    plt.show()


def arbolbiS(nodos):
    relacionAB = [
        (nodos[0], nodos[1]),
        (nodos[1], nodos[2]),
        (nodos[2], nodos[3]),
        (nodos[1], nodos[4]),
        (nodos[4], nodos[5]),
        (nodos[2], nodos[6]),
        (nodos[6], nodos[7]),
        (nodos[7], nodos[8]),
        (nodos[3], nodos[9]),
        (nodos[9], nodos[10]),
        (nodos[5], nodos[11]),
        (nodos[11], nodos[12]),
        (nodos[8], nodos[13]),
        (nodos[10], nodos[14]),
    ]
    d = nx.DiGraph()
    d.add_nodes_from(nodos)
    d.add_edges_from(relacionAB)
    pos = {
        nodos[0]: (0, 0),
        nodos[1]: (-5, -1),
        nodos[2]: (0, -2),
        nodos[3]: (6, -3),
        nodos[4]: (-7, -2),
        nodos[5]: (-5, -3),
        nodos[6]: (-2, -3),
        nodos[7]: (0, -4),
        nodos[8]: (2, -5),
        nodos[9]: (4, -4),
        nodos[10]: (6, -5),
        nodos[11]: (-7, -4),
        nodos[12]: (-5, -5),
        nodos[13]: (0, -6),
        nodos[14]: (4, -6),
    }
    plt.title("Árbol Binario B(S)")
    nx.draw(d, pos, with_labels=True, node_color="pink", node_size=1500)
    plt.show()


def generarARCHO(nodos):
    relacionARCHO = [
        (nodos[0], nodos[1]),
        (nodos[0], nodos[2]),
        (nodos[1], nodos[3]),
        (nodos[2], nodos[4]),
        (nodos[2], nodos[5]),
        (nodos[4], nodos[6]),
        (nodos[4], nodos[7]),
        (nodos[5], nodos[8]),
        (nodos[5], nodos[9]),
    ]
    return relacionARCHO


def digrafoARCHO(nodos, relacionARCHO):
    d = nx.DiGraph()
    d.add_nodes_from(nodos)
    d.add_edges_from(relacionARCHO)
    pos = {
        nodos[0]: (0, 0),
        nodos[1]: (-4, -1),
        nodos[2]: (4, -1),
        nodos[3]: (-4, -2),
        nodos[4]: (1, -2),
        nodos[5]: (7, -2),
        nodos[6]: (0, -3),
        nodos[7]: (2, -3),
        nodos[8]: (6, -3),
        nodos[9]: (8, -3),
    }

    plt.figtext(
        0.02,
        0.03,
        f"{nodos[0]}: Archosauiria\n{nodos[1]}: Crocodylidae\n{nodos[2]}: Aves\n{nodos[3]}: Crocodilo del Nilo\n"
        f"{nodos[4]}: Paleognathae\n{nodos[5]}: Neognathae\n{nodos[6]}: Emu\n{nodos[7]}: Avestruz",
    )
    plt.figtext(
        0.25,
        0.03,
        f"{nodos[8]}: Gallina\n{nodos[9]}: Neoaves",
    )
    plt.title("Dígrafo del árbol filogenetico del Archosauria")
    nx.draw(d, pos, with_labels=True, node_color="pink", node_size=1500)
    plt.show()


def arbolbiARCHO(nodos):
    relacionAB = [
        (nodos[0], nodos[1]),
        (nodos[1], nodos[2]),
        (nodos[1], nodos[3]),
        (nodos[2], nodos[4]),
        (nodos[4], nodos[5]),
        (nodos[4], nodos[6]),
        (nodos[5], nodos[8]),
        (nodos[6], nodos[7]),
        (nodos[8], nodos[9]),
    ]
    d = nx.DiGraph()
    d.add_nodes_from(nodos)
    d.add_edges_from(relacionAB)
    pos = {
        nodos[0]: (0, 0),
        nodos[1]: (-2, -1),
        nodos[2]: (0, -2),
        nodos[3]: (-4, -2),
        nodos[4]: (-2, -3),
        nodos[5]: (0, -4),
        nodos[6]: (-4, -4),
        nodos[7]: (-2.5, -5),
        nodos[8]: (-1.5, -5),
        nodos[9]: (0, -6),
    }
    plt.figtext(
        0.02,
        0.03,
        f"{nodos[0]}: Archosauiria\n{nodos[1]}: Crocodylidae\n{nodos[2]}: Aves\n{nodos[3]}: Crocodilo del Nilo\n"
        f"{nodos[4]}: Paleognathae",
    )

    plt.figtext(
        0.25,
        0.03,
        f"{nodos[5]}: Neognathae\n{nodos[6]}: Emu\n{nodos[7]}: Avestruz\n{nodos[8]}: Gallina\n{nodos[9]}: Neoaves",
    )

    plt.title("Árbol Binario del árbol filogenetico del Archosauria")
    nx.draw(d, pos, with_labels=True, node_color="pink", node_size=1500)
    plt.show()


def generarBOVI(nodos):
    relacionBOVI = [
        (nodos[0], nodos[1]),
        (nodos[0], nodos[2]),
        (nodos[1], nodos[3]),
        (nodos[1], nodos[4]),
        (nodos[2], nodos[5]),
        (nodos[2], nodos[6]),
        (nodos[3], nodos[7]),
        (nodos[3], nodos[8]),
        (nodos[4], nodos[9]),
        (nodos[5], nodos[10]),
        (nodos[6], nodos[11]),
        (nodos[6], nodos[12]),
    ]
    return relacionBOVI


def digrafoBOVI(nodos, relacionBOVI):
    d = nx.DiGraph()
    d.add_nodes_from(nodos)
    d.add_edges_from(relacionBOVI)
    pos = {
        nodos[0]: (0, 0),
        nodos[1]: (-7, -1),
        nodos[2]: (7, -1),
        nodos[3]: (-10, -2),
        nodos[4]: (-4, -2),
        nodos[5]: (4, -2),
        nodos[6]: (10, -2),
        nodos[7]: (-11.5, -3),
        nodos[8]: (-8.5, -3),
        nodos[9]: (-4, -3),
        nodos[10]: (4, -3),
        nodos[11]: (8.5, -3),
        nodos[12]: (11.5, -3),
    }

    plt.figtext(
        0.02,
        0.45,
        f"{nodos[0]}: Bovidae\n{nodos[1]}: Bovinae\n{nodos[2]}: Antilopinae\n{nodos[3]}: Bovini\n"
        f"{nodos[4]}: Tregelaphini\n{nodos[5]}: Antilopini\n{nodos[6]}: Caprini\n{nodos[7]}: Vaca\n"
        f"{nodos[8]}: Búfalo de agua\n{nodos[9]}: Taurotragus oryx\n{nodos[10]}: Gacela\n{nodos[11]}: Oveja\n"
        f"{nodos[12]}: Cabra",
    )
    plt.title("Dígrafo del árbol filogenetico del Bovidae")
    nx.draw(d, pos, with_labels=True, node_color="pink", node_size=1500)
    plt.show()


def arbolbiBOVI(nodos):
    relacionAB = [
        (nodos[0], nodos[1]),
        (nodos[1], nodos[2]),
        (nodos[1], nodos[3]),
        (nodos[2], nodos[5]),
        (nodos[3], nodos[4]),
        (nodos[3], nodos[7]),
        (nodos[4], nodos[9]),
        (nodos[5], nodos[6]),
        (nodos[5], nodos[10]),
        (nodos[6], nodos[11]),
        (nodos[7], nodos[8]),
        (nodos[11], nodos[12]),
    ]
    d = nx.DiGraph()
    d.add_nodes_from(nodos)
    d.add_edges_from(relacionAB)
    pos = {
        nodos[0]: (0, 0),
        nodos[1]: (-5, -1),
        nodos[2]: (0, -2),
        nodos[3]: (-10, -2),
        nodos[4]: (-7, -3),
        nodos[5]: (-3, -3),
        nodos[6]: (-1, -4),
        nodos[7]: (-13, -3),
        nodos[8]: (-11, -4),
        nodos[9]: (-9, -4),
        nodos[10]: (-5, -4),
        nodos[11]: (-3, -5),
        nodos[12]: (-1, -6),
    }

    plt.figtext(
        0.02,
        0.03,
        f"{nodos[0]}: Bovidae\n{nodos[1]}: Bovinae\n{nodos[2]}: Antilopinae\n{nodos[3]}: Bovini\n"
        f"{nodos[4]}: Tregelaphini\n{nodos[5]}: Antilopini\n{nodos[6]}: Caprini",
    )

    plt.figtext(
        0.25,
        0.03,
        f"{nodos[7]}: Vaca\n{nodos[8]}: Búfalo de agua\n{nodos[9]}: Taurotragus oryx\n{nodos[10]}: Gacela\n"
        f"{nodos[11]}: Oveja\n{nodos[12]}: Cabra",
    )
    plt.title("Árbol Binario del árbol filogenetico del Bovidae")
    nx.draw(d, pos, with_labels=True, node_color="pink", node_size=1500)
    plt.show()


def generarCHI(nodos):
    relacionCHI = [
        (nodos[0], nodos[1]),
        (nodos[0], nodos[2]),
        (nodos[1], nodos[3]),
        (nodos[1], nodos[4]),
        (nodos[2], nodos[5]),
        (nodos[3], nodos[6]),
        (nodos[3], nodos[7]),
        (nodos[4], nodos[8]),
        (nodos[4], nodos[9]),
        (nodos[5], nodos[10]),
    ]
    return relacionCHI


def digrafoCHI(nodos, relacionARCHO):
    d = nx.DiGraph()
    d.add_nodes_from(nodos)
    d.add_edges_from(relacionARCHO)
    pos = {
        nodos[0]: (0, 0),
        nodos[1]: (-3, -1),
        nodos[2]: (3, -1),
        nodos[3]: (-5, -2),
        nodos[4]: (-1, -2),
        nodos[5]: (3, -2),
        nodos[6]: (-6, -3),
        nodos[7]: (-4, -3),
        nodos[8]: (-2, -3),
        nodos[9]: (0, -3),
        nodos[10]: (3, -3),
    }

    plt.figtext(
        0.02,
        0.45,
        f"{nodos[0]}: Chimaeriformes\n{nodos[1]}: Selachimorpha\n{nodos[2]}: Batoidea\n"
        f"{nodos[3]}: Tiburón ángel\n{nodos[4]}: Tiburón vaca\n{nodos[5]}: Raya eléctrica\n"
        f"{nodos[6]}: Tiburón sierra\n{nodos[7]}: Squaliformes\n{nodos[8]}: Tiburón alfombra\n"
        f"{nodos[9]}: Tiburón toro\n{nodos[10]}: Pez sierra",
    )
    plt.title("Dígrafo del árbol filogenetico del Chimaeriformes")
    nx.draw(d, pos, with_labels=True, node_color="pink", node_size=1500)
    plt.show()


def arbolbiCHI(nodos):
    relacionAB = [
        (nodos[0], nodos[1]),
        (nodos[1], nodos[2]),
        (nodos[1], nodos[3]),
        (nodos[2], nodos[5]),
        (nodos[3], nodos[4]),
        (nodos[3], nodos[6]),
        (nodos[4], nodos[8]),
        (nodos[5], nodos[10]),
        (nodos[6], nodos[7]),
        (nodos[8], nodos[9]),
    ]
    d = nx.DiGraph()
    d.add_nodes_from(nodos)
    d.add_edges_from(relacionAB)
    pos = {
        nodos[0]: (0, 0),
        nodos[1]: (-3, -1),
        nodos[2]: (0, -2),
        nodos[3]: (-6, -2),
        nodos[4]: (-4, -3),
        nodos[5]: (-1, -3),
        nodos[6]: (-8, -3),
        nodos[7]: (-7, -4),
        nodos[8]: (-5, -4),
        nodos[9]: (-4, -5),
        nodos[10]: (-2, -4),
    }
    plt.figtext(
        0.02,
        0.5,
        f"{nodos[0]}: Chimaeriformes\n{nodos[1]}: Selachimorpha\n{nodos[2]}: Batoidea\n{nodos[3]}: Tiburón ángel\n"
        f"{nodos[4]}: Tiburón vaca\n{nodos[5]}: Raya eléctrica\n{nodos[6]}: Tiburón sierra\n{nodos[7]}: Squaliformes\n"
        f"{nodos[8]}: Tiburón alfombra\n{nodos[9]}: Tiburón toro\n{nodos[10]}: Pez sierra",
    )

    plt.title("Árbol Binario del árbol filogenetico del Chimaeriformes")
    nx.draw(d, pos, with_labels=True, node_color="pink", node_size=1500)
    plt.show()


# Preorden, inorden y postorden:
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []


def construir_arbol(relacion):
    _nodos = {}  # Diccionario para almacenar los nodos por valor
    for padre, hijo in relacion:
        if padre not in _nodos:
            _nodos[padre] = Nodo(padre)
        if hijo not in _nodos:
            _nodos[hijo] = Nodo(hijo)
        _nodos[padre].hijos.append(_nodos[hijo])
    return _nodos[relacion[0][0]]  # Se retorna el nodo raíz


def preorden(nodo, nodos):
    if nodo:
        print(nodos[nodo.valor], end=" ")
        for hijo in nodo.hijos:
            preorden(hijo, nodos)


def inorden(nodo, nodos):
    if nodo:
        if len(nodo.hijos) > 1:
            inorden(nodo.hijos[0], nodos)
            print(nodos[nodo.valor], end=" ")
            for hijo in nodo.hijos[1:]:
                inorden(hijo, nodos)
        else:
            for hijo in nodo.hijos:
                inorden(hijo, nodos)
            print(nodos[nodo.valor], end=" ")


def postorden(nodo, nodos):
    if nodo:
        for hijo in nodo.hijos:
            postorden(hijo, nodos)
        print(nodos[nodo.valor], end=" ")


# -------------------------------------------------


def ejercicio1():
    conjunto = generarDatos(10)
    nodos = generarDR(5, conjunto)
    relacionT = generarT(nodos)

    _relacionT = [
        (0, 1),
        (0, 2),
        (1, 3),
        (2, 4),
    ]
    _arbolT = construir_arbol(_relacionT)

    print("Elementos del conjunto X= ", conjunto)
    print("Elementos de relación de X, T= ", relacionT)

    print("\nPreorden de T: ")
    preorden(_arbolT, nodos)
    print("\nInorden de T: ")
    inorden(_arbolT, nodos)
    print("\nPostorden de T: ")
    postorden(_arbolT, nodos)

    digrafoT(nodos, relacionT)
    arbolbiT(nodos)


def ejercicio2():
    conjunto = generarDatos(13)
    nodos = generarDR(13, conjunto)
    relacionR = generarR(nodos)

    _relacionR = [
        (0, 1),
        (0, 2),
        (1, 3),
        (1, 4),
        (2, 5),
        (2, 6),
        (3, 7),
        (3, 8),
        (4, 9),
        (4, 10),
        (5, 11),
        (5, 12),
    ]
    _arbolR = construir_arbol(_relacionR)

    print("Elementos del conjunto X= ", conjunto)
    print("Elementos de relación de X, R= ", relacionR)

    print("\nPreorden de R: ")
    preorden(_arbolR, nodos)
    print("\nInorden de R: ")
    inorden(_arbolR, nodos)
    print("\nPostorden de R: ")
    postorden(_arbolR, nodos)

    digrafoR(nodos, relacionR)
    arbolbiR(nodos)


def ejercicio3():
    conjunto = generarDatos(15)
    nodos = generarDR(15, conjunto)
    relacionS = generarS(nodos)

    _relacionS = [
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 4),
        (1, 5),
        (2, 6),
        (2, 7),
        (2, 8),
        (3, 9),
        (3, 10),
        (5, 11),
        (5, 12),
        (8, 13),
        (10, 14),
    ]
    _arbolS = construir_arbol(_relacionS)

    print("Elementos del conjunto X= ", conjunto)
    print("Elementos de relación de X, S= ", relacionS)

    print("\nPreorden de S: ")
    preorden(_arbolS, nodos)
    print("\nInorden de S: ")
    inorden(_arbolS, nodos)
    print("\nPostorden de S: ")
    postorden(_arbolS, nodos)

    digrafoS(nodos, relacionS)
    arbolbiS(nodos)


def ejercicio4():
    conjunto = generarDatos(10)
    nodos = generarDR(10, conjunto)
    relacionARCHO = generarARCHO(nodos)

    _relacionARCHO = [
        (0, 1),
        (0, 2),
        (1, 3),
        (2, 4),
        (2, 5),
        (4, 6),
        (4, 7),
        (5, 8),
        (5, 9),
    ]
    _arbolARCHO = construir_arbol(_relacionARCHO)

    print("Elementos del conjunto X= ", conjunto)
    print("Elementos de relación de X, A= ", relacionARCHO)

    print("\nPreorden de A: ")
    preorden(_arbolARCHO, nodos)
    print("\nInorden de A: ")
    inorden(_arbolARCHO, nodos)
    print("\nPostorden de A: ")
    postorden(_arbolARCHO, nodos)

    digrafoARCHO(nodos, relacionARCHO)
    arbolbiARCHO(nodos)


def ejercicio5():
    conjunto = generarDatos(13)
    nodos = generarDR(13, conjunto)
    relacionBOVI = generarBOVI(nodos)

    _relacionBOVI = [
        (0, 1),
        (0, 2),
        (1, 3),
        (1, 4),
        (2, 5),
        (2, 6),
        (3, 7),
        (3, 8),
        (4, 9),
        (5, 10),
        (6, 11),
        (6, 12),
    ]

    _arbolBOVI = construir_arbol(_relacionBOVI)

    print("Elementos del conjunto X= ", conjunto)
    print("Elementos de relación de X, B= ", relacionBOVI)

    print("\nPreorden de B: ")
    preorden(_arbolBOVI, nodos)
    print("\nInorden de B: ")
    inorden(_arbolBOVI, nodos)
    print("\nPostorden de B: ")
    postorden(_arbolBOVI, nodos)

    digrafoBOVI(nodos, relacionBOVI)
    arbolbiBOVI(nodos)


def ejercicio6():
    conjunto = generarDatos(11)
    nodos = generarDR(11, conjunto)
    relacionCHI = generarCHI(nodos)

    _relacionCHI = [
        (0, 1),
        (0, 2),
        (1, 3),
        (1, 4),
        (2, 5),
        (3, 6),
        (3, 7),
        (4, 8),
        (4, 9),
        (5, 10),
    ]

    _arbolCHI = construir_arbol(_relacionCHI)

    print("Elementos del conjunto X= ", conjunto)
    print("Elementos de relación de X, C= ", relacionCHI)

    print("\nPreorden de C: ")
    preorden(_arbolCHI, nodos)
    print("\nInorden de C: ")
    inorden(_arbolCHI, nodos)
    print("\nPostorden de C: ")
    postorden(_arbolCHI, nodos)

    digrafoCHI(nodos, relacionCHI)
    arbolbiCHI(nodos)


def main():
    os.system("cls")
    mostrar_estudiantes()
    while True:
        os.system("cls")
        mostrar_menu()
        opcion = input("Selecciona una opción (1, 2, 3): ")

        if opcion == "1":
            while True:
                os.system("cls")
                menu_ejercicios()
                opcion = input("Selecciona una opción (1, 2, 3, 4): ")

                if opcion == "1":
                    os.system("cls")
                    ejercicio1()
                    input("\nPresiona Enter para continuar...")
                elif opcion == "2":
                    os.system("cls")
                    ejercicio2()
                    input("\nPresiona Enter para continuar...")
                elif opcion == "3":
                    os.system("cls")
                    ejercicio3()
                    input("\nPresiona Enter para continuar...")
                elif opcion == "4":
                    break
                else:
                    print("Opción no válida. Inténtalo de nuevo.")
                    input("\nPresiona Enter para continuar...")
        elif opcion == "2":
            while True:
                os.system("cls")
                menu_filogenia()
                opcion = input("Selecciona la cantidad de elementos(10, 11, 13, 0(salir)): ")

                if opcion == "10":
                    os.system("cls")
                    ejercicio4()
                    input("\nPresiona Enter para continuar...")
                elif opcion == "11":
                    os.system("cls")
                    ejercicio5()
                    input("\nPresiona Enter para continuar...")
                elif opcion == "13":
                    os.system("cls")
                    ejercicio6()
                    input("\nPresiona Enter para continuar...")
                elif opcion == "0":
                    break
                else:
                    print("Opción no válida. Inténtalo de nuevo.")
                    input("\nPresiona Enter para continuar...")
        elif opcion == "3":
            os.system("cls")
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            input("\nPresiona Enter para continuar...")


main()
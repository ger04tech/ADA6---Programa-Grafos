import networkx as nx
import matplotlib.pyplot as plt

# Definición de los estados y conexiones con sus costos
estados = ["A", "B", "C", "D", "E", "F", "G"]
conexiones = [
    ("A", "B", 10), ("A", "C", 15), ("B", "D", 20),
    ("C", "D", 25), ("D", "E", 30), ("E", "F", 35),
    ("F", "G", 40), ("G", "A", 45)
]

# Crear el grafo y añadir las conexiones con sus costos
G = nx.Graph()
G.add_weighted_edges_from(conexiones)

# Función para mostrar los estados y sus relaciones
def mostrar_relaciones(grafo):
    print("Estados y sus relaciones:")
    for origen, destino, datos in grafo.edges(data=True):
        print(f"{origen} <-> {destino} con costo {datos['weight']}")

# Función para calcular el costo de un recorrido
def calcular_costo(grafo, recorrido):
    costo_total = 0
    for i in range(len(recorrido) - 1):
        if grafo.has_edge(recorrido[i], recorrido[i + 1]):  # Verificar si la conexión existe
            costo_total += grafo[recorrido[i]][recorrido[i + 1]]['weight']
        else:
            print(f"No existe conexión entre {recorrido[i]} y {recorrido[i + 1]}")
            return None
    return costo_total

# Dibujar el grafo
def dibujar_grafo(grafo):
    pos = nx.spring_layout(grafo)  # Posiciones de los nodos para el grafo
    nx.draw(grafo, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight="bold")
    labels = nx.get_edge_attributes(grafo, 'weight')
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)
    plt.show()

# Ejemplo de recorrido sin repetir y con repetición
recorrido_sin_repetir = ["A", "B", "D", "E", "F", "G", "C"]
recorrido_con_repeticion = ["A", "B", "D", "E", "F", "G", "A"]

# Mostrar relaciones
mostrar_relaciones(G)

# Calcular y mostrar costos
costo_sin_repetir = calcular_costo(G, recorrido_sin_repetir)
if costo_sin_repetir is not None:
    print(f"Recorrido sin repetir: {recorrido_sin_repetir} - Costo: {costo_sin_repetir}")

costo_con_repeticion = calcular_costo(G, recorrido_con_repeticion)
if costo_con_repeticion is not None:
    print(f"Recorrido con repetición: {recorrido_con_repeticion} - Costo: {costo_con_repeticion}")

# Dibujar el grafo
dibujar_grafo(G)

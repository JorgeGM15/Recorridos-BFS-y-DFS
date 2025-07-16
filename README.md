# Implementación de Grafos y Recorridos BFS/DFS en Python

Este repositorio contiene tres scripts de Python que demuestran la creación de una estructura de datos de tipo **Grafo** y la implementación de dos algoritmos de recorrido fundamentales: la **Búsqueda en Profundidad (DFS)** y la **Búsqueda por Amplitud (BFS)**.

---

## 📜 Descripción de los Archivos

### 1. `Representacion de grafos.py`
* **Objetivo**: Muestra una representación básica de un grafo no dirigido mediante **listas de adyacencia**.
* **Nota**: Esta implementación contiene errores de diseño fundamentales (ver sección de "Errores de Diseño Comunes").

### 2. `Recorrido DFS.py`
* **Objetivo**: Proporciona una implementación **correcta y eficiente** del algoritmo de **Búsqueda en Profundidad (DFS)**.
* **Destacado**: Este script es el modelo a seguir en términos de diseño de clases, ya que utiliza un constructor `__init__` para garantizar que cada grafo sea una instancia independiente. El algoritmo calcula los tiempos de descubrimiento y finalización de cada vértice.

### 3. `Recorrido BFS.py`
* **Objetivo**: Implementa el algoritmo de **Búsqueda por Amplitud (BFS)**, ideal para encontrar el camino más corto en grafos sin pesos.
* **Nota**: Aunque la lógica del algoritmo BFS es correcta, el script sufre de los mismos errores de diseño que `Representacion de grafos.py` y contiene un error lógico en su ejecución principal.

---

## 🧠 Algoritmos Explicados

* **Búsqueda en Profundidad (DFS)**: Un algoritmo recursivo que explora tan lejos como sea posible a lo largo de cada rama antes de retroceder. Es útil para encontrar ciclos, componentes conectados y para ordenamiento topológico.
* **Búsqueda por Amplitud (BFS)**: Un algoritmo iterativo que explora los nodos "nivel por nivel". Utiliza una cola para gestionar los nodos pendientes de visitar y es la base para encontrar el camino más corto entre dos nodos en un grafo no ponderado.

---

## 🚀 Cómo Ejecutar los Scripts

Asegúrate de tener **Python 3** instalado. Abre una terminal en el directorio del proyecto y ejecuta el archivo que desees:

```bash
# Para ejecutar el script de representación
python "Representacion de grafos.py"

# Para ejecutar el recorrido DFS
python "Recorrido DFS.py"

# Para ejecutar el recorrido BFS
python "Recorrido BFS.py"

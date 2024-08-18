import uuid

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def heapify(arr, n, i):
    largest = i  # Ініціалізуємо найбільший елемент як корінь
    l = 2 * i + 1  # Лівий дочірній вузол
    r = 2 * i + 2  # Правий дочірній вузол

    # Перевірка чи існує лівий дочірній вузол і чи більше він за корінь
    if l < n and arr[i] < arr[l]:
        largest = l

    # Перевірка чи існує правий дочірній вузол і чи більше він за найбільший на даний момент
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Заміна кореня, якщо потрібно
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Заміна
        heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)

    # Побудова макс-купи
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

def heap_to_tree(arr):
    if not arr:
        return None

    def inner(index):
        if index >= len(arr):
            return None
        node = Node(arr[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner(0)

# Приклад використання
heap = [3, 9, 2, 1, 4, 5]
build_max_heap(heap)
print("Макс-купа:", heap)

# Побудова дерева з макс-купи
root = heap_to_tree(heap)

# Відображення дерева
draw_tree(root)

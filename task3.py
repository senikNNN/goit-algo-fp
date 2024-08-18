import heapq

class Graph:
    def __init__(self):
        self.edges = {}
        self.vertices = set()

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex in self.edges:
            self.edges[from_vertex].append((to_vertex, weight))
        else:
            self.edges[from_vertex] = [(to_vertex, weight)]
        self.vertices.add(from_vertex)
        self.vertices.add(to_vertex)

    def dijkstra(self, start_vertex):
        # Ініціалізуємо початкові відстані до всіх вершин як нескінченність
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start_vertex] = 0

        # Черга пріоритетів (heapq)
        priority_queue = [(0, start_vertex)]  # (відстань, вершина)
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Якщо відстань, отримана з черги, більша за вже відому, пропустити
            if current_distance > distances[current_vertex]:
                continue

            # Перевіряємо всіх сусідів поточної вершини
            for neighbor, weight in self.edges.get(current_vertex, []):
                distance = current_distance + weight

                # Якщо знайдено коротший шлях до сусіда, оновлюємо його
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

# Приклад використання
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)

start_vertex = 'A'
shortest_paths = graph.dijkstra(start_vertex)

print(f"Найкоротші шляхи від вершини {start_vertex}:")
for vertex, distance in shortest_paths.items():
    print(f"Вершина {vertex}: {distance}")

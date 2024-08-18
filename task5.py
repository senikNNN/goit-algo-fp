import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_sample_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root

def dfs_iterative(root):
    stack = [root]
    node_order = []
    edges = []
    
    while stack:
        node = stack.pop()
        if node:
            node_order.append(node.value)
            if node.right:
                stack.append(node.right)
                edges.append((node.value, node.right.value))
            if node.left:
                stack.append(node.left)
                edges.append((node.value, node.left.value))
    
    return node_order, edges

def bfs_iterative(root):
    queue = deque([root])
    node_order = []
    edges = []
    
    while queue:
        node = queue.popleft()
        if node:
            node_order.append(node.value)
            if node.left:
                queue.append(node.left)
                edges.append((node.value, node.left.value))
            if node.right:
                queue.append(node.right)
                edges.append((node.value, node.right.value))
    
    return node_order, edges

def color_for_step(step, total_steps):
    """ Generate a color from dark to light """
    color_intensity = int((step / total_steps) * 255)
    return f'#{color_intensity:02X}96F0'

def draw_tree(node_order, edges, traversal_type):
    graph = nx.DiGraph()
    graph.add_edges_from(edges)
    
    pos = nx.spring_layout(graph)
    node_colors = [color_for_step(i, len(node_order)) for i in range(len(node_order))]
    
    plt.figure(figsize=(10, 8))
    nx.draw(graph, pos, with_labels=True, node_color=node_colors, edge_color='gray', node_size=2000, font_size=16, font_color='black')
    plt.title(f'{traversal_type} Traversal')
    plt.show()

def visualize_tree_traversals(root):
    # DFS
    node_order_dfs, edges_dfs = dfs_iterative(root)
    draw_tree(node_order_dfs, edges_dfs, 'DFS')
    
    # BFS
    node_order_bfs, edges_bfs = bfs_iterative(root)
    draw_tree(node_order_bfs, edges_bfs, 'BFS')

# Build the sample tree and visualize traversals
root = build_sample_tree()
visualize_tree_traversals(root)

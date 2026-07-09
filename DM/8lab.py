import random

def add_edge(graph, u, v, cap):
    if u not in graph:
        graph[u] = {}
    if v not in graph[u]:
        graph[u][v] = 0
    graph[u][v] += cap

def dfs(graph, beginning, stock, parent):
    stack = [(beginning, 10**5)]
    visited = set([beginning])
    
    while stack:
        u, flow = stack.pop()
        for v, cap in graph[u].items():
            if v not in visited and cap > 0:
                visited.add(v)
                parent[v] = u
                new_flow = min(flow, cap)
                if v == stock:
                    return new_flow
                stack.append((v, new_flow))
    return 0

def max_flow(graph, beginning, stock):
    parent = {}
    total_flow = 0
    
    while True:
        path_flow = dfs(graph, beginning, stock, parent)
        if path_flow == 0:
            break
        
        v = stock
        while v != beginning:
            u = parent[v]
            graph[u][v] -= path_flow
            
            if v not in graph:
                graph[v] = {}
            if u not in graph[v]:
                graph[v][u] = 0
            graph[v][u] += path_flow
            v = u
        
        total_flow += path_flow
        parent = {}
    
    return total_flow

def find_points(graph, beginning):
    visited = set()
    stack = [beginning]
    visited.add(beginning)
    
    while stack:
        u = stack.pop()
        for v, cap in graph[u].items():
            if v not in visited and cap > 0:
                visited.add(v)
                stack.append(v)
    
    return visited

def min_cut(original_edges, graph, beginning):
    reachable = find_points(graph, beginning)
    cut_edges = []
    
    for u, v, cap in original_edges:
        if u in reachable and v not in reachable:
            cut_edges.append((u, v, cap))
    
    return cut_edges


edges = [
    ('S', '1'), ('S', '2'), ('S', '3'),
    ('3', '2'), ('2', '1'), ('1', '4'),
    ('2', '4'), ('2', '7'), ('3', '5'),
    ('5', '2'), ('3', '8'), ('7', '5'),
    ('4', '7'), ('4', '6'), ('8', '7'),
    ('7', '6'), ('7', '9'), ('8', '9'),
    ('6', 't'), ('7', 't'), ('9', 't')
]

edges_numeric = []
for u, v in edges:
    cap = random.randint(100, 1000)
    edges_numeric.append((u, v, cap))
graph = {}

for u, v, cap in edges_numeric:
    add_edge(graph, u, v, cap)

beginning = 'S'
stock = 't'
flow = max_flow(graph, beginning, stock)
print(f"Максимальный поток = {flow}")

cut_edges = min_cut(edges_numeric, graph, beginning)
print("Минимальный разрез (рёбра из S в t):")
cut_sum = 0
for u, v, cap in cut_edges:
    print(f"  {u} → {v} : {cap}")
    cut_sum += cap
print(f"Пропускная способность разреза = {cut_sum}")

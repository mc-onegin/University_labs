def coloring(graph):
    colors = {}
    for node in graph:
        used_colors = set(colors.get(near) for near in graph[node] if near in colors)
        color = 0
        while color in used_colors:
            color += 1
        colors[node] = color
    return colors

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['C']
}
print(coloring(graph))
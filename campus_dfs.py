from campus_helper import get_campus_graph, test_paths

# DFS to find all paths from start to goal

def dfs_all_paths(graph, start, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()
    path.append(start)
    visited.add(start)
    if start == goal:
        return [list(path)]
    paths = []
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            found_paths = dfs_all_paths(graph, neighbor, goal, path, visited)
            for p in found_paths:
                paths.append(p)
    path.pop()
    visited.remove(start)
    return paths

# Main function: returns the longest path from start to goal

def dfs_longest_path(graph, start, goal):
    all_paths = dfs_all_paths(graph, start, goal)
    if not all_paths:
        return None
    return max(all_paths, key=len)

# DFS for shortest path (not optimal, but finds all and selects shortest)
# Limitation: DFS explores all paths, so it's inefficient for shortest path search in large graphs.
def dfs_shortest_path(graph, start, goal):
    all_paths = dfs_all_paths(graph, start, goal)
    if not all_paths:
        return None
    return min(all_paths, key=len)

# For testing
if __name__ == "__main__":
    print("Testing longest paths:")
    test_paths(dfs_longest_path)
    print("\nTesting shortest paths:")
    test_paths(dfs_shortest_path)

# (i) Recursion helps by exploring all possible paths, backtracking when dead ends are reached.
# Visited nodes are tracked temporarily during recursion to avoid cycles and infinite loops.
# (j) DFS is not optimal for shortest path because it explores all paths, which is inefficient for large graphs. BFS is preferred for shortest path.


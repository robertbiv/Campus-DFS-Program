# Campus DFS Program

A Python program that uses Depth-First Search (DFS) to find paths between campus buildings. This project demonstrates graph traversal algorithms applied to a real-world navigation scenario on a college campus.

## Overview

This program models a campus as a graph where buildings are nodes and walkways are edges. It implements DFS algorithms to find both the shortest and longest paths between different campus locations.

## Features

- **Find All Paths**: Discovers all possible paths between two campus buildings
- **Longest Path**: Identifies the longest path from a starting point to a destination
- **Shortest Path**: Finds the shortest path (though DFS is not optimal for this - BFS would be better)
- **Cycle Handling**: Properly handles cycles in the campus graph using visited node tracking
- **Backtracking**: Uses recursion and backtracking to explore all possible routes

## Campus Map

The program includes the following campus buildings:

- Student Enrichment Center
- Olmsted Building
- Science and Tech Building
- Kulkarni Theatre
- Vartan Plaza
- Library
- Swatara Building

## Installation

1. Clone the repository:
```bash
git clone https://github.com/robertbiv/Campus-DFS-Program.git
cd Campus-DFS-Program
```

2. Ensure you have Python 3 installed:
```bash
python3 --version
```

No additional dependencies are required - the program uses only Python standard library.

## Usage

Run the program to test path-finding between various campus locations:

```bash
python3 campus_dfs.py
```

### Example Output

```
Testing longest paths:
Path from Student Enrichment Center to Library: ['Student Enrichment Center', 'Olmsted Building', 'Library']
Path from Swatara Building to Library: ['Swatara Building', 'Olmsted Building', 'Library']
Path from Vartan Plaza to Library: ['Vartan Plaza', 'Science and Tech Building', 'Student Enrichment Center', 'Olmsted Building', 'Library']

Testing shortest paths:
Path from Student Enrichment Center to Library: ['Student Enrichment Center', 'Olmsted Building', 'Library']
Path from Swatara Building to Library: ['Swatara Building', 'Olmsted Building', 'Library']
Path from Vartan Plaza to Library: ['Vartan Plaza', 'Science and Tech Building', 'Student Enrichment Center', 'Olmsted Building', 'Library']
```

## Code Structure

### `campus_dfs.py`

The main program file containing the DFS implementations:

- **`dfs_all_paths(graph, start, goal, path=None, visited=None)`**: Recursively finds all possible paths from start to goal
  - Uses backtracking to explore different routes
  - Maintains a visited set to avoid cycles
  - Returns a list of all valid paths

- **`dfs_longest_path(graph, start, goal)`**: Returns the longest path between two points
  - Finds all paths using `dfs_all_paths`
  - Selects the path with maximum length

- **`dfs_shortest_path(graph, start, goal)`**: Returns the shortest path between two points
  - Finds all paths using `dfs_all_paths`
  - Selects the path with minimum length
  - Note: Not optimal for shortest path (BFS would be better)

### `campus_helper.py`

Helper file containing the campus graph data and testing utilities:

- **`get_campus_graph()`**: Returns the campus map as an adjacency list
- **`test_paths(dfs_func)`**: Tests a DFS function with predefined start-goal pairs

## How It Works

### Depth-First Search (DFS)

The program uses recursive DFS with backtracking:

1. **Start** at the initial building
2. **Mark** the current building as visited
3. **Check** if we've reached the goal
   - If yes, return the current path
   - If no, continue exploring
4. **Explore** each unvisited neighbor recursively
5. **Backtrack** by removing the current building from the path and visited set
6. **Return** all paths found

### Recursion and Backtracking

- Recursion allows the algorithm to explore all possible paths systematically
- Visited nodes are tracked during recursion to avoid cycles and infinite loops
- When a path is fully explored, the algorithm backtracks by removing nodes from the visited set
- This allows the same node to be visited in different paths

### Limitations

- **DFS for Shortest Path**: DFS explores all paths to find the shortest one, which is inefficient. Breadth-First Search (BFS) would be more optimal as it explores paths level by level.
- **Time Complexity**: For dense graphs with many paths, DFS can be slow as it explores all possibilities.

## Algorithm Complexity

- **Time Complexity**: O(V + E) for simple DFS, but finding all paths can be exponential in the worst case
- **Space Complexity**: O(V) for the recursion stack and visited set, where V is the number of vertices (buildings)

## Educational Purpose

This project demonstrates:
- Graph representation using adjacency lists
- Recursive algorithms and backtracking
- Cycle detection in graphs
- Trade-offs between different search algorithms (DFS vs BFS)

## License

This is an educational project created for coursework.

## Author

robertbiv

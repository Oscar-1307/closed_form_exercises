# U3A1 - Graph Connected Subgraphs

## Overview

Implementation of a graph data structure using adjacency matrix representation and an algorithm to find connected subgraphs using Depth-First Search (DFS).

## Files

- `graph.py` - Main implementation with Graph class and connected subgraphs algorithm
- `graph_report.ipynb` - Jupyter notebook with detailed analysis and results
- `README.md` - This file

## Usage

### Running the Python script

```bash
python graph.py
```

### Converting notebook to PDF

```bash
jupyter nbconvert --to pdf graph_report.ipynb
```

## Algorithm

The implementation finds all connected subgraphs in a directed graph by treating it as undirected:

1. Uses adjacency matrix for O(1) edge lookup
2. DFS traversal to explore connected nodes
3. Returns tuple of sets, each containing nodes in a connected subgraph

## Complexity

- **Time**: O(V²) where V is the number of vertices
- **Space**: O(V²) for adjacency matrix

## Results

The graph contains **2 connected subgraphs**:
- Graph 1: 35 nodes
- Graph 2: 15 nodes

# Graphs

## Functionality
A **Graph** is a non-linear network consisting of a set of **Vertices (Nodes)** connected by **Edges**. Graphs can be directed/undirected and weighted/unweighted, typically represented via **Adjacency Lists** or **Adjacency Matrices**.

## Pros
* **Expressive Modeling**: Models complex real-world relationships, pathways, and networks accurately.
* **Versatile Traversal**: Supports specialized algorithms for shortest path, network flow, and cycle detection.

## Cons
* **High Space & Time Complexity**: Traversals and updates can become computationally expensive on dense graphs (O(V^2) or $O(V + E)).
* **Implementation Complexity**: Requires handling cycles, disconnected subgraphs, and complex edge state management.

## When to Use
* You need to represent interconnected networks (social media connections, road networks, recommendation engines).
* You need to find optimal routes, dependencies (topological sort), or clustering patterns.

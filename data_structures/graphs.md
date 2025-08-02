# 🕸️ Graphs

## 📋 Overview

**Graphs** are non-linear data structures consisting of vertices (nodes) connected by edges. They represent relationships between entities and are fundamental in computer science for modeling networks, dependencies, and connections.

---

## 🎯 Key Properties

- **Vertices & Edges:** Nodes connected by relationships
- **Directed/Undirected:** Edges may or may not have direction
- **Weighted/Unweighted:** Edges may have associated costs
- **Connected/Disconnected:** All vertices reachable or isolated components
- **Cyclic/Acyclic:** May or may not contain cycles

---

## 📊 Time & Space Complexity

| Representation | Space | Add Vertex | Add Edge | Remove Vertex | Remove Edge | Query |
|----------------|-------|------------|----------|---------------|-------------|-------|
| Adjacency List | O(V + E) | O(1) | O(1) | O(V + E) | O(E) | O(V) |
| Adjacency Matrix | O(V²) | O(V²) | O(1) | O(V²) | O(1) | O(1) |

*V = vertices, E = edges*

---

## 🔍 Visual Representation

```
Undirected Graph:
    A --- B
    |     |
    C --- D

Directed Graph:
    A → B
    ↑   ↓
    C ← D

Weighted Graph:
    A --5-- B
    |       |
    3       2
    |       |
    C --4-- D

Adjacency List:
A: [B, C]
B: [A, D]  
C: [A, D]
D: [B, C]

Adjacency Matrix:
    A B C D
A [ 0 1 1 0 ]
B [ 1 0 0 1 ]
C [ 1 0 0 1 ]
D [ 0 1 1 0 ]
```

---

## 🚀 Top 5 Essential Algorithms

### 1. Graph Traversals (DFS & BFS)

**Use Cases:** Exploring graphs, pathfinding, connectivity checking, topological sorting

#### C# Implementation
```csharp
using System;
using System.Collections.Generic;

public class GraphTraversal 
{
    // Graph representation using adjacency list
    public class Graph 
    {
        private Dictionary<int, List<int>> adjacencyList;
        
        public Graph() 
        {
            adjacencyList = new Dictionary<int, List<int>>();
        }
        
        public void AddVertex(int vertex) 
        {
            if (!adjacencyList.ContainsKey(vertex)) 
            {
                adjacencyList[vertex] = new List<int>();
            }
        }
        
        public void AddEdge(int from, int to, bool bidirectional = true) 
        {
            AddVertex(from);
            AddVertex(to);
            
            adjacencyList[from].Add(to);
            if (bidirectional) 
            {
                adjacencyList[to].Add(from);
            }
        }
        
        public List<int> GetNeighbors(int vertex) 
        {
            return adjacencyList.ContainsKey(vertex) ? 
                   adjacencyList[vertex] : new List<int>();
        }
        
        public HashSet<int> GetAllVertices() 
        {
            return new HashSet<int>(adjacencyList.Keys);
        }
    }
    
    // Depth-First Search (Recursive)
    public static List<int> DFSRecursive(Graph graph, int startVertex) 
    {
        var visited = new HashSet<int>();
        var result = new List<int>();
        
        DFSHelper(graph, startVertex, visited, result);
        return result;
    }
    
    private static void DFSHelper(Graph graph, int vertex, HashSet<int> visited, List<int> result) 
    {
        visited.Add(vertex);
        result.Add(vertex);
        
        foreach (int neighbor in graph.GetNeighbors(vertex)) 
        {
            if (!visited.Contains(neighbor)) 
            {
                DFSHelper(graph, neighbor, visited, result);
            }
        }
    }
    
    // Depth-First Search (Iterative)
    public static List<int> DFSIterative(Graph graph, int startVertex) 
    {
        var visited = new HashSet<int>();
        var result = new List<int>();
        var stack = new Stack<int>();
        
        stack.Push(startVertex);
        
        while (stack.Count > 0) 
        {
            int vertex = stack.Pop();
            
            if (!visited.Contains(vertex)) 
            {
                visited.Add(vertex);
                result.Add(vertex);
                
                // Add neighbors in reverse order to maintain left-to-right traversal
                var neighbors = graph.GetNeighbors(vertex);
                for (int i = neighbors.Count - 1; i >= 0; i--) 
                {
                    if (!visited.Contains(neighbors[i])) 
                    {
                        stack.Push(neighbors[i]);
                    }
                }
            }
        }
        
        return result;
    }
    
    // Breadth-First Search
    public static List<int> BFS(Graph graph, int startVertex) 
    {
        var visited = new HashSet<int>();
        var result = new List<int>();
        var queue = new Queue<int>();
        
        queue.Enqueue(startVertex);
        visited.Add(startVertex);
        
        while (queue.Count > 0) 
        {
            int vertex = queue.Dequeue();
            result.Add(vertex);
            
            foreach (int neighbor in graph.GetNeighbors(vertex)) 
            {
                if (!visited.Contains(neighbor)) 
                {
                    visited.Add(neighbor);
                    queue.Enqueue(neighbor);
                }
            }
        }
        
        return result;
    }
    
    // Find all connected components
    public static List<List<int>> FindConnectedComponents(Graph graph) 
    {
        var visited = new HashSet<int>();
        var components = new List<List<int>>();
        
        foreach (int vertex in graph.GetAllVertices()) 
        {
            if (!visited.Contains(vertex)) 
            {
                var component = new List<int>();
                DFSHelper(graph, vertex, visited, component);
                components.Add(component);
            }
        }
        
        return components;
    }
    
    // Check if graph is connected
    public static bool IsConnected(Graph graph) 
    {
        var vertices = graph.GetAllVertices();
        if (vertices.Count == 0) return true;
        
        int startVertex = vertices.First();
        var reachable = DFSRecursive(graph, startVertex);
        
        return reachable.Count == vertices.Count;
    }
    
    // Find path between two vertices
    public static List<int> FindPath(Graph graph, int start, int end) 
    {
        var visited = new HashSet<int>();
        var path = new List<int>();
        
        if (FindPathHelper(graph, start, end, visited, path)) 
        {
            return path;
        }
        
        return new List<int>(); // No path found
    }
    
    private static bool FindPathHelper(Graph graph, int current, int target, 
                                      HashSet<int> visited, List<int> path) 
    {
        visited.Add(current);
        path.Add(current);
        
        if (current == target) return true;
        
        foreach (int neighbor in graph.GetNeighbors(current)) 
        {
            if (!visited.Contains(neighbor)) 
            {
                if (FindPathHelper(graph, neighbor, target, visited, path)) 
                {
                    return true;
                }
            }
        }
        
        path.RemoveAt(path.Count - 1); // Backtrack
        return false;
    }
    
    // BFS shortest path (unweighted)
    public static List<int> ShortestPath(Graph graph, int start, int end) 
    {
        var visited = new HashSet<int>();
        var queue = new Queue<int>();
        var parent = new Dictionary<int, int>();
        
        queue.Enqueue(start);
        visited.Add(start);
        parent[start] = -1;
        
        while (queue.Count > 0) 
        {
            int vertex = queue.Dequeue();
            
            if (vertex == end) 
            {
                // Reconstruct path
                var path = new List<int>();
                int current = end;
                
                while (current != -1) 
                {
                    path.Add(current);
                    current = parent.ContainsKey(current) ? parent[current] : -1;
                }
                
                path.Reverse();
                return path;
            }
            
            foreach (int neighbor in graph.GetNeighbors(vertex)) 
            {
                if (!visited.Contains(neighbor)) 
                {
                    visited.Add(neighbor);
                    parent[neighbor] = vertex;
                    queue.Enqueue(neighbor);
                }
            }
        }
        
        return new List<int>(); // No path found
    }
}
```

---

### 2. Dijkstra's Shortest Path

**Use Cases:** Finding shortest paths in weighted graphs, GPS navigation, network routing

#### C# Implementation
```csharp
using System;
using System.Collections.Generic;

public class DijkstraShortestPath 
{
    public class WeightedGraph 
    {
        private Dictionary<int, List<(int neighbor, int weight)>> adjacencyList;
        
        public WeightedGraph() 
        {
            adjacencyList = new Dictionary<int, List<(int, int)>>();
        }
        
        public void AddVertex(int vertex) 
        {
            if (!adjacencyList.ContainsKey(vertex)) 
            {
                adjacencyList[vertex] = new List<(int, int)>();
            }
        }
        
        public void AddEdge(int from, int to, int weight, bool bidirectional = true) 
        {
            AddVertex(from);
            AddVertex(to);
            
            adjacencyList[from].Add((to, weight));
            if (bidirectional) 
            {
                adjacencyList[to].Add((from, weight));
            }
        }
        
        public List<(int neighbor, int weight)> GetNeighbors(int vertex) 
        {
            return adjacencyList.ContainsKey(vertex) ? 
                   adjacencyList[vertex] : new List<(int, int)>();
        }
        
        public HashSet<int> GetAllVertices() 
        {
            return new HashSet<int>(adjacencyList.Keys);
        }
    }
    
    public static (Dictionary<int, int> distances, Dictionary<int, int> previous) 
        Dijkstra(WeightedGraph graph, int start) 
    {
        var distances = new Dictionary<int, int>();
        var previous = new Dictionary<int, int>();
        var priorityQueue = new PriorityQueue<int, int>();
        var visited = new HashSet<int>();
        
        // Initialize distances
        foreach (int vertex in graph.GetAllVertices()) 
        {
            distances[vertex] = int.MaxValue;
            previous[vertex] = -1;
        }
        
        distances[start] = 0;
        priorityQueue.Enqueue(start, 0);
        
        while (priorityQueue.Count > 0) 
        {
            int current = priorityQueue.Dequeue();
            
            if (visited.Contains(current)) continue;
            visited.Add(current);
            
            foreach (var (neighbor, weight) in graph.GetNeighbors(current)) 
            {
                if (visited.Contains(neighbor)) continue;
                
                int newDistance = distances[current] + weight;
                
                if (newDistance < distances[neighbor]) 
                {
                    distances[neighbor] = newDistance;
                    previous[neighbor] = current;
                    priorityQueue.Enqueue(neighbor, newDistance);
                }
            }
        }
        
        return (distances, previous);
    }
    
    public static List<int> GetShortestPath(Dictionary<int, int> previous, int start, int end) 
    {
        var path = new List<int>();
        int current = end;
        
        while (current != -1) 
        {
            path.Add(current);
            current = previous.ContainsKey(current) ? previous[current] : -1;
        }
        
        if (path[path.Count - 1] != start) 
        {
            return new List<int>(); // No path exists
        }
        
        path.Reverse();
        return path;
    }
    
    // Single source shortest paths to all vertices
    public static Dictionary<int, int> ShortestPaths(WeightedGraph graph, int start) 
    {
        var (distances, _) = Dijkstra(graph, start);
        return distances;
    }
    
    // Shortest path between two specific vertices
    public static (int distance, List<int> path) ShortestPath(WeightedGraph graph, int start, int end) 
    {
        var (distances, previous) = Dijkstra(graph, start);
        
        if (!distances.ContainsKey(end) || distances[end] == int.MaxValue) 
        {
            return (-1, new List<int>()); // No path exists
        }
        
        var path = GetShortestPath(previous, start, end);
        return (distances[end], path);
    }
    
    // A* Algorithm (heuristic-based shortest path)
    public static (int distance, List<int> path) AStar(WeightedGraph graph, int start, int end, 
                                                       Func<int, int, int> heuristic) 
    {
        var gScore = new Dictionary<int, int>();
        var fScore = new Dictionary<int, int>();
        var previous = new Dictionary<int, int>();
        var priorityQueue = new PriorityQueue<int, int>();
        var visited = new HashSet<int>();
        
        foreach (int vertex in graph.GetAllVertices()) 
        {
            gScore[vertex] = int.MaxValue;
            fScore[vertex] = int.MaxValue;
            previous[vertex] = -1;
        }
        
        gScore[start] = 0;
        fScore[start] = heuristic(start, end);
        priorityQueue.Enqueue(start, fScore[start]);
        
        while (priorityQueue.Count > 0) 
        {
            int current = priorityQueue.Dequeue();
            
            if (current == end) 
            {
                var path = GetShortestPath(previous, start, end);
                return (gScore[end], path);
            }
            
            if (visited.Contains(current)) continue;
            visited.Add(current);
            
            foreach (var (neighbor, weight) in graph.GetNeighbors(current)) 
            {
                if (visited.Contains(neighbor)) continue;
                
                int tentativeGScore = gScore[current] + weight;
                
                if (tentativeGScore < gScore[neighbor]) 
                {
                    previous[neighbor] = current;
                    gScore[neighbor] = tentativeGScore;
                    fScore[neighbor] = gScore[neighbor] + heuristic(neighbor, end);
                    priorityQueue.Enqueue(neighbor, fScore[neighbor]);
                }
            }
        }
        
        return (-1, new List<int>()); // No path found
    }
    
    // Floyd-Warshall (All pairs shortest paths)
    public static int[,] FloydWarshall(WeightedGraph graph) 
    {
        var vertices = graph.GetAllVertices().ToList();
        int n = vertices.Count;
        var dist = new int[n, n];
        var vertexIndex = new Dictionary<int, int>();
        
        // Create vertex index mapping
        for (int i = 0; i < n; i++) 
        {
            vertexIndex[vertices[i]] = i;
        }
        
        // Initialize distance matrix
        for (int i = 0; i < n; i++) 
        {
            for (int j = 0; j < n; j++) 
            {
                if (i == j) 
                {
                    dist[i, j] = 0;
                }
                else 
                {
                    dist[i, j] = int.MaxValue;
                }
            }
        }
        
        // Fill in direct edges
        foreach (int vertex in vertices) 
        {
            int i = vertexIndex[vertex];
            foreach (var (neighbor, weight) in graph.GetNeighbors(vertex)) 
            {
                int j = vertexIndex[neighbor];
                dist[i, j] = weight;
            }
        }
        
        // Floyd-Warshall algorithm
        for (int k = 0; k < n; k++) 
        {
            for (int i = 0; i < n; i++) 
            {
                for (int j = 0; j < n; j++) 
                {
                    if (dist[i, k] != int.MaxValue && dist[k, j] != int.MaxValue) 
                    {
                        dist[i, j] = Math.Min(dist[i, j], dist[i, k] + dist[k, j]);
                    }
                }
            }
        }
        
        return dist;
    }
}
```

---

### 3. Union Find (Disjoint Set)

**Use Cases:** Detecting cycles, connected components, Kruskal's MST, dynamic connectivity

#### C# Implementation
```csharp
using System;
using System.Collections.Generic;

public class UnionFind 
{
    private int[] parent;
    private int[] rank;
    private int count; // Number of connected components
    
    public UnionFind(int n) 
    {
        parent = new int[n];
        rank = new int[n];
        count = n;
        
        for (int i = 0; i < n; i++) 
        {
            parent[i] = i;
            rank[i] = 0;
        }
    }
    
    public int Find(int x) 
    {
        if (parent[x] != x) 
        {
            parent[x] = Find(parent[x]); // Path compression
        }
        return parent[x];
    }
    
    public bool Union(int x, int y) 
    {
        int rootX = Find(x);
        int rootY = Find(y);
        
        if (rootX == rootY) return false; // Already connected
        
        // Union by rank
        if (rank[rootX] < rank[rootY]) 
        {
            parent[rootX] = rootY;
        }
        else if (rank[rootX] > rank[rootY]) 
        {
            parent[rootY] = rootX;
        }
        else 
        {
            parent[rootY] = rootX;
            rank[rootX]++;
        }
        
        count--;
        return true;
    }
    
    public bool Connected(int x, int y) 
    {
        return Find(x) == Find(y);
    }
    
    public int Count => count;
    
    public int GetComponentSize(int x) 
    {
        int root = Find(x);
        int size = 0;
        
        for (int i = 0; i < parent.Length; i++) 
        {
            if (Find(i) == root) 
            {
                size++;
            }
        }
        
        return size;
    }
}

// Weighted Union Find (for more complex applications)
public class WeightedUnionFind 
{
    private int[] parent;
    private double[] weight; // Weight from node to its parent
    private int count;
    
    public WeightedUnionFind(int n) 
    {
        parent = new int[n];
        weight = new double[n];
        count = n;
        
        for (int i = 0; i < n; i++) 
        {
            parent[i] = i;
            weight[i] = 0.0;
        }
    }
    
    public int Find(int x) 
    {
        if (parent[x] != x) 
        {
            int root = Find(parent[x]);
            weight[x] += weight[parent[x]]; // Update weight during path compression
            parent[x] = root;
        }
        return parent[x];
    }
    
    public bool Union(int x, int y, double w) 
    {
        int rootX = Find(x);
        int rootY = Find(y);
        
        if (rootX == rootY) return false;
        
        parent[rootX] = rootY;
        weight[rootX] = weight[y] - weight[x] + w;
        count--;
        return true;
    }
    
    public bool Connected(int x, int y) 
    {
        return Find(x) == Find(y);
    }
    
    public double GetWeight(int x, int y) 
    {
        if (!Connected(x, y)) return double.NaN;
        return weight[x] - weight[y];
    }
}

// Union Find Applications
public class UnionFindApplications 
{
    // Number of Islands
    public static int NumIslands(char[][] grid) 
    {
        if (grid == null || grid.Length == 0) return 0;
        
        int rows = grid.Length;
        int cols = grid[0].Length;
        var uf = new UnionFind(rows * cols);
        int waterCells = 0;
        
        int[][] directions = { new int[] {0, 1}, new int[] {1, 0}, 
                              new int[] {0, -1}, new int[] {-1, 0} };
        
        for (int i = 0; i < rows; i++) 
        {
            for (int j = 0; j < cols; j++) 
            {
                if (grid[i][j] == '0') 
                {
                    waterCells++;
                    continue;
                }
                
                foreach (var dir in directions) 
                {
                    int ni = i + dir[0];
                    int nj = j + dir[1];
                    
                    if (ni >= 0 && ni < rows && nj >= 0 && nj < cols && grid[ni][nj] == '1') 
                    {
                        uf.Union(i * cols + j, ni * cols + nj);
                    }
                }
            }
        }
        
        return uf.Count - waterCells;
    }
    
    // Graph Valid Tree
    public static bool ValidTree(int n, int[][] edges) 
    {
        if (edges.Length != n - 1) return false; // Tree must have n-1 edges
        
        var uf = new UnionFind(n);
        
        foreach (var edge in edges) 
        {
            if (!uf.Union(edge[0], edge[1])) 
            {
                return false; // Cycle detected
            }
        }
        
        return uf.Count == 1; // Must be connected
    }
    
    // Redundant Connection
    public static int[] FindRedundantConnection(int[][] edges) 
    {
        var uf = new UnionFind(edges.Length + 1);
        
        foreach (var edge in edges) 
        {
            if (!uf.Union(edge[0], edge[1])) 
            {
                return edge; // This edge creates a cycle
            }
        }
        
        return new int[0];
    }
    
    // Accounts Merge
    public static IList<IList<string>> AccountsMerge(IList<IList<string>> accounts) 
    {
        var uf = new UnionFind(accounts.Count);
        var emailToIndex = new Dictionary<string, int>();
        
        // Build email to account index mapping
        for (int i = 0; i < accounts.Count; i++) 
        {
            for (int j = 1; j < accounts[i].Count; j++) 
            {
                string email = accounts[i][j];
                if (emailToIndex.ContainsKey(email)) 
                {
                    uf.Union(i, emailToIndex[email]);
                }
                else 
                {
                    emailToIndex[email] = i;
                }
            }
        }
        
        // Group emails by root account
        var groups = new Dictionary<int, HashSet<string>>();
        foreach (var kvp in emailToIndex) 
        {
            int root = uf.Find(kvp.Value);
            if (!groups.ContainsKey(root)) 
            {
                groups[root] = new HashSet<string>();
            }
            groups[root].Add(kvp.Key);
        }
        
        // Build result
        var result = new List<IList<string>>();
        foreach (var kvp in groups) 
        {
            var account = new List<string> { accounts[kvp.Key][0] };
            var sortedEmails = kvp.Value.OrderBy(e => e).ToList();
            account.AddRange(sortedEmails);
            result.Add(account);
        }
        
        return result;
    }
    
    // Satisfiability of Equality Equations
    public static bool EquationsPossible(string[] equations) 
    {
        var uf = new UnionFind(26);
        
        // Process equality equations first
        foreach (string eq in equations) 
        {
            if (eq[1] == '=') 
            {
                int x = eq[0] - 'a';
                int y = eq[3] - 'a';
                uf.Union(x, y);
            }
        }
        
        // Check inequality equations
        foreach (string eq in equations) 
        {
            if (eq[1] == '!') 
            {
                int x = eq[0] - 'a';
                int y = eq[3] - 'a';
                if (uf.Connected(x, y)) 
                {
                    return false;
                }
            }
        }
        
        return true;
    }
}
```

---

### 4. Topological Sort

**Use Cases:** Task scheduling, dependency resolution, course prerequisites, build systems

#### C# Implementation
```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class TopologicalSort 
{
    public class DirectedGraph 
    {
        private Dictionary<int, List<int>> adjacencyList;
        private Dictionary<int, int> inDegree;
        
        public DirectedGraph() 
        {
            adjacencyList = new Dictionary<int, List<int>>();
            inDegree = new Dictionary<int, int>();
        }
        
        public void AddVertex(int vertex) 
        {
            if (!adjacencyList.ContainsKey(vertex)) 
            {
                adjacencyList[vertex] = new List<int>();
                inDegree[vertex] = 0;
            }
        }
        
        public void AddEdge(int from, int to) 
        {
            AddVertex(from);
            AddVertex(to);
            
            adjacencyList[from].Add(to);
            inDegree[to]++;
        }
        
        public List<int> GetNeighbors(int vertex) 
        {
            return adjacencyList.ContainsKey(vertex) ? 
                   adjacencyList[vertex] : new List<int>();
        }
        
        public int GetInDegree(int vertex) 
        {
            return inDegree.ContainsKey(vertex) ? inDegree[vertex] : 0;
        }
        
        public HashSet<int> GetAllVertices() 
        {
            return new HashSet<int>(adjacencyList.Keys);
        }
    }
    
    // Kahn's Algorithm (BFS-based)
    public static List<int> TopologicalSortKahn(DirectedGraph graph) 
    {
        var result = new List<int>();
        var queue = new Queue<int>();
        var inDegreeCount = new Dictionary<int, int>();
        
        // Initialize in-degree counts
        foreach (int vertex in graph.GetAllVertices()) 
        {
            inDegreeCount[vertex] = graph.GetInDegree(vertex);
            if (inDegreeCount[vertex] == 0) 
            {
                queue.Enqueue(vertex);
            }
        }
        
        while (queue.Count > 0) 
        {
            int vertex = queue.Dequeue();
            result.Add(vertex);
            
            foreach (int neighbor in graph.GetNeighbors(vertex)) 
            {
                inDegreeCount[neighbor]--;
                if (inDegreeCount[neighbor] == 0) 
                {
                    queue.Enqueue(neighbor);
                }
            }
        }
        
        // Check for cycles
        if (result.Count != graph.GetAllVertices().Count) 
        {
            return new List<int>(); // Cycle detected, no valid topological order
        }
        
        return result;
    }
    
    // DFS-based Topological Sort
    public static List<int> TopologicalSortDFS(DirectedGraph graph) 
    {
        var visited = new HashSet<int>();
        var recursionStack = new HashSet<int>();
        var stack = new Stack<int>();
        
        foreach (int vertex in graph.GetAllVertices()) 
        {
            if (!visited.Contains(vertex)) 
            {
                if (!DFSHelper(graph, vertex, visited, recursionStack, stack)) 
                {
                    return new List<int>(); // Cycle detected
                }
            }
        }
        
        var result = new List<int>();
        while (stack.Count > 0) 
        {
            result.Add(stack.Pop());
        }
        
        return result;
    }
    
    private static bool DFSHelper(DirectedGraph graph, int vertex, HashSet<int> visited, 
                                 HashSet<int> recursionStack, Stack<int> stack) 
    {
        visited.Add(vertex);
        recursionStack.Add(vertex);
        
        foreach (int neighbor in graph.GetNeighbors(vertex)) 
        {
            if (!visited.Contains(neighbor)) 
            {
                if (!DFSHelper(graph, neighbor, visited, recursionStack, stack)) 
                {
                    return false; // Cycle detected
                }
            }
            else if (recursionStack.Contains(neighbor)) 
            {
                return false; // Back edge found, cycle detected
            }
        }
        
        recursionStack.Remove(vertex);
        stack.Push(vertex);
        return true;
    }
    
    // Check if topological order is possible (no cycles)
    public static bool CanFinish(int numCourses, int[][] prerequisites) 
    {
        var graph = new DirectedGraph();
        
        for (int i = 0; i < numCourses; i++) 
        {
            graph.AddVertex(i);
        }
        
        foreach (var prereq in prerequisites) 
        {
            graph.AddEdge(prereq[1], prereq[0]); // prereq[1] -> prereq[0]
        }
        
        var topOrder = TopologicalSortKahn(graph);
        return topOrder.Count == numCourses;
    }
    
    // Find a valid course schedule
    public static int[] FindOrder(int numCourses, int[][] prerequisites) 
    {
        var graph = new DirectedGraph();
        
        for (int i = 0; i < numCourses; i++) 
        {
            graph.AddVertex(i);
        }
        
        foreach (var prereq in prerequisites) 
        {
            graph.AddEdge(prereq[1], prereq[0]);
        }
        
        var topOrder = TopologicalSortKahn(graph);
        
        if (topOrder.Count != numCourses) 
        {
            return new int[0]; // No valid order exists
        }
        
        return topOrder.ToArray();
    }
    
    // Alien Dictionary
    public static string AlienOrder(string[] words) 
    {
        var graph = new DirectedGraph();
        var chars = new HashSet<char>();
        
        // Collect all characters
        foreach (string word in words) 
        {
            foreach (char c in word) 
            {
                chars.Add(c);
                graph.AddVertex(c - 'a');
            }
        }
        
        // Build graph from word comparisons
        for (int i = 0; i < words.Length - 1; i++) 
        {
            string word1 = words[i];
            string word2 = words[i + 1];
            
            int minLen = Math.Min(word1.Length, word2.Length);
            bool foundDiff = false;
            
            for (int j = 0; j < minLen; j++) 
            {
                if (word1[j] != word2[j]) 
                {
                    graph.AddEdge(word1[j] - 'a', word2[j] - 'a');
                    foundDiff = true;
                    break;
                }
            }
            
            // If word1 is prefix of word2 but longer, invalid order
            if (!foundDiff && word1.Length > word2.Length) 
            {
                return "";
            }
        }
        
        var topOrder = TopologicalSortKahn(graph);
        
        if (topOrder.Count != chars.Count) 
        {
            return ""; // Cycle detected
        }
        
        return string.Join("", topOrder.Select(i => (char)('a' + i)));
    }
    
    // Parallel Courses (minimum semesters)
    public static int MinimumSemesters(int n, int[][] relations) 
    {
        var graph = new DirectedGraph();
        
        for (int i = 1; i <= n; i++) 
        {
            graph.AddVertex(i);
        }
        
        foreach (var relation in relations) 
        {
            graph.AddEdge(relation[0], relation[1]);
        }
        
        var queue = new Queue<int>();
        var inDegreeCount = new Dictionary<int, int>();
        
        for (int i = 1; i <= n; i++) 
        {
            inDegreeCount[i] = graph.GetInDegree(i);
            if (inDegreeCount[i] == 0) 
            {
                queue.Enqueue(i);
            }
        }
        
        int semesters = 0;
        int studiedCourses = 0;
        
        while (queue.Count > 0) 
        {
            int courseCount = queue.Count;
            semesters++;
            
            for (int i = 0; i < courseCount; i++) 
            {
                int course = queue.Dequeue();
                studiedCourses++;
                
                foreach (int nextCourse in graph.GetNeighbors(course)) 
                {
                    inDegreeCount[nextCourse]--;
                    if (inDegreeCount[nextCourse] == 0) 
                    {
                        queue.Enqueue(nextCourse);
                    }
                }
            }
        }
        
        return studiedCourses == n ? semesters : -1;
    }
}
```

---

### 5. Minimum Spanning Tree (MST)

**Use Cases:** Network design, clustering, optimization problems, circuit design

#### C# Implementation
```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class MinimumSpanningTree 
{
    public class Edge : IComparable<Edge> 
    {
        public int From { get; set; }
        public int To { get; set; }
        public int Weight { get; set; }
        
        public Edge(int from, int to, int weight) 
        {
            From = from;
            To = to;
            Weight = weight;
        }
        
        public int CompareTo(Edge other) 
        {
            return Weight.CompareTo(other.Weight);
        }
    }
    
    // Kruskal's Algorithm using Union-Find
    public static (List<Edge> mst, int totalWeight) KruskalMST(List<Edge> edges, int numVertices) 
    {
        var mst = new List<Edge>();
        int totalWeight = 0;
        
        // Sort edges by weight
        edges.Sort();
        
        var uf = new UnionFind(numVertices);
        
        foreach (var edge in edges) 
        {
            if (uf.Union(edge.From, edge.To)) 
            {
                mst.Add(edge);
                totalWeight += edge.Weight;
                
                // MST is complete when we have numVertices - 1 edges
                if (mst.Count == numVertices - 1) 
                {
                    break;
                }
            }
        }
        
        return (mst, totalWeight);
    }
    
    // Prim's Algorithm using Priority Queue
    public static (List<Edge> mst, int totalWeight) PrimMST(Dictionary<int, List<(int to, int weight)>> graph, int start) 
    {
        var mst = new List<Edge>();
        var visited = new HashSet<int>();
        var priorityQueue = new PriorityQueue<(int from, int to, int weight), int>();
        int totalWeight = 0;
        
        visited.Add(start);
        
        // Add all edges from start vertex
        foreach (var (to, weight) in graph.GetValueOrDefault(start, new List<(int, int)>())) 
        {
            priorityQueue.Enqueue((start, to, weight), weight);
        }
        
        while (priorityQueue.Count > 0 && visited.Count < graph.Count) 
        {
            var (from, to, weight) = priorityQueue.Dequeue();
            
            if (visited.Contains(to)) continue;
            
            // Add edge to MST
            mst.Add(new Edge(from, to, weight));
            totalWeight += weight;
            visited.Add(to);
            
            // Add all edges from newly added vertex
            foreach (var (nextTo, nextWeight) in graph.GetValueOrDefault(to, new List<(int, int)>())) 
            {
                if (!visited.Contains(nextTo)) 
                {
                    priorityQueue.Enqueue((to, nextTo, nextWeight), nextWeight);
                }
            }
        }
        
        return (mst, totalWeight);
    }
    
    // Borůvka's Algorithm
    public static (List<Edge> mst, int totalWeight) BoruvkaMST(List<Edge> edges, int numVertices) 
    {
        var mst = new List<Edge>();
        int totalWeight = 0;
        var uf = new UnionFind(numVertices);
        
        while (mst.Count < numVertices - 1) 
        {
            var cheapest = new Edge[numVertices];
            
            // Find cheapest edge for each component
            foreach (var edge in edges) 
            {
                int comp1 = uf.Find(edge.From);
                int comp2 = uf.Find(edge.To);
                
                if (comp1 != comp2) 
                {
                    if (cheapest[comp1] == null || edge.Weight < cheapest[comp1].Weight) 
                    {
                        cheapest[comp1] = edge;
                    }
                    if (cheapest[comp2] == null || edge.Weight < cheapest[comp2].Weight) 
                    {
                        cheapest[comp2] = edge;
                    }
                }
            }
            
            // Add cheapest edges to MST
            for (int i = 0; i < numVertices; i++) 
            {
                if (cheapest[i] != null && uf.Union(cheapest[i].From, cheapest[i].To)) 
                {
                    mst.Add(cheapest[i]);
                    totalWeight += cheapest[i].Weight;
                }
            }
        }
        
        return (mst, totalWeight);
    }
    
    // MST Applications
    
    // Minimum Cost to Connect All Points
    public static int MinCostConnectPoints(int[][] points) 
    {
        int n = points.Length;
        var edges = new List<Edge>();
        
        // Generate all possible edges
        for (int i = 0; i < n; i++) 
        {
            for (int j = i + 1; j < n; j++) 
            {
                int distance = Math.Abs(points[i][0] - points[j][0]) + 
                              Math.Abs(points[i][1] - points[j][1]);
                edges.Add(new Edge(i, j, distance));
            }
        }
        
        var (mst, totalWeight) = KruskalMST(edges, n);
        return totalWeight;
    }
    
    // Critical Connections (Bridges)
    public static IList<IList<int>> CriticalConnections(int n, IList<IList<int>> connections) 
    {
        var graph = new Dictionary<int, List<int>>();
        
        for (int i = 0; i < n; i++) 
        {
            graph[i] = new List<int>();
        }
        
        foreach (var conn in connections) 
        {
            graph[conn[0]].Add(conn[1]);
            graph[conn[1]].Add(conn[0]);
        }
        
        var result = new List<IList<int>>();
        var visited = new HashSet<int>();
        var disc = new int[n];
        var low = new int[n];
        var parent = new int[n];
        int time = 0;
        
        Array.Fill(parent, -1);
        
        for (int i = 0; i < n; i++) 
        {
            if (!visited.Contains(i)) 
            {
                BridgeUtil(graph, i, visited, disc, low, parent, result, ref time);
            }
        }
        
        return result;
    }
    
    private static void BridgeUtil(Dictionary<int, List<int>> graph, int u, HashSet<int> visited,
                                  int[] disc, int[] low, int[] parent, List<IList<int>> result, ref int time) 
    {
        visited.Add(u);
        disc[u] = low[u] = ++time;
        
        foreach (int v in graph[u]) 
        {
            if (!visited.Contains(v)) 
            {
                parent[v] = u;
                BridgeUtil(graph, v, visited, disc, low, parent, result, ref time);
                
                low[u] = Math.Min(low[u], low[v]);
                
                // If low[v] > disc[u], then u-v is a bridge
                if (low[v] > disc[u]) 
                {
                    result.Add(new List<int> { u, v });
                }
            }
            else if (v != parent[u]) 
            {
                low[u] = Math.Min(low[u], disc[v]);
            }
        }
    }
    
    // Optimize Water Distribution
    public static int MinCostToSupplyWater(int n, int[] wells, int[][] pipes) 
    {
        var edges = new List<Edge>();
        
        // Add virtual source (node 0) connected to all wells
        for (int i = 0; i < n; i++) 
        {
            edges.Add(new Edge(0, i + 1, wells[i]));
        }
        
        // Add all pipe connections
        foreach (var pipe in pipes) 
        {
            edges.Add(new Edge(pipe[0], pipe[1], pipe[2]));
        }
        
        var (mst, totalWeight) = KruskalMST(edges, n + 1);
        return totalWeight;
    }
}
```

---

## 🎯 Common Patterns & Tips

### Pattern Recognition
- **Graph Traversal:** Use DFS for deep exploration, BFS for shortest paths in unweighted graphs
- **Shortest Path:** Use Dijkstra for weighted graphs, BFS for unweighted graphs
- **Connectivity:** Use Union-Find for dynamic connectivity and cycle detection
- **Ordering:** Use topological sort for dependency resolution and scheduling
- **Optimization:** Use MST algorithms for minimum cost connection problems

### Optimization Tips
1. **Choose right representation:** Adjacency list for sparse graphs, matrix for dense graphs
2. **Use appropriate algorithm:** Consider graph properties (weighted/unweighted, directed/undirected)
3. **Implement path compression** in Union-Find for better performance
4. **Consider space-time tradeoffs** in shortest path algorithms
5. **Use early termination** when target is found in search algorithms

### Common Pitfalls
- **Infinite loops** in graph traversal without proper visited tracking
- **Stack overflow** in deep recursion for large graphs
- **Incorrect edge handling** in directed vs undirected graphs
- **Not handling disconnected components** properly
- **Memory issues** with dense graph representations

---

## 📚 Related LeetCode Problems

### Easy
- [Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/)
- [Employee Importance](https://leetcode.com/problems/employee-importance/)
- [Number of Islands](https://leetcode.com/problems/number-of-islands/)

### Medium
- [Course Schedule](https://leetcode.com/problems/course-schedule/)
- [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)
- [Network Delay Time](https://leetcode.com/problems/network-delay-time/)
- [Minimum Spanning Tree](https://leetcode.com/problems/min-cost-to-connect-all-points/)

### Hard
- [Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/)
- [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)
- [Optimize Water Distribution in a Village](https://leetcode.com/problems/optimize-water-distribution-in-a-village/)

---

[← Back to Main Guide](./README.md)

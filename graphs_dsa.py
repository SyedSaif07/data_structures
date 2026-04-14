"""
Graphs are data structures used to represent relationships.
Any kind of relationships.

Examples:
    Facebook has friendship as a relationship.
    LinkedIn has two types of relationship like connections and followers.
    Map contains different points - relationship of routes.

Graph has Vertices and Edges:
    Vertices are the nodes or points.
    Edges connect the vertices.

In real world, there are many types of relationships.
    Bidirectional relationship: In Facebook, if I'm your friend then you are my friend.
                                 In case of Maps, Point L1 and L2 can be two-way road.
    Uni-directional relationship: Followers are like you follow a celebrity but the celebrity
                                  doesn't necessarily follow you.

Types:
    Un-directed graphs: Follows bidirectional relationship as A to B can also be B to A.

    Directed graphs: Follows uni-directional relationship.Graphs have directions like insta followers.
                     To achieve bidirectional, we will use two directed edges.

    Weighted graphs: Not all relationships are equal. There are stronger relationships.
                     To achieve this we allocate weights for each relationship.
                     A to B is 70, B to C 40, C to D is 5.

    Un-weighted graphs: Graphs with no weights.

    Planar graphs: Graphs that lie in 2-D plane.

    Simple graphs: No parallel edges. Parallel edges are two undirected edges for same two nodes.
                   No self loop. Self loop in an edges starts and ends in the same node.

    Cyclic graphs: Path which starts a node and ends in the same node. Any graph that contains
                   a cycle is called as cyclic graphs. It can be both directed and un-directed.

    Acyclic graphs: Graphs with no cycle.

    Directed acyclic graphs: Directed graphs with no cycle.

    Tree: A graph with no cycle and only one connected component.
          No of edges = No of vertex - 1

    Forests: A graph with no cycle but has more than one connected component.
             Every tree is a forest but not every forest is a tree.

    Complete graph: Any graph with all possible edges is a complete graph.
                    Represented by letter K. K4 means complete graph with 4 nodes.

    Bi-partite graphs: Divide graph into two sets. Edges between the nodes from one to set another.
                       Edges are not within the nodes of the same set.


Path: Start at a vertex and traverse to another vertex.

Cycle: Any path starts and ends at the same vertex.

Adjacent nodes: Any vertices that are reachable for a vertex via its edge.

Incoming edges: In case of directed graphs, edges which are incoming to a vertex.

Outgoing edges: In case of directed graphs, edges which go out from a vertex or node.
                In case of adjacent nodes, they are only applicable for outgoing nodes.

In degree: Total number of incoming edges.

Out degree: Total number of outgoing edges.

Adjacency matrix is used to represent graph.
    In case of non-weighted graphs, add True for  the nodes that are connected Eg: True if 0,1 is connected.

    In case of weighted graphs, add the weight for  the nodes that are connected Eg: 20 if 0,1 is connected.

    The drawback of adjacency matrix is space complexity. We save 0s for those nodes that are
    not connected.

    Use adjacency matrix for < 1000 nodes. Not suitable for >1000 nodes.

Adjacent list implementation fixes adjacent matrix. It consumes less space.
"""


class Graph:
    """
    Adjacency matrix implementation
    """

    def __init__(self, n, directed):
        self.n = n
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]
        self.directed = directed

    def addEdge(self, u, v, w):  # w can be weight for weighted graphs
        self.matrix[u][v] = w
        if not self.directed:
            self.matrix[v][u] = w

    def addEdgeNw(self, u, v):
        self.addEdge(u, v, 1)

    def printGraph(self):
        print(self.matrix)


# g1 = Graph(4, False)
# g1.addEdge(1, 2, 78)
# g1.addEdge(1, 3, 50)
# g1.addEdge(0, 3, 45)
# g1.printGraph()


"""
Traversals: 
    Breadth first search (BFS): Traverse along the breadth of the graph.
                                Eg: In a book, you read 1st chapter's 1st page and 2nd chapter's 2nd page.
                                    Like wise 1st chapter's 2nd page and 2nd chapter's 2nd page.
                                
                                In an unweighted graph, bfs always visits in the shortest path order.
                                
                                0-1 bfs applicable on binary weighted graphs where the weights are 0 or 1. We will use 
                                deque - sometimes we will push at the front sometimes at the end. But we will pop
                                from the front always.

    Depth first search (BFS): Traverse along the depth of the graph. Visit all the nodes of the branch you picked
                              and move to the next branch.
                              Eg: Read the complete 1st chapter and then go to the 2nd chapter.
                              
Cycle detection: 
    It is not necessary that the full graph is in cycle. It is enough that few nodes are
    in a cycle. And wherever there is a cycle we must be able to detect it.
    
    Many problems in the real world can be solved by cycle detection algorithm.
    
    Using cycle detection in a directed graph, we can identify whether a graph is a DAG or not.
    DAG is Directed Acyclic Graph. DAGs can help us simulate many real world applications.
    
    There are specific algorithms that run only on DAG algorithm.
    
    Curl back is essential for cycle where the branch comes back to one of its own node of the same branch.
    If not, it won't be a cycle. Curling back doesn't always mean there is a cycle.
    
    Scenario 1: All edges going forward so there is no cycle.
    Scenario 2: Edges coming back to the same branch so there is a cycle.
    Scenario 3: When there is a backward edge, but it going to a different branch then there
                is no cycle.
                
    Back edge is actually creating cycle.
    
    To detect cycle, we will again use hash table. In this we will maintain 3 states of
    any node. 
        Untouched/Unvisited(U) : Node has never been touched or visited.
        Visited(V): Node has been visited.
        Processed(P): Visited the node and processed all its children.
        
    Back edge is identified when you visit a node (mark it as visited) and start processing
    its children where the child is already visited, then that is a back edge.
    Eg: A visited -> B visited -> D visited -> F processed -> E visited -> B visited.

DAG - Directed Acyclic Graphs:
    The two properties of DAG is directed and acyclic properties. More than properties,
    DAGs have practical applications.
    
    To detect a DAG, we can use dfs. If a graph is directed and doesnt have a cycle then it
    is a DAG else if it is directed but has a cycle then it is not a DAG.
    
    Topological sorting: This concept is applicable only for DAGs.
                         This sorting is applied by writing down the nodes in such a manner
                         if there is an edge between U to V then U comes before V.
                         0 -> 1 -> 2 -> 3 -> 4
                         0 -> 2 -> 1 -> 4 -> 3
                         0 -> 2 -> 1 -> 3 -> 3
                         
                         For the edge between 0 and 1, 0 comes before 1. 
                         
                         Any order that satisfies this condition then that is called
                         topological sorting.
                         
                         Eg: If there are 4 courses in college, A, B, C, D.
                         Before A, take B 
                         Before B, take C
                         Before C, take D
                         Before B, take D
                          
                         is it possible to take all the courses? D C B A
                         
Single Source Shortest Path:
    In a weighted direct graph, from a source node how much shortest weight with which
    each node can be reached.
    Eg: Source A, {B: 2, C:2, D:6, E: infinity}
    E is infinity because E cannot be reached from A.
    
    Dijkstra's Algorithm: When the graph has non negative edge weights.
                          This is a greedy algorithm.
                          
                          To implement this algorithm, there will be a source node A
                          provided in the problem. We create a hash table that contains the 
                          distance of all nodes.Distance of source node is 0. All other node's
                          distances are infinity. As we discover the other nodes through the source
                          we will update the distance of that respective node.
                          {A:0, B:∞, C:∞, D:∞, E:∞}
                          
                          We will maintain a priority queue, [(0,A)] at first. -> [(distance, node)]
                          While pq is not empty, 
                            top = pq.pop()
                            d[B] = d[A] + d[B] = 0 + 2 = 2
                            pq = [(B,2)]
                            d[C] = d[A] + d[C] = 0 + 1 = 1
                            pq = [(B,2), (C, 1)]
                            {A:0, B:2, C:1, D:∞, E:∞}
                         
                         The core idea behind this algorithm is it traverses the shortest
                         distance first. From A there are two nodes available but the shortest
                         is C. 
                            pq.pop() => C pops out
                            pq = [(B,2)]
                            d[D] = d[C] + d[D] = 1 + 5 = 6
                            {A:0, B:2, C:1, D:6, E:∞}
                            pq = [(B,2), (6,D)]
                            pq.pop() => B pops out
                            pq = [(6,D)]
                        
                        From B there are two nodes, C and D
                            d[C] = d[B] + d[C] = 2 + 0 = 2 but I already know the distance of C is 1.
                            so we won't update the distance of C
                            d[D] = d[B] + d[D] = 2 + 3 = 5 Now the distance of D will be updated to 5 as it 
                            is lesser than the old distance of D.
                            pq = [(6,D), (5,D)]
                            {A:0, B:2, C:1, D:5, E:∞}
                        
                        Now when we pop pq, it will be (5,D). From D the outgoing edge is E.
                            pq = [(6,D)]
                            d[E] = d[D] + d[E] = 5 + 6 = 11
                            {A:0, B:2, C:1, D:5, E:11}
                            pq = [(6,D), (11, E)]
                        
                        In the next iteration we pop (6,D) but we found optimal distances so we will
                        ignore this. And pop (11,E) but E doesnt have nodes to reach to. Now my algorithm will
                        stop.
                            
    Bellman Ford Algorithm: DP based algorithm. 
                            Applicable even for negative edge weights.
    

"""


class GraphAdjList:
    """
    Adjacency list implementation
    """

    def __init__(self, n, directed):
        self.n = n
        self.directed = directed
        self.adj = [[] for _ in range(n)]

    def addEdge(self, u, v):
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)

    def addWeightedEdge(self, u, v, w):
        self.adj[u].append((w, v))
        if not self.directed:
            self.adj[v].append(u)

    def printGraph(self):
        print(self.adj)

    def bfsCore(self, source, visited):
        from collections import deque
        q = deque()
        q.append(source)
        while len(q) > 0:
            top = q.popleft()  # main reason for bfs
            print(top)

            for nei in self.adj[top]:
                if not visited[nei]:
                    q.append(nei)
                    visited[nei] = True

    def bfs(self):
        visited = {}
        for i in range(self.n):
            visited[i] = False

        for i in range(self.n):  # This loop is for graphs with more than one connected components
            if not visited[i]:
                visited[i] = True
                self.bfsCore(i, visited)

    def dfsCore(self, source, visited):
        stack = [source]
        while len(stack) > 0:
            top = stack.pop()  # main reason for bfs
            print(top)

            for nei in self.adj[top]:
                if not visited[nei]:
                    stack.append(nei)
                    visited[nei] = True

    def dfsRecurrCore(self, source, visited):
        if not visited[source]:
            visited[source] = True
            print(source)
            for nei in self.adj[source]:
                if not visited[nei]:
                    self.dfsRecurrCore(nei, visited)

    def dfs(self):
        visited = {}
        for i in range(self.n):
            visited[i] = False

        for i in range(self.n):  # This loop is for graphs with more than one connected components
            if not visited[i]:
                # visited[i] = True # Uncomment for dfcCore
                # self.dfsCore(i, visited) # Uncomment for dfcCore
                self.dfsRecurrCore(i, visited)  # calling dfsRecurrCore

    def dfsDetectCycleCore(self, source, state):
        if state[source] == "U":
            state[source] = "V"
            print(source)
            for nei in self.adj[source]:
                self.dfsDetectCycleCore(nei, state)
            state[source] = "P"
        elif state[source] == "V":
            print("Cycle found at " + str(source))

    def detect_cycle(self):
        state = {}
        for i in range(self.n):
            state[i] = "U"

        for i in range(self.n):
            if state[i] == "U":
                self.dfsDetectCycleCore(i, state)

    def djikstra(self, source):
        import heapq
        import math
        heap = []
        distance = {}
        for i in range(self.n):
            distance[i] = math.inf
        distance[source] = 0

        heapq.heappush(heap, (0, source))

        while len(heap) > 0:
            top = heap[0]
            heapq.heappop(heap)

            node = top[1]
            dis = top[0]
            if dis <= distance[node]:
                distance[node] = dis
                for nei in self.adj[node]:
                    nei_node = nei[1]
                    weight = nei[0]
                    if distance[node] + weight < distance[nei_node]:
                        distance[nei_node] = distance[node] + weight
                        heapq.heappush(heap, (distance[nei_node], nei_node))
        return distance


g2 = GraphAdjList(5, True)
# g2.addEdge(0, 1)
# g2.addEdge(1, 2)
# g2.addEdge(0, 2)
# g2.addEdge(3, 1)
# g2.addEdge(2, 3)

# g2.printGraph()
# g2.bfs()
# g2.dfs()

# g2.detect_cycle()

g2.addWeightedEdge(0, 1, 5)
g2.addWeightedEdge(0, 3, 10)
g2.addWeightedEdge(1, 2, 11)
g2.addWeightedEdge(1, 4, 4)
g2.addWeightedEdge(2, 4, 9)
g2.addWeightedEdge(3, 2, 2)

print(g2.djikstra(0))
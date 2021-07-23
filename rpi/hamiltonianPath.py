# stores the vertices in the graph
vertices = []
# stores the number of vertices in the graph
vertices_no = 0
graph = []

#Calculate Distance
def distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5

#Add vertex to graph
def add_vertex(v):
  global graph
  global vertices_no
  global vertices
  if v in vertices:
    print("Vertex ", v, " already exists")
  else:
    vertices_no = vertices_no + 1
    vertices.append(v)
    if vertices_no > 1:
        for vertex in graph:
            vertex.append(0)
    temp = []
    for i in range(vertices_no):
        temp.append(0)
    graph.append(temp)

# Add edge between vertex v1 and v2 with weight e
def add_edge(v1, v2, e):
    global graph
    global vertices_no
    global vertices
    # Check if vertex v1 is a valid vertex
    if v1 not in vertices:
        print("Vertex ", v1, " does not exist.")
    # Check if vertex v1 is a valid vertex
    elif v2 not in vertices:
        print("Vertex ", v2, " does not exist.")
    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = e
        graph[index2][index1] = e

# Print the graph
def print_graph():
  global graph
  global vertices_no
  for i in range(vertices_no):
    for j in range(vertices_no):
      if graph[i][j] != 0:
        print(vertices[i], " -> ", vertices[j], \
        " edge weight: ", graph[i][j])

def shortestPath(obstacle_android):
    obstacle_number = len(obstacle_android)
    print('No. of obstacles:',obstacle_number)
    origin = [0,0]
    obstacle_list = []
    visited_vertex = [0] * obstacle_number
    obstacle_distance = []
    list = []

    for i in range(0, obstacle_number):
        obstacle_list.append ([obstacle_android[i][0],obstacle_android[i][1]])

    for i in range(0, obstacle_number):
        obstacle_distance.append(distance(origin,obstacle_list[i]))
        add_vertex(i) # Add vertices to the graph
    first_vertex = obstacle_distance.index(min(obstacle_distance))
    
    # Add the edges between the vertices with the edge weights.
    for i in range(0, obstacle_number-1):
        for j in range(i+1, obstacle_number):
            add_edge(i, j, round(distance(obstacle_list[i],obstacle_list[j]),2))

    # Update the current vertex
    current_vertex = first_vertex
    shortest_path = [400] * obstacle_number
    for i in range(0, obstacle_number):
        shortest_path[i] = current_vertex
        minimum = 200
        min_index = 0
        visited_vertex[current_vertex] = 1
        for j in range (0, obstacle_number):
            if graph[current_vertex][j]<minimum and current_vertex!=j:
                if visited_vertex[j] == 0 :
                    minimum = graph[current_vertex][j]
                    min_index = j
        current_vertex = min_index

    for i in range(len(shortest_path)):
        list.append(obstacle_android[shortest_path[i]])
    return list


        

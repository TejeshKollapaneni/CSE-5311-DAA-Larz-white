def Floyd_Warshall(graph):
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    print_graph(graph)

def print_graph(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            if (graph[i][j] == 1e7): 
                print("%7s" % ("INF"), end=" ")
            else: 
                print("%7d\t" % (graph[i][j]), end=' ')
            if j == len(graph)-1: 
                print()

# Updated Testing
graph = [
    [0, 2, 1e7, 5], 
    [1e7, 0, 4, 1e7], 
    [3, 1e7, 0, 6], 
    [1e7, 1e7, 2, 0]
]

Floyd_Warshall(graph)

'''Output:

      0	    2	    3	    5	 
      7	    0	    4	    8	 
      3	    5	    0	    6	 
      5	    7	    2	    0	 
'''

from collections import *
from load_graph import *


def bfs(start, goal):  # Defines Breadth-First Search function.

    backpointers = {}
    d = deque()

    # Add the starting Vertex to the queue.
    d.append(start)
    backpointers[start] = None

    visited = []

    # While the queue is not empty, queue and de-queue.
    while len(d) != 0:

        x = d.popleft()

        # While not at the end of the path, adjust queue.

        if x != goal:

            for y in x.adjacent:

                if y not in backpointers:
                    backpointers[y] = x
                    d.append(y)

        # Traverse through backpointers to return list of visited Vertices.

        else:

            while backpointers[x] is not None:

                visited.append(x)
                x = backpointers[x]

            visited.append(start)

    return visited

# Driver code to test bfs function with graph defined in vertices.txt.

dict = load_graph("vertices.txt")
list = bfs(dict["B"], dict["G"])

set = []

for entry in list:
    set.append(str(entry))

set.reverse()

print(set)

from collections import *
from load_graph import *

fo = None
ba = None


def bcs(start, goal):  # Defines Bidirectional Breadth-First Search (Breadcrumb Search) function.

    global fo, ba

    forward = deque()
    backward = deque()

    backpointers_forward = {}
    backpointers_backward = {}

    # Add the starting Vertex to the queue.
    forward.append(start)
    backpointers_forward[start] = None

    backward.append(goal)
    backpointers_backward[goal] = None

    visited_forward = []
    visited_backward = []

    if start != goal:

        # While the queue is not empty, queue and de-queue.
        while len(forward) != 0 and len(backward) != 0:

            fo = forward.popleft()

            if fo == goal or fo in backward:
                break

            for vertex_fo in fo.adjacent:

                if vertex_fo not in backpointers_forward:
                    backpointers_forward[vertex_fo] = fo
                    forward.append(vertex_fo)

            ba = backward.popleft()

            if ba == start or ba in forward:
                break

            for vertex_ba in ba.adjacent:

                if vertex_ba not in backpointers_backward:
                    backpointers_backward[vertex_ba] = ba
                    backward.append(vertex_ba)

        # Maintains proper direction of BFS to middle vertex in each direction.

        if ba in forward:
            fo = ba
        if fo in backward:
            ba = fo

        # Traverse through backpointers to return forward and backward paths from middle vertex.

        while backpointers_forward[fo] is not None:

            visited_forward.append(fo)
            fo = backpointers_forward[fo]

        visited_forward.append(fo)

        while backpointers_backward[ba] is not None:

            visited_backward.append(ba)
            ba = backpointers_backward[ba]

        visited_backward.append(ba)

    return visited_forward, visited_backward


# Driver code to test bcs function with graph defined in vertices.txt.

dict = load_graph("vertices.txt")
list1, list2 = bcs(dict["B"], dict["G"])

# Half paths from each BFS search from middle to start or goal vertex.

set1 = []
set2 = []

for entry in list1:
    set1.append(str(entry))

for entry in list2:
    set2.append(str(entry))

print("half paths: " + str(set1) + ", " + str(set2))

# Full path between start and goal vertices found from combination of half paths.

full_list = []

set1.pop(0)

i = len(set1)

while i > 0:
    full_list.append(set1[-1])
    del set1[len(set1) - 1]
    i = i - 1

for entry in list2:
    full_list.append(str(entry))

print("full path: " + str(full_list))

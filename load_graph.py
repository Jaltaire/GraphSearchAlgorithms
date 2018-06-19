from vertex import *

def parse_line(line):  # Parses and splits each line in the graph data file.
    section_split = line.split(";")

    vertex_name = section_split[0].strip()
    adjacent_vertices = section_split[1].strip().split(",")

    # add all except empty strings
    adjacent = []
    for a in adjacent_vertices:
        if a:
            adjacent.append(a.strip())

    return vertex_name, adjacent


# Creates a dictionary of Vertex objects from each line in the graph data file.
def load_graph(data_file):
    vertex_dict = {}

    # Read the lines in the file into a list of lines:
    file_first = open(data_file, "r")

    for line in file_first:  # First pass

        # if this is a line in the correct format:
        if len(line.split(";")) == 2:
            vertex_name, adjacent_vertices = parse_line(line)

            vertex_dict[vertex_name] = Vertex(vertex_name, [])

    file_first.close()

    file_second = open(data_file, "r")

    for line in file_second:

        # if this is a line in the correct format:
        if len(line.split(";")) == 2:
            vertex_name, adjacent_vertices = parse_line(line)

            for adjacent_vertex in adjacent_vertices:
                vertex_dict[vertex_name].adjacent.append(vertex_dict[adjacent_vertex])

    file_second.close()

    return vertex_dict

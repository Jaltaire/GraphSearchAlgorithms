class Vertex:  # Creates Vertex class.

    def __init__(self, name, adjacent):  # Instantiates Vertex object.

        self.name = name
        self.adjacent = adjacent

    def __str__(self):  # Returns string containing Vertex information (location, coordinates, and adjacent vertices.)

        adjacent_vertices = []

        for vertex in self.adjacent:  # Creates list of adjacent Vertex names.
            adjacent_vertices.append(vertex.name)

        data = self.name
        return data

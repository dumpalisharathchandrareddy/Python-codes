import math


class Polygon:
    # This class variable keeps track of how many polygons have been created
    polygon_count = 0

    def __init__(self, name, vertices, num_vertices=None, ):
        # We start by validating the name to make sure it's a non-empty string
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Polygon name must be a non-empty string.")
        
        # Make sure there are at least 3 vertices for the polygon
        if not isinstance(vertices, list) or len(vertices) < 3:
            raise ValueError("A polygon must have at least 3 vertices.")
        
        # Now, let's make sure each vertex is a tuple of two numbers (x, y)
        for vertex in vertices:
            if not (isinstance(vertex, tuple) and len(vertex) == 2):
                raise ValueError("Each vertex must be a tuple with two numeric values (x, y).")
            if not all(isinstance(coord, (int, float)) for coord in vertex):
                raise ValueError("Vertex coordinates must be integers or floats.")
        
        # Assign the polygon name and vertices to the instance variables
        self.name = name.strip()
        self.vertices = vertices
        self.num_vertices = num_vertices if num_vertices else len(vertices)  # Automatically calculate the number of vertices if  not provided
        
        # Every time we create a polygon, we increment the count
        Polygon.polygon_count += 1

    @classmethod
    def total_polygons(cls):
        # This class method returns the total number of polygons created
        return cls.polygon_count

    def side_count(self):
        # This method returns the number of sides, which is the same as the number of vertices
        return self.num_vertices

    def side_lengths(self):
        # Here, we calculate the length of each side using the distance formula
        lengths = []
        for i in range(self.num_vertices):
            # We get the coordinates of the current and next vertex (wrapping around to the start)
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % self.num_vertices]
            # Calculate the distance between the two points (side length)
            length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            lengths.append(length)
        return lengths

    def formatted_results(self):
        # Now, we get the lengths of all the sides for display
        sides = self.side_lengths()
        
        # We format the vertices into a nice string for easy reading
        vertex_list = ", ".join(f"({x:.2f}, {y:.2f})" for x, y in self.vertices)
        
        # Format the side lengths and display them clearly
        side_info = "\n".join(f"  Side {i + 1}: {length:.2f}" for i, length in enumerate(sides))
        
        # Put everything together in a clean, formatted string
        return (
            f"Polygon Details:\n"
            f"----------------\n"
            f"Name: {self.name}\n"
            f"Number of Vertices: {self.num_vertices}\n"
            f"Vertices: {vertex_list}\n"
            f"Number of Sides: {self.side_count()}\n"
            f"Side Lengths:\n{side_info}\n"
        )

    def __str__(self):
        # When we print a Polygon, we want it to show the formatted results
        return self.formatted_results()

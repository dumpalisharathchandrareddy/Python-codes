from Polygonclass import Polygon

def create_polygon():
    # This function gets the user input to create a new polygon with name, number of vertices and vertices!
    while True:
        try:
            # First, ask for the name of the polygon
            name = input("Enter the name of the polygon: ").strip()
            if not name:
                raise ValueError("Polygon name cannot be empty.")
            
            # Now, ask how many vertices the polygon should have (minimum 3)
            num_vertices = int(input(f"Enter the number of vertices for {name} (minimum 3): "))
            if num_vertices < 3:
                raise ValueError("A polygon must have at least 3 vertices.")
            
            # Create a list to store the vertices
            vertices = []
            print(f"Enter the coordinates for the {num_vertices} vertices (format: x y) x and y with space in between:")
            for i in range(num_vertices):
                while True:
                    try:
                        # Get the x, y coordinates as floats
                        x, y = map(float, input(f"  Vertex {i + 1}: ").split())
                        vertices.append((x, y))
                        break
                    except ValueError:
                        print("Invalid input! Please enter two numeric values separated by a space.")
            
            # Return the new polygon created with the provided details
            return Polygon(name, vertices)
        except ValueError as e:
            # If there’s an error, print it and ask if the user wants to try again
            print(f"Error: {e}")
            retry = input("Would you like to try again? (yes/no) (default no): ").strip().lower()  # Default is no
            if retry != 'yes':  # If not 'yes'
                return None  # Return None to exit the creation process


def main():
    # This is the main function where the program starts
    print("Welcome to Sharath's Polygon Instance Function!")
    polygons = []  # This will hold all the polygons we create

    while True:
        try:
            # Ask if the user wants to continue or exit the app
            user_action = input("\nDo you want to create a polygon? (yes/no): ").strip().lower()

            if user_action == 'no':  # User wants to exit the application
                print("Exiting the Sharath's Polygon Instance Function! Goodbye!!!")
                break  # Exit the loop and end the program

            if user_action == 'yes':  # User wants to create a polygon
                # Ask how many polygons the user wants to create
                num_polygons = int(input("How many polygons would you like to create? "))
                if num_polygons <= 0:
                    raise ValueError("The number of polygons must be greater than zero.")

                # Create the polygons based on the user input
                for _ in range(num_polygons):
                    polygon = create_polygon()  # Call the function to create a polygon
                    if polygon:
                        polygons.append(polygon)

                # Display all the polygons that have been created
                print("\nDisplaying All Created Polygons:\n")
                for i, poly in enumerate(polygons, start=1):
                    print(f"Polygon {i}:")
                    print(poly)  # Prints each polygon's details
                    print("-" * 40)  # Adding a separator line for readability

                # Show the total number of polygons created
                print(f"Total Polygons Created: {Polygon.total_polygons()}")

                # Ask if the user wants to create more polygons
                continue_creating = input("Would you like to create more polygons? (yes/no): ").strip().lower()
                if continue_creating != 'yes':
                    print("Exiting the Polygon creation process. Goodbye!")
                    break  # Exit the loop if the user doesn't want to continue

            else:
                print("Invalid input! Please type 'yes' to create polygons or 'no' to exit.")
        
        except ValueError as e:
            # Catch any errors at the main level and print a message
            print(f"Error: {e}")
            print("Exiting the Sharath's Polygon Instance Function! Sorry, Bye!!!")
            break  # Exit the loop on error

if __name__ == "__main__":
    # This makes sure the main function runs when the script is executed
    main()

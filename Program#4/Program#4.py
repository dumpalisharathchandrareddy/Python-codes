#Sharath Chandra Reddy -- Dumpali
# 00864049

# List of 8 location names and their coordinates
location_names = ['Boston', 'Seattle', 'Miami', 'Dallas', 'Denver', 'Atlanta', 'LasVegas', 'SanFrancisco']
location_coords = [(1.0, 2.0, 3.0), (4.0, 5.0, 6.0), (7.0, 8.0, 9.0), 
                   (2.0, 3.0, 1.0), (5.0, 6.0, 4.0), (8.0, 9.0, 7.0), 
                   (3.0, 1.0, 2.0), (6.0, 4.0, 5.0)]

# Function to calculate the Euclidean distance between two 3D points
def calculate_distance(coord1, coord2):
    return ((coord2[0] - coord1[0])**2 + 
            (coord2[1] - coord1[1])**2 + 
            (coord2[2] - coord1[2])**2) ** 0.5

# 1. Create a list of distances with names using list comprehension
distances_list = [
    [f"Distance{location_names[i]}To{location_names[i+1]}", calculate_distance(location_coords[i], location_coords[i+1])]
    for i in range(len(location_names) - 1)
]

# Print original location names and coordinates
print("Original Location Names and Coordinates:")
for i in range(len(location_names)):
    print(f"{location_names[i]}: {location_coords[i]}")

# Print distances between consecutive locations
print("\nDistances between consecutive locations:")
for distance in distances_list:
    print(f"{distance[0]}: {distance[1]:.3f}")

# 2. Create a list of tuples where each tuple contains the distance name and a list that has the distance and coordinates
distances_tuples = [
    (f"Distance{location_names[i]}To{location_names[i+1]}", 
    [calculate_distance(location_coords[i], location_coords[i+1]), location_coords[i], location_coords[i+1]])
    for i in range(len(location_names) - 1)
]

# Print the list of tuples with distance names, distances, and coordinates
print("\nDistance Tuples:")
for item in distances_tuples:
    print(f"{item[0]}: Distance {item[1][0]:.3f}, Coordinates {item[1][1]}, {item[1][2]}")
#Sharath Chandra Reddy Dumpali -- 00864049

# Step 1: Creating a List of Cities and a List of Zip Codes
locations = ['Hartford', 'Bloomfield', 'Vernon', 'Danville', 'Manchester']
postal_codes = ['06103', '06002', '06066', '24541', '06040']

print("Cities: ",locations)
print("\nZip codes: ",postal_codes)

# Step 2: Associating the Cities and Zip Codes positionally
combined_list = [locations, postal_codes]
print("\nComposite List of Cities and Zipcodes: ",combined_list)

# Step 3: Demonstrating how to index, append, and delete elements
# Indexing individual lists
print("\nCity at index 2:", locations[2])  # Outputs the loctaion at index 2
print("Zip Code at index 3:", postal_codes[3])  # Outputs the zipcode at index 3

# Indexing the composite list
print("\nCity at index 1 of combined list:", combined_list[0][1])  
print("Zip Code at index 1 of combined list:", combined_list[1][1])  

# Appending elements to individual lists
locations.append('New London')  # Added a new city 
postal_codes.append('06320')    # Added a corresponding zip code
print("\nUpdated locations and postal codes:\n", locations, '\n', postal_codes) #Updated lists of locations and zip codes after appending new elements

# Append a new city and zip code to the respective lists in the composite list
combined_list[0].append('West Haven')  # Adding to the city list
combined_list[1].append('06516')       # Adding to the zip code list

print("\nComposite list after appending:")
print(combined_list)  # Displays the updated composite list

# Deleting elements from individual lists
del locations[0]  # Removes the location at index 0 i.e 1st element
del postal_codes[0]  # Removes the zip code at index 0 i.e 1st element
print("\nLocations and Postal Codes after deletion:", locations,'\n', postal_codes)

print(combined_list)
# Delete the first city and zip code from the respective lists in the composite list
del combined_list[0][0]  # Removes 'Bloomfield' from the city list
del combined_list[1][0]  # Removes '06002' from the zip code list

print("\nComposite list after deletion:")
print(combined_list)  # Displays the updated composite list after deletions

# Step 4: Demonstrating obtaining the size of the composite and individual lists
print("\nNumber of locations:", len(locations))
print("Number of postal codes:", len(postal_codes))
print("Number of lists in combined list:", len(combined_list))

# Step 5: Demonstrate indexing from the end to the beginning of the individual and composite lists
print("\nLast city in the list:", locations[-1])  # Outputs 'West Haven'
print("Second to last zip code:", postal_codes[-2])  # Outputs '24541'
print("Last city in combined list:", combined_list[0][-1])  # Outputs 'West Haven'
print("Last zip code in combined list:", combined_list[1][-1])  # Outputs '06516'

# Step 6: Walk through the Lists and create a formatted output
print("\nListing of Cities & Zip Codes")
print(f"Total Unique Entries: {len(locations)}")
for i in range(len(locations)):
    print(f"City #{i+1}: {locations[i]}. Zip #{i+1}: {postal_codes[i]}")

# Step 7: Demonstrating a List of Tuples and its operations
tuple_list = list(zip(locations, postal_codes))

# Indexing, appending, deleting, and size of the List of Tuples
print("\nList of Tuples:")
print(tuple_list)

# Indexing
print("\nTuple at index 2:", tuple_list[2])  # Outputs the third tuple

# Appending a new Tuple
tuple_list.append(('New London', '06320'))
print("\nAppended list of tuples:", tuple_list)

# Deleting a Tuple
del tuple_list[0]  # Removes the first tuple
print("\nList of tuples after deletion:", tuple_list)

# Size of the List of Tuples
print("\nSize of the list of tuples:", len(tuple_list))

# Indexing from end to beginning
print("\nLast tuple in the list:", tuple_list[-1])  # Outputs the last tuple

# Walk through the List of Tuples and create a formatted output
print("\nListing of Cities & Zip Codes (Tuples)")
print(f"Total Unique Entries: {len(tuple_list)}")
for i, (city, postal_code) in enumerate(tuple_list, start=1):
    print(f"City #{i}: {city}. Zip #{i}: {postal_code}")
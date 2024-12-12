myString = input("Input the String: ")
char_list = []
for char in myString:
    char_found = False
    for item in char_list:
        if item[0].lower() == char.lower():
            item[1] += 1
            char_found = True
            break
    if not char_found:
        char_list.append([char, 1])
        
print(char_list)

for item in char_list:

    print(f"{item[0]} count: {item[1]}")

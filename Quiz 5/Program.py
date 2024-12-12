person=0 #Count of person starts at 0
Person_list=[] #Empty List for each person
List_of_persons=[] #Empty List for list of Persons
for i in range(11): #iterates for 11 persons
    first_name=input("Enter First Name: ") #First Name of person
    last_name=input("Enter Last Name: ") # Last Name of Person
    age=int(input("Enter the age of the person: ")) # Age of Person
    Person_list.append(first_name) # add the first name to list
    Person_list.append(last_name) # add the last name to list
    Person_list.append(age) # add the age to list
    person+=1 #increment
    List_of_persons.append(Person_list) #add the list to list 
    Person_list=[] #list for another person
  

for i in List_of_persons:
    print("Name: ", i[0],"",i[1], "age: ",i[2]) # print list of persons info 
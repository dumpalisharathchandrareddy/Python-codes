n= int(input("Enter n: "))
fact=1
for i in range(1,n+1):
    fact = fact * i  # Multiply the factorial by each number from n to
    i+=1
print ("The factorial of", n, "is", fact)



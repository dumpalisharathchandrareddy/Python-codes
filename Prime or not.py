a= int(input("Enter the number: "))
if a<2:
    print("The number is not Prime")
elif a==2 or a==3:
    print("The number is Prime")
else:
    for i in range(2,a):
        if (a % i) == 0:
            print("The number is not Prime")
            break
    else:
        print("The number is Prime")
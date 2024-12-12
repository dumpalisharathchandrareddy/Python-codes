n=int(input("Enter n: "))
start=0
first =1
print(start)
print(first)

for i in range(1,n-1):
    next_num= start+first
    print(next_num)
    start= first
    first= next_num
    i+=1
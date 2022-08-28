nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

even = []
odd = []

for i in nums:
    if(i % 2 == 0):
        even.append(i)
    else:
        odd.append(i)
        
print("Even List: ",even)
print("Odd List: ",odd)


num = int(input("Enter number:-"))

def filter(num):
    even=[]
    odd=[]
    for i in range(num):
        if(i%2 ==0) and (i != 0):
            even.append(i)
        else:
            odd.append(i)

    print(f"Odd list is:{odd} and Even list is :{even}")


filter(num) 
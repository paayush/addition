a = int(input("enter a number:-"))
b = int(input("enter second number:-"))
def add_number():
    sum = a+b #sum of two numbers 
    print(sum)

add_number()


def add(num1,num2):
    sum  = num1+num2
    return(sum)

num1 = int(input("enter first number:-"))
num2 = int(input("enter second number:-"))
sum = add(num1,num2)
print(f"sum is {sum}")

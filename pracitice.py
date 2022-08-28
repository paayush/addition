num = int(input("enter a number:-"))

even = []
odd = []

def number_checker():
    for i in range(num):
        if (i % 2 == 0) and (i != 0):
            even.append(i)
        else:
            odd.append(i)

    print(f"list of odd number{odd} and even number {even}")

number_checker()
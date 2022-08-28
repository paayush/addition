'''brand_name = input("enter which brand your laptop is:-")
model_name = input("enter model of your laptop:-")
price = input("enter at which price your laptop is aavailable at:-")

def detail():
    print(brand_name, model_name, price)


detail()'''



#string formation

'''brand = input("enter which brand your laptop is:-")
model = input("enter model of your laptop:-")
price = input("enter at which price your laptop is aavailable at:-")

def detail(brand,model,price) :
    print(f"{brand} {model} @ rs{price}")

laptop_detail = detail(brand ,model ,price)
print(laptop_detail)'''



#working process of atm

'''total_price = 0
card_type = "visa"
is_same_bank = True
is_expired=False

def read_card():
    print("Fetching Card Details from bank ....")
    card_details = [1200,True,False]
    total_price = card_details[0]
    is_same_bank=card_details[1]
    is_expired= card_details[2]
    if is_expired:
        print("Sorry, this card can not be accepted here")
    else:
        perform_tansaction(total_price,is_same_bank)


def perform_tansaction(total_amt, is_same_bank):
    charge = 0
    if not is_same_bank:
        charge = 5
        if required_amt > total_amt:
            return "Not enough balance"
        else:
            print(f"Ant withdrwn: {required_amt}")
            print(f"Remaining available balance: {total_amt-required_amt-charge}")
    else:
        if required_amt > total_amt:
            return "Not enough balance"
        else:
            print(f"Ant withdrwn: {required_amt}")
            print(f"Remaining available balance: {total_amt-required_amt-charge}")


print("Please insert your atm card:")
input()
print("Card inserted!!")
required_amt = int(input("Please enter a amount:"))
read_card()
'''

#days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

'''for i in range(0,10,3):
    if i % 2 == 0:'''

#print(days.index('tuesday'))

#append method():- it is used to insert data into existing list
    #day_list.append(saturday2)

#pop():- it is used tp eject the last element/item from the list and return to us
    #day_list.pop()

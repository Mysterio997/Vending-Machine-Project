# Initial Price Variables
CEREALBAR=50
CRISPS=60
CHOCOLATEBAR=80
BOTTLEDWATER=90
# Other Variables
PRICETOPAY=0 # Total Amount Needed
CHANGE=0 # Change In Pence
POUNDCHANGE=0 # Change In Pounds
PAYMENTACCEPTED = ("false")  # Payment Accepted?
ITEMDISPENSED = ("false")  # Item Dispensed?

print()
print("Welcome To The Vending Machine!")
print("==============================")
print("Here are your options below:")
print()
print(f"Cereal bar = {CEREALBAR}p" )
print(f"Crisps = {CRISPS}p")
print(f"Chocolate bar = {CHOCOLATEBAR}p")
print(f"Bottled water = {BOTTLEDWATER}p")
print()
print("Accepted payment options: 10p, 20p, 50p, £1. Please pay in pence.")
print("==============================")
print()

Selection = input("What Item Will You Be Selecting?")
Selection.strip()

if Selection.lower() == "cereal bar" or Selection.lower()=="cerealbar":  
    PRICETOPAY = CEREALBAR
    CHOICE = "Cereal Bar"
    print(f"Please pay {CEREALBAR}p for a Cereal Bar!")
elif Selection.lower() == "crisps":  
    PRICETOPAY = CRISPS
    CHOICE = "Crisps"
    print(f"Please pay {CRISPS}p for Crisps!")
elif Selection.lower() == "chocolate bar" or Selection.lower()=="chocolatebar":  
    PRICETOPAY = CHOCOLATEBAR
    CHOICE = "Chocolate Bar"
    print(f"Please pay {CHOCOLATEBAR}p for a Chocclate Bar!")
elif Selection.lower() == "bottled water" or Selection.lower()=="bottledwater":  
    PRICETOPAY = BOTTLEDWATER
    CHOICE = "Bottled Water"
    print(f"Please pay {BOTTLEDWATER}p")
else:   
    print("You have not selected a valid option, please try again")
      quit()

PAYMENT = int(input("How Much Money Did You Insert?"))

if (PAYMENT == 10) or (PAYMENT == 20) or (PAYMENT == 50) or (PAYMENT == 100):
    PAYMENT = PAYMENT
    PAYMENTACCEPTED = ("true") 
else: 
    print("Inserted payment is not not accepted. Accepted payment options: 10p, 20p, 50p, £1. Please pay in pence.") 
    PAYMENTACCEPTED = ("false") 

if PAYMENTACCEPTED == "true" and PAYMENT < PRICETOPAY:
    while PAYMENT < PRICETOPAY:
        AMOUNTNEEDED = PRICETOPAY - PAYMENT
        print(f"Please insert more money, total amount needed is {AMOUNTNEEDED}p")
        PAYMENT2 = int(input("How much more money do you insert?"))
# Payment validation logic does not apply to PAYMENT2
        PAYMENT = PAYMENT + PAYMENT2

if PAYMENTACCEPTED == "true" and PAYMENT >= PRICETOPAY:
    print(f"Dispensed {CHOICE}")
elif PAYMENT >= PRICETOPAY:
    CHANGE = PAYMENT - PRICETOPAY
elif CHANGE == "0":
    print("No change required")
elif CHANGE > 99:
    CHANGE % 100 == POUNDCHANGE
    print(f"Change dispensed is {POUNDCHANGE} pounds")
elif CHANGE > 0:
    print(f"Change dispensed is {CHANGE}p")

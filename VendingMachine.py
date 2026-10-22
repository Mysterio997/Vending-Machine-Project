# Initial Price Variables
CEREALBAR=50
CRISPS=60
CHOCOLATEBAR=80
BOTTLEDWATER=90
# Other Variables
PAYMENT2 = 0 # Extra payment if needed
PRICETOPAY=0 # Total Amount Needed
CHANGE=0 # Change In Pence
INVALIDPAYMENT="Inserted payment is not not accepted. Accepted payment options: 10p, 20p, 50p, £1. Please pay in pence."

print()
print("Welcome To The Vending Machine!")
print("==============================")
print("Here are your options below:")
print()
print(f"Cereal bar = {CEREALBAR}p - Button A" )
print(f"Crisps = {CRISPS}p - Button B")
print(f"Chocolate bar = {CHOCOLATEBAR}p - Button C")
print(f"Bottled water = {BOTTLEDWATER}p - Button D")
print()
print("Accepted payment options: 10p, 20p, 50p, £1. Please pay in pence.")
print("==============================")
print()

Selection = input("What Item Will You Be Selecting?")
Selection.strip()

if Selection.lower() == "a":
    PRICETOPAY = CEREALBAR
    CHOICE = "Cereal Bar"
    print(f"Please pay {CEREALBAR}p for a Cereal Bar!")
elif Selection.lower() == "b":
    PRICETOPAY = CRISPS
    CHOICE = "Crisps"
    print(f"Please pay {CRISPS}p for Crisps!")
elif Selection.lower() == "c":
    PRICETOPAY = CHOCOLATEBAR
    CHOICE = "Chocolate Bar"
    print(f"Please pay {CHOCOLATEBAR}p for a Chocclate Bar!")
elif Selection.lower() == "d":
    PRICETOPAY = BOTTLEDWATER
    CHOICE = "Bottled Water"
    print(f"Please pay {BOTTLEDWATER}p")
else:   
    print("You have not selected a valid option, please try again")
    quit()

PAYMENT = int(input("What coins did you insert?"))
VALIDPAYMENT = "false"
AMOUNTNEEDED="0"
if (PAYMENT == 10) or (PAYMENT == 20) or (PAYMENT == 50) or (PAYMENT == 100):
    VALIDPAYMENT = "true" 

while VALIDPAYMENT == "true" and PAYMENT < PRICETOPAY:
    AMOUNTNEEDED = PRICETOPAY - PAYMENT
    print(f"Please insert more money, total amount needed is {AMOUNTNEEDED}p")
    PAYMENT2 = int(input("How much more did you insert? "))
    if PAYMENT2 not in [10 , 20, 50, 100]:
        print(f"{INVALIDPAYMENT}")
        exit()
    if PAYMENT2 in [10 , 20, 50, 100]:
        PAYMENT = PAYMENT + PAYMENT2


if VALIDPAYMENT == "true" and PAYMENT >= PRICETOPAY:
    CHANGE = PAYMENT - PRICETOPAY
    if CHANGE == "0":
        print(f"Dispensed {CHOICE}, no change.")
    else:
        print(f"Dispensed {CHOICE}, your total change is {CHANGE}p")


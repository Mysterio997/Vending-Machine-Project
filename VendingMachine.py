PRICE=0
CEREALBAR=0.50
CRISPS=0.60
CHOCOLATEBAR=0.80
BOTTLEDWATER=0.90

CEREAL_BAR=0
CRISPS_1=0
CHOCOLATE_BAR=0
BOTTLED_WATER=0

CHOICE = "No Choice"
print()
print("Welcome To The Vending Machine!")
print()
print("==============================")
print("Here are your options below:")
print()
print(f"Cereal bar = {CEREALBAR:.2f}" )
print(f"Crisps = {CRISPS:.2f}")
print(f"Chocolate bar = {CHOCOLATEBAR:.2f}")
print(f"Bottled water = {BOTTLEDWATER:.2f}")
print()
print("Accepted payment options: 10p, 20p, 50p, £1")
print("==============================")
print()

# Inital Definition Of Item Choice And Price
choice = input("What item are you choosing?")
if choice.lower() == "cereal bar" or choice.lower()=="cerealbar":  
    PRICE = CEREALBAR
    CHOICE = "Cereal Bar"
    print(f"Please pay {CEREALBAR:.2f} for a Cereal Bar!")
elif choice.lower() == "crisps":  
    PRICE = CRISPS
    CHOICE = "Crisps"
    print(f"Please pay {CRISPS:.2f} for Crisps!")
elif choice.lower() == "chocolate bar" or choice.lower()=="chocolatebar":  
    PRICE = CHOCOLATEBAR
    CHOICE = "Chocolate Bar"
    print(f"Please pay {CHOCOLATEBAR:.2f} for a Chocclate Bar!")
elif choice.lower() == "bottled water" or choice.lower()=="bottledwater":  
    PRICE = BOTTLEDWATER
    CHOICE = "Bottled Water"
    print(f"Please pay {BOTTLEDWATER:.2f}")
else:   
    print("You have not selected a valid option, please try again")

# Defining Payment And Extra Payment If Not Enough Inserted
PAYMENT = float(input("How Much Money Did You Insert?"))
PAYMENT2 = 0

# Do Not Have Enough For Item
if PAYMENT < 0.50 and choice.lower() == "cereal bar" or choice.lower()=="cerealbar":  
    print("You do not have enough money for this item, please insert extra money.")
    PAYMENT2 = float(input("How Much extra Money Did You Insert?"))
elif PAYMENT < 0.60 and choice.lower() == "crisps":    
    print("You do not have enough money for this item, please insert extra money.")
    PAYMENT2 = float(input("How Much extra Money Did You Insert?"))
elif PAYMENT < 0.80 and choice.lower() == "chocolate bar" or choice.lower()=="chocolatebar":   
    print("You do not have enough money for this item, please insert extra money.")
    PAYMENT2 = float(input("How Much extra Money Did You Insert?"))
elif PAYMENT < 0.90 and choice.lower() == "bottled water" or choice.lower()=="bottledwater":  
    print("You do not have enough money for this item, please insert extra money.")
    PAYMENT2 = float(input("How Much extra Money Did You Insert?"))




# If still do not have enough after extra inserted money
if PAYMENT + PAYMENT2 < 0.50 and choice.lower() == "cereal bar" or choice.lower()=="cerealbar":  
    print("You do not have enough money for this item.")
elif PAYMENT + PAYMENT2  < 0.60 and choice.lower() == "crisps":    
    print("You do not have enough money for this item.")
elif PAYMENT + PAYMENT2  < 0.80 and choice.lower() == "chocolate bar" or choice.lower()=="chocolatebar":   
    print("You do not have enough money for this item.")
elif PAYMENT + PAYMENT2 < 0.90 and choice.lower() == "bottled water" or choice.lower()=="bottledwater":  
    print("You do not have enough money for this item.")

# If they have enough
if PAYMENT + PAYMENT2 >= 0.50 and choice.lower() == "cereal bar" or choice.lower()=="cerealbar":  
    print("Thank you for your purchase.")
    print(f"Dispensed {CHOICE}")
elif PAYMENT + PAYMENT2 >= 0.60 and choice.lower() == "crisps":    
    print("Thank you for your purchase.")
    print(f"Dispensed {CHOICE}")
elif PAYMENT + PAYMENT2 >= 0.80 and choice.lower() == "chocolate bar" or choice.lower()=="chocolatebar":   
    print("Thank you for your purchase.")
    print(f"Dispensed {CHOICE}")
elif PAYMENT + PAYMENT2 >= 0.90 and choice.lower() == "bottled water" or choice.lower()=="bottledwater":  
    print("Thank you for your purchase.")
    print(f"Dispensed {CHOICE}")



TOTAL = 0

# Change
if PAYMENT + PAYMENT2 > 0.50 and choice.lower() == "cereal bar" or choice.lower()=="cerealbar":  
    TOTAL = PAYMENT + PAYMENT2 - 0.50
    print(f"Please take {TOTAL:.2f} change")
elif PAYMENT + PAYMENT2 > 0.60 and choice.lower() == "crisps":    
    TOTAL = PAYMENT + PAYMENT2 - 0.60 
    print(f"Please take {TOTAL:.2f} change")
elif PAYMENT + PAYMENT2 > 0.80 and choice.lower() == "chocolate bar" or choice.lower()=="chocolatebar":   
    TOTAL = PAYMENT + PAYMENT2 - 0.80
    print(f"Please take {TOTAL:.2f} change")
elif PAYMENT + PAYMENT2 > 0.90 and choice.lower() == "bottled water" or choice.lower()=="bottledwater":  
    TOTAL = PAYMENT + PAYMENT2 - 0.90
    print(f"Please take {TOTAL:.2f} change")
else:
    print("No change.")

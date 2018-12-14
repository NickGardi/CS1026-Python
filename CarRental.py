# Nick Gardi 250868721 assignment1

# Setting up majority of the variables and inputs together and at the start to make it easier to locate them if I need to make a change
customerName = input("What is your name?")
customerAge = int(input("What is your age?"))
classCode = input("What is the classification code for the vehicle you rented?(B,D, or W)").upper()
daysRented = int(input("How many days did you rent the vehicle for?"))
odoBefore = int(input("What was the odometer reading at the start of the rental?"))
odoAfter = int(input("What was the odometer reading at the end of the rental?"))
kmDriven = (odoAfter - odoBefore)

# The $10 per day charge if the customer is under the age of 25
if customerAge > 25 :
    ageSurcharge = 0
else:
    ageSurcharge = 10*daysRented

# Defines the base charge and KM charge for vehicles with class code B
if classCode == "B" :
    baseCharge = 20 * daysRented
    kmCharge = kmDriven * 0.3

# Defines the base charge and KM charge for vehicles with class code D
if classCode == "D" :
    baseCharge = 50 * daysRented
    if (kmDriven / daysRented) <= 100 :
        kmCharge = 0
    else :
        kmCharge = (kmDriven - (100*daysRented)) * 0.3

# Defines the base charge and KM charge for vehicles with class code W
if classCode == "W":
    weeksRented = round((daysRented/7)+ 0.49)
    baseCharge = 200 * weeksRented
    if (kmDriven / weeksRented) <= 1000 :
        kmCharge = 0
    elif (kmDriven / weeksRented) > 1000 and (kmDriven / weeksRented) <= 2000 :
        kmCharge = 50 * weeksRented
    else :
        kmCharge = (100 * weeksRented) + (((kmDriven / weeksRented) - (2000 * weeksRented)) * 0.3)

# Printing out the customers information and final cost in the proper format "$0.00"
if classCode in ["B", "D", "W"] :
    totalCost = "%0.2f" % (baseCharge + kmCharge + ageSurcharge)
    print("Name:", customerName)
    print("Age:", customerAge)
    print("Vehicle classification code:", classCode)
    print("Number of days vehicle was rented:", daysRented)
    print("Odometer reading at start of rental:", odoBefore)
    print("Odometer reading at the end of rental:", odoAfter)
    print("Kilometres driven:", kmDriven)
    print(("Total cost of rental: ${}").format(totalCost))
else:
    print("", "Name:", customerName, "\n" , "Age:", customerAge, "\n" , "The vehicle classification code '{}' is not valid, please try again.".format(classCode))
# Validating the user input for the vehicle class code, and telling them to try again if their input is invalid

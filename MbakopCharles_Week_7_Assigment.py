# Submission Reuiremnts Name/Class/Date
def Myname(): 
    print("Charles Mbakop") 
    print("CMSC 105 7380")
    print("05/03/2024")
# Function that dispalys the stop locations and prices, iterating through stop and prices array to pull data
def displayMenu(stops, prices):
    print("\n\nBus Stops and Ticket Prices:")
    for i in range(len(stops)):
        print(f"Enter {i+1} for {stops[i]} (${prices[i]})")
# Here we collect passenger info 
def passengerInfo():
    passengers = []
    passengerCount = 0  # Initialize passenger count
    while True:
        if passengerCount >= 30:
            print("Maximum number of passengers reached.")
            break
        name = input("\nEnter passenger name or (type 'done' to exit): ")
        if name.lower() == 'done':
            break
        stop = int(input("Enter the stop location (1, 2, or 3): ")) - 1 
        while stop not in [0, 1, 2]:
            print("Invalid stop location. Enter 1, 2, or 3.")
            stop = int(input("Enter the stop location 1, 2, or 3: ")) - 1
        age = int(input("Enter passenger age: "))
        while age <= 12:
            print("Passenger must be older than 12.")
            age = int(input("Enter passenger age: "))
        passengers.append((name, stop, age))
        passengerCount += 1  # Increment passenger count
    return passengers

# Processes the passenger data, counts amount of passangers, in each age group, and calculates final ticket price
def calculateTotals(passengers, prices):
    numSeniors = 0
    numAdults = 0
    numChildren = 0
    stopPrices = [0, 0, 0] 

    for passenger in passengers:
        stop = passenger[1]
        age = passenger[2]
        if age >= 65:
            numSeniors += 1
        elif age >= 18:
            numAdults += 1
        else:
            numChildren += 1
        stopPrices[stop] += prices[stop]

    totalCombinedPrice = sum(stopPrices)
    return numSeniors, numAdults, numChildren, stopPrices, totalCombinedPrice

# This function dispays collected passenger data
def displayResults(numSeniors,numAdults, numChildren, stopPrices, totalCombinedPrice):
    print("\nPassenger Data:")
    print("Name\t\tStop\t\tAge")
    for passenger in passengers:
        print(f"{passenger[0]}\t\t{stops[passenger[1]]}\t\t{passenger[2]}")
    
    print("\nAnalysis:")
    print("Number of Seniors:", numSeniors)
    print("Number of Non-Senior Adults:", numAdults)
    print("Number of Non-Adults:", numChildren)
    print("Total Ticket Prices of Each Stop:")
    for i in range(len(stops)):
        print(f"{stops[i]}: ${stopPrices[i]}")
    print("Total Combined Ticket Prices:", totalCombinedPrice)
Myname()
# Sets stops and prices in array
stops = ["Norfolk", "Wilmington", "Miami"]
prices = [50, 40, 100]

# Display menu
displayMenu(stops, prices)

# Collect passenger information
passengers = passengerInfo()

# Calculate totals
numSeniors, numAdults, numChildren, stopPrices, totalCombinedPrice = calculateTotals(passengers, prices)

# Display Final results
displayResults(numSeniors, numAdults, numChildren, stopPrices, totalCombinedPrice)
    

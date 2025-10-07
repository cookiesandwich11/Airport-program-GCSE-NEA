import csv

airports = []
loop = True

def render_menu():
    print("Choose one of the following options:")
    print("1 Enter airport details")
    print("2 Enter flight details")
    print("3 Enter pricle plan and calculate profit")
    print("4 Clear data")
    print("5 Quit")
    choice = input("Enter a number corresponding to the option you want to select: ")
    return choice

#parse csv file
with open("Airports.txt") as f:
    reader = csv.reader(f)
    for row in reader:
        airports.append(row)
print(airports)


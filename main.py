import csv
import os
from tabulate import tabulate
airports = []
loop = True
msg = None
ovport = None
ukport = None
planetype = None
fclassnum = None
planechoice = None
sclassnum = None

planeinfo = {"1": ["Medium narrow body", 8, 2650, 180, 8],
             "2": ["Large narrow body", 7, 5600, 220, 10],
             "3": ["Medium wide body", 5, 4050, 406, 14]
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


    

def check_valid_port(portcode):
    valid_port = False
    for port in airports:
        if portcode in port:
            valid_port = True
    return valid_port

def get_port_index(portcode):
    for port in airports:
        if portcode in port:
            i = airports.index(port)
    return i

def get_port_name(portindex):
    return airports[portindex][1]

def get_port_distance_lpl(portindex):
    return int(airports[portindex][2])

def get_port_distance_boh(portindex):
    return int(airports[portindex][3])

def render_menu(msg):
    clear()
    if msg != None:
        print(msg)
    print("Choose one of the following options:")
    print("1 Enter airport details")
    print("2 Enter flight details")
    print("3 Enter pricle plan and calculate profit")
    print("4 Clear data")
    print("5 Quit")
    choice = input("Enter a number corresponding to the option you want to select: ")
    msg = ""
    return choice

def choose_airports():
    msg = "Airport Details selected!"
    ovport = None
    clear()
    ukport = input("Please input the three letter code for a UK airport: ")
    if ukport != "LPL" and ukport != "BOH":
        msg = "Invalid input"
    else:
        ovport = input("Please input the three letter code for an overseas airport: ")
        if check_valid_port(ovport):
            print("Valid")
        else:
            msg = "Invalid input"
    return ukport, ovport, msg

def choose_flight():
    clear()
    print("Please select a type of aircraft:")
    print("1 Medium narrow body")
    print("2 Large narrow body")
    print("3 Medium wide body")
    planechoice = input("Select a plane type with the corresponding number: ")
    if planechoice != "1" and planechoice != "2" and planechoice != "3":
        msg = "Invalid input"
    else:
        clear()
        print(f"Selected plane: {planeinfo[planechoice][0]} \nRunning cost per 100km: {planeinfo[planechoice][1]} \nMaximum flight range: {planeinfo[planechoice][2]} \nCapacity if all seats are standard class: {planeinfo[planechoice][3]} \nMinimum number of first class seats: {planeinfo[planechoice][4]}")
        fclassnum = int(input("How many first class seats are on the aircraft? "))
        if fclassnum != 0:
            if fclassnum < planeinfo[planechoice][4]:
                planechoice = None
                fclassnum = None
                msg = "Too few first class seats"
            elif fclassnum > planeinfo[planechoice][3] * 0.5:
                planechoice = None
                fclassnum = None
                msg = "Too many first class seats"
            else:
                msg = "Plane details selected!"
    return planechoice, fclassnum, msg

def calculate(planechoice, distance, fclassnum, ukport, ovport):
    clear()
    sclassprice = int(input("How much does a standard class seat cost? "))
    fclassprice = int(input("How much does a first class seat cost? "))
    sclassnum = planeinfo[planechoice][3]-(fclassnum*2)
    costperseat = planeinfo[planechoice][1] * distance/100
    cost = costperseat * (fclassnum+sclassnum)
    income = (fclassnum * fclassprice) + (sclassnum * sclassprice)
    profit = income - cost
    ukportname = "Liverpool John Lennon" if ukport == "LPL" else "Bournmouth International Airport"
    table = tabulate([["UK airport", ukportname], ["Overseas airport",get_port_name(get_port_index(ovport))], 
                    ["Distance", f"{distance}km"], 
                    ["Type of aircraft", planeinfo[planechoice][0]], 
                    ["Maximum flight range", f"{planeinfo[planechoice][2]}km"], 
                    ["Running cost per seat per 100km", f"£{planeinfo[planechoice][1]}"], 
                    ["Capacity if all seats are standard class", planeinfo[planechoice][3]],
                    ["Number of first class seats", fclassnum],
                    ["Number of standard class seats", sclassnum],
                    ["Price of a standard class seat", f"£{sclassprice}"],
                    ["Price of a first class seat", f"£{fclassprice}"],
                    ["Flight cost per seat", f"£{costperseat}"],
                    ["Flight cost", f"£{cost}"],
                    ["Flight income", f"£{income}"],
                    ["Flight profit", f"£{profit}"]
                       ], tablefmt="simple_grid")
    clear()
    print(table)
    input("\nPress enter to continue")



#parse csv file
with open("Airports.txt") as f:
    reader = csv.reader(f)
    for row in reader:
        airports.append(row)
print(airports)

while loop:
    mode = render_menu(msg)
    if mode == "1":
        ukport, ovport, msg = choose_airports()
    elif mode == "2":
        planechoice, fclassnum, msg = choose_flight()
    elif mode =="3":
        if ukport == None or ovport == None:
            msg = "Select the airports first"
        elif planechoice == None or fclassnum == None:
            msg = "Select the plane details first"
        else:
            if ukport == "LPL":
                if planeinfo[planechoice][2] < int(get_port_distance_lpl(get_port_index(ovport))):
                    msg = "The selected plane cannot travel that far."
                else:
                    calculate(planechoice, get_port_distance_lpl(get_port_index(ovport)), fclassnum, ukport, ovport)
            elif ukport == "BOH":
                if planeinfo[planechoice][2] < int(get_port_distance_boh(get_port_index(ovport))):
                    msg = "The selected plane cannot travel that far."
                else:
                    calculate(planechoice, get_port_distance_boh(get_port_index(ovport)), fclassnum, ukport, ovport)    
                    pass
    elif mode == "4":
        ovport = None
        ukport = None
        planetype = None
        fclassnum = None
        sclassnum = None
        planechoice = None
        msg = "Data has been cleared!"
    elif mode == "5":
        loop = False
    else:
        msg = "Invalid input"
clear()
print("Thank you for using Airport Cost Calculator 1.0")
#print(f"{ukport}, {ovport}, {planechoice}, {fclassnum}")
import csv
import os
airports = []
loop = True
msg = ""
ovport = ""
ukport = ""

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



def render_menu(msg):
    clear()
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
    msg = ""
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
    print("Please select a type of aircraft:")
    print("1 Medium narrow body")
    print("2 Large narrow body")
    print("3 Medium wide body")


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
        pass
    elif mode =="3":
        pass
    elif mode == "4":
        pass
    elif mode == "5":
        loop = False
    else:
        msg = "Invalid input"
clear()
print("Thank you for using Airport Cost Calculator 1.0")
print(f"{ukport}, {ovport}")

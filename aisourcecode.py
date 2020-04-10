import time
from termcolor import colored
localtime = time.asctime( time.localtime(time.time()) )

print(colored("\t\tWelcome to  parking system",'green',attrs=['bold']))
car = input(colored("Enter Car price for parking:",'blue'))
car: int = int(car)
bike = input(colored("Enter Bike price for parking: ",'blue'))
bike = int(bike)
truck = input(colored("Enter Truck price for parking: ",'blue'))
truck = int(truck)
bicycle = input(colored("Enter Bicycle price for parking: ",'blue'))
bicycle = int(bicycle)
bus = input(colored("Enter Bus price for parking: ",'blue'))
bus = int(bus)
maxx = input( colored("Enter Maximum Parking Slots: ", "grey" ) )
print('\n******')
maxx = int(maxx)
total = 0
tcar = pcar = tbike = pbike = ttruck = ptruck = tbicycle = pbicycle = tbus = pbus = tslot = 0
tslot = maxx
while maxx:
    print(colored(f'Total Slots are {tslot}\t\tFree Slots are {maxx}\n','magenta'))
    vehicle = input(
        "which vehile you want to park?\nEnter 1 for Car\nEnter 2 for Bike\nEnter 3 for Truck\nEnter 4 for Bicycle\nEnter 5 for Bus\nEnter 6 to view record \nEnter 7 to delete record\n")
    print('\n*****')
    vehicle: int = int(vehicle)
    if vehicle == 1:
        total += car
        tcar += 1
        pcar += car
        print("         ", localtime)
        z  = 0
        sum=z+1

        print( "            ", "Your slot number is", str( sum ) + 'a' )



        print(" ", "            ", colored("please take right", 'red', attrs=['bold','concealed', 'blink']))
    elif vehicle == 2:
        total += bike
        tbike += 1
        pbike += bike
        print("         ", localtime)
        z = 0
        sum = z + 1

        print( "            ", "Your slot number is", str( sum ) + 'b' )

        print("         ", " ", colored("please take right", 'red', attrs=['bold','concealed', 'blink']))

    elif vehicle == 3:
        total += truck
        ttruck += 1
        ptruck += truck
        print("         ", localtime)
        z = 0
        sum = z + 1

        print( "            ", "Your slot number is", str( sum ) + 'c' )



        print("         ", " ", colored("please take right", 'red', attrs=['bold','concealed', 'blink']))

    elif vehicle == 4:
        total += bicycle
        tbicycle += 1
        pbicycle += bicycle
        print("         ", localtime)
        z = 0
        sum = z + 1

        print( "            ", "Your slot number is", str( sum ) + 'd' )
        print("         ", " ", colored("please take right", 'red', attrs=['bold','concealed', 'blink']))

    elif vehicle == 5:
        total += bus
        tbus += 1
        pbus += bus
        print("         ", localtime)
        z = 0
        sum = z + 1

        print( "            ", "Your slot number is", str( sum ) + 'e' )
        print("         ", " ", colored("please take right", 'red', attrs=['bold','concealed', 'blink']))

    elif vehicle == 6:
        print(
            f'Total Cars:{tcar}\t\tCars total price:{pcar}\nTotal Bikes{tbike}\t\tBikes total price:{pbike}\nTotal trucks:{ttruck}\t\tTrucks total price:{ptruck}\nTotal Bicycle:{tbicycle}\t\tBicycles total price:{pbicycle}\nTotal Bus:{tbus}\t\tBusses total price:{pbus}\n')
        print('\n******')
        maxx += 1
        print("             ", colored("Bye!", 'red', attrs=['reverse', 'blink']))
    elif vehicle == 7:
        tcar = pcar = tbike = pbike = ttruck = ptruck = tbicycle = pbicycle = tbus = pbus = 0
        maxx = tslot + 1
    else:
        print("\n", "       ", colored( 'You\'ve entered wrong slot number', 'red', attrs=[ 'reverse', 'blink' ] ) )
    maxx -= 1
    if maxx == 0:
        print('Slots are Full')
print(f'total price for parking vehicles is {total}')
from models import Driver ,Passenger


D = Driver("Marcus",33232,"blue",23,"M")
P = Passenger("Ama",12,"F")

"""matching logic behind pairing each driver 
to a respective 
passenger going to the same
#direction"""

def matching_logic():
    for passenger_trip in P.trips_passenger:#checks every index in list(trips_passenger)
        for driver_trip in D.trips:#checks every index in list(trips)
            if (

                passenger_trip["start"] == driver_trip["start"] #finds key-"start" checks the value:actual starting point
                and
                passenger_trip["stop"] == driver_trip["stop"]#finds key-"start" checks the value:actual starting point
                
            ):
                print(f"\nMatch found: {passenger_trip}")


t1 = P.create_trip("Accra","togo")
t2 = P.create_trip("Abeka","Lapaz")


trip2 = D.create_trip("Accra","togo")
trip3 = D.create_trip("Togo","Iran")




def main():
    print("=== Ride App Simulation ===")

    # create driver
    driver = Driver("Marcus", "GR-2398", "blue", 23, "female")

    # create passenger
    passenger = Passenger("Marcus", 23, "Male")

    while True:
        print("\n1. Driver create trip")
        print("2. Passenger create trip")
        print("3. View driver trips")
        print("4. View passenger trips")
        print("5. Search for match")
        print("6. Exit")

        choice = input("Select option: ")

        if choice == "1":
            start = input("Enter start location: ")
            stop = input("Enter destination: ")
            print(driver.create_trip(start, stop))

        elif choice == "2":
            start = input("Enter start location: ")
            stop = input("Enter destination: ")
            print(passenger.create_trip(start, stop))

        elif choice == "3":
            print("Driver Trips:", driver.view_trips())

        elif choice == "4":
            print("Passenger Trips:", passenger.view_trips())

        elif choice == "5":
            print("Searching for a match...")
            matching_logic()
        elif choice == "6":
            print("Exiting app")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
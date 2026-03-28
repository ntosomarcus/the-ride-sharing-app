
class Driver:
    #initialize the parameters needed when a driver account is created
    def __init__(self, driver_name, car_number, car_color, age, sex):
        self.driver_name = driver_name
        self.car_number = car_number
        self.car_color = car_color
        self.age = age
        self.sex = sex
        
        #keep the drivers INFORMATION(dictiontary)
        self.driver_ID = {
            self.driver_name:
            {
                "car_no": self.car_number,
                "car_color": self.car_color,
                "age": self.age,
                "sex": self.sex
            }}
        

        self.trips = [] # stores the trips history for the Driver(tracking the trips made)

#method for creating a trip; having a starting point and a stop(destination)
    def create_trip(self, drivers_start, drivers_stop):
        if isinstance(drivers_start, str) and isinstance(drivers_stop, str):#to make sure input is string
            trip = {
                "start": drivers_start,
                "stop": drivers_stop
            }
            self.trips.append(trip) #appends trip(dictionary) in list self.trips

            return f"Trip added: {drivers_start} --> {drivers_stop}"
        else:
            return "Enter valid starting point and destination"

    def view_trips(self):
        return(self.trips) 
    


class Passenger:
    ##initialize the parameters needed when a passenger account is created
    def __init__(self,passenger_name,age,sex):
        self.passenger_name = passenger_name
        self.age = age
        self.sex = sex
        
        self.passenger_ID =  {
                "name": self.passenger_name,
                "age": self.age,
                "sex": self.sex
            }
        # varaible to store HISTORY of trips
        self.trips_passenger = []

    #method for creating a trip; having a starting point and a stop(destination)
    def create_trip(self, passenger_start, passenger_stop):
        if isinstance(passenger_start, str) and isinstance(passenger_stop, str):
            trip = {
                "start": passenger_start,
                "stop": passenger_stop
            }
            self.trips_passenger.append(trip)

            return f"Trip added: {passenger_start} → {passenger_stop}"
        else:
            return "Enter valid starting point and destination"
    
    def view_trips(self): # to view trip history
        return(self.trips_passenger)
    

    



P = Passenger("Marcus",23,"Male")
t1 = P.create_trip("USA","Iran")
t2 = P.create_trip("Abeka","Lapaz")


    
D = Driver("Marcus","GR-2398","blue",23,"female")
trip1 = D.create_trip("Accra","Kumasi")




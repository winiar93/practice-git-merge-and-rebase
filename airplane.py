class Plane:
    def __init__(self, model, capacity, airline):
        self.model = model
        self.capacity = capacity
        self.airline = airline
        self.passengers = []

    def get_model(self):
        return self.model

    def get_capacity(self):
        return self.capacity

    def get_airline(self):
        return self.airline

    def get_something(self):
        return len(self.passengers)

    def book_seat(self, passenger_name):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger_name)
            print(f"Seat booked for {passenger_name} on {self.airline}'s {self.model}.")
        else:
            print("Sorry, the plane is already full.")
    def change_airline_name(self, new_airline_name):
        self.airline = new_airline_name

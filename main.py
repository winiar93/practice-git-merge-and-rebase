from airplane import Plane


plane1 = Plane("Boeing 747", 6, "Rebase Airlines")

# Accessing plane information using methods
print("Model:", plane1.get_model())
print("Capacity:", plane1.get_capacity())

# Booking seats
plane1.book_seat("Alice")
plane1.book_seat("Bob")
plane1.book_seat("Charlie")
plane1.book_seat("Dave")
plane1.book_seat("ekiM")
plane1.book_seat(213)
plane1.book_seat("Piter")

plane1.change_airline_name('Merge airlines')

print(plane1.get_airline())
print(plane1.get_passengers_number())

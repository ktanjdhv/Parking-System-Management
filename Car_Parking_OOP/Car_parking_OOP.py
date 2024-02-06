class Reservation:
    def __init__(self, user_id, duration):
        self.user_id = user_id
        self.duration = duration

class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.available_slots = capacity
        self.reservations = {}
        self.user_counter = 1  # Initialize user counter

    def generate_user_id(self):
        user_id = f"User{self.user_counter}"  # Generate user ID based on counter
        self.user_counter += 1  # Increment counter for the next user
        return user_id

    def check_availability(self):
        return self.available_slots

    def make_reservation(self, duration):
        if self.available_slots == 0:
            return "Parking lot is full"
        else:
            user_id = self.generate_user_id()  # Generate unique user ID
            self.reservations[user_id] = Reservation(user_id, duration)
            self.available_slots -= 1
            return "Reservation successful. Your user ID is: " + user_id

    def cancel_reservation(self, user_id):
        if user_id in self.reservations:
            del self.reservations[user_id]
            self.available_slots += 1
            return "Reservation canceled"
        else:
            return "No reservation found for the user"

def main():
    parking_lot = ParkingLot(capacity=5)  # Initialize parking lot with 5 slots
    print("Welcome to Parking Management System")

    while True:
        print("\n1. Check Availability")
        print("2. Make Reservation")
        print("3. Cancel Reservation")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Available slots:", parking_lot.check_availability())
        elif choice == '2':
            duration = int(input("Enter duration of reservation (hours): "))
            print(parking_lot.make_reservation(duration))
        elif choice == '3':
            user_id = input("Enter user ID: ")
            print(parking_lot.cancel_reservation(user_id))
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

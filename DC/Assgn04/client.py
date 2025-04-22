import Pyro4

def main():
    uri = input("Enter server URI: ")  # e.g., PYRO:obj_abc123@localhost:port
    hotel = Pyro4.Proxy(uri)

    while True:
        print("\n1. Book Room\n2. Cancel Booking\n3. Exit")
        choice = input("Select option: ")

        if choice == '1':
            name = input("Enter guest name: ")
            print(hotel.book_room(name))
        elif choice == '2':
            name = input("Enter guest name: ")
            print(hotel.cancel_booking(name))
        elif choice == '3':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
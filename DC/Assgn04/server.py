import Pyro4

@Pyro4.expose
class HotelBookingSystem:
    def __init__(self):
        self.rooms = {}    #guest room no
        self.next_room = 1

    def book_room(self, guest_name):
        if guest_name in self.rooms:
            return f"{guest_name} already has a room {self.rooms[guest_name]}"
        
        self.rooms[guest_name] = self.next_room
        self.next_room += 1

        return f"Room {self.rooms[guest_name]} booked for {guest_name}"
    
    def cancel_booking (self, guest_name):
        if guest_name in self.rooms:
            room = self.rooms.pop(guest_name)
            return f"Bookin for {guest_name} cancelled. Room {room} is now available."
        else:
            return f"{guest_name} does not have a booking."
        
def main():
    # Create a Pyro4 daemon
    daemon = Pyro4.Daemon()
    uri = daemon.register(HotelBookingSystem)
    print("Server is running! URI: ", uri)
    daemon.requestLoop()

if __name__ == "__main__":
    main()
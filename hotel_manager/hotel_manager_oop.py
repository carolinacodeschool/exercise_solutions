class Room:
    def __init__(self, room_number, guests):
        self.room_number = room_number
        self.guests = guests

    def __str__(self):
        return f"Room {self.room_number}: {', '.join(self.guests)}"


class Floor:
    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.rooms = {}

    def check_in(self, room_number, guests):
        if room_number not in self.rooms:
            self.rooms[room_number] = Room(room_number, guests)
        else:
            print(f"Room {room_number} already occupied.")

    def __str__(self):
        return f"Floor {self.floor_number}: {', '.join(str(room) for room in self.rooms.values())}"


class Hotel:
    def __init__(self):
        self.floors = {}

    def check_in(self):
        floor_num = int(input("Which floor? "))
        room_num = int(input("Which room number? "))
        number_of_guests = int(input("How many in your party? "))
        names_of_guests = []

        for person in range(number_of_guests):
            name = input("Name of person #%d: " % (person + 1))
            names_of_guests.append(name)

        if floor_num not in self.floors:
            self.floors[floor_num] = Floor(floor_num)

        self.floors[floor_num].check_in(room_num, names_of_guests)

        self.show_occupancy()

    def show_occupancy(self):
        for floor in self.floors:
            print(f"{self.floors[floor]}")



hotel = Hotel()
hotel.floors = {
    1: Floor(1),
    2: Floor(2),
    3: Floor(3)
}
hotel.floors[1].check_in(101, ['George Jefferson', 'Wheezy Jefferson'])
hotel.floors[2].check_in(237, ['Jack Torrance', 'Wendy Torrance'])
hotel.floors[3].check_in(333, ['Neo', 'Trinity', 'Morpheus'])

hotel.check_in()

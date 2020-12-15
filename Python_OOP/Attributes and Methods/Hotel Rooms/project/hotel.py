class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    def get_room_by_number(self, room_number):
        return [room for room in self.rooms if room.number == room_number][0]

    @classmethod
    def from_stars(cls, stars_count):
        name = f'{stars_count} stars Hotel'
        return Hotel(name)

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = self.get_room_by_number(room_number)
        result = room.take_room(people)
        if result:
            return result
        self.guests += people

    def free_room(self, room_number):
        room = self.get_room_by_number(room_number)
        guests_to_remove = room.guests
        result = room.free_room()
        if result:
            return result
        self.guests -= guests_to_remove

    def print_status(self):
        rooms_free = ', '.join(str(room.number) for room in self.rooms if room.is_taken)
        rooms_taken = ', '.join(str(room.number) for room in self.rooms if not room.is_taken)

        message = f'''Hotel {self.name} has {self.guests} total guests
Free rooms: {rooms_free}
Taken rooms: {rooms_taken}'''
        print(message)

from project.hotel import Hotel
from project.room import Room

hotel = Hotel.from_stars(5)

first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)

hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)

hotel.take_room(1, 4)
hotel.take_room(1, 2)
hotel.take_room(3, 1)
hotel.take_room(3, 1)

hotel.print_status()


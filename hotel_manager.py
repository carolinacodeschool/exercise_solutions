hotel = {
    1: {
        101: ['George Jefferson', 'Wheezy Jefferson'],
    },
    2: {
        237: ['Jack Torrance', 'Wendy Torrance'],
    },
    3: {
        333: ['Neo', 'Trinity', 'Morpheus']
    }
}


def check_in():
    floor_num = int(input("Which floor? "))
    room_num = int(input("Which room number? "))
    number_of_guests = int(input("How many in your party? "))
    names_of_guests = []

    for person in range(number_of_guests):
        name = input("Name of person #%d: " % (person + 1))
        names_of_guests.append(name)

    hotel[floor_num] = {room_num: names_of_guests}
    print(hotel)
    return hotel


def check_out():
    floor_num = int(input("What floor were you on?"))
    room_num = int(input("What was your room number? "))

    del hotel[floor_num][room_num]
    print(hotel)
    return hotel


def check_in_or_out(response):
    if response == 'in':
        check_in()
        return True
    elif response == 'out':
        check_out()
        return False
    else:
        print('Invalid input, please answer either \'in\' or \'out\'')
        return True


concierge = True
while concierge:
    in_or_out = input("Are you checking, in or out? ").lower()
    concierge = check_in_or_out(in_or_out)

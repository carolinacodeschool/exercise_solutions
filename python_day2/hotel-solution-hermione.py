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

def get_room_and_floor():
    floor = None
    room = None
    while floor == None:
        floor = int(input('What floor number? '))
        if floor != None:
            break
        else:
            print('please enter a valid floor number')
    while room == None:
        room = int(input("What room number? "))
        if room != None:
            break
        else:
            print("Enter a valid room number, please")
    return floor,room

def get_occupants():
    occupants = None
    names = []
    while occupants == None:
        occupants = int(input("How many people are staying in the room?"))
        if occupants != None:
            if occupants > 6:
                print("You can't have more than 6 people in one room - FIRE CODE!")
                occupants = None
        else:
            print("please type a number")
    for i in range(occupants):
        name = input("What is occupant #%d's name? " % (i+1,))
        names.append(name)
    return(occupants,names)

def room_empty(floor,room):
    if floor in hotel.keys():        #check that the floor exists (1,2,3 currently)
        if room in hotel[floor].keys():  #check if that room is occupied
            return False
        else:
            return True        #room doesn't exist
    else:
        return True            #floor doesn't exist
    return False                #something else wrong

def clear_room(floor,room):
    if floor in hotel.keys():        #check that the floor exists (1,2,3 currently)
        if room in hotel[floor].keys():  #check if that room is occupied
            del hotel[floor][room]
            return True
        else:
            print("That room doesn't exist.  Please start over")
            return False
    else:
        print("That floor doesn't exist.  Please start over")
        return False

def check_in(location,people):      #only called with valid_room
    #if the floor doesn't exist yet, create it
    if location[0] in hotel.keys():     #floor exists
        hotel[location[0]][location[1]] = people[1]     #create room
    else:
        hotel[location[0]] = {}         #create floor
        hotel[location[0]][location[1]] = people[1]     #create room
    return True     #passed

def check_in_or_out():
    checkinout = None
    while checkinout == None:
        checkinout = input("Are you checking in our out? ").lower()
        if checkinout in ('in','out'):
            return checkinout
        else:
            print("Please type 'in' or 'out'")
            checkinout = None
    return None    #it shuld never get here

run = True

while run:          #control-c to exit.  it will continue to run
    checkinout = check_in_or_out()      #are they checking in or out
    valid_room = False
    while valid_room == False:
        location = get_room_and_floor()     #returns(floor,room)
        valid_room = room_empty(location[0],location[1])
        if valid_room and checkinout == 'in':
            people = get_occupants()
            checked_in = check_in(location,people)  #returns True of False
            # print(people)
        elif valid_room and checkinout == 'out':
            print("No one is in that room.  Please try again")
        elif valid_room == False and checkinout == 'in':
            print("That room is occupied.  Please select a different one")
        elif valid_room == False and checkinout == 'out':       #checkinout = 'out'
            valid_room = clear_room(location[0],location[1])    # True or False
        else:
            break
    #pprint.pprint(hotel)
    print(hotel)

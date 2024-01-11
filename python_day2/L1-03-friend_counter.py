ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
        {
            'name': 'Jasmine',
            'email': 'jasmine@yahoo.com',
            'interests': ['photography', 'tennis']
        },
        {
            'name': 'Jan',
            'email': 'jan@hotmail.com',
            'interests': ['movies', 'tv']
        }
    ]
}

## Crystal Atkinson solution

def countFriends(dictionary, key, new_key):
    count = 0
    for friends in dictionary[key]:
        count += 1
    # print(friends_count)
    new_dictionary = dictionary.copy()
    new_dictionary[new_key] = count
    print(new_dictionary)
    return new_dictionary


countFriends(ramit, 'friends', 'friends_count')
countFriends(ramit, "interests", "interests_count")

## Veronica solution:

def countFriends2(someDictionary):
    newDictionary = someDictionary.copy()
    newDictionary["friends_count"] = len(newDictionary['friends'])
    return newDictionary

countFriends2(ramit)
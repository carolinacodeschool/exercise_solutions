# Garden simulator
#
# Create the following classes to simulate a garden:
#     - `Tree` - its shade decreases water loss by `2`
#     - `Gnome` - each instance adds a `5%` chance of rain
#     - `Woodchuck` - creates a `5%` chance of a `Tree` disappearing
#     - `Garden` - has separate lists for instances of `Tree`, `Gnome`, and `Woodchuck`
#
#   Create a main `while` loop that runs your simulator.
#   During each turn, your `Garden` may experience rain, or may have a `Woodchuck` move in.
#   For each of its lists, tally up the various percents that an event will occur and
#   use the built-in `random` module to decide what happens during that turn.
#   (See https://docs.python.org/3.5/library/random.html for more information)
#
#   Every 10th turn, you have a random chance of earning another `Tree` or `Gnome`.
#
#   The simulation ends if you reach `10` `Tree` instances.
#
#   Adding more classes
#
#     - `FruitTree` (a subclass of `Tree`) - after its `water_level` reaches `100`, it should increase its `fruit` attribute by `1`
#     - `Squirrel` - each one adds a 5% chance that your `fruit` levels will decrease by `1`.
#
# The simulation ends if your `FruitTree` instances are able produce `10` fruits.

import random, time

class Tree:
    def __init__(self, type_of_tree = "Oak"):
        self.type_of_tree = type_of_tree
        return

    def throw_shade(self, garden):
        garden.water += 2


class Gnome:
    def __init__(self):
        return

    def rain(self, garden, probability=0.2):
        if random.random() < probability:
            garden.water += 1


class Woodchuck:
    def __init__(self):
        return

    def eat_tree(self, tree, garden, probability=0.2):
        if random.random() < probability:
            garden.trees.remove(tree)


class Garden:
    def __init__(self, trees=[], gnomes=[], woodchucks=[], water=5):
        self.trees = trees
        self.gnomes = gnomes
        self.woodchucks = woodchucks
        self.water = water

    def __str__(self):
        num_of_trees = len(self.trees)
        num_of_gnomes = len(self.gnomes)
        return f"The garden has {num_of_trees} trees, {'needs' if self.water > 5 else 'has plenty'} water. There {'are' if num_of_gnomes > 1 else 'is'} {num_of_gnomes} gnome{'s'*(num_of_gnomes!= 1)}."

    def grow_tree(self, tree):
        self.trees.append(tree)

    def add_gnome(self, gnome):
        self.gnomes.append(gnome)

    def woodchuck_moves_in(self, woodchuck):
        self.woodchucks.append(woodchuck)


my_garden = Garden(["a", "b", "c", "d", "e", "f"], ["Gnomey"], [], 5)
counter = 0
probability = 0.5

while len(my_garden.trees) <= 10 and len(my_garden.trees) > 0:
    print(counter)
    counter += 1
    if counter <= 1:
        print('Welcome to the garden!')
    print(my_garden)

    oak = Tree('Oak')
    pine = Tree('Pine')
    time.sleep(1)

    if random.random() < probability:
        my_garden.woodchuck_moves_in("Chuckles")
    else:
        my_garden.water += 1
    if counter % 10 == 0:
        if random.random() < probability:
            print("Lo, a wild tree appears!")
            if random.randrange(2,8) % 2:
                my_garden.grow_tree(oak)
                print(f"{oak.type_of_tree} has been planted.")
            else:
                my_garden.grow_tree(pine)
                print(f"{pine.type_of_tree} has been planted.")
        else:
            print("HARK! A gnome!")
            my_garden.add_gnome('Sherlock Gnomes')

    print("---")
    print("Press 1 to continue working in the garden")
    print("Press any other key leave")
    print("---")
    user_choice = input()
    if user_choice == "1":
        pass
    else:
        print("👋 Goodbye")
        break

# Training Exercises

## Level 1

1. Overriding `__str__()` in `CuddlyPet`

    When you pass a `CuddlyPet` instance to the `print()` function, it uses the `Pet` version of the method.

    Override the definition of `__str__()` in `CuddlyPet` so that the return value includes the string `"Extra cuddly"`.

    :::details Solution

    To override the `Pet` version of `__str__()` so taht `CuddlyPet` has a custom version, add a `def __str__(self)` to `CuddlyPet`:

    ```py{15-20}
    class CuddlyPet(Pet):
        def __init__(self, name, fullness=50, hunger=5, cuddle_level=1):
            super().__init__(name, fullness, 100, hunger, 1)
            self.cuddle_level = cuddle_level

        def be_alive(self):
            self.fullness -= self.hunger
            self.happiness -= self.mopiness/2

        def cuddle(self, other_pet):
            # Super cuddle powers, activate!
            for i in range(self.cuddle_level):
                other_pet.get_love()

        def __str__(self):
            return """
    Extra Cuddly %s:
    Fullness: %d
    Happiness: %d
    """ % (self.name, self.fullness, self.happiness)
    ```
    :::

2. Using `super()` in `CuddlyPet.be_alive()`

    `CuddlyPet` has a custom version of `be_alive()`, but it's nearly identical to the definition in `Pet`.  The only difference is that we subtract `self.mopiness/2` from `self.happiness` for a `CuddlyPet`.

    If our Virtual Pets get more complex, we might add more lines to `be_alive()`. It would be tedious to update both versions of `be_alive()`.

    One solution is for `CuddlyPet` to call `Pet.be_alive()` and then increase its `self.happiness`.  Modify `CuddlyPet.be_alive()` so that it calls `super()` to invoke `Pet`'s version of `be_alive()`.

    :::details Solution

    ```py{7,8}
    class CuddlyPet(Pet):
        def __init__(self, name, fullness=50, hunger=5, cuddle_level=1):
            super().__init__(name, fullness, 100, hunger, 1)
            self.cuddle_level = cuddle_level

        def be_alive(self):
            super().be_alive()
            self.happiness += self.mopiness/2
    ```
    :::

### Level 2

1. Add a `Treat` class to your `Pet` simulator.

    When you give one of your `Pet` objects a treat, prompt the user to choose one of three kinds:

    - `ColdPizza`
    - `Bacon`
    - `VeganSnack`

    Create a class for each of these, and customize them so that they have differing effects on the `Pet` object's `fullness` and `happiness` levels.

    :::details Solution

    First, create a `treat.py` file with a `Treat` class. Give it a constructor that accepts arguments for setting the `yum` and `joy` attributes:

    ```py
    class Treat:
        def __init__(self, yum=10, joy=10):
            self.yum = yum
            self.joy = joy
    ```

    Create three subclasses of `Treat`, each passing in custom values for `yum` and `joy` using `super().__init()`:

    ```py
    class ColdPizza(Treat):
        def __init__(self):
            super().__init__(15, 20)

    class Bacon(Treat):
        def __init__(self):
            super().__init__(30, 30)

    class VeganSnack(Treat):
        def __init__(self):
            super().__init__(2, 1)
    ```

    Modify your `Pet` class so that it knows how to `eat_treat()`:

    ```py
    class Pet:
        #...
        def eat_treat(self, treat):
            self.fullness += treat.yum
            self.happiness += treat.joy
    ```

    Finally, modify your main program, adding imports and menu options for giving treats to your pets:

    ```py
    from pet import Pet, CuddlyPet
    from toy import Toy

    # Import your treats
    from treat import ColdPizza, Bacon, VeganSnack

    #...
    # Add a variable for the `treat_menu`
    adoption_menu = [
        "Pet",
        "Cuddly Pet"
    ]

    treat_menu = [
        "ColdPizza",
        "Bacon",
        "VeganSnack"
    ]

    #...
    # Add to the main menu:
            if choice == 6:
                # Pet levels naturally lower.
                for pet in pets:
                    pet.be_alive()
            if choice == 7:
                print("Please choose what type of treat:")
                treat_choice = get_user_choice(treat_menu)
                if treat_choice == 1:
                    for pet in pets:
                        pet.eat_treat(ColdPizza())
                if treat_choice == 2:
                    for pet in pets:
                        pet.eat_treat(Bacon())
                if treat_choice == 3:
                    for pet in pets:
                        pet.eat_treat(VeganSnack())


    ```

    :::

2. Create a `Menu` class for your `Pet` simulator.

    Create a `Menu` class that has the following attributes:

    - `prompt_text` - the text to show the user

    Add the following methods:

    - `get_choice()` - shows the user the `prompt_text` and converts their input to an `int`, prompting again if they enter an invalid value.

    Modify the `while` loop of your `Pet` simulator so that it uses a `Menu` instance to handle user interaction.

    For each additional prompt (such as choosing which kind of `Pet` subclass to adopt), use additional `Menu` instances.

    :::details Solution
    Start by creating a `menu.py` file with a `Menu` class. Define the `__init__()` so that it accepts `prompt_text` as an argument. Define `get_choice()` but leave it blank for now.

    ```py
    class Menu:
        def __init__(self, prompt_text):
            self.prompt_text = prompt_text

        def get_choice(self):
            pass

    ```

    The functions you called inside of your `while` loop can be moved to this class. They will need to be modified so that they accept the `self` argument. They also need to be modified to call each other using the `self.` prefix.

    In addition, the `choices_to_string()` method should use `self.prompt_text` instead of the hard-coded `"Please choose an option: "`

    ```py{11,17,20,22,29}
    class Menu:
        def __init__(self, prompt_text):
            self.prompt_text = prompt_text

        def get_choice(self):
            pass

        def print_menu_error(self):
            print("That was not a valid choice. Try again.\n\n\n")

        def choices_to_string(self, choice_list):
            choice_string = ""
            num = 1
            for choice in choice_list:
                choice_string += "%d: %s\n" % (num, choice)
                num += 1
            choice_string += self.prompt_text
            return choice_string

        def get_user_choice(self, choice_list):
            choice = -1
            choice_string = self.choices_to_string(choice_list)
            while choice == -1:
                try:
                    choice = int(input(choice_string))
                    if choice <= 0 or choice > len(choice_list):
                        raise ValueError
                except ValueError:
                    self.print_menu_error()
            return choice
    ```

    Update `get_choice()` so that it:

    - accepts a `choice_list`
    - calls `self.get_user_choice()` and passes it `choice_list`

    ```py
        def get_choice(self, choice_list):
            return self.get_user_choice(choice_list)
    ```

    Modify your main program so that it uses your new `Menu` class.

    ```py{4,10-12,15,18,41}
    from pet import Pet, CuddlyPet
    from toy import Toy
    from treat import ColdPizza, Bacon, VeganSnack
    from menu import Menu

    #...


    def main():
        app = Menu("Please choose an option: ")
        types = Menu("Please choose the type of pet: ")
        treats = Menu("Please choose a treat: ")

        while True:
            choice = app.get_choice(main_menu)
            if choice == 1:
                pet_name = input("What would you like to name your pet? ")
                type_choice = types.get_choice(adoption_menu)
                if type_choice == 1:
                    pets.append(Pet(pet_name))
                else:
                    pets.append(CuddlyPet(pet_name))
                print("You now have %d pets" % len(pets))
            if choice == 2:
                for pet in pets:
                    pet.get_love()
            if choice == 3:
                for pet in pets:
                    pet.eat_food()
            if choice == 4:
                for pet in pets:
                    print(pet)
            if choice == 5:
                for pet in pets:
                    pet.get_toy(Toy())
            if choice == 6:
                # Pet levels naturally lower.
                for pet in pets:
                    pet.be_alive()
            if choice == 7:
                treat_choice = treats.get_choice(treat_menu)
                if treat_choice == 1:
                    for pet in pets:
                        pet.eat_treat(ColdPizza())
                if treat_choice == 2:
                    for pet in pets:
                        pet.eat_treat(Bacon())
                if treat_choice == 3:
                    for pet in pets:
                        pet.eat_treat(VeganSnack())

    ```


    Bonus: the code could be improved further. Instead of passing the `choice_list` to `get_choice()`, it could be passed into the constructor:

    ```py
        def __init__(self, prompt_text, choice_list):
            self.prompt_text = prompt_text
            self.choice_list = choice_list

        def get_choice(self):
            return self.get_user_choice(self.choice_list)
    ```

    Your `main()` function changes to:

    ```py{2-4,7,10,33}
    def main():
        app = Menu("Please choose an option: ", main_menu)
        types = Menu("Please choose the type of pet: ", adoption_menu)
        treats = Menu("Please choose a treat: ", treat_menu)

        while True:
            choice = app.get_choice()
            if choice == 1:
                pet_name = input("What would you like to name your pet? ")
                type_choice = types.get_choice()
                if type_choice == 1:
                    pets.append(Pet(pet_name))
                else:
                    pets.append(CuddlyPet(pet_name))
                print("You now have %d pets" % len(pets))
            if choice == 2:
                for pet in pets:
                    pet.get_love()
            if choice == 3:
                for pet in pets:
                    pet.eat_food()
            if choice == 4:
                for pet in pets:
                    print(pet)
            if choice == 5:
                for pet in pets:
                    pet.get_toy(Toy())
            if choice == 6:
                # Pet levels naturally lower.
                for pet in pets:
                    pet.be_alive()
            if choice == 7:
                treat_choice = treats.get_choice()
                if treat_choice == 1:
                    for pet in pets:
                        pet.eat_treat(ColdPizza())
                if treat_choice == 2:
                    for pet in pets:
                        pet.eat_treat(Bacon())
                if treat_choice == 3:
                    for pet in pets:
                        pet.eat_treat(VeganSnack())

    ```

    :::

### Large

1. Garden simulator

    Create the following classes to simulate a garden:

    - `Tree` - its shade decreases water loss by `2`
    - `Gnome` - each instance adds a `5%` chance of rain
    - `Woodchuck` - creates a `5%` chance of a `Tree` disappearing
    - `Garden` - has separate lists for instances of `Tree`, `Gnome`, and `Woodchuck`

    Create a main `while` loop that runs your simulator. During each turn, your `Garden` may experience rain, or may have a `Woodchuck` move in. For each of its lists, tally up the various percents that an event will occur and use the built-in `random` module to decide what happens during that turn. (See https://docs.python.org/3.5/library/random.html for more information)

    Every 10th turn, you have a random chance of earning another `Tree` or `Gnome`.

    The simulation ends if you reach `10` `Tree` instances.

2. Adding more classes

    - `FruitTree` (a subclass of `Tree`) - after its `water_level` reaches `100`, it should increase its `fruit` attribute by `1`
    - `Squirrel` - each one adds a 5% chance that your `fruit` levels will decrease by `1`.

    The simulation ends if your `FruitTree` instances are able produce `10` fruits.

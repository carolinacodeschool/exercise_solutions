import random
user_input = int(input("Guess a number between 5-50: "))
magic_number = random.randint(5, 50)

print(magic_number)

# if user_input == magic_number:
#     print("ARE YOU A MIND READER!?!?")
# elif user_input > 50:
#     print("Guess was too high!")
# elif user_input < 5:
#     print("Guess was too low")
# else:
#     print("Sorry. Try again.")

if user_input == magic_number:
    print("ARE YOU A MIND READER!?!?!")
elif (user_input < 5) or (user_input > 50):
    print("YOU'RE OUT OF RANGE!!")
else:
    print("Sorry. Try again.")
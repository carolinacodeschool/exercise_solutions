# Celsius to Fahrenheit
# The formula to convert a temperature from Celsius to Fahrenheit is:
# `F = (C * 9/5) + 32`
# Write a function that takes a temperature in Celsius, converts it Fahrenheit, and returns the value.

user_input = int(input("Enter a temperature in Celsius: "))

def convert_temp_f(celcius):
    return (celcius * 9/5) + 32

farhrenheit = convert_temp_f(user_input)
print(farhrenheit)


# Fahrenheit to Celsius
# The formula to convert a temperature from Fahrenheit to Celsius is:
# `C = (F - 32) * 5/9`
# Write a function that takes a temperature in Fahrenheit, converts it to Celsius, and returns the value.

user_input_2 = int(input("Enter a temperature in Fahrenheit"))

def convert_temp_c(fahrenheit):
    return (fahrenheit - 32 ) * 5/9

celcius = convert_temp_c(user_input_2)
print(celcius)
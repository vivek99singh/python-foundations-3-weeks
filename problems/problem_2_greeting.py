"""
A program that takes as input:
    - your name
    - a weather condition
    - high temperature
    - low temperature

And prints a greeting:
    Good morning, {name}!
    Today is going to be {condition}.
    High: {high_c} °C ({high_f} °F)
    Low: {low_c} °C ({low_f} °F)

Scenario 2 practice
"""
## Get some input from the user
name = input("What is your name? ")
weather = input("What is the weather like? ")
temp_h_c = float(input("What is the high temp? "))
temp_l_c = float(input("What is the low temp? "))
## Convert the temperatures
temp_f_h = ((temp_h_c) * (9/5)) +32
temp_f_l = ((temp_l_c) * (9/5)) +32
## Print the greeting
print('Good Morning ' + name + ' !')
print('Today is going to be ' + weather + '.')
print(f'High: {temp_h_c} °C , {temp_f_h} °F')  # Updated
print(f'Low: {temp_l_c} °C , {temp_f_l} °F')     # Updated






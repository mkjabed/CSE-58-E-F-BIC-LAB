
# **You Do 6:** Create a variable called `temperature`. 
# Write an if/elif/else block that prints "It is hot" if the temperature is above 30, 
# "It is nice" if it's between 20 and 30, and "It is cold" if it is below 20.

temperature = int(input("Enter the temperature? "))

if temperature > 30:
    print("It is hot")
elif temperature >= 20 and temperature <= 30:
    print("It is nice")
elif temperature < 20: 
    print("It is cold")
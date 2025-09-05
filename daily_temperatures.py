
import numpy as np

print("\nThis is a 7 day temperature recorder. These are the current recorded temperatues: \n")

seven_day_temperatures = np.array([18, 21, 23, 19, 15, 17, 20])

print("Array:", seven_day_temperatures)

print("\n==Temperatures==")
print("Monday:", seven_day_temperatures[0])
print("Tuesday:", seven_day_temperatures[1])
print("Wednesday:", seven_day_temperatures[2])
print("Thursday:", seven_day_temperatures[3])
print("Friday:", seven_day_temperatures[-3])
print("Saturday:", seven_day_temperatures[-2])
print("Sunday:", seven_day_temperatures[-1])

lowest_temperature = np.min(seven_day_temperatures)
print("\nLowest temperature:", lowest_temperature)

highest_temperature = np.max(seven_day_temperatures)
print("Highest temperature:", highest_temperature)

mean_of_temperatures = np.mean(seven_day_temperatures)
print("Mean of temperatures:", mean_of_temperatures)

answer= int(input("\nWhat would you like to do? \n1. Change all temperatures \n2. Quit\n"))

if answer == 1:
    print("Input new temperatures:\n")
    Monday = input("Monday: ")
    Tuesday = input("Tuesday: ")
    Wednesday = input("Wednesday: ")
    Thursday = input("Thursday: ")
    Friday = input("Friday: ")
    Saturday = input("Saturday: ")
    Sunday = input("Sunday: ")

    seven_day_temperatures.splice(0, 1, Monday)
    seven_day_temperatures.splice(1, 1, Tuesday)
    seven_day_temperatures.splice(2, 1, Monday)
    seven_day_temperatures.splice(3, 1, Wednesday)
    seven_day_temperatures.splice(4, 1, Thursday)
    seven_day_temperatures.splice(5, 1, Friday)
    seven_day_temperatures.splice(6, 1, Saturday)
    seven_day_temperatures.splice(6, 1, Sunday)

# fruits.splice(1, 1, "grape"); // Remove 1 element at index 1, then insert "grape"
# console.log(fruits); // Output: ["apple", "grape", "cherry"]



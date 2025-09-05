import numpy as np

Turn_start = True

numpy_matrix = np.array([
    [0, 1, 2, 3, 4],
    [1, " ", " ", " ", " "],
    [2, " ", " ", " ", " "],
    [3, " ", " ", " ", " "],
    [4, " ", " ", " ", " "]
])

def no_cords(a,b):

    while Turn_start == True:

        a = input("Input x value: ")
        b = input("Input y value: ")
        if a == 0:
            print("Invalid input. Please try again.\n")

        elif b == 0:
            print("Invalid input. Please try again.\n")

        #oh


print("==Welcome to the tic tac toe board!==\n")
print("I'll be Os, you can be Xs! Type out the coordinates to place your mark!")
print("You can go first~")



print(numpy_matrix)


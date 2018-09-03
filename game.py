import random

def game():
    field_1 = [[0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0]]

    num_ship = input("Enter the number of ships")

    num_ship = int(num_ship)
    if not 1 <= num_ship <= 25:
        print("Invalid data!")


    for i in range(num_ship):
        vertical = random.randint(0, 4)
        horizontal = random.randint(0, 4)
        if field_1[vertical][horizontal] == 0:
            field_1[vertical][horizontal] += 1
        else:
            num_ship += 1


    print(field_1)

    while True:
        i = input("(0 - 4)Enter i:")
        j = input("(0 - 4)Enter j:")

        i = int(i)
        j = int(j)
        if not 0 <= i and j <= 4:
            print("Invalid data! \n Try again!")
            continue

        if field_1[i][j] == 1:
            field_1[i][j] -= 1

            print("The ship is destroyed.")
        else:
            print("Missed")

        if field_1.count(1) == 0:
            print("You win")

game()
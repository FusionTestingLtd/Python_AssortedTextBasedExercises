# The user will be prompted with a menu where he/she will select a shape.
# Then the user will give the appropriate information needed to solve for the area,
# and the computer will give the area!

# The menu!
def menu():
    print("1. Circle")
    print("2. Square")  # Just because i want to tell the difference.
    print("3. Rectangle")
    print("4. Triangle")
    while True:
        try:
            menu_selection = int(input("What would like to find the area of? "))
            if menu_selection < 1 or menu_selection > 4:
                print("Please Select a valid menu item\n")
                continue
            return menu_selection
        except ValueError:
            print("Please Enter a valid menu item\n")
            continue


def square(slength, dp):
    area = slength**2
    return round(area, dp)


def rectangle(rlength, rwidth, dp):
    area = rlength*rwidth
    return "{} {}".format("\nArea =", round(area, dp))


def triangle(base, height, dp):
    area = (height * base) / 2
    return "{} {}".format("\nArea =", round(area, dp))


# ---------------- Main Program ------------------
choice = menu()

if choice == 1:  # CIRCLE
    while True:
        try:
            pi = 3.141592653589793238
            accuracy = int(input("Up to how many decimal places would you like the result?(1-10) "))
            if accuracy > 10 or accuracy < 1:
                print("Decimal place range is between 1 and 10\n")
                continue
            while True:
                try:
                    r = float(input("What is the radius? "))
                    print("{} {}".format("\nArea =", round(pi*r**2, accuracy)))
                except ValueError:
                    print("Please Enter a valid number\n")
                    continue
        except ValueError:
            print("Please Enter a valid number\n")
            continue
        else:
            break
elif choice == 2:  # SQUARE
    while True:
        try:
            side_length = float(input("What is the length of the side? "))
            if side_length < 0:
                print("Error: Positive numbers please.\n")
                continue
            while True:
                try:
                    number_of_places = int(input("Up to how many decimal places would you like the result?(1-10) "))
                    if number_of_places < 1 or number_of_places > 10:
                        print("Err (1-10)\n")
                        continue
                    print("{} {}".format("\nArea =", square(side_length, number_of_places)))
                    break
                except ValueError:
                    print("Please enter a number\n")
                    continue
        except ValueError:
            print("Please enter a number\n")
            continue
        else:
            break
elif choice == 3:  # RECTANGLE
    while True:
        try:
            number_of_places = int(input("Up to how many decimal places would you like the result?(1-10) "))
            if number_of_places < 1 or number_of_places > 10:
                print("Err (1-10)")
                continue
            while True:
                try:
                    length = float(input("What is length? "))
                    if length < 0:
                        print("Err")
                        continue
                    while True:
                        try:
                            width = float(input("What is the width? "))
                            if width < 0:
                                print("Err")
                                continue
                            elif width == length:
                                print("Ah! you meant a square!")
                                print("{} {}".format("Area =", square(width, number_of_places)))
                            else:
                                print(rectangle(length, width, number_of_places))
                                break
                        except ValueError:
                            print("Err")
                            continue
                        else:
                            break
                except ValueError:
                    print("Err")
                    continue
                else:
                    break
        except ValueError:
            print("Err - please enter a whole number")
            continue
        else:
            break
else:  # TRIANGLE
    while True:
        try:
            number_of_places = int(input("Up to how many decimal places would you like the result?(1-10) "))
            if number_of_places < 1 or number_of_places > 10:
                print("Err (1-10)\n")
                continue
            while True:
                try:
                    base = float(input("What is the length of the base of the triangle? "))
                    if base < 0:
                        print("ERR\n")
                        continue
                    while True:
                        try:
                            height = float(input("What is the height? "))
                            if height < 0:
                                print("ERR\n")
                                continue
                            else:
                                print(triangle(base, height, number_of_places))
                                # break
                        except ValueError:
                            print("Err\n")
                        else:
                            break
                except ValueError:
                    print("Err\n")
                else:
                    break
        except ValueError:
            print("Err\n")
            continue
        else:
            break




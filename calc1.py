print("calculator! ")
while True:
        while True:
            try:
                x, z, y = input("type in 2 integers and an operation seperated by a space: ").split()
                x = float(x)
                y = float(y)
                z = str(z)
                if z not in ["+", "/", "-", "*"]:
                    print("choose a correct operator")
                    continue
                else:
                    break
            except ValueError:
                print("choose an integer or seperate values with a space")
        if z == "+":
            print(x + y)
        elif z == "-":
            print(x - y)
        elif z == "/":
            while True:
                while y == 0:
                    try:
                        y = float(input("choose a rational denominator: "))
                    except ValueError:
                        print("enter a valid integer.")
                    continue
                else:
                    print(x / y)
                    break
        elif z == "*":
            print(x * y)

        RepeatLoop = input("would you like to calculate anything else? y/n: ").lower()
        if RepeatLoop in ["no", "n"]:
            break
        if RepeatLoop in ["yes", "y"]:
            continue
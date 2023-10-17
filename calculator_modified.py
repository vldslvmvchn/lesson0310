while True:

    value_operator = input("\nPlease choose an operator: \n 1 '+'\n 2 '-'\n 3 '*'\n 4 '/'\nYour answer ")
    value_int_1 = float
    value_int_2 = float

    while value_operator > "4" or value_operator == str:

        try:

            value_operator = input("\nPlease choose an operator: \n 1 '+'\n 2 '-'\n 3 '*'\n 4 '/'\nYour answer ")

        except NameError:

            pass


    if value_operator == "1":

        while value_int_1 == float:

            try:
                value_int_1 = float(input("Input a number 1: "))

            except ValueError:

                while value_int_1 == str:

                    if value_int_1 == str:

                        print("It should be a number")

                    else:

                        value_int_1 = float(input("Input a number 1: "))

        while value_int_2 == float:

            try:
                value_int_2 = float(input("Input a number 2: "))

            except ValueError:

                while value_int_2 == str:

                    if value_int_2 == str:

                        print("It should be a number")

                    else:

                        value_int_2 = float(input("Input a number 2: "))

        result = value_int_1 + value_int_2

    elif value_operator == "2":

        while value_int_1 == float:

            try:
                value_int_1 = float(input("Input a number 1: "))

            except ValueError:

                while value_int_1 == str:

                    if value_int_1 == str:

                        print("It should be a number")

                    else:

                        value_int_1 = float(input("Input a number 1: "))

        while value_int_2 == float:

            try:
                value_int_2 = float(input("Input a number 2: "))

            except ValueError:

                while value_int_2 == str:

                    if value_int_2 == str:

                        print("It should be a number")

                    else:

                        value_int_2 = float(input("Input a number 2: "))

        result = value_int_1 - value_int_2

    elif value_operator == "3":

        while value_int_1 == float:

            try:
                value_int_1 = float(input("Input a number 1: "))

            except ValueError:

                while value_int_1 == str:

                    if value_int_1 == str:

                        print("It should be a number")

                    else:

                        value_int_1 = float(input("Input a number 1: "))

        while value_int_2 == float:

            try:
                value_int_2 = float(input("Input a number 2: "))

            except ValueError:

                while value_int_2 == str:

                    if value_int_2 == str:

                        print("It should be a number")

                    else:

                        value_int_2 = float(input("Input a number 2: "))

        result = value_int_1 * value_int_2

    elif value_operator == "4":

        while value_int_1 == float:

            try:
                value_int_1 = float(input("Input a number 1: "))

            except ValueError:

                while value_int_1 == str:

                    if value_int_1 == str:

                        print("It should be a number")

                    else:

                        value_int_1 = float(input("Input a number 1: "))

        while value_int_2 == 0 or value_int_2 == float:

            try:
                value_int_2 = float(input("Input a number 2: "))

                while value_int_2 == 0:

                    if value_int_2 == 0:
                        print("It should not be a 0\n enter another number")

                        value_int_2 = float(input("Input a number 2: "))

            except ValueError:

                while value_int_2 == str:

                    if value_int_2 == str:
                        print("It should be a number")

                    else:
                        value_int_2 = float(input("Input a number 2: "))

        result = value_int_1 / value_int_2

    print(result)

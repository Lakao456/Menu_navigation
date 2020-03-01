def Temperature_converter():
    print("this program converts the given temprature to the desired unit.")
    count = 0
    while count == 0:
        print("Enter the temp with units, 'k','c' or 'f'")
        t = input("input the temp::")
        m = float(t[0:-1])
        # KELVIN
        if "k" in t.lower():
            n = round(m - 273.15)
            print("The temprature is ", n, "° Celsius")
            n = round((m - 273.15) * (9 / 5) + 32, 2)
            print("The temprature is ", n, "° Fahrenheit")
        # CELSIUS
        elif "c" in t.lower():
            n = round(m + 273.15, 2)
            print("The temprature is ", n, "° Kelvin")
            n = round(m * (9 / 5) + 32, 2)
            print("The temprature is ", n, "° Fahrenheit")
        # FAHRENHEIT
        elif "f" in t.lower():
            n = round((m - 32) * (5 / 9), 2)
            print("The temprature is ", n, "° Celsius")
            n = round((m - 32) * (5 / 9) + 273.15, 2)
            print("The temprature is ", n, "° Kelvin")
        else:
            print("invalid input")

        print("Do you want to repeat ?")

        if "n" in input("Y/N::").lower():
            count = 1

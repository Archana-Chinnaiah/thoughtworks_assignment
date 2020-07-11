while True:
    num = input("Please enter a number ")
    try:
        val = int(num)
        print("entered is an integer number")
        break;
    except ValueError:
        print("Enter the input again as an integer.")

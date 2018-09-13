while True:
    val = input("Enter an integer: ")
    try:
        val = int(val)
        print('the square of the number you entered is ',val**2)
        break #this exits the while loop
    except ValueError:
        print(val, ' is not an integer')


    x = 1
    try:
        print(5/x)
    except ZeroDivisionError:
        print("Something went wrong")
    else:
        print("I am the else clause")
    finally:
        print("I am the finally clause ")


    print("I am executing after the clause")


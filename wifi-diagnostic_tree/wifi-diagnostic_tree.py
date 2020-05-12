print("Reboot the computer and try to connect.")

response = input("Did that fix the problem? (y/n): ")

if response == "n":
    print("Reboot the computer and try to connect.")
    response = input("Did that fix the problem? (y/n): ")
    if response == "n":
        print("Make sure the cables between the router & modem are plugged in firmly.")
        response = input("Did that fix the problem? (y/n): ")
        if response == "n":
            print("Move the router to a new location and try to connect.")
            response = input("Did that fix the problem? (y/n): ")
            if response == "n":
                print("Get a new router.")

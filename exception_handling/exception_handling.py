try:
    file = open("numbers.txt", mode="r")

    total = 0
    count = 0

    for line in file:
        total += int(line)
        count += 1

    average = total / count

    print("Average: ", average)

    file.close()
except IOError:
    print("Error occurred reading the file.")
except ValueError:
    print("Error occurred converting string to number.")
    

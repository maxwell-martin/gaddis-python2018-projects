HOTDOGS_PACKAGE = 10
BUNS_PACKAGE = 8

num_people = int(input("Enter the number of people attending: "))
num_hdpp = int(input("Enter the number of hot dogs per person: "))

total_per_item = num_people * num_hdpp

min_hotdog_pkgs = 0
min_hotdogbuns_pkgs = 0
leftover_hotdogs = 0
leftover_hotdogbuns = 0

if total_per_item > 0:
    if total_per_item < HOTDOGS_PACKAGE:
        min_hotdog_pkgs = 1
        leftover_hotdogs = HOTDOGS_PACKAGE - total_per_item
    elif total_per_item % HOTDOGS_PACKAGE == 0:
        min_hotdog_pkgs = total_per_item // HOTDOGS_PACKAGE
    else:
        min_hotdog_pkgs = total_per_item // HOTDOGS_PACKAGE + 1
        leftover_hotdogs = min_hotdog_pkgs * HOTDOGS_PACKAGE - total_per_item

    if total_per_item < BUNS_PACKAGE:
        min_hotdogbuns_pkgs = 1
        leftover_hotdogbuns = BUNS_PACKAGE - total_per_item
    elif total_per_item % BUNS_PACKAGE == 0:
        min_hotdogbuns_pkgs = total_per_item // BUNS_PACKAGE
    else:
        min_hotdogbuns_pkgs = total_per_item // BUNS_PACKAGE + 1
        leftover_hotdogbuns = min_hotdogbuns_pkgs * BUNS_PACKAGE - total_per_item
        
print("Minimum number of packages of hot dogs required:", min_hotdog_pkgs)
print("Minimum number of packages of hot dog buns required:", min_hotdogbuns_pkgs)
print("Number of hotdogs leftover:", leftover_hotdogs)
print("Number of hotdog buns leftover:", leftover_hotdogbuns)

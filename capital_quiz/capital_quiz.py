import random

usa = { 'Alabama': 'Montgomery',
        'Alaska': 'Juneau',
        'Arizona':'Phoenix',
        'Arkansas':'Little Rock',
        'California': 'Sacramento',
        'Colorado':'Denver',
        'Connecticut':'Hartford',
        'Delaware':'Dover',
        'Florida': 'Tallahassee',
        'Georgia': 'Atlanta',
        'Hawaii': 'Honolulu',
        'Idaho': 'Boise',
        'Illinios': 'Springfield',
        'Indiana': 'Indianapolis',
        'Iowa': 'Des Monies',
        'Kansas': 'Topeka',
        'Kentucky': 'Frankfort',
        'Louisiana': 'Baton Rouge',
        'Maine': 'Augusta',
        'Maryland': 'Annapolis',
        'Massachusetts': 'Boston',
        'Michigan': 'Lansing',
        'Minnesota': 'St. Paul',
        'Mississippi': 'Jackson',
        'Missouri': 'Jefferson City',
        'Montana': 'Helena',
        'Nebraska': 'Lincoln',
        'Nevada': 'Carson City',
        'New Hampshire': 'Concord',
        'New Jersey': 'Trenton',
        'New Mexico': 'Santa Fe',
        'New York': 'Albany',
        'North Carolina': 'Raleigh',
        'North Dakota': 'Bismarck',
        'Ohio': 'Columbus',
        'Oklahoma': 'Oklahoma City',
        'Oregon': 'Salem',
        'Pennsylvania': 'Harrisburg',
        'Rhode Island': 'Providence',
        'South Carolina': 'Columbia',
        'South Dakoda': 'Pierre',
        'Tennessee': 'Nashville',
        'Texas': 'Austin',
        'Utah': 'Salt Lake City',
        'Vermont': 'Montpelier',
        'Virginia': 'Richmond',
        'Washington': 'Olympia',
        'West Virginia': 'Charleston',
        'Wisconsin': 'Madison',
        'Wyoming': 'Cheyenne' }

again = "y"

correct = 0
incorrect = 0

while again.lower() == "y" and len(usa) != 0:
    keys_dict_view = usa.keys()
    keys_list = []
    
    for key in keys_dict_view:
        keys_list.append(key)

    index = random.randint(0, len(usa) - 1)
    
    s = keys_list[index]
    c = usa.pop(s, "")

    capital = input("Enter capital of " + s + ": ").rstrip(" ").lstrip(" ")
    
    if capital.lower() == c.lower():
        print("Correct!")
        correct += 1
    else:
        print("Incorrect! The capital of", s, "is", c + ".")
        incorrect += 1
        
    again = input("Keep going (y/n)? ")

print("Number correct:", correct)
print("Number incorrect:", incorrect)

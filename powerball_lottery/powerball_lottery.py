def main():
    numbers_dict_all = {}
    numbers_dict_reg = {}
    numbers_dict_pb = {}
    numbers_dict_days = {}
    with open("pbnumbers.txt", "r") as infile:
        day_index = 1
        for line in infile:
            index = 0
            numbers = line.split()
            for number in numbers:

                # Build dictionary of all numbers
                if number in numbers_dict_all.keys():
                    numbers_dict_all[number] += 1
                else:
                    numbers_dict_all[number] = 1

                # Build dictionary of regular numbers only (slots 1-5)
                if index < len(numbers) - 1:
                    if number in numbers_dict_reg.keys():
                        numbers_dict_reg[number] += 1
                    else:
                        numbers_dict_reg[number] = 1

                # Build dictionary of powerball numbers only (slot 6)
                if index > len(numbers) - 2:
                    if number in numbers_dict_pb.keys():
                        numbers_dict_pb[number] += 1
                    else:
                        numbers_dict_pb[number] = 1

                # Build dictionary of all numbers with most recent day drawn as value
                numbers_dict_days[number] = day_index

                index += 1
                
            day_index += 1
                    
    print("10 most common numbers (most to least)\n",
          "Format ('Number', Frequency):\n",
          get_most_or_least(numbers_dict_all, True), sep = "")
    print()

    print("10 least common numbers (least to most)\n",
          "Format ('Number', Frequency):\n",
          get_most_or_least(numbers_dict_all, False), sep = "")
    print()

    print("10 most overdue numbers (most overdue to least overdue)\n",
          "Format ('Number', Last day drawn):\n",
          get_most_or_least(numbers_dict_days, False), sep = "")
    print()

    print("Frequency of regular numbers (1-69):\n", numbers_dict_reg, sep = "")
    print()
    
    print("Frequency of powerball numbers (1-26):\n", numbers_dict_pb, sep = "")

def get_most_or_least(d, reverse_needed):
    values = list(d.values())
    values.sort(reverse = reverse_needed)
    values = values[0:10]
    keys = {}
    for value in values:
        for k, v in d.items():
            if value == v and k not in keys.keys() and (len(keys) < 10):
                keys[k] = value
    return keys

main()

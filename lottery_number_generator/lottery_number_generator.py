import random

lottery_num_list = []

for i in range(7):
    rnum = random.randint(0,9)
    lottery_num_list.append(rnum)

for num in lottery_num_list:
    print(num, end="")

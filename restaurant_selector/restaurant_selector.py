HEAD = "Here are your restaurant choices:"
NNN = "\tJoe's Gourmet Burgers\n\tMain Street Pizza Company\n\tCorner Cafe\n\tMama's Fine Italian\n\tThe Chef's Kitchen"
YNN = "\tMain Street Pizza Company\n\tCorner Cafe\n\tMama's Fine Italian\n\tThe Chef's Kitchen"
YYN = "\tCorner Cafe\n\tThe Chef's Kitchen"
YYY = "\tCorner Cafe\n\tThe Chef's Kitchen"
NYN = "\tCorner Cafe\n\tThe Chef's Kitchen"
NYY = "\tCorner Cafe\n\tThe Chef's Kitchen"
NNY = "\tMain Street Pizza Company\n\tCorner Cafe\n\tThe Chef's Kitchen"
YNY = "\tMain Street Pizza Company\n\tCorner Cafe\n\tThe Chef's Kitchen"


veget = input("Is anyone in your party vegetarian? (y/n): ")
vegan = input("Is anyone in your party vegan? (y/n): ")
gf = input("Is anyone in your party gluten-free? (y/n): ")

print(HEAD)

if veget == "y" and vegan == "n" and gf == "n":
    print(YNN)
elif veget == "y" and vegan == "y" and gf == "n":
    print(YYN)
elif veget == "y" and vegan == "y" and gf == "y":
    print(YYY)
elif veget == "n" and vegan == "y" and gf == "n":
    print(NYN)
elif veget == "n" and vegan == "y" and gf == "y":
    print(NYY)
elif veget == "n" and vegan == "n" and gf == "y":
    print(NNY)
elif veget == "y" and vegan == "n" and gf == "y":
    print(YNY)
else:
    print(NNN)

row_length_ft = float(input("Enter the length of the row, in feet: "))
end_post_ft = float(input("Enter the the amount of space used by the end-post assembly, in feet: "))
vines_spacing_ft = float(input("Enter the the amount of space between vines, in feet: "))
num_of_grapevines = (row_length_ft - 2 * end_post_ft) / vines_spacing_ft
print("The number of grapevines that will fit in the row is:", format(num_of_grapevines, ".0f"))

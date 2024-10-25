#Program #1: Initials
#Clara Riley
#Luke Snell
#10/24/24

full_name = input("Please enter your first, middle, and last names: ")

names = full_name.split()

initials = [name[0].upper() for name in names]

print(". ".join(initials) + ".")

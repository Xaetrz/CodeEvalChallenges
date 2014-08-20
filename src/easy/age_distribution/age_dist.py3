import sys

file = open(sys.argv[1], 'r')

for line in file:
    age = int(line)
    
    if age >= 0 and age <= 100:
        if age <= 2:
            print("Still in Mama's arms")
        elif age <= 4:
            print("Preschool Maniac")
        elif age <= 11:
            print("Elementary school")
        elif age <= 14:
            print("Middle school")
        elif age <= 18:
            print("High school")
        elif age <= 22:
            print("College")
        elif age <= 65:
            print("Working for the man")
        else:
            print("The Golden Years")
    else:
        print("This program is for humans")
        
file.close()

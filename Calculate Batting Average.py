runs = int(input("Enter total runs scored: "))
outs = int(input("Enter number of times the player got out: "))

if outs != 0:
    average = runs / outs
    print("Batting Average =", average)
else:
    print("Average cannot be calculated (outs cannot be zero)")
import random
wrfile = open("random.csv","w")

print("x,y", file=wrfile)
for i in range(0, 25):
    for x in range(0, 101):
        print(x, ",", random.randrange(-50, 50), file=wrfile)
wrfile.close()

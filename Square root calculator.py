loop = False
while loop == False: 
    y = 1
    x = int(input("What integer would you like to perfect square root?"))
    correct = False

    while correct == False:
        if y == x/y:
            print (x,"Sqrt =", y )
            correct = True
        else :
            y += 1
            if y == 1000000:
                print ("error either not a perfect square root or too high")
                correct = True
                # While it technically didnt get the correct answer if it was too high we still need to start over
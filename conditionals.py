userReplay = input("Do you need to ship a package? (Enter yes or no)")
if userReplay == "yes":
    print("we can help you ship that package!")
else:
        print("Please come back when you need to ship a package. Thank you.")
userReplay = input("Would you like to buy stamp, buy an envelop, or make a copy? (Enter stamp, envelop, or copy) ")
if userReplay == "stamps":
    print("we have many stamps designs to choose from.")
elif userReplay == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReplay == "copy":
    copies = input("How many copies would you like? (Enter number) ")
    print("Here are {} copies.".format(copies))
else: 
    print("Thank you. Please come again.")
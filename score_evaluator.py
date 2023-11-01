score = input("Please write your score!\n") #\n makes it go down a line?
score = int(score) #This changes the string to integer since first one saves it as string

if score >= 70:
    print("You did well ^-^")
    
elif (score <70) and (score >=45):
    print("You did OK -_-")
    
else:
    print("You failed :○")
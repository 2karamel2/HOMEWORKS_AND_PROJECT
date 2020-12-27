name=input("What's your name? ")
print("Welcome " + name.capitalize())
print("You shoul guess the word. ")
print("Good luck " + name.capitalize())
print("")
print("Let's begin ")
import random
words=["recovery","airplane","pilot","crack"]
a=list(random.choice(words))
j=[" "]*len(a)
right=7
k=0
okay=False    
while right != 0:
    char=input("Please enter a character => ").lower()
    for i in a:
        k+=1
        if i==char:
            okay=True
            j[k -1 ]=char
        if " " not in j:
             print("You're doing well.Go on! ")
             exit()
    if okay==False:
        right-=1
        print("Wrong guess! ")
        print(right, "be left ")
    if right==0 and "_ " in j:
        print("Sorry. :( You didn't find it. ")
        exit()
    k=0
    okay=False
    print(j)
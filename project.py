name='melis'
surname='kara'

i=0
while(i<3):
    i=i+1
    a=input("Please enter your name => ")
    b=input("Please enter your surname => ")
    if a==name and b==surname:
        print("Welcome! ")
        lessons=["math","turkish","art","algorithm","english"]
        print(lessons)
        print("You should choose less than 4 lessons")        

        choosinglessons=[]

        for i in range(5):
            x=input("Which courses do you want to choose.If you don't want choose click on space button. ")
            choosinglessons.append(x)

        a=choosinglessons.count(' ') 


        if a>4:
           print("You failed in class. ")
        else:
            print("You should choose one of them.")
            midterm=int(input("Enter your midterm point => "))
            project=int(input("Enter your project point => "))
            final=int(input("Enter your final point => "))

            Notes={"Midterm": midterm ,
                   "Project ": project ,
                   "Final ": final}
            print(Notes)

            i=midterm/100*30
            j=project/100*20
            k=final/100*50

            grade=i+j+k

            if grade > 90:
               print("YOU GOT AA !!! ")
            elif 70 < grade < 90:
                print(" ")
                print("YOU G0T BB !!! ")
            elif 50 < grade < 70:
               print(" ")
               print("YOU GOT CC !!! ")
            elif 30 < grade < 50:
               print(" ")
               print("YOU GOT DD !!! ")
            elif grade < 30:
               print(" ")
               print("FAILURE !!! ")
                
            
    else:
        print("Please try again ")
        continue
        lessons=["math","turkish","art","algorithm","english"]
        print(lessons)
        print("You should choose less than 4 lessons")        

        choosinglessons=[]

        for i in range(5):
            x=input("Which courses do you want to choose.If you don't want choose click on space button. ")
            choosinglessons.append(x)

        a=choosinglessons.count(' ') 


        if a>4:
           print("You failed in class. ")
        else:
            print("You should choose one of them.")
            midterm=int(input("Enter your midterm point => "))
            project=int(input("Enter your project point => "))
            final=int(input("Enter your final point => "))

            Notes={"Midterm": midterm ,
                   "Project ": project ,
                   "Final ": final}
            print(Notes)

            i=midterm/100*30
            j=project/100*20
            k=final/100*50

            grade=i+j+k

            if grade > 90:
               print("YOU GET AA !!! ")
            elif 70 < grade < 90:
                print(" ")
                print("YOU GET BB !!! ")
            elif 50 < grade < 70:
                print(" ")
                print("YOU GET CC !!! ")
            elif 30 < grade < 50:
                print(" ")
                print("YOU GET DD !!! ")
            elif grade < 30:
                print(" ")
                print("FAILURE !!! ")
    
    if i==3:
        print("Please try next ")

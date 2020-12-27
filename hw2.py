for i in range(10000):
    first=input("Please enter your first name =>")
    last=input("Please enter your last name =>")
    date=int(input("Please enter your birtday year =>"))
    age=(input("Pleasse enter your age for result =>"))
    if int(age) <= 18:
        print("Your first name and last name => {} {}".format(first,last))
        print("Your birthday year is {}".format(date))
        print("Your age is {}".format(age))
        print("You can't go out because it's too dangerous.")
    else:
        print("Your first name and last name => {} {}".format(first,last))
        print("Your birthday year is {}".format(date))
        print("Your age is {}".format(age))
        print("You can go out to the street.")

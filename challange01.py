#!/user/bin/env python3

#week =["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]



def main():

#user input for the week
    while True:
        userWeekValue = input("what day of the week is today?,  please enter in lowerCase: ")
        if userWeekValue.lower() == "thursday":
            print("Correct!!  today is "+userWeekValue)
            break
        else:
            print("InCorrect!!  Please try again")
         
if __name__=="__main__":
    main()

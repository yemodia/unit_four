grade = int(input("What grade are you in?"))

if grade >0 and grade < 6:
    print("You are in elementary")
elif grade >6 and grade < 9:
    print("You are in middle school")
else:
    print("You are in high school")



email = input("Write your e-mail ")

if "@" in email:
    if "." in email:
        print("No problem")
    else:
        print("Add at least one dot")
else:
    print("You forgot to add @ to your e-mail")
    


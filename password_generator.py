fname = str(input("Please enter your first name: "))
sname = str(input("Please enter your second name: "))
age = int(input("Please enter your age: "))
length = int(input("How many characters should your password have (min: 6, max: 12): "))

fname = fname.lower().strip()
sname = sname.lower().strip()
password = fname + sname
password = password[::-1] + "{}".format(age)

print()
if 5 < length < 13:
    if length == 6:
        print("Try this password: ", password[2:8])
    elif length == 7:
        print("Try this password: ", password[2:9])
    elif length == 8:
        print("Try this password: ", password[2:10])
    elif length == 9:
        print("Try this password: ", password[2:11])
    elif length == 10:
        print("Try this password: ", password[2:12])
    elif length == 11:
        print("Try this password: ", password[2:13])
    elif length == 12:
        print("Try this password: ", password[0:11])
else:
    print("Your password should contain between 6-12 characters. Enter a valid number")
print()
print("Remember to invite your friends to get themselves safe and secure passwords")
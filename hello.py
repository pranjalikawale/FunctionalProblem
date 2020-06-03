import re

username=input("Enter username")
pattern=re.compile("^[A-Z]{1}[a-z]{2,}$")

if re.match(r"[A-Z]{3,}",username):
    print("Hello"+username)
else:
    print("Plz enter valid username")    
# ([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+
import re
name, email = input("Enter your name==> ").title(), input(
    "enter your email address==> ".title())
v_email = re.search(
    "([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})", email)
if v_email:
    print(f"Hello {name.title()} you email==>{email} is Valid")
else:
    print(f"Hello {name.title()} you email==> {email} is NOT VALId")
    print("Email should be like that ==>\nname.surname@gmail.com\nanonymous123@yahoo.co.uk\nmy_email@outlook.co")
print("="*20)

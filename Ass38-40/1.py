# 1
name = str(input("Enter your name==> ").title().lstrip().rstrip().strip())
print(f"Hello {name}, Happy To See You Here.")
print("="*25)
# 2
age = int(input("enter your age==> ".title()))
if age < 16:
    print(
        f"Hello {name} Your Age Is Under 16, Some Articles Is Not Suitable For You........")
else:
    print(f"Hello {name} Your Age Is {age}, All Articles Is Suitable For You..")
print("="*25)
# 3

first_name = input("enter your first name==> ")
second_name = input("enter your secound name==> ".title()).title().rstrip()
print(f"hello {first_name}.{second_name[0:1]}".title())
print("="*25)
# 4
em_ail = input("enter your email==> ".title()).strip()
print(f'your name is==> {em_ail[0:em_ail.index("@")]}'.title())
print(
    f'email service provider is==> {em_ail[em_ail.index("@")+1:em_ail.index(".")]}'.title())
print(f'Top Level Domain Is==> {em_ail.index(".")+1:}'.title())

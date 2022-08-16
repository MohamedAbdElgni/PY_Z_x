Age = int(input("Enter your Age please==> ".title()).strip().lstrip().rstrip())
months = Age*12
days = months*30
hours = days*24
mins = hours*60
seconds = mins*60
print(f"your age in months==> {months}".rjust(28, "-"))
print(f"your age in days==> {days}".rjust(28, "-"))
print(f"your age in hours==> {hours}".rjust(28, "-"))
print(f"your age in mins==> {mins}".rjust(28, "-"))
print(f"your age in sec==> {seconds}".rjust(28, "-"))

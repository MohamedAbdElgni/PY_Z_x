# 1
print(bool(54))
print(bool('s'))
print(bool(.020))
print(bool('#'))
print("-"*25)
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(0))
print("="*25)
# 2
html = 80
css = 60
javascript = 70
print(bool(html > 50))
print(bool(css > 50))
print(bool(javascript > 50))
print("="*25)
# 3
num_one = 10
num_two = 20
num = 20
print(bool(num > num_one or num_two))
print(bool((num > num_two and num_one)))
print("="*25)
# 4
result = num_one+num_two
print(result)
print(result**3)
print((result**3) % 26000)
print(((result**3) % 26000)/5)
print(type(str((((result**3) % 26000)/5))))

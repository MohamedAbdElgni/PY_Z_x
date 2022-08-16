def say_hello(name="unknown", age="unknown", country="unknown"):
    print(f"hello {name} your age is {age} and you live in {country}".title())


name = input("Enter your name ==> ".title())
age = input("Enter your age ==> ".title())
country = input("Whats your country ==> ".title())

say_hello(name, age, country)
say_hello()

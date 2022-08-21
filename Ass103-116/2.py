class User():
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name.title()
        self.age = age
        self.gender = str(gender).title()

    def full_details(self):
        if self.gender.title() == "Male":
            return fr"hello Mr {self.first_name} {self.last_name[0]}. [{str(40-self.age).zfill(2)}] years to reach 40".title()
        elif self.gender == "Female":
            return fr"hello Mrs {self.first_name} {self.last_name[0]}. [{str(40-self.age).zfill(2)}] years to reach 40".title()
        else:
            return fr"hello {self.first_name} {self.last_name[0]}. [{str(40-self.age).zfill(2)}] years to reach 40".title()


user_one = User("Osama", "Mohamed", 38, "male".title())
user_two = User("Eman", "Omar", 25, "female".title())
print(user_one.full_details())
print(user_two.full_details())

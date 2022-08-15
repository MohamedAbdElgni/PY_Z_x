def decor(func):
    def nes_fun():
        print("Sugar Added From Decorators")
        func()
        print("="*20)
    return nes_fun


@decor
def make_coffe():
    print("Coffe created")


@decor
def make_tea():
    print("Tea Created")


make_coffe()
make_tea()

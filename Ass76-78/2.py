# import sys
# sys.path.append(r"E:\Mohamed\Python TRY\my_mod.py")
# print(sys.path)
from my_mod import say_welcome as new_welcome
from my_mod import say_hello as new_hello

import my_mod as zz
# print(dir(my_mod))
zz.say_hello("mohamed")
zz.say_welcome("mohamed")
new_welcome('mohamed')
new_hello("mohamed")

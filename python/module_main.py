# import mymodule
# from  mymodule import say_hello

# print(mymodule.say_hello("Alice"))

# print(mymodule.say_goodbye("Alice"))

# print(say_hello("Bob"))


from mypackage import mymodule
import mypackage.mymodule as mm

print(mymodule.say_hello("Alice"))

print(mm.say_hello("Alice"))
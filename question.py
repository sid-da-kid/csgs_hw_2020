import time
name = input("What is your name?\n")
print("Hello " + name)
time.sleep(2)
print(name + " is a nice name")
time.sleep(2)
character = len(name)
print("Did you know that your name consists of " + str(character) + " characters")
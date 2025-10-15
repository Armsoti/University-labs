while True:
    print("Who are you?")
    name = input()
    if name != "Joe":
        continue
    print("Hello, {}. What is the passport?(it is a fish) ".format(name))
    passport = input()
    if passport == "swordfish":
        break
print("Access granted!")
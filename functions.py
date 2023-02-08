def thing1(name):
    print(f"Welcome to function one {name}")
    def thing2():
        print(f"Welcome to function two {name}")
    thing2()

thing1("Galina")

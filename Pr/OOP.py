class Supernatural:
    """
    class Supernatural is for people who's born with supernatural powers
    """

    def __init__(self, name, age, power):
        self.name = name
        self.age = age
        self.power = power

    S_class_powers = ["fire", "water", "earth", "air"]
    A_class_powers = ["light", "gravity", "darkness", "lava", "void", "magnetism"]
    B_class_powers = ["lightning", "metal", "ice", "wood", "smoke", "poison", "sand", "stone"]

    """
    deciding classes for supernatural person based on how strong their powers are.
    """
    def enroll(self):
        if self.power in self.S_class_powers:
            self.upper_class.append(self.name)
        elif self.power in self.A_class_powers:
            self.middle_class.append(self.name)
        elif self.power in self.B_class_powers:
            self.lower_class.append(self.name)

    upper_class = []
    middle_class = []
    lower_class = []

person1 = Supernatural("Gela", 16, "sand")
person2 = Supernatural("Cico", 17, "void")
person3 = Supernatural("Khvicha", 13, "water")

person1.enroll()
person2.enroll()
person3.enroll()

"""
putting your information to find out what class you belong to.
"""

i_name = input("Enter your name: ")
i_age = int(input("Enter your age: "))
i_power = input("Enter your power: ")

if i_age < 6:
    print("Sorry, you're too young for this school.")
elif i_age > 18:
    print("Sorry, you're too old for this school.")
else:
    info = Supernatural(i_name, i_age, i_power)
    info.enroll()

    if i_name in Supernatural.upper_class:
        print(f"You belong in the Upper class, your classmates are: {Supernatural.upper_class[0:-1]}")
    elif i_name in Supernatural.middle_class:
        print(f"You belong in the Middle class, your classmates are: {Supernatural.middle_class[0:-1]}")
    elif i_name in Supernatural.lower_class:
        print(f"You belong in the Lower class, your classmates are: {Supernatural.lower_class[0:-1]}")
    else:
        print("Invalid power input.")
class Developer:
    raise_amt = 1.05  # static

    def __init__(self, name: str, pay: int):
        self.name = name
        self.pay = pay

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def fromString(cls, empStr: str):
        name, pay = empStr.split("-")
        return cls(name, int(pay))


res = Developer.fromString("Aditya-50000")
print(res.pay)

# class Manager(Developer):
#   def __init__(self, name, pay,teamsize:int):
#     self.teamsize=teamsize
#     super().__init__(name, pay)


# Python handles Multiple Inheritance flawlessly using an algorithm called C3 Linearization. Python calculates a flat list of who has priority. You can view it anytime by printing Manager.__mro__.
class FiringPower:
    def fire_employee(self, target_name: str):
        print(target_name, "is fired.")


# Multiple Inheritance! Manager inherits from both Developer AND FiringPower
class Manager(Developer, FiringPower):
    def __init__(self, name: str, pay: int, team_size: int):
        Developer.__init__(self, name, pay)
        # super().__init__(name,pay) -> mro
        self.team_size = team_size


def __eq__(self, other: object) -> bool:
    # 1. Type check: Ensure we aren't comparing a Developer to an Integer
    if not isinstance(other, Developer):
        return NotImplemented  # Let Python try the reverse comparison!

    # 2. Value check
    return self.name == other.name and self.pay == other.pay


def __repr__(self) -> str:
    # !r automatically puts quotes around strings
    return f"{self.__class__.__name__}(name={self.name!r},pay={self.pay})"
    # Output: Developer(name='Aditya', pay=50000)


class Team:
    def __init__(self, members: list[str]):
        self.members = members

    # Replaces C++ operator[]
    def __getitem__(self, index: int) -> str:
        return self.members[index]


if __name__ == "__main__":
    boss = Manager("Aditya", 10000, team_size=5)
    print(f"Boss Name: {boss.name}")
    print(f"Boss Pay: ${boss.pay}")
    boss.fire_employee("bob the intern")
    print(__repr__(boss))
    my_team = Team(["Aditya", "Rahul"])
    print(my_team[0])  # Secretly calls my_team.__getitem__(0) -> "Aditya"

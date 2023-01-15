class Band:
    def __init__(self, name=""):
        self.name = name
        self.person = []
        self.people_dictionary = {}

    def __str__(self):
        return f"{self.name} ({str(self.person).lstrip('[').rstrip(']')})"

    def add(self, musician):
        self.people_dictionary[musician.name] = musician.instruments
        self.person.append(f"{musician.name} ({musician.instruments})")

    def play(self):
        for person in self.people_dictionary:
            if not self.people_dictionary[person]:
                print(f"{person} needs an instrument!")
            else:
                print(f"{person} is playing: {self.people_dictionary[person][0]}")

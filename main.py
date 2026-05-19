# 10
class Hospital:
    def __init__(self, name, rooms):
        self.name = name
        self.__room = rooms

    def get_rooms(self):
        return self.__room, self.name

    def set_rooms(self, new_rooms):
        self.__room = new_rooms


h1 = Hospital("Shifo", 50)

h1.set_rooms(70)
print(h1.get_rooms())

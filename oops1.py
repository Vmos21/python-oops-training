class Student:
    def __init__(self, name, avg):
        self.name = name
        self.avg = avg

l = []
name = input("Enter your name: ")
for i in range(0, 4):
    l.append(int(input("Enter mark: ")))

s1 = Student(name, sum(l)/4)
print("Name: ", s1.name, "\nAverage: ", s1.avg)
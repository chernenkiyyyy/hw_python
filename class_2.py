import os

class A:
    def __init__(self):
        self.file_1 = "ffile__1.json"
        self.file_2 = "ffile_2.json"

    def read_file_1(self):
        with open(self.file_1, "r") as file_11:
            return "The file {} contains this information: \n{}".format(self.file_1, file_11.readline())

    def read_file_2(self):
        with open(self.file_2, "r") as file_11:
            return "The file {} contains this information: \n{}".format(self.file_2, file_11.readline())

    def way_1(self):
        return os.path.abspath(self.file_1)

    def way_2(self):
        return os.path.relpath(r"C:\Users\андрей\PycharmProjects\work\ffile_2.json")

    def write_1(self, file):
        with open(file, "w") as new_file:
            text = input(str(" oh"))
            new_file.write(text)








class_a = A()
print(class_a.read_file_1())
print(class_a.read_file_2())
print(class_a.way_1())
print(class_a.way_2())
print(class_a.write_1("ffile__1.json"))
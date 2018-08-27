

class Address:

    def __init__(self):
        self.list = ["10.12.45.13", "12.96.14.41", "76.35.14.14"]
        self.task_2 = ""
        self.task_3 = ""
        self.task_4 = ""


    def __str__(self):
        return " IP address - {} ,\n Expanded list - {}, \n List without first act - {},\n List latest acts - {}"\
            .format(str(list), self.task_2, self.task_3, self.task_4)

    def expanded_list(self):#Expanded list
        self.task_2 = str([".".join(i.split(".")[::-1]) for i in self.list])

    def get_no_first(self): #List without first act
        self.task_3 = str([".".join(i.split(".")[1::]) for i in self.list])

    def get_func(self): #List latest acts
        self.task_4 = str([i.split(".")[-1] for i in self.list])



my_class = Address()
print(my_class.__dict__)
my_class.expanded_list()
my_class.get_no_first()
my_class.get_func()
print(my_class.__dict__)
























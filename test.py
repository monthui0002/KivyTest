class Test():
    def __init__(self):
        self.name = "Huong"
        self.age = 20


class Married(Test):
    def __init__(self, **kwargs):
        print(kwargs)
        super(Married, self).__init__()
        print(self)
        self.info = kwargs["ok"]

    def update(self):
        print(self.info)
        print(self.name)
        print(self.age)


m = Married(ok="Hau")

m.update()

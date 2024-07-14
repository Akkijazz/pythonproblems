class parent:
    def func1(self):
        print(f"I am in parent")


class child1(parent):
    def func2(self):
        print(f"I am in child 1")


class child2(parent):
    def func3(self):
        print(f"I am in child 2")


c1 = child1()
c1.func1()
c2 = child2()
c2.func3()
c2.func1()

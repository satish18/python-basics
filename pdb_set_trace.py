import pdb

class MyClass():

    def __init__(self, num_loops):
        self.count = num_loops

    def go(self):
        for i in range(self.count):
            pdb.set_trace()
            print(i)
        return

if __name__ == '__main__':
    MyClass(5).go()

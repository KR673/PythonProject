class param:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        return print(self.name)
    
if __name__ == '__main__':
    print(param('11', '22').getName)
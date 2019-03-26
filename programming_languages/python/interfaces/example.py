class IInterface(object):
    def __init__(self):
        pass

    def show(self):
        raise Exception("NotImplementedException")


class MyClass(IInterface):
   def __init__(self):
       IInterface.__init__(self)

   def show(self):
       print('Hello World!')

if __name__ == "__main__":
    aclass = MyClass()
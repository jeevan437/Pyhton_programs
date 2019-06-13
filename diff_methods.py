class Methods:

    def __init__(self):
        print("init method")

    def instance_method(self):
        print("instane method")

    @staticmethod
    def static_method():
        print("static method")

    @classmethod
    def class_method(cls):
        print("class methods")

obj = Methods()
obj.instance_method()
Methods.class_method()
Methods.static_method()

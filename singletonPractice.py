import logging

class Mylogger:
    _instance = None

    def __new__(cls,*args,**kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self,class_name="CustomLogger",debug_level=10):
        if not hasattr(self, 'logger'):
            self.logger = logging.getLogger(class_name)
            self.logger.setLevel(debug_level)
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger

class A:
    def __init__(self):
        self.logger = Mylogger("A").get_logger()

    def do_something(self):
        self.logger.info("Doing work in A")

class B:
    def __init__(self):
        self.logger = Mylogger("B").get_logger()

    def do_something(self):
        self.logger.info("Doing work in B")



a = A()
b = B()
a.do_something()
b.do_something()
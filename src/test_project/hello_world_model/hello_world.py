class HelloWorld:
    def __init__(self):
        self._name = None

    def set_name(self, name):
        self._name = name

    def print(self):
        print('Hello ' + self._name)
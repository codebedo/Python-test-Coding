class FooError(Exception):
    def __init__(self, message):
        self.message = message


    def foo(self):
        print("bar")


try:
    raise FooError("This is the test error")
except FooError as e:
    e.foo()

    

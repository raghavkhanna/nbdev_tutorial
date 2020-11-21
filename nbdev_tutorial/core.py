# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['say_hello', 'HelloSayer']

# Cell
def say_hello(to):
    "Say hello to somebody"
    return f'Hello {to}!'

# Cell
class HelloSayer:
    "Say hello to `to` using `say_hello`"
    def __init__(self, to):
        self.to = to

    def say(self):
        "Do the saying"
        return say_hello(self.to)
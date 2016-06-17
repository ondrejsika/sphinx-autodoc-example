"""
This is a module docstring
"""

class Hello(object):
    """
    This is a Hello class docstring
    """

    def __init__(self, name):
        """
        This is an __init__ method docstring.

        Creates a new :class:`Hello` instance.

        :param name: name for the hello
        :type name: str
        """
        self.name = name

    def say_hello(self):
        """
        This is a say_hello method decorator
        """
        print 'Hello %s' % self.name


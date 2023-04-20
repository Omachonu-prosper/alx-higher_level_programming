#!/usr/bin/python3

"""Square module."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class."""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return '[Square] ({}) {}/{} - {}'.format(
            self.id,
            self.x,
            self.y,
            self.width
        )

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        Rectangle.validateValue(value, 'width')
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the instance attributes."""
        if len(args) == 0:
            self.id = kwargs['id'] if kwargs.get('id') else self.id
            self.size = kwargs['size'] if kwargs.get('size') else self.size
            self.x = kwargs['x'] if kwargs.get('x') else self.x
            self.y = kwargs['y'] if kwargs.get('y') else self.y
        else:
            if len(args) > 0:
                self.id = args[0]

            if len(args) > 1:
                self.size = args[1]

            if len(args) > 2:
                self.x = args[2]

            if len(args) > 3:
                self.y = args[3]

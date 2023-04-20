#!/usr/bin/python3

"""Rectangle module."""


from models.base import Base


class Rectangle(Base):
    """Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        Rectangle.validateValue(width, 'width')
        Rectangle.validateValue(height, 'height')
        Rectangle.validateValue(x, 'x')
        Rectangle.validateValue(y, 'y')
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id,
            self.__x,
            self.__y,
            self.__width,
            self.__height
        )

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        Rectangle.validateValue(value, 'width')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        Rectangle.validateValue(value, 'height')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        Rectangle.validateValue(value, 'x')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        Rectangle.validateValue(value, 'y')
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print a representation of the rectangle."""
        width = self.__width
        height = self.__height
        x = self.__x
        y = self.__y
        print('\n' * y, end='')

        for i in range(height):
            print(' ' * x + '#' * width)

    def update(self, *args, **kwargs):
        """Updates the instance attributes."""
        w = self.width
        h = self.height

        if len(args) == 0:
            self.id = kwargs['id'] if kwargs.get('id') else self.id
            self.width = kwargs['width'] if kwargs.get('width') else w
            self.height = kwargs['height'] if kwargs.get('height') else h
            self.x = kwargs['x'] if kwargs.get('x') else self.x
            self.y = kwargs['y'] if kwargs.get('y') else self.y
        else:
            if len(args) > 0:
                self.id = args[0]

            if len(args) > 1:
                self.width = args[1]

            if len(args) > 2:
                self.height = args[2]

            if len(args) > 3:
                self.x = args[3]

            if len(args) > 4:
                self.y = args[4]

    @staticmethod
    def validateValue(value, value_type):
        """Validates the values before instantiation and for setters.

        - If the input is not an integer, raise the TypeError exception with
        the message: <name of the attribute> must be an integer.
        Example: width must be an integer

        - If width or height is under or equals 0,
        raise the ValueError exception with the message:
        <name of the attribute> must be > 0.
        Example: width must be > 0

        - If x or y is under 0,
        raise the ValueError exception with the message:
        <name of the attribute> must be >= 0.
        Example: x must be >= 0

        @value is the value to be validated
        @value_type is the use of the value (height, width, x or y)
        represented as stings

        Example Usage: Rectangle.validateValue(5, 'height')
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(value_type))

        if value_type in ['height', 'width']:
            if value <= 0:
                raise ValueError('{} must be > 0'.format(value_type))

        elif value_type in ['x', 'y']:
            if value < 0:
                raise ValueError('{} must be >= 0'.format(value_type))

        if value_type not in ['width', 'height', 'x', 'y']:
            raise ValueError('{} is not a valid value type'.format(value_type))

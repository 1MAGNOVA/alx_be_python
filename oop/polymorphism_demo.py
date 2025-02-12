"""n this script, define a base class Shape with a method area() and derived classes Rectangle and Circle, each overriding the area() method to calculate their respective areas."""


class Shape:
    """base class defined"""

"""Method: area(self), which simply raises a NotImplementedError, indicating that derived classes need to override this method."""
    def area(self):
        raise NotImplementedError("derived classes need to override this method")


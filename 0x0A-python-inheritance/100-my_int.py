#!/usr/bin/python3
class MyInt(int):
    def __eq__(self, other):
        return super().__ne__(other)  # Invert the behavior of ==

    def __ne__(self, other):
        return super().__eq__(other)  # Invert the behavior of !=

# Test your custom MyInt class
if __name__ == "__main__":
    my_i = MyInt(3)
    print(my_i)        # Output: 3
    print(my_i == 3)   # Output: False (opposite of int's ==)
    print(my_i != 3)   # Output: True (opposite of int's !=)

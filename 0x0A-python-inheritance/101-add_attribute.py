#!/usr/bin/python3
def add_attribute(obj, attr_name, attr_value):
    """
    Add a new attribute to an object if possible.
    
    :param obj: The object to which the attribute will be added.
    :param attr_name: The name of the new attribute.
    :param attr_value: The value of the new attribute.
    :raises TypeError: If the object cannot have new attributes.
    """
    # Check if the object is an instance of a class that allows attribute addition
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    
    # Add the new attribute to the object
    setattr(obj, attr_name, attr_value)

# Example usage:
class ExampleClass:
    def __init__(self, initial_value):
        self.initial_value = initial_value

obj = ExampleClass(42)

# Try adding a new attribute to the object
add_attribute(obj, 'new_attribute', 'Hello, World!')

# Access the new attribute
print(obj.new_attribute)  # Output: Hello, World!

# Try adding a new attribute to an integer (should raise a TypeError)
add_attribute(42, 'new_attribute', 'Invalid')  # Raises TypeError

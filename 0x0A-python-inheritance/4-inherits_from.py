#!/usr/bin/python3
# 4-inherits_from.py
#!/usr/bin/python3
# 4-inherits_from.py
"""
===================================
 A defined class and inherited class-checking function.
===================================
"""

def inherits_from(obj, a_class):
    """
    return True if an object is an instance of a class
    that inherited from
    """

    return False if type(obj) is a_class else isinstance(obj, a_class)



###############################################################################

######  INTEGER PROCESSING

def is_int(obj):
    return isinstance(obj, int)

def error_not_int(obj, ref="Object"):
    if not is_int(obj):
        raise TypeError(f"{repr(ref)} must be an integer!")

######  FLOAT PROCESSING

def is_float(obj):
    return isinstance(obj, float)

######  STRING PROCESSING

def is_string(obj):
    return isinstance(obj, str)

def error_not_string(obj, ref="Object"):
    if not is_string(obj):
        raise TypeError(f"{repr(ref)} must be a string!")

######  INTEGER AND FLOAT PROCESSING

def is_int_or_float(obj):
    return is_int(obj) or is_float(obj)

def error_not_int_or_float(obj, ref="Object"):
    if not is_int_or_float(obj):
        raise TypeError(f"{repr(ref)} must be an integer or float!")

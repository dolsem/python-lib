

# Taken from
# https://stackoverflow.com/questions/10307696/how-to-put-a-variable-into-python-docstring
def docstring_params(*params):
    def dec(obj):
        obj.__doc__ = obj.__doc__.format(*params)
        return obj
    return dec

def add_integers(n1, n2):

    '''adds two numbers
    raises error if non integer is passed as argument

    :param n1: the first int
    :param n2: the second int
    '''

    assert_int(n1)
    assert_int(n2)
    return n1 + n2

def assert_int(n):

    '''raises TypeError if number is not integer'''
    tmp = "{} is not type int"
    if not isinstance(n, int):
        raise TypeError(tmp.format(n))
    return True



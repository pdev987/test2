def check_is_integer(x):
    """
    check x is integer or not
    """
    return isinstance(x, int)

def a_greater_than_b(a,b):
    """
    this is temporary function that is comparing
    two variables a and b if they are numbers
    compare them are return the 
    a is greater than b or not
    """
    if check_is_integer(a) and check_is_integer(b):
            return a > b
    else:
        # if they are not number 
        # return None
        return None

if __name__ == "__main__":
    print(a_greater_than_b(10, 1))
        

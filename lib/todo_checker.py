def todo_checker(string):
    if type(string) != str:
        raise Exception("Please entry a string")
    if string.upper() == "#TODO":
        raise Exception("Please also include task")

    if "#TODO" in string.upper():
        return True
    else:
        return False
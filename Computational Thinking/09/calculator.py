def summary(*para):
    result = 0
    for num in para:
        result += num
    return result


def subscribe(*para):
    result = 0
    for num in para:
        result -= num
    return result


def multiply(*para):
    result = 1
    for num in para:
        result *= num
    return result


def divide(*para):
    result = 1
    for num in para:
        result /= num
    return result

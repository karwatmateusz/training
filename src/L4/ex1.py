


def not_divide_by_zero(func):
    def wrapper(a, b):
        if b != 0:
            func(a, b)
        else:
            raise ZeroDivisionError("Dzielenie przez zero zabronione")
    return wrapper


# def not_divide_by_zero_catch(func):
#     def wrapper():
#         try:
            

@not_divide_by_zero
def divide(a, b):
    result = a / b
    # print(result)
    return result


x = divide(4, 2)
print(x)
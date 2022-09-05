def not_divide_by_zero(func):
    def wrapper(a, b):
        if b != 0:
            result = func(a, b)
            return result
        else:
            raise ZeroDivisionError("Dzielenie przez zero zabronione")

    return wrapper


def not_divide_by_zero_catch(func):
    def wrapper(a, b):
        try:
            result = func(a, b)
            return result
        except ZeroDivisionError as e:
            print(f"{e}, nie mozesz dzielic przez zero")

    return wrapper


# @not_divide_by_zero
@not_divide_by_zero_catch
def divide(a, b):
    result = a / b
    return result


x = divide(4, 0) if divide(4, 0) is not None else "Brak wyniku"
# to discuss
# x = divide(4,0)
# if x is None:
#     x = 'Brak wyniku'

print(x)

#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.
    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.
    Returns:
        A new list of length list_length containing all the divisions.
    """
    result = []
    for num in range(list_length):
        try:
            value_1 = my_list_[num] if num < len(my_list_1) else 0
            value_2 = my_list_2[num] if num < len(my_list_2) else 1

            try:
                division_result = value_1 / value_2
                result.append(division_result)
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass

    return (result)

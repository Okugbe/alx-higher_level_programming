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
            division_result = my_list_1[num] / my_list_2[num]
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

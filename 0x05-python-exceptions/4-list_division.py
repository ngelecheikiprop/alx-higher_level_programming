#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    div_list = []
    while i < list_length:
        try:
            div_list.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            div_list.append(0)
        except (TypeError, ValueError):
            print("wrong type")
            div_list.append(0)
        except IndexError:
            print("out of range")
            div_list.append(0)
        finally:
            i += 1
    return div_list

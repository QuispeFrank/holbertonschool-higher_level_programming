#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    div_list = []
    for idx in range(list_length):
        try:
            coc = my_list_1[idx] / my_list_2[idx]

        except ZeroDivisionError:
            print("division by 0")
            coc = 0
        except TypeError:
            print("wrong type")
            coc = 0
        except IndexError:
            print("out of range")
            coc = 0
        finally:
            div_list.append(coc)

    return (div_list)

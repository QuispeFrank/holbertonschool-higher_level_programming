def safe_print_list(my_list=[], x=0):

    items = 0
    for idx in range(x):
        try:
            print(f"{my_list[idx]}", end="")
            items += 1

        except:
            break

    print()
    return (items)
